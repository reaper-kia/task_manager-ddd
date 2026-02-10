from pydantic import BaseModel

from app.domain.entities.tasks import Task

class AddTaskRequest(BaseModel):
   list_id: str
   title: str
   description: str

class TaskResponse(BaseModel):
   id: str
   title: str
   description: str
   is_complete: bool
   list_tasks_id: str
   
   @classmethod
   def from_entity(cls, task: Task, list_tasks_id: str):
      return cls(
         id=task.id,
         title=task.title.value,
         description=task.description.value if task.description else None,
         is_complete=task.is_complete,
         list_tasks_id=list_tasks_id
      )

class CompleteTaskRequest(BaseModel):
   list_id: str
   task_id: str

class DeleteTaskRequest(BaseModel):
   list_id: str
   task_id: str