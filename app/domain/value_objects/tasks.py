from dataclasses import dataclass

from app.domain.exceptions.tasks import EmptyTextException, TextToLongException
from app.domain.value_objects.base import BaseValueObject 

@dataclass(frozen=True)
class Title(BaseValueObject):
   value: str
   
   def validate(self):
      if len(self.value) <= 0:
         raise EmptyTextException(self.value)
      
      if len(self.value) > 255:
         raise TextToLongException(self.value)
   
   def as_generic_type(self):
      return str(self.value)

@dataclass(frozen=True)
class Description(BaseValueObject):
   value: str
   
   def validate(self):
      if len(self.value) <= 0:
         raise EmptyTextException(self.value)
      
      if len(self.value) > 1023:
         raise TextToLongException(self.value)
   
   def as_generic_type(self):
      return str(self.value)