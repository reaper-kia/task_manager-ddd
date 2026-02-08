from dataclasses import dataclass
from sqlalchemy import select
from sqlalchemy.orm import Session

from app.application.query.dto import ListTasksReadDTO, TaskReadDTO
from app.infra.db.models.tasks import ListTasksModel
from app.infra.repository.query.base import ListTasksQueryRepository 

@dataclass 
class SQLAlchemyListTasksQueryRepository(ListTasksQueryRepository):
   session: Session
   
   def get_by_id(self, list_tasks_id: str):
      stmt = select(ListTasksModel).where(ListTasksModel.id == list_tasks_id)
      result = self.session.execute(stmt)
      list_tasks = result.scalars().first()
      
      if list_tasks is None:
         return None
      
      return self._to_dto(list_tasks)
   

   def get_all_lists(self):
      models = (
         self.session
         .execute(select(ListTasksModel))
         .scalars()
         .all()
         )
      return [self._to_dto(model) for model in models]
   
   
   @staticmethod
   def _to_dto(model: ListTasksModel):
      return ListTasksReadDTO(
         id=model.id,
         title=model.title,
         description=model.description if model.description else None,
         tasks=[
            TaskReadDTO(
               id=task.id,
               title=task.title,
               description=task.description if task.description else None,
               is_complete=task.is_complete,
               list_tasks_id=task.list_tasks_id,
            )
            for task in model.tasks
         ]
      )