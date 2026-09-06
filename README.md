# Task Manager API

A simple RESTful API for managing tasks, built with **FastAPI**, **SQLAlchemy**, and **SQLite**.

## Features

- ✅ Create, read, update, and delete tasks (CRUD)
- 🔍 Filter tasks by completion status
- 🔎 Search tasks by title
- 💚 Health check endpoint
- 🔄 Reset all tasks endpoint

## Tech Stack

| Technology | Icon |
|-----------|------|
| Python | 🐍 |
| FastAPI | ⚡ |
| SQLAlchemy | 🔗 |
| SQLite | 💾 |
| Pydantic | ✅ |

## Project Structure

```text
task-manager-api/
├── app/
│   ├── main.py               # FastAPI app entry point
│   ├── database.py           # DB engine/session configuration
│   ├── models.py             # SQLAlchemy models
│   ├── schemas.py            # Pydantic request/response schemas
│   └── routers/
│       └── tasks.py          # Task API routes
├── .gitignore
└── README.md
```

## Requirements

- Python 3.10+

## Installation

1. Clone the repository:

```bash
git clone https://github.com/omar23py/task-manager-api.git
cd task-manager-api
```

2. (Optional but recommended) Create and activate a virtual environment:

```bash
python -m venv .venv
source .venv/bin/activate        # macOS/Linux
# .venv\Scripts\activate         # Windows PowerShell
```

3. Install dependencies:

```bash
pip install fastapi uvicorn sqlalchemy pydantic
```

## Run the API

From the project root:

```bash
uvicorn app.main:app --reload
```

The API will be available at:

- Base URL: `http://127.0.0.1:8000`
- Swagger UI: `http://127.0.0.1:8000/docs`
- ReDoc: `http://127.0.0.1:8000/redoc`

## Database

- Uses SQLite with database file: `app.db`
- Tables are auto-created on startup via:
  - `Base.metadata.create_all(bind=engine)`

## API Endpoints

### Utility

- `GET /` — API metadata
- `GET /health` — Health check

### Tasks

- `GET /tasks/` — Get all tasks with optional filtering by title or completion status
- `GET /tasks/{id}` — Get a task by ID
- `POST /tasks/` — Create a new task
- `PUT /tasks/{id}` — Update an existing task (partial update supported)
- `DELETE /tasks/{id}` — Delete a task
- `POST /tasks/reset` — Reset all tasks (delete all tasks from database)

## Query Parameters

The `GET /tasks/` endpoint supports optional query parameters:

- `search` (string, optional) — Search for tasks by title. Provide a string to search for tasks containing that string in their title.
- `done` (boolean, optional) — Filter tasks based on their completion status. Set to `true` to retrieve completed tasks, or `false` for incomplete tasks.

## Example Requests

### Create a task:

```bash
curl -X POST "http://127.0.0.1:8000/tasks/" \
  -H "Content-Type: application/json" \
  -d '{
    "title": "Finish assignment",
    "description": "Complete the Task Manager API",
    "done": false
  }'
```

### Get all tasks:

```bash
curl -X GET "http://127.0.0.1:8000/tasks/"
```

### Get completed tasks:

```bash
curl -X GET "http://127.0.0.1:8000/tasks/?done=true"
```

### Search tasks by title:

```bash
curl -X GET "http://127.0.0.1:8000/tasks/?search=assignment"
```

### Update a task:

```bash
curl -X PUT "http://127.0.0.1:8000/tasks/1" \
  -H "Content-Type: application/json" \
  -d '{
    "done": true
  }'
```

### Delete a task:

```bash
curl -X DELETE "http://127.0.0.1:8000/tasks/1"
```

### Reset all tasks:

```bash
curl -X POST "http://127.0.0.1:8000/tasks/reset"
```

## Notes

- CORS is currently configured with permissive defaults (`allow_origins=["*"]`).
- This API is built as an assignment for flyRank internship.

## Author

[@omar23py](https://github.com/omar23py)
