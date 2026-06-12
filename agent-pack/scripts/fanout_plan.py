#!/usr/bin/env python3
"""Generate a simple Markdown fan-out plan from the agent matrix."""

from __future__ import annotations

import argparse
from pathlib import Path


def parse_agent_purposes(matrix_path: Path) -> list[tuple[str, str]]:
    """Parse the small agent_matrix.yaml shape used by this pack."""
    agents: list[tuple[str, str]] = []
    in_agents = False
    current: str | None = None
    for line in matrix_path.read_text(encoding="utf-8").splitlines():
        if line == "agents:":
            in_agents = True
            continue
        if line == "workflows:":
            break
        if not in_agents:
            continue
        if line.startswith("  ") and line.endswith(":") and not line.startswith("    "):
            current = line.strip()[:-1]
            continue
        if current and line.startswith("    purpose:"):
            purpose = line.split(":", 1)[1].strip()
            agents.append((current, purpose))
    return agents


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
    for name, output in parse_agent_purposes(root / "agent_matrix.yaml"):
        if name == "orchestrator":
            continue
        print(f"## {name}\n")
        print(f"- Task: {output}")
        print("- Inputs: user request, repository state, relevant sources")
        print("- Output: concise findings or patch notes")
        print("- Acceptance: pass the relevant checklist in review/checklists.md\n")
    return 0


if __name__ == "__main__":
    raise SystemExit(main())
