from dataclasses import dataclass, field
from uuid import uuid4

from app.domain.entities.base import BaseEntity
from app.domain.exceptions.tasks import NotFoundTask, TaskAlreadyCompleteException
from app.domain.value_objects.tasks import Description, Title

@dataclass 
class Task(BaseEntity):
   title: Title
   description: Description | None = None
   is_complete: bool = False
   
   @classmethod
   def create(
      cls,
      title: Title,
      description: Description = None,
   ):
      return cls(
         title=title,
         description=description,
         )
   
   def _complete(self) -> 'Task':
      if self.is_complete:
         raise TaskAlreadyCompleteException(self.id)   
      self.is_complete = True
      return self

@dataclass
class ListTasks(BaseEntity):
   title: Title
   description: Description | None = None
   tasks: list[Task] = field(default_factory=list)

   
   def add_task(self, task: Task):
      self.tasks.append(task)
   
   def get_task(self, task_id: str) -> Task:
      for task in self.tasks:
         if task.id == task_id:
            return task
      raise NotFoundTask(task_id)
   
   def complete_task(self, task_id: str):
      task = self.get_task(task_id)
      task._complete()
      return self
   
   def remove_task(self, task_id):
      task = self.get_task(task_id)
      self.tasks.remove(task)