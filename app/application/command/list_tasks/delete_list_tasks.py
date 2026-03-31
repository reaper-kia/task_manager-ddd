from dataclasses import dataclass

@dataclass(frozen=True)
class DeleteListTasksCommand:
   list_id: str