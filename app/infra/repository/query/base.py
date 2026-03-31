from abc import ABC, abstractmethod
from dataclasses import dataclass

from app.application.query.dto import ListTasksReadDTO

@dataclass
class ListTasksQueryRepository(ABC):
   
   @abstractmethod
   def get_by_id(self, tilst_tasks_id: str) -> ListTasksReadDTO:
      ...
   
   @abstractmethod
   def get_all_lists(self) -> list[ListTasksReadDTO]:
      ...
