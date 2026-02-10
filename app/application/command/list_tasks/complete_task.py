from dataclasses import dataclass

@dataclass(frozen=True)
class CompleteTaskCommand:
   list_id: str
   task_id: str