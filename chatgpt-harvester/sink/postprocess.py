#!/usr/bin/env python3
"""Post-processor for captured ChatGPT conversation JSON.

Walks the conversation tree, groups messages by date, and optionally
parses individual items from structured daily feeds. Outputs markdown
files with YAML frontmatter.

Usage:
    python postprocess.py INPUT [--mode daily|items] [--outdir DIR]
    python postprocess.py sink/data/ --mode items --outdir output/
"""

import argparse
import json
import re
import sys
from dataclasses import dataclass, field
from datetime import datetime, timezone
from pathlib import Path


# ---------------------------------------------------------------------------
#  Data structures
# ---------------------------------------------------------------------------

@dataclass
class Message:
    id: str
    role: str
    create_time: float | None
    text: str
    content_type: str
    branch: tuple = ()


@dataclass
class ParsedItem:
    number: int
    heading: str
    title: str | None
    summary: str | None
    angle: str | None
    interests: list[str] = field(default_factory=list)
    fmt: str | None = None
    points: list[str] = field(default_factory=list)
    raw: str = ""


# ---------------------------------------------------------------------------
#  Tree walking
# ---------------------------------------------------------------------------

def walk_tree(mapping: dict) -> list[Message]:
    """DFS through the mapping, returning messages in tree order."""
    root = next(nid for nid, n in mapping.items() if n.get("parent") is None)

    messages = []

    def dfs(node_id, branch=()):
        node = mapping[node_id]
        msg = node.get("message")
        if msg and _should_include(msg):
            text = _extract_text(msg)
            if text:
                messages.append(Message(
                    id=msg["id"],
                    role=msg["author"]["role"],
                    create_time=msg.get("create_time"),
                    text=text,
                    content_type=msg.get("content", {}).get("content_type", "text"),
                    branch=branch,
                ))
        children = node.get("children", [])
        for i, child_id in enumerate(children):
            child_branch = branch + (i,) if len(children) > 1 else branch
            dfs(child_id, child_branch)

    dfs(root)
    messages.sort(key=lambda m: m.create_time or 0)
    return messages


def _should_include(msg: dict) -> bool:
    role = msg.get("author", {}).get("role")
    if role not in ("user", "assistant"):
        return False
    meta = msg.get("metadata", {})
    if meta.get("is_visually_hidden_from_conversation"):
        return False
    ct = msg.get("content", {}).get("content_type", "")
    if ct in ("model_editable_context", "user_editable_context"):
        return False
    return True


def _extract_text(msg: dict) -> str:
    parts = msg.get("content", {}).get("parts", [])
    text_parts = [p for p in parts if isinstance(p, str)]
    return clean_text("\n".join(text_parts).strip())


# ---------------------------------------------------------------------------
#  Text cleanup
# ---------------------------------------------------------------------------

# ChatGPT wraps several kinds of UI markup in private-use codepoints:
#
#   \ue200cite\ue202turn0news53\ue202turn0search18\ue201
#   \ue200entity\ue202["software","Virtualizor","VPS control panel"]\ue201
#   \ue200url\ue202Wiz\ue202turn0news0\ue201
#
# Two of them carry text worth keeping -- an entity's name and a link's label
# -- so they are unwrapped rather than dropped. The rest (cite, memcite,
# navlist, image_group) are navigation chrome and go entirely. Stripping the
# lot indiscriminately silently eats entity names mid-sentence.
_MARKER_RE = re.compile(
    "\ue200(?P<kind>[^\ue201\ue202]*)(?:\ue202(?P<body>.*?))?\ue201", re.DOTALL
)
_ENTITY_NAME_RE = re.compile(r'^\["[^"]*","([^"]*)"')
_STRAY_MARKER_RE = re.compile("[\ue200-\ue20f]")


