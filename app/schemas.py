from pydantic import BaseModel, Field
from typing import Optional


class TaskBase(BaseModel):
    title: str = Field(min_length=2, max_length=100)
    description: str = Field(min_length=2, max_length=1000)
    done: bool = Field(default=False)


class TaskCreate(TaskBase):
    pass


class TaskUpdate(BaseModel):
    title: Optional[str] = Field(default=None, min_length=2, max_length=100)
    description: Optional[str] = Field(default=None, min_length=2, max_length=1000)
    done: Optional[bool] = Field(default=None)


class TaskRead(TaskBase):
    id: int
    model_config = {"from_attributes": True}


class QueryParams(BaseModel):
    search: str | None = Field(
        default=None,
        min_length=1,
        max_length=100,
        example="project",
        description="Search for tasks by title. Provide a string to search for tasks containing that string in their title.",
    )
    done: bool | None = Field(
        default=None,
        example=True,
        description="Filter tasks based on their completion status. Set to true to retrieve completed tasks, or false for incomplete tasks.",
    )
