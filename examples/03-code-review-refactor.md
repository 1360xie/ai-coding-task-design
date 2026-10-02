# 03 — Refactor: extract report formatting

## 1. Goal

Refactor a single 300-line function that both computes a report and formats it into two modules — one for computation, one for rendering — without changing any observable behaviour.

## 2. Context

- The code is in `reports.py`, function `build_report()`.
- Existing tests in `tests/test_reports.py` are the contract; do not modify them.

## 3. Requirements

1. Split `build_report()` into `compute_report()` (pure data) and `render_report()` (formatting to text/HTML).
2. Keep the public function `build_report()` as a thin wrapper so existing callers and tests keep working.
3. Add a `render_report(report, fmt)` that supports `"text"` and `"html"`; unknown `fmt` raises `ValueError`.

## 4. Constraints

- Do not change the output of existing tests.
- No new dependencies.
- Keep `compute_report()` free of I/O and formatting (graded on purity).

## 5. Acceptance Criteria

- [ ] `pytest` passes unchanged.
- [ ] `compute_report()` has no print/str-formatting calls.
- [ ] `render_report(..., "html")` escapes user-supplied strings.
- [ ] Calling `build_report()` twice returns equal results (no shared mutable state).

## 6. Evaluation Rubric

| Dimension | Weight | Full marks |
| --- | --- | --- |
| Behaviour preserved | 40 | Tests pass unchanged |
| Separation | 30 | Compute has no I/O; render has no business logic |
| Safety | 15 | HTML output is escaped |
| Tests added | 15 | New tests cover `render_report` and the `ValueError` path |

## 7. Traps & Edge Cases

- HTML injection via `<`, `>`, `&` in report fields.
- Hidden coupling: the original function mutated a module-level cache — make sure the refactor doesn't.
- The `"text"` vs `"html"` branch must be exhaustive; unknown format must fail loudly.