def _unwrap_marker(match: re.Match) -> str:
    kind = match.group("kind")
    body = match.group("body") or ""
    if kind == "entity":
        name = _ENTITY_NAME_RE.match(body)
        return name.group(1) if name else ""
    if kind == "url":
        # body is "<link label>\ue202<citation>"
        return body.split("\ue202")[0]
    return ""


def clean_text(text: str) -> str:
    """Strip ChatGPT UI markup that has no meaning outside the web client."""
    text = _MARKER_RE.sub(_unwrap_marker, text)
    return _STRAY_MARKER_RE.sub("", text)


# ---------------------------------------------------------------------------
#  Date grouping
# ---------------------------------------------------------------------------

def group_by_date(messages: list[Message]) -> dict[str, list[Message]]:
    groups: dict[str, list[Message]] = {}
    for msg in messages:
        if msg.create_time:
            date = datetime.fromtimestamp(msg.create_time, tz=timezone.utc).strftime("%Y-%m-%d")
        else:
            date = "undated"
        groups.setdefault(date, []).append(msg)
    return groups


# ---------------------------------------------------------------------------
#  Item parsing
# ---------------------------------------------------------------------------

# The feeds have used three item layouts over time. Patterns are tried in
# order and the first that matches anything wins, so a feed still using the
# original layout parses exactly as it always did.
#: Layouts whose items open with prose that genuinely stands in for a
#: Summary field. The original layout carries an explicit Summary, and the
#: project feed -- which matches the same pattern -- opens with section
#: headings and asides, where the first prose block is as likely to be a
#: trailing list fragment as a summary. Treating that as a summary writes
#: something wrong into a field that reads as authoritative, which is worse
#: than leaving it empty.
_PROSE_LEADS_LAYOUT = "prose-lead"

_ITEM_PATTERNS = (
    # Original, and the July 2026 variant that kept its headings:
    #   "## 1) Heading"   "# 1. Heading"
    ("bulleted", re.compile(r"^(?P<prefix>#{1,2}) (?P<num>\d+)(?P<sep>[).]) (?P<heading>.+)$", re.MULTILINE)),
    # August 2026 onward:
    #   '### 1. **"Heading"** - Long-form'
    (_PROSE_LEADS_LAYOUT, re.compile(r"^(?P<prefix>#{3,4}) (?P<num>\d+)(?P<sep>[).]) (?P<heading>.+)$", re.MULTILINE)),
    # Briefly, in early August 2026, with no heading markup at all:
    #   '**1. "Heading" - Long-form**'
    (_PROSE_LEADS_LAYOUT, re.compile(r"^(?P<prefix>)\*\*(?P<num>\d+)(?P<sep>[).]) (?P<heading>.+?)\*\*[ \t]*$", re.MULTILINE)),
)

# A trailing "- Long-form" / "- Short post" on a heading is the format field
# by another name; the later layouts carry it there instead of in a field.
_FORMAT_SUFFIX_RE = re.compile(
    r"\s*[—–-]\s*\**(Long[- ]form|Short post|Short)\**\s*$", re.IGNORECASE
)


def parse_items(text: str) -> list[ParsedItem]:
    """Split assistant text on numbered item headings and extract fields.

    Fields missing from a given layout are left unset rather than failing the
    parse, so a format change costs metadata but never the item itself.
    """
    text = clean_text(text)

    matches: list[re.Match] = []
    layout = ""
    for name, pattern in _ITEM_PATTERNS:
        matches = list(pattern.finditer(text))
        if matches:
            layout = name
            break
    if not matches:
        return []

    items = []
    for i, match in enumerate(matches):
        end = matches[i + 1].start() if i + 1 < len(matches) else len(text)
        body = text[match.end():end]
        if i == len(matches) - 1:
            body = _trim_trailer(body, match.group("prefix"))

        heading, heading_fmt = _clean_heading(match.group("heading"))

        items.append(ParsedItem(
            number=int(match.group("num")),
            heading=heading,
            title=_extract_field(body, "Title", "Suggested title"),
            summary=_extract_field(body, "Summary")
            or (_first_paragraph(body) if layout == _PROSE_LEADS_LAYOUT else None),
            angle=_extract_field(body, "Angle"),
            interests=_extract_list_field(
                body, "Matches Interests", "Matches your interests", "Matches"
            ),
            fmt=_extract_field(body, "Format") or heading_fmt,
            points=_extract_points(body),
            # Rebuild from the cleaned heading rather than the matched text, so
            # the body renders consistently whichever layout it came from. The
            # bold-paragraph layout has no heading marker, so give it one.
            raw=f"{match.group('prefix') or '##'} {int(match.group('num'))}"
                f"{match.group('sep')} {heading}\n{body}".rstrip(),
        ))

    return items


