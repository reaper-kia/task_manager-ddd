from dataclasses import dataclass
from typing import Callable

from app.application.command.list_tasks.create_list_tasks import CreateListTasksCommand
from app.application.uow.base import UnitOfWork
from app.domain.entities.tasks import ListTasks
from app.domain.value_objects.tasks import Description, Title

@dataclass
class CreateListTasksCommandHandler:
   uow_factory: Callable[[], UnitOfWork]
   
   def handle(self, command: CreateListTasksCommand) -> ListTasks:
      with self.uow_factory() as uow:
         list_tasks= ListTasks(
            title=Title(command.title),
            description=Description(command.description) if command.description else None,
            tasks=[], 
         )
         
         uow.list_tasks_repo.save(list_tasks)
         return list_tasks