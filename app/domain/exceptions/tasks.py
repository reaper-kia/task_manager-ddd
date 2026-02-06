from dataclasses import dataclass

from app.domain.exceptions.base import ApplicationException 

@dataclass
class TextToLongException(ApplicationException):
   value: str
   
   @property
   def message(self):
      return f"Text to long error - {self.value}"

@dataclass 
class EmptyTextException(ApplicationException):
   value: str
   
   @property
   def message(self):
      return f"Text should not be empty error - {self.value}"

@dataclass 
class TaskAlreadyCompleteException(ApplicationException):
   value: str
   
   @property
   def message(self):
      return f"Task already complete - {self.value}"

@dataclass 
class NotFoundTask(ApplicationException):
   value: str
   
   @property
   def message(self):
      return f"Not found task with id: {self.value}"