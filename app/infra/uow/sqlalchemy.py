from typing import Callable
from sqlalchemy.orm import Session

from app.application.uow.base import UnitOfWork
from app.infra.repository.command.sqlalchemy_list_tasks import SQLAlchemyListTasksRepository


class SQLAlchemyUnitOfWork(UnitOfWork):
   def __init__(self, session_factory: Callable[[], Session]):
      self._session_factory= session_factory
   
   def __enter__(self):
      self.session: Session = self._session_factory()
      self.list_tasks_repo = SQLAlchemyListTasksRepository(self.session)
      return self
   
   def __exit__(self, exc_type, exc, tb):
      if exc_type:
         self.rollback()
      else:
         self.commit()
      self.session.close()
   
   def commit(self):
      self.session.commit()
   
   def rollback(self):
      self.session.rollback()