from abc import ABC, abstractmethod
from dataclasses import dataclass

from app.domain.entities.tasks import ListTasks
from app.infra.db.models.tasks import ListTasksModel

@dataclass
class ListTasksRepository(ABC):
   
   @abstractmethod
   def add(self, list_tasks: ListTasks):
      ...

   @abstractmethod
   def save(self, list_tasks: ListTasks):
      ...
            
   @abstractmethod
   def delete(self, list_tasks_id: str):
      ...
   
   @abstractmethod
   def get_by_id(self, lost_tasks_id: str) -> ListTasksModel:
      ...

@dataclass
class CalendarRepository(ABC):
   
   @abstractmethod
   def save(self):
      ...