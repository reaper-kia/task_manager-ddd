from dataclasses import dataclass

@dataclass(frozen=True)
class DeleteTaskCommand:
   list_id: str
   task_id: str