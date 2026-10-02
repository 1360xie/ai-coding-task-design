# Task Specification Template

Copy this template and fill in every section before handing the task to an AI coding agent (or a human engineer). A task is "done" to the extent that a reviewer can check every acceptance criterion without asking the author for clarification.

## 1. Title

One line that names the task and its scope.

## 2. Goal

One or two sentences on what the change should accomplish, from the user's point of view. State the outcome, not the steps.

## 3. Context

What the agent starts with and what it may assume:

- Repo / files it will read or modify
- Existing conventions, stack, and versions
- Anything that is already implemented and must be preserved

## 4. Requirements

Numbered, imperative, and testable. Each requirement should be independently verifiable. Prefer "the CLI exits 0 when …" over "the CLI works".

## 5. Constraints

Hard limits and preferences:

- Stack and dependency versions
- Files that must not be touched
- Style / lint rules
- Performance or size budgets (when they matter)

## 6. Acceptance Criteria

A checklist where every item is a yes/no question a reviewer can answer mechanically.

```markdown
- [ ] Running `make test` passes all existing and new tests
- [ ] The command prints … for input …
- [ ] …
```

## 7. Evaluation Rubric

Weighted dimensions used to grade the result. Weights should sum to 100.

| Dimension | Weight | What "full marks" looks like |
| --- | --- | --- |
| Correctness | 40 | All acceptance criteria pass |
| Code quality | 25 | Readable, idiomatic, no dead code |
| Test coverage | 20 | New behaviour is covered by tests |
| Error handling | 15 | Edge cases handled; failures are loud and clear |

## 8. Traps & Edge Cases

The failure modes the agent is likely to hit. Writing these down is the difference between a task and a good task:

- Empty input, missing files, large inputs
- Case sensitivity, encodings, trailing whitespace
- Idempotency / re-running the same command

## 9. Definition of Done

A single sentence combining the above: "The task is done when every acceptance criterion passes and the reviewer can verify each one without asking a question."
