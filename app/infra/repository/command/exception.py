from dataclasses import dataclass

@dataclass
class NotFound(Exception):
   value: str
   @property
   def message(self):
      return f"not found list_tasks with id: {self.value}"