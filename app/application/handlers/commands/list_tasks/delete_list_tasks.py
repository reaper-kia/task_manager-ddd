from dataclasses import dataclass
from typing import Callable

from app.application.command.list_tasks.delete_list_tasks import DeleteListTasksCommand
from app.application.uow.base import UnitOfWork

@dataclass
class DeleteListTasksCommandHandler:
   uow_factory: Callable[[], UnitOfWork]
   
   def handle(self, command: DeleteListTasksCommand):
      with self.uow_factory() as uow:
         if uow.list_tasks_repo.delete(command.list_id):
            return True