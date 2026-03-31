from dataclasses import dataclass
from typing import Callable

from app.application.command.list_tasks.complete_task import CompleteTaskCommand
from app.application.uow.base import UnitOfWork
from app.domain.entities.tasks import ListTasks, Task

@dataclass
class CompleteTaskCommandHandler:
   uow_factory: Callable[[], UnitOfWork]
   
   def handle(self, command: CompleteTaskCommand) -> ListTasks:
      with self.uow_factory() as uow:
         list_tasks=uow.list_tasks_repo.get_by_id(command.list_id)
         
         list_tasks = list_tasks.complete_task(command.task_id)
         uow.list_tasks_repo.save(list_tasks)
         
         return list_tasks