# demo — rubric grader

A small, dependency-free Python tool that grades a submission against the
rubric declared in a task spec (markdown).

```bash
# Rule-based scoring (no API key or network needed)
python grader.py ../examples/01-python-data-cli.md example_submission.py --mock

# Print the structured prompt an LLM reviewer would answer
python grader.py ../examples/01-python-data-cli.md example_submission.py
```

The task spec follows [`../task-spec-template.md`](../task-spec-template.md).
