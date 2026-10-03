# 01 — Python Data CLI: `summarize`

## 1. Goal

A command-line tool that reads a CSV or JSON file of records and prints a per-group summary to stdout.

## 2. Context

- Language: Python 3.10+, standard library only (no pandas).
- The tool lives in a new module `summarize/` with a `__main__.py` entry point.
- Input files are UTF-8 encoded.

## 3. Requirements

1. `python -m summarize <file> --by <column> --on <numeric-column>` prints, for each distinct value of `<column>`, the count and the mean of `<numeric-column>`.
2. Support both CSV and JSON input; detect the format from the file extension.
3. Exit `0` on success and non-zero with a clear message on any error (missing file, unknown column, unparsable row).
4. Print a `--help` message.

## 4. Constraints

- Standard library only.
- Do not read the entire file into memory; stream row-by-row (the spec is graded on this).

## 5. Acceptance Criteria

- [ ] `python -m summarize data.csv --by region --on sales` prints one line per region with correct counts and means.
- [ ] A JSON file produces identical output to the equivalent CSV.
- [ ] A missing file exits non-zero and prints a message to stderr.
- [ ] An unknown `--by` column exits non-zero with the column name in the message.

## 6. Evaluation Rubric

| Dimension | Weight | Full marks |
| --- | --- | --- |
| Correctness | 40 | All acceptance criteria pass on the provided fixtures |
| Streaming | 20 | Never holds more than one row in memory at once |
| Error handling | 20 | Every failure mode in §8 produces a clear, non-zero exit |
| Style | 20 | Idiomatic, typed, no dead code |

## 7. Traps & Edge Cases

- Empty file → print nothing and exit 0.
- Column values with commas inside quotes (CSV quoting).
- Non-numeric values in the `--on` column → skip the row and report the count of skipped rows.
- Re-running produces identical output (no global mutable state).
- `--by` and `--on` naming the same column → exit non-zero with a clear message.
