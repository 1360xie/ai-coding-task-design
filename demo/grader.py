#!/usr/bin/env python3
"""Grade a code submission against the rubric declared in a task spec.

The task spec is a markdown file following `task-spec-template.md`. This tool
extracts the Acceptance Criteria and the Evaluation Rubric from that file and
produces a reviewer prompt (or, with --mock, a cheap rule-based score) for a
given submission.

Usage:
    python grader.py <task-spec.md> <submission> [--mock]
"""
from __future__ import annotations

import argparse
import re
import sys
from pathlib import Path


def parse_sections(text: str) -> dict[str, str]:
    """Split a markdown spec into `## Title` -> body sections."""
    sections: dict[str, str] = {}
    current: str | None = None
    for line in text.splitlines():
        m = re.match(r"^#{2}\s+(.+)$", line)
        if m:
            current = m.group(1).strip()
            sections[current] = ""
        elif current is not None:
            sections[current] += line + "\n"
    return sections


def first_section_like(sections: dict[str, str], keyword: str) -> str:
    for title, body in sections.items():
        if keyword in title.lower():
            return body
    return ""


def acceptance_criteria(spec: dict[str, str]) -> list[str]:
    body = first_section_like(spec, "acceptance")
    return re.findall(r"-\s*\[ \]\s*(.+)", body)


def rubric_rows(spec: dict[str, str]) -> list[tuple[str, str]]:
    body = first_section_like(spec, "rubric")
    rows: list[tuple[str, str]] = []
    for line in body.splitlines():
        if line.strip().startswith("|") and "---" not in line:
            cells = [c.strip() for c in line.strip().strip("|").split("|")]
            if len(cells) >= 2 and cells[0] and cells[0].lower() != "dimension":
                rows.append((cells[0], cells[1]))
    return rows


def mock_checks(code: str) -> dict[str, bool]:
    """Rule-based, no-network heuristics that stand in for a real review."""
    lines = [line for line in code.splitlines() if line.strip()]
    return {
        "non-empty": bool(lines),
        "no leftover TODO/FIXME/pass": not re.search(
            r"\b(TODO|FIXME)\b|^\s*pass\s*$", code, re.M
        ),
        "has error handling": bool(re.search(r"\b(try|raise|except)\b", code)),
        "has an entry point": bool(
            re.search(r"if __name__ == .__main__.|def main\(", code)
        ),
        "not a stub": len(lines) >= 20,
    }


def render_mock(checks: dict[str, bool]) -> str:
    rows = [f"- [{'x' if ok else ' '}] {name}" for name, ok in checks.items()]
    score = sum(checks.values())
    return "\n".join(["## Mock grade (rule-based)", *rows, f"\nScore: {score}/{len(checks)}"])


def build_prompt(spec_path: Path, submission: str) -> str:
    spec = parse_sections(spec_path.read_text(encoding="utf-8"))
    criteria = acceptance_criteria(spec)
    rubric = rubric_rows(spec)
    crit = "\n".join(f"- [ ] {c}" for c in criteria)
    rub = "\n".join(f"- {d} ({w})" for d, w in rubric)
    return f"""You are reviewing a coding submission against its task spec ({spec_path.name}).

## Acceptance criteria
{crit}

## Rubric
{rub}

## Submission
```python
{submission}
```

For each acceptance criterion state pass/fail with a one-line reason, then
score each rubric dimension out of its weight. End with a total score."""


def main(argv: list[str]) -> int:
    ap = argparse.ArgumentParser(description="Grade a submission against a task spec.")
    ap.add_argument("spec", type=Path, help="path to the task spec markdown")
    ap.add_argument("submission", type=Path, help="path to the submission file")
    ap.add_argument("--mock", action="store_true", help="rule-based scoring, no LLM")
    args = ap.parse_args(argv)

    if not args.spec.exists():
        print(f"error: spec not found: {args.spec}", file=sys.stderr)
        return 2
    if not args.submission.exists():
        print(f"error: submission not found: {args.submission}", file=sys.stderr)
        return 2

    code = args.submission.read_text(encoding="utf-8")

    if args.mock:
        print(render_mock(mock_checks(code)))
        return 0

    print(build_prompt(args.spec, code))
    return 0


if __name__ == "__main__":
    raise SystemExit(main(sys.argv[1:]))
