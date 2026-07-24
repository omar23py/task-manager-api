from sqlalchemy import Column,Integer,String,Boolean
from database import Base

class Task (Base):
    __tablename__="tasks"
    id=Column(Integer,primary_key=True,autoincrement=True,index=True,nullable=False)
    title=Column(String(100),default=f"Task {id}",nullable=False)
    description=Column(String(1000),nullable=True)
    done=Column(Boolean,default=False)
    
    
    
    