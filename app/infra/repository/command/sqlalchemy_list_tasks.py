from dataclasses import dataclass
from sqlalchemy import select
from sqlalchemy.orm import Session

from app.domain.entities.tasks import ListTasks
from app.infra.db.models.tasks import ListTasksModel, TaskModel
from app.infra.repository.command.base import ListTasksRepository

@dataclass
class SQLAlchemyListTasksRepository(ListTasksRepository):
   session: Session
   
   def add(self, list_tasks: ListTasks):
      model = ListTasksModel.from_entity(list_tasks=list_tasks)
      self.session.add(model)
   
   def save(self, list_tasks: ListTasks):
      model = self.session.get(ListTasksModel, list_tasks.id)
      
      if model is None:
         self.add(list_tasks)
         return
      
      model.title = list_tasks.title.value
      model.description = list_tasks.description.value if list_tasks.description else None
      
      model.tasks.clear()
      model.tasks.extend(
         TaskModel.from_entity(task=task, list_tasks_id=list_tasks.id) for task in list_tasks.tasks 
      )
   
   def delete(self, list_tasks_id: str):
      model = self.session.get(ListTasksModel, list_tasks_id)
      if model:  
         self.session.delete(model)
         return True
   
   def get_by_id(self, list_tasks_id: str) -> ListTasks:
      stmt = select(ListTasksModel).where(ListTasksModel.id == list_tasks_id)
      result = self.session.execute(stmt)
      list_tasks = result.scalars().first()
      
      if list_tasks is None:
         return None
      
      return list_tasks.to_entity()