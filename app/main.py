from database import Base, engine
from fastapi import FastAPI
from fastapi.middleware.cors import CORSMiddleware
from routers import tasks

Base.metadata.create_all(bind=engine)

app = FastAPI(
    title="Task Management API",
    description="API for managing tasks and it is an assignment for flyRank internship",
)
app.include_router(tasks.router)


app.add_middleware(
    CORSMiddleware,
    allow_origins=["*"],
    allow_methods=["*"],
)


@app.get("/", status_code=200)
def root():
    return {"name": "Task API", "version": "1.0", "endpoint": ["/tasks"]}


@app.get("/health", status_code=200)
def health():
    return {"status": "ok"}
