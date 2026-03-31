from dataclasses import dataclass

@dataclass(frozen=True)
class ListTasksReadDTO:
   id: str
   title: str
   description: str | None
   tasks: list["TaskReadDTO"]

   
@dataclass(frozen=True)
class TaskReadDTO:
   id: str
   title: str
   description: str | None
   is_complete: bool
   list_tasks_id: str