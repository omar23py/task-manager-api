
from pydoc import text
from fastapi import APIRouter, Depends,HTTPException,status
from sqlalchemy import text
from database import get_db
from schemas import TaskRead,TaskCreate,TaskUpdate
from sqlalchemy.orm import Session
from models import Task

router=APIRouter(prefix="/tasks",tags=["Tasks"])

@router.get('/',response_model=list[TaskRead],status_code=status.HTTP_200_OK)
def getAll(db:Session=Depends(get_db)):
   return db.query(Task).all()



@router.get('/{id}',response_model=TaskRead,status_code=status.HTTP_200_OK)
def getId(id: int, db:Session=Depends(get_db)):
    task=db.query(Task).filter(Task.id==id).first() 
    if not task:
        raise HTTPException(status_code=status.HTTP_404_NOT_FOUND, detail="Task not found")
    return task



@router.get('/done/{done}',status_code=status.HTTP_200_OK,response_model=list[TaskRead])
def get_byDone(done:bool,db:Session=Depends(get_db)):
    return db.query(Task).filter(Task.done==done).all()
    

@router.get('/search/{search}',status_code=status.HTTP_200_OK,response_model=list[TaskRead])
def get_byTitle(search:str,db:Session=Depends(get_db)):
    task=db.query(Task).filter(Task.title.ilike(f"%{search}%")).all()
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
        raise HTTPException(status_code=status.HTTP_400_BAD_REQUEST,detail="No data provided for update")
    update_task=db.query(Task).filter(Task.id==id).update(data)
    if not update_task:
        raise HTTPException(status_code=status.HTTP_404_NOT_FOUND,detail="Task not Found")
    db.commit()
    return {"message":"Task updated successfully"}


@router.delete('/{id}',status_code=status.HTTP_204_NO_CONTENT)
def delete_task(id:int,db:Session=Depends(get_db)):
    task=db.query(Task).filter(Task.id==id).first()
    if not task:
        raise HTTPException(status_code=status.HTTP_404_NOT_FOUND,detail="Task not Found")
    db.delete(task)
    db.commit()
    return {"message":"Task deleted successfully"}





    
    
    
    

