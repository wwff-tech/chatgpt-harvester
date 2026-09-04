#!/usr/bin/env -S uv run --quiet --script
# /// script
# requires-python = ">=3.12"
# dependencies = ["httpx>=0.27", "jsonschema>=4.21"]
# ///
"""Compare Codex models on the idea-generation task.

Every model sees the same frozen candidate set, so differences are the
model's rather than the feed's. Repeats matter as much as the headline
score: a model that picks a different six items every run is telling you
its ranking is noise, which no single run would show.

Scored on what can be checked mechanically. Grounding is the one that
actually matters -- a cited URL that was never in the candidate set is a
fabricated source, and no amount of good prose makes up for it.

    ./eval.py --candidates eval-candidates.json --repeats 2
"""

from __future__ import annotations

import argparse
import json
import re
import statistics
import sys
from pathlib import Path

from jsonschema import Draft202012Validator

sys.path.insert(0, str(Path(__file__).parent))
from generate import BRIEF, SCHEMA_PATH, format_candidates, run_codex  # noqa: E402

TOKENS_RE = re.compile(r"tokens used\s+([\d,]+)")
# Above this word overlap, the angle is restating the summary rather than
# adding a take, which is the failure the brief is trying to prevent.
ANGLE_OVERLAP_LIMIT = 0.6


def words(text: str | None) -> set[str]:
    return set(re.findall(r"[a-z]{4,}", (text or "").lower()))


def score(response: dict, candidate_urls: set[str]) -> dict:
    ideas = response.get("items", [])
    if not ideas:
        return {"n": 0}

    cited = [s["url"] for idea in ideas for s in idea.get("sources", [])]
    confidences = [i["confidence"] for i in ideas if isinstance(i.get("confidence"), (int, float))]
    primary = [idea["sources"][0]["url"] for idea in ideas if idea.get("sources")]

    distinct_angles = 0
    for idea in ideas:
        angle, summary = words(idea.get("angle")), words(idea.get("summary"))
        overlap = len(angle & summary) / len(angle) if angle else 0.0
        if overlap < ANGLE_OVERLAP_LIMIT:
            distinct_angles += 1

    return {
        "n": len(ideas),
        # Fabricated sources: cited URLs that were never offered.
        "grounding": sum(u in candidate_urls for u in cited) / len(cited) if cited else 0.0,
        "sourced": sum(bool(i.get("sources")) for i in ideas) / len(ideas),
        "conf_spread": (max(confidences) - min(confidences)) if len(confidences) > 1 else 0.0,
        "conf_stdev": statistics.pstdev(confidences) if len(confidences) > 1 else 0.0,
        "points_ok": sum(3 <= len(i.get("points", [])) <= 6 for i in ideas) / len(ideas),
        "angle_distinct": distinct_angles / len(ideas),
        "source_variety": len(set(primary)) / len(ideas) if primary else 0.0,
        "primary": primary,
    }


def main() -> int:
    parser = argparse.ArgumentParser(description=__doc__)
    parser.add_argument("--candidates", default="eval-candidates.json")
    parser.add_argument("--models", default="gpt-5.6-luna,gpt-5.6-terra,gpt-5.6-sol")
    parser.add_argument("--repeats", type=int, default=2)
    parser.add_argument("--count", type=int, default=6)
    parser.add_argument("--effort", default="low")
    parser.add_argument("--out", default="eval-results.json")
    parser.add_argument("--signal-urls", metavar="PATH",
                        help="JSON list of the candidate URLs that are genuinely worth picking. "
                             "Turns the run into a precision test: how much of what the model "
                             "chose was signal rather than filler.")
    args = parser.parse_args()

    items = json.loads(Path(args.candidates).read_text())
    candidate_urls = {i["canonical_url"] for i in items}
    signal = set(json.loads(Path(args.signal_urls).read_text())) if args.signal_urls else None
    prompt = BRIEF.format(count=args.count, candidates=format_candidates(items))
    validator = Draft202012Validator(json.loads(SCHEMA_PATH.read_text()))

    runs = []
    for model in args.models.split(","):
        for repeat in range(args.repeats):
            print(f"  {model} run {repeat + 1}/{args.repeats} ...", file=sys.stderr, flush=True)
            response, output, elapsed = run_codex(prompt, model, args.effort)
            problems = list(validator.iter_errors(response))
            tokens = TOKENS_RE.search(output)
            runs.append({
                "model": model,
                "repeat": repeat,
                "latency_s": round(elapsed, 1),
                "tokens": int(tokens.group(1).replace(",", "")) if tokens else None,
                "schema_valid": not problems,
                "schema_errors": [p.message[:120] for p in problems[:3]],
                **score(response, candidate_urls),
                "response": response,
            })

    Path(args.out).write_text(json.dumps(runs, indent=2, ensure_ascii=False))

    print(f"\n{'model':16} {'run':>3} {'secs':>5} {'tokens':>7} {'ok':>3} {'ideas':>5} "
          f"{'ground':>7} {'srcd':>5} {'spread':>7} {'pts':>5} {'angle':>6} {'variety':>8}"
          + (f" {'signal':>7}" if signal else ""))
    for r in runs:
        print(f"  {r['model'].replace('gpt-5.6-',''):14} {r['repeat']+1:>3} {r['latency_s']:>5.0f} "
              f"{str(r['tokens'] or '-'):>7} {'y' if r['schema_valid'] else 'NO':>3} {r['n']:>5} "
              f"{r.get('grounding',0):>7.0%} {r.get('sourced',0):>5.0%} {r.get('conf_spread',0):>7.2f} "
              f"{r.get('points_ok',0):>5.0%} {r.get('angle_distinct',0):>6.0%} "
              f"{r.get('source_variety',0):>8.0%}"
              + (f" {sum(u in signal for u in r['primary'])/len(r['primary']):>7.0%}"
                 if signal and r.get('primary') else ""))

    print("\n=== run-to-run stability (overlap of chosen sources) ===")
    for model in args.models.split(","):
        picks = [set(r["primary"]) for r in runs if r["model"] == model and r.get("primary")]
        if len(picks) < 2:
            continue
        overlap = len(set.intersection(*picks)) / max(len(p) for p in picks)
        print(f"  {model.replace('gpt-5.6-',''):14} {overlap:.0%} of picks repeated across runs")

    print(f"\nfull responses in {args.out}")
    return 0


if __name__ == "__main__":
    raise SystemExit(main())
