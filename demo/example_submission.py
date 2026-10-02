#!/usr/bin/env python3
"""Example submission for the `summarize` task (examples/01-python-data-cli.md).

Compact on purpose — this is the file the grader in demo/ scores.
"""
import argparse
import csv
import json
import sys
from collections import defaultdict
from pathlib import Path


def summarize(path: Path, by: str, on: str) -> None:
    groups = defaultdict(lambda: [0, 0.0])
    skipped = 0

    def record(item):
        nonlocal skipped
        try:
            key = item[by]
            value = float(item[on])
        except (KeyError, ValueError):
            skipped += 1
            return
        groups[key][0] += 1
        groups[key][1] += value

    if path.suffix == ".json":
        for item in json.loads(path.read_text(encoding="utf-8")):
            record(item)
    else:
        with path.open(encoding="utf-8", newline="") as fh:
            for item in csv.DictReader(fh):
                record(item)

    for key, (n, total) in sorted(groups.items()):
        print(f"{key}\t{n}\t{total / n:.2f}")
    if skipped:
        print(f"(skipped {skipped} malformed row(s))", file=sys.stderr)


def main(argv=None) -> int:
    parser = argparse.ArgumentParser(description="Per-group summary of a CSV/JSON file.")
    parser.add_argument("file", type=Path)
    parser.add_argument("--by", required=True, help="column to group by")
    parser.add_argument("--on", required=True, help="numeric column to aggregate")
    args = parser.parse_args(argv)

    if not args.file.exists():
        print(f"error: file not found: {args.file}", file=sys.stderr)
        return 1
    try:
        summarize(args.file, args.by, args.on)
    except Exception as exc:  # pragma: no cover
        print(f"error: {exc}", file=sys.stderr)
        return 1
    return 0


if __name__ == "__main__":
    raise SystemExit(main())