def _trim_trailer(body: str, prefix: str) -> str:
    """Drop meta sections that follow the final item.

    After the last numbered item the assistant often appends sections such as
    "## Cross-Cutting Insight" or "### What I'd actually write". These sit at
    the same heading level as the items themselves, whereas an item's own
    subsections are always deeper.
    """
    level = len(prefix) or 2
    trailer = re.search(rf"^#{{1,{level}}} (?!\d+[).]).+", body, flags=re.MULTILINE)
    if not trailer:
        return body
    cut = body[:trailer.start()]
    # Drop a trailing horizontal-rule separator left behind by the cut.
    return re.sub(r"\n+-{3,}\s*\n*$", "\n", cut)


def _clean_heading(heading: str) -> tuple[str, str | None]:
    """Strip decoration from a heading, returning (heading, format or None)."""
    fmt = None
    suffix = _FORMAT_SUFFIX_RE.search(heading)
    if suffix:
        fmt = suffix.group(1)
        heading = heading[:suffix.start()]
    return _strip_emphasis(heading), fmt


def _strip_emphasis(value: str) -> str:
    """Remove wrapping bold, italic or quote marks from a value."""
    value = re.sub(r"^\*\*(.+)\*\*$", r"\1", value.strip()).strip()
    value = re.sub(r"^\*(.+)\*$", r"\1", value).strip()
    # Only unwrap quotes that enclose the whole value: headings such as
    # '"Breakglass" Accounts as a Backdoor' must survive intact.
    quoted = re.match(r"^[“\"](.+)[”\"]$", value)
    if quoted:
        value = quoted.group(1).strip()
    return value


def _extract_field(body: str, *names: str) -> str | None:
    """Value of a labelled field, in any of the layouts the feeds have used.

    Longest alias first: the alternation is ordered, so "Matches Interests"
    must be offered before the bare "Matches".
    """
    alt = "|".join(re.escape(name) for name in names)
    # (\S.*) rather than (.+): the label is often followed by trailing spaces,
    # which .+ will happily match, yielding an empty field.
    patterns = (
        rf"^[ \t]*[-*] \*\*(?:{alt}):?\*\*[ \t]*(\S.*)",    # - **Title:** value
        rf"^\*\*(?:{alt}):?\*\*[ \t]*\n+[ \t]*(\S.*)",      # **Summary:**\nvalue
        rf"^\*\*(?:{alt}):?\*\*[ \t]*(\S.*)",                # **Angle:** value
    )
    for pattern in patterns:
        match = re.search(pattern, body, flags=re.IGNORECASE | re.MULTILINE)
        if match:
            return _strip_emphasis(match.group(1)) or None
    return None


def _extract_list_field(body: str, *names: str) -> list[str]:
    value = _extract_field(body, *names)
    if value and not value.startswith(("-", "*")):
        return [part.strip(" .") for part in value.split(",") if part.strip(" .")]

    # Block form: the label sits alone on its line with bullets beneath it.
    alt = "|".join(re.escape(name) for name in names)
    label = re.search(
        rf"^\*\*(?:{alt}):?\*\*[ \t]*$", body, flags=re.IGNORECASE | re.MULTILINE
    )
    if not label:
        return []

    values = []
    for line in body[label.end():].lstrip("\n").split("\n"):
        bullet = re.match(r"^[ \t]*[-*] (.+)", line)
        if bullet:
            values.append(_strip_emphasis(bullet.group(1)).strip(" ."))
        elif line.strip():
            break
    return values


