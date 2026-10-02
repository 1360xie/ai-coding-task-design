# 02 — Full-stack Task API: tasks CRUD

## 1. Goal

A minimal full-stack "tasks" app: a REST API plus a browser UI that can create, list, and complete tasks.

## 2. Context

- Backend: Python + FastAPI + SQLite (via SQLAlchemy).
- Frontend: plain HTML/CSS/JS served as static files by the same app (no build step).
- Single process: the API and the static frontend run together.

## 3. Requirements

1. `POST /tasks` creates a task `{title, done}` and returns it with an `id`.
2. `GET /tasks` returns all tasks, newest first.
3. `PATCH /tasks/{id}` toggles `done`.
4. `DELETE /tasks/{id}` removes a task and returns `204`.
5. The frontend at `/` lists tasks and lets the user add and complete them without a page reload.

## 4. Constraints

- No frontend framework or build step.
- Validate `title` (non-empty, ≤ 200 chars) and return `422` on violation.
- Persist to SQLite; the database file must be git-ignored.

## 5. Acceptance Criteria

- [ ] `POST /tasks` with `{"title": "write tests"}` returns `201` with an `id` and `done=false`.
- [ ] `GET /tasks` returns the created task.
- [ ] `PATCH /tasks/{id}` with `{"done": true}` flips the flag; a second identical `PATCH` leaves it `true` (idempotent).
- [ ] `DELETE` of a missing id returns `404` with a JSON error body.
- [ ] A `title` longer than 200 chars returns `422`.

## 6. Evaluation Rubric

| Dimension | Weight | Full marks |
| --- | --- | --- |
| API correctness | 40 | All acceptance criteria pass |
| Data layer | 20 | Proper ORM usage, no raw string SQL |
| Error handling | 20 | Consistent JSON error shape, correct status codes |
| Frontend | 20 | Functional without a build step; clear, accessible markup |

## 7. Traps & Edge Cases

- Concurrent requests must not corrupt SQLite (use a session per request).
- JSON body with missing/extra fields → `422`, not a crash.
- Frontend must handle an empty task list gracefully.
