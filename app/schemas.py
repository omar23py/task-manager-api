from pydantic import BaseModel,Field
from typing import Optional




class TaskBase(BaseModel):
        title : str = Field(min_length=2,max_length=100)
        description : str = Field(min_length=2,max_length=1000)
        done: bool = Field(default=False)
        
        

class TaskCreate(TaskBase):
        pass


class TaskUpdate(BaseModel):
    title: Optional[str] = Field(default=None, min_length=2, max_length=100)
    description: Optional[str] = Field(default=None, min_length=2, max_length=1000)
    done: Optional[bool] = Field(default=None)
  
class TaskRead(TaskBase):
        id : int
        model_config = {"from_attributes": True}
       
       