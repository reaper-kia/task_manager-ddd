from dataclasses import dataclass
from typing import Callable, Dict

@dataclass
class Mediator:
   handlers: Dict[type, Callable]
   
   def register(self, message_type: type, handler: Callable):
      self.handlers[message_type] = handler
   
   def send(self, message):
      handler = self.handlers[type(message)]
      
      if not handler:
         raise ValueError(f"not found handler")
      
      return handler.handle(message)