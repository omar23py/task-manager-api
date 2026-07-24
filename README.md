# Task Manager API

A simple RESTful API for managing tasks, built with **FastAPI**, **SQLAlchemy**, and **SQLite**.

## Features

- Create, read, update, and delete tasks (CRUD)
- Filter tasks by completion status
- Search tasks by title
- Health check endpoint
- Automatic interactive API docs via Swagger UI

## Tech Stack

- Python
- FastAPI
- SQLAlchemy
- SQLite
- Pydantic

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

- `GET /tasks/` — Get all tasks
- `GET /tasks/{id}` — Get a task by ID
- `GET /tasks/done/{done}` — Get tasks filtered by done status (`true`/`false`)
- `GET /tasks/search/{search}` — Search tasks by title
- `POST /tasks/` — Create a new task
- `PUT /tasks/{id}` — Update an existing task (partial update supported)
- `DELETE /tasks/{id}` — Delete a task

## Example Request

Create a task:

```bash
curl -X POST "http://127.0.0.1:8000/tasks/" \
  -H "Content-Type: application/json" \
  -d '{
    "title": "Finish assignment",
    "description": "Complete the Task Manager API",
    "done": false
  }'
```

## Notes

- CORS is currently configured with permissive defaults (`allow_origins=["*"]`).
- This project currently uses SQLite for local development and learning purposes.

## Author

[@omar23py](https://github.com/omar23py)
