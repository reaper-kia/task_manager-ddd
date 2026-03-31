from dataclasses import dataclass
from typing import Callable

from app.application.command.list_tasks.delete_task import DeleteTaskCommand
from app.application.uow.base import UnitOfWork

@dataclass
class DeleteTaskCommandHandler:
   uow_factory: Callable[[], UnitOfWork]
   
   def handle(self, command: DeleteTaskCommand):
      with self.uow_factory() as uow:
         list_tasks = uow.list_tasks_repo.get_by_id(command.list_id)
         
         list_tasks.remove_task(command.task_id)
         uow.list_tasks_repo.save(list_tasks)
         
         return True