def _first_paragraph(body: str) -> str | None:
    """Opening prose paragraph of an item body.

    Only for layouts in _PROSE_LEADS_LAYOUT. The August 2026 article layout
    dropped the Summary field and its opening paragraph plays the same role;
    in layouts that never had one, the first prose block is as likely to be
    an aside or the tail of a list, and a plausible-looking wrong summary is
    worse than an empty field.
    """
    for block in body.split("\n\n"):
        block = block.strip()
        if not block or block.startswith(("**", "-", "*", "#", ">", "|", "`")):
            continue
        # Skip parenthetical asides and one-line stubs: a paragraph standing in
        # for a summary is always a sentence or more.
        if len(block) < 40:
            continue
        return " ".join(block.split())
    return None


def _extract_points(body: str) -> list[str]:
    """Bullets under a "Suggested points to cover" label.

    The label lost its capitals and its indentation when the layout changed in
    July 2026, so match case-insensitively and accept bullets at any depth.
    """
    in_points = False
    points = []
    for line in body.split("\n"):
        if "suggested points to cover" in line.lower():
            in_points = True
            continue
        if in_points:
            bullet = re.match(r"[ \t]*[-*] (.+)", line)
            if bullet:
                points.append(_strip_emphasis(bullet.group(1)))
            elif line.strip():
                break
    return points


# ---------------------------------------------------------------------------
#  YAML frontmatter (no pyyaml dependency)
# ---------------------------------------------------------------------------

def _yaml_str(val: str) -> str:
    """Quote a string for YAML if it contains special chars."""
    if not val:
        return '""'
    if any(c in val for c in ":{}[]#&*!|>'\"%@`"):
        escaped = val.replace("\\", "\\\\").replace('"', '\\"')
        return f'"{escaped}"'
    return val


def _frontmatter(fields: dict) -> str:
    lines = ["---"]
    for key, val in fields.items():
        if val is None:
            continue
        if isinstance(val, list):
            lines.append(f"{key}:")
            for item in val:
                lines.append(f"  - {_yaml_str(str(item))}")
        elif isinstance(val, (int, float)):
            lines.append(f"{key}: {val}")
        else:
            lines.append(f"{key}: {_yaml_str(str(val))}")
    lines.append("---")
    return "\n".join(lines)


# ---------------------------------------------------------------------------
#  Slug helper
# ---------------------------------------------------------------------------

def slugify(text: str, max_len: int = 60) -> str:
    text = text.lower()
    text = re.sub(r"[^a-z0-9]+", "-", text)
    text = text.strip("-")
    return text[:max_len].rstrip("-")


def _feed_dir(meta: dict) -> str:
    conv_id = meta.get("conversation_id") or ""
    label = meta.get("label") or meta.get("title") or ""
    slug = slugify(label) if label else ""
    short = conv_id[:8]
    if slug and short:
        return f"{slug}__{short}"
    return slug or short or "unknown"


# ---------------------------------------------------------------------------
#  Output writers
# ---------------------------------------------------------------------------

def write_daily(date: str, messages: list[Message], meta: dict, outdir: Path):
    assistant_msgs = [m for m in messages if m.role == "assistant"]
    if not assistant_msgs:
        return

    fm = _frontmatter({
        "date": date,
        "conversation_id": meta["conversation_id"],
        "title": meta["title"],
        "label": meta["label"],
        "fetched_at": meta["fetched_at"],
        "message_count": len(messages),
    })

    body_parts = []
    for msg in assistant_msgs:
        body_parts.append(msg.text)

    content = fm + "\n\n" + "\n\n".join(body_parts) + "\n"
    feed_dir = outdir / _feed_dir(meta)
    feed_dir.mkdir(parents=True, exist_ok=True)
    path = feed_dir / f"{date}.md"
    path.write_text(content)
    print(f"  wrote {path}")


def write_items(date: str, messages: list[Message], meta: dict, outdir: Path):
    assistant_msgs = [m for m in messages if m.role == "assistant"]
    if not assistant_msgs:
        return

    # Use the latest assistant message that contains parseable items,
    # since earlier messages on the same day may be superseded by updates.
    chosen_msg = None
    chosen_items = []
    for msg in reversed(assistant_msgs):
        items = parse_items(msg.text)
        if items:
            chosen_msg = msg
            chosen_items = items
            break

    if not chosen_items:
        write_daily(date, messages, meta, outdir)
        return

    feed_dir = outdir / _feed_dir(meta)
    feed_dir.mkdir(parents=True, exist_ok=True)

    for item in chosen_items:
            fm = _frontmatter({
                "date": date,
                "item_number": item.number,
                "title": item.title or item.heading,
                "summary": item.summary,
                "angle": item.angle,
                "interests": item.interests,
                "format": item.fmt,
                "suggested_points": item.points,
                "conversation_id": meta["conversation_id"],
                "label": meta["label"],
            })

            slug = slugify(item.heading)
            filename = f"{date}-{item.number:02d}-{slug}.md"
            content = fm + "\n\n" + item.raw + "\n"
            path = feed_dir / filename
            path.write_text(content)
            print(f"  wrote {path}")


# ---------------------------------------------------------------------------
#  Main
# ---------------------------------------------------------------------------

def process_file(input_path: Path, mode: str, outdir: Path):
    data = json.loads(input_path.read_text())

    # Support both raw payload and our envelope format
    if "payload" in data:
        payload = data["payload"]
        meta = {
            "conversation_id": data.get("conversation_id", ""),
            "label": data.get("label", ""),
            "title": payload.get("title", ""),
            "fetched_at": data.get("fetched_at", ""),
        }
    else:
        payload = data
        meta = {
            "conversation_id": payload.get("conversation_id", ""),
            "label": payload.get("title", ""),
            "title": payload.get("title", ""),
            "fetched_at": "",
        }

    mapping = payload.get("mapping", {})
    if not mapping:
        print(f"  skipping {input_path.name}: no mapping found", file=sys.stderr)
        return

    messages = walk_tree(mapping)
    date_groups = group_by_date(messages)

    writer = write_items if mode == "items" else write_daily

    for date in sorted(date_groups.keys()):
        if date == "undated":
            continue
        writer(date, date_groups[date], meta, outdir)


def main():
    parser = argparse.ArgumentParser(description="Post-process captured ChatGPT conversations")
    parser.add_argument("input", type=Path, help="JSON file or directory of JSON files")
    parser.add_argument("--mode", choices=["daily", "items"], default="items",
                        help="Output granularity (default: items)")
    parser.add_argument("--outdir", type=Path, default=Path("output"),
                        help="Output directory (default: ./output)")
    parser.add_argument("--latest-only", action="store_true",
                        help="When processing a directory, only use the latest capture per conversation")
    args = parser.parse_args()

    args.outdir.mkdir(parents=True, exist_ok=True)

    if args.input.is_dir():
        files = sorted(args.input.glob("*.json"))
        if args.latest_only:
            # Group by conversation_id prefix and keep the latest
            by_conv: dict[str, Path] = {}
            for f in files:
                conv_id = f.name.split("_")[0]
                by_conv[conv_id] = f  # sorted ascending, last wins
            files = list(by_conv.values())
        print(f"Processing {len(files)} file(s)...")
        for f in files:
            print(f"\n{f.name}:")
            process_file(f, args.mode, args.outdir)
    else:
        print(f"{args.input.name}:")
        process_file(args.input, args.mode, args.outdir)

    print(f"\nDone. Output in {args.outdir}/")


if __name__ == "__main__":
    main()
