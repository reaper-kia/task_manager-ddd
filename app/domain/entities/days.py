from dataclasses import dataclass, field
from datetime import date
from uuid import uuid4


from app.domain.entities.base import BaseEntity


@dataclass
class Calendar:
   id: str = field(default_factory=lambda:str(uuid4()))
   days: dict[date: 'Day']
   
   def add_list_to_day(self, date: date, list_tasks_id: str):
      if date not in self.days:
         self.days[date] = Day(date, [])
      self.days[date].add_list_tasks(list_tasks_id)

@dataclass 
class Day(BaseEntity):
   date: date
   list_tasks_ids: list[str]
   calendar_id: str
   
   def add_list_tasks(self, list_tasks_id: str):
      if list_tasks_id not in self.list_tasks_ids:
         self.list_tasks_ids.append(list_tasks_id)
   
   def remove_list_tasks(self, list_tasks_id: str):
      if list_tasks_id in self.list_tasks_ids:
         self.list_tasks_ids.remove(list_tasks_id)