from dataclasses import dataclass
import re

from app.domain.exceptions.tasks import TextToLongException
from app.domain.value_objects.base import BaseValueObject

@dataclass(frozen=True)
class Name(BaseValueObject):
   value: str
   
   def validate(self):
      if len(self.value) > 255:
         raise TextToLongException(self.value)
   
   def as_generic_type(self):
      return str(self.value)


EMAIL_REGEX = re.compile(r"^[^@\s]+@[^@\s]+\.[^@\s]+$")

@dataclass(frozen=True)
class Email(BaseValueObject):
   value: str
   
   def validate(self):
      if not EMAIL_REGEX.match(self.value):
         raise ValueError("Invalid format email")
   
   def as_generic_type(self):
      return str(self.value)

