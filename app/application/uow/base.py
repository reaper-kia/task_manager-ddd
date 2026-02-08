from abc import ABC, abstractmethod
from typing import Optional

from app.infra.repository.base import CalendarRepository, ListTasksRepository


class UnitOfWork(ABC):
   list_tasks_repo: Optional[ListTasksRepository] = None
   calendar_repo: Optional[CalendarRepository]
   
   @abstractmethod
   def __enter__(self):
      ...
   
   @abstractmethod
   def __exit__(self, exc_type):
      ...
   
   @abstractmethod
   def commit(self):
      ...
   
   @abstractmethod
   def rollback(self):
      ...