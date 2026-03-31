from dataclasses import dataclass
from datetime import datetime

from app.domain.entities.base import BaseEntity
from app.domain.value_objects.users import Email, Name

@dataclass
class User(BaseEntity):
   name: Name
   data_created: datetime
   email: Email
   password_hash: str