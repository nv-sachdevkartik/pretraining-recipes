#!/usr/bin/env python3
"""Generate a simple Markdown fan-out plan from the agent matrix."""

from __future__ import annotations

import argparse
from pathlib import Path


DEFAULT_AGENTS = [
    ("vla-researcher", "Collect source-backed evidence and caveats."),
    ("sphinx-docs-builder", "Implement clean Sphinx source and run local build checks."),
    ("github-pages-deployer", "Verify GitHub Actions and public Pages deployment."),
    ("visual-qa", "Inspect rendered pages and assets."),
    ("expert-reviewer", "Review claims, code/docs quality, and public tone."),
    ("memory-curator", "Capture reusable lessons and remove noise."),
]


def parse_args() -> argparse.Namespace:
    parser = argparse.ArgumentParser(description=__doc__)
    parser.add_argument("--goal", required=True, help="Goal to fan out.")
    parser.add_argument(
        "--root",
        default=None,
        help="Agent pack root. Defaults to the parent directory of this script.",
    )
    return parser.parse_args()


def main() -> int:
    args = parse_args()
    root = (
        Path(args.root).expanduser().resolve()
        if args.root
        else Path(__file__).resolve().parents[1]
    )
    print(f"# Fan-Out Plan: {args.goal}\n")
    print("## Orchestrator Packet\n")
    print(f"- Goal: {args.goal}")
    print("- Pattern: staged fan-out with final expert review and memory curation")
    print(f"- Agent matrix: {root / 'agent_matrix.yaml'}\n")
    for name, output in DEFAULT_AGENTS:
        print(f"## {name}\n")
        print(f"- Task: {output}")
        print("- Inputs: user request, repository state, relevant sources")
        print("- Output: concise findings or patch notes")
        print("- Acceptance: pass the relevant checklist in review/checklists.md\n")
    return 0


if __name__ == "__main__":
    raise SystemExit(main())
