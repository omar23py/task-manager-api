
from pydoc import text
from fastapi import APIRouter, Depends,HTTPException,status,Query
from sqlalchemy import text
from database import get_db
from schemas import TaskRead,TaskCreate,TaskUpdate,QueryParams
from sqlalchemy.orm import Session
from models import Task
from typing import Annotated

router=APIRouter(prefix="/tasks",tags=["Tasks"])




@router.get('/{id}',response_model=TaskRead,status_code=status.HTTP_200_OK)
def getId(id: int, db:Session=Depends(get_db)):
    task=db.query(Task).filter(Task.id==id).first() 
    if not task:
        raise HTTPException(status_code=status.HTTP_404_NOT_FOUND, detail="Task not found")
    return task

@router.get('/',status_code=status.HTTP_200_OK,response_model=list[TaskRead],summary="Get tasks with optional filtering",description="Retrieve a list of tasks with optional filtering based on title and completion status. You can provide query parameters to filter the results.")
def get_tasks(params: Annotated[QueryParams, Query()],db:Session=Depends(get_db)):
    query = db.query(Task)
    if params.search is not None:
        query = query.filter(Task.title.ilike(f"%{params.search}%"))
    if params.done is not None:
        query = query.filter(Task.done == params.done)
    task = query.all()
    if not task:
         raise HTTPException(status_code=status.HTTP_404_NOT_FOUND,detail="Task not found")
    return task

@router.post('/',status_code=status.HTTP_201_CREATED,response_model=TaskRead)
def create_task(task:TaskCreate,db:Session=Depends(get_db)):
    new_task=Task(**task.model_dump())
    db.add(new_task)
    db.commit()
    db.refresh(new_task)
    return new_task


@router.post('/reset')
def reset_tasks(db:Session=Depends(get_db)):
    db.query(Task).delete()
    db.commit()
    return {"message":"All tasks have been reset successfully"}


@router.put('/{id}',status_code=status.HTTP_200_OK)
def update_task(id:int,task:TaskUpdate,db:Session=Depends(get_db)):
    data=task.model_dump(exclude_unset=True)
    if not data:
        raise HTTPException(status_code=status.HTTP_400_BAD_REQUEST,detail="No fields provided for update")
    task_db=db.query(Task).filter(Task.id==id).first()
    if not task_db:
        raise HTTPException(status_code=status.HTTP_404_NOT_FOUND,detail="Task not Found")
    for key,value in data.items():
        setattr(task_db,key,value)
    db.commit()
    db.refresh(task_db)
    return {"message":"Task updated successfully","task":task_db}    
        
   


@router.delete('/{id}',status_code=status.HTTP_204_NO_CONTENT)
def delete_task(id:int,db:Session=Depends(get_db)):
    task=db.query(Task).filter(Task.id==id).first()
    if not task:
        raise HTTPException(status_code=status.HTTP_404_NOT_FOUND,detail="Task not Found")
    db.delete(task)
    db.commit()
    return {"message":"Task deleted successfully"}





    
    
    
    

