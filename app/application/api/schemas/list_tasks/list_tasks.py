from pydantic import BaseModel

from app.application.api.schemas.list_tasks.tasks import TaskResponse
from app.domain.entities.tasks import ListTasks

class CreateListTasksRequest(BaseModel):
   title: str
   description: str | None
   
class ListTasksResponse(BaseModel):
   id: str
   title: str
   description: str | None
   tasks: list[TaskResponse]
   
   @classmethod
   def from_entity(cls, list_tasks: ListTasks):
      return cls(
         id=list_tasks.id,
         title=list_tasks.title.value,
         description=list_tasks.description.value if list_tasks.description else None,
         tasks=[
            TaskResponse.from_entity(task, list_tasks.id) for task in list_tasks.tasks
         ]
      )

class GetAllListsTasksRequest(BaseModel):
   limit: int
   offset: int

