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
    return "\n".join(text_parts).strip()


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

def parse_items(text: str) -> list[ParsedItem]:
    """Split assistant text on ## N) or ## N. headings and extract structured fields."""
    pattern = r"^## (\d+)[).] (.+)$"
    splits = re.split(pattern, text, flags=re.MULTILINE)

    # Strip trailing non-item content from the last body.  After the
    # last ## N) item, the assistant often appends observations / meta
    # commentary separated by --- and a top-level heading (# …).
    if len(splits) >= 4:
        trailer = re.search(r"\n---\s*\n+(?=#\s)", splits[-1])
        if trailer:
            splits[-1] = splits[-1][:trailer.start()]

    items = []
    # splits: [preamble, num, heading, body, num, heading, body, ...]
    for i in range(1, len(splits), 3):
        if i + 2 > len(splits):
            break
        number = int(splits[i])
        heading = splits[i + 1].strip()
        # Strip bold markers that wrap the heading (e.g. **Heading**)
        heading = re.sub(r"^\*\*(.+)\*\*$", r"\1", heading)
        body = splits[i + 2] if i + 2 < len(splits) else ""

        item = ParsedItem(
            number=number,
            heading=heading,
            title=_extract_field(body, "Title"),
            summary=_extract_field(body, "Summary"),
            angle=_extract_field(body, "Angle"),
            interests=_extract_list_field(body, "Matches Interests"),
            fmt=_extract_field(body, "Format"),
            points=_extract_points(body),
            raw=f"## {number}) {heading}\n{body}".rstrip(),
        )
        items.append(item)

    return items


def _extract_field(body: str, name: str) -> str | None:
    match = re.search(rf"- \*\*{name}:\*\*\s*(.+)", body)
    if not match:
        return None
    val = match.group(1).strip()
    # Strip surrounding italic markers and bold markers
    val = re.sub(r"^\*\*(.+)\*\*$", r"\1", val)
    val = re.sub(r"^\*(.+)\*$", r"\1", val)
    return val


def _extract_list_field(body: str, name: str) -> list[str]:
    val = _extract_field(body, name)
    if not val:
        return []
    return [s.strip() for s in val.split(",")]


def _extract_points(body: str) -> list[str]:
    in_points = False
    points = []
    for line in body.split("\n"):
        if "Suggested Points to Cover" in line:
            in_points = True
            continue
        if in_points:
            m = re.match(r"\s+- (.+)", line)
            if m:
                points.append(m.group(1).strip())
            elif line.strip() and not line.startswith(" "):
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
