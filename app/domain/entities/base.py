from abc import ABC
from dataclasses import dataclass, field
from uuid import uuid4 

@dataclass(kw_only=True)
class BaseEntity:
   id: str = field(default_factory=lambda:str(uuid4()))