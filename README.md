# AI Coding Task Design

![CI](https://github.com/1360xie/ai-coding-task-design/actions/workflows/ci.yml/badge.svg)
![Python 3.10+](https://img.shields.io/badge/Python-3.10%2B-blue)
![License: MIT](https://img.shields.io/badge/License-MIT-yellow)

A practical framework and a set of worked examples for **designing high-quality coding tasks for AI coding agents** — tasks that produce correct, reviewable, and testable results on the first attempt.

The core idea: an AI coding agent is only as good as the task you give it. This repository captures a repeatable way to turn a vague request ("build me a CLI") into a task specification an agent can execute and a reviewer can grade.

## What's inside

| Path | What it is |
| --- | --- |
| [`task-spec-template.md`](task-spec-template.md) | The reusable task specification template |
| [`examples/`](examples/) | Complete, ready-to-use task specs (Python CLI, full-stack API, refactor) |
| [`evaluation-checklist.md`](evaluation-checklist.md) | A checklist for judging whether a task is well designed |
| [`demo/`](demo/) | A small Python tool that grades a submission against a task's rubric |

## The method

A good coding task is **specific about the outcome, explicit about the constraints, and verifiable without ambiguity**. Every task carries six pieces:

1. **Goal** — the outcome, stated from the user's point of view.
2. **Context** — the repo, stack, and conventions the agent starts with.
3. **Requirements** — numbered, imperative, independently testable.
4. **Acceptance criteria** — a checklist of yes/no checks a reviewer can answer mechanically.
5. **Evaluation rubric** — weighted dimensions that sum to 100 and name what "full marks" means.
6. **Traps & edge cases** — the likely failure modes, written down before the agent runs into them.

When the rubric is written before the code, "does this pass?" stops being an opinion and becomes a checklist.

## Quick start

```bash
# Rule-based scoring of a submission against a task's rubric (no API key, no network).
python demo/grader.py examples/01-python-data-cli.md demo/example_submission.py --mock

# Print the structured prompt an LLM reviewer would answer instead.
python demo/grader.py examples/01-python-data-cli.md demo/example_submission.py
```

## Verification

A small, dependency-free test suite and a CI workflow keep the repo honest:

```bash
python -m unittest discover -s tests -v
```

Every push runs the same checks on Python 3.10-3.12 (see [`.github/workflows/ci.yml`](.github/workflows/ci.yml)).

## Background

I work across the stack — Python, frontend, and backend. These specs reflect how real coding tasks get decomposed: explicit interfaces, testable acceptance criteria, and rubrics a reviewer can apply mechanically.
