from dataclasses import dataclass
from datetime import date


from app.domain.entities.base import BaseEntity
from app.domain.entities.tasks import ListTasks

@dataclass 
class Day(BaseEntity):
   date: date
   list_tasks: ListTasks
