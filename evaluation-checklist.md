# Task Evaluation Checklist

Use this to judge whether a coding task is ready to hand to an agent. Score each item 0 (missing) or 1 (present); a task is ready at 12/15 or better.

## Clarity

- [ ] The goal states the outcome, not the steps.
- [ ] Every requirement is independently verifiable.
- [ ] A reviewer who has not seen the task before can tell when it is done.

## Verifiability

- [ ] Acceptance criteria are yes/no checkboxes, not prose.
- [ ] At least one criterion asserts a concrete output (exact string, exit code, file).
- [ ] The rubric weights sum to 100 and name what "full marks" means.

## Constraints & scope

- [ ] The stack and versions are pinned.
- [ ] Files that must not be touched are named explicitly.
- [ ] The task is scoped small enough to finish in one session.

## Failure modes

- [ ] At least three traps/edge cases are written down.
- [ ] Error paths specify the expected exit code or status.
- [ ] Idempotency / re-runnability is addressed.

## Testability

- [ ] A mechanical way to check the result exists (tests, fixture, script).
- [ ] Fixtures or sample inputs are provided or referenced.
- [ ] At least one rubric dimension rewards tests or verification.
