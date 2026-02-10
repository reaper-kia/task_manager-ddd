from dataclasses import dataclass
from datetime import date

@dataclass(frozen=True)
class CreateListTasksCommand:
   title: str
   description: str | None