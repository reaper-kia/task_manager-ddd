from dataclasses import dataclass
from typing import Callable

from app.application.command.list_tasks.add_task_to_list import AddTaskToListCommand
from app.application.uow.base import UnitOfWork
from app.domain.entities.tasks import Task
from app.domain.value_objects.tasks import Description, Title

@dataclass 
class AddTaskToListCommandHandler:
   uow_factory: Callable[[], UnitOfWork]
   
   def handle(self, command: AddTaskToListCommand):
      with self.uow_factory() as uow:
         list_tasks = uow.list_tasks_repo.get_by_id(command.id_list)
         
         list_tasks.add_task(Task.create(
            title=Title(command.title_task),
            description=Description(command.description_task) if command.description_task else None,
         ))
         
         uow.list_tasks_repo.save(list_tasks)
      return {'opertion': 'success'}