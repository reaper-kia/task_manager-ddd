from dataclasses import dataclass

@dataclass(frozen=True)
class GetListTasksQuery:
   list_tasks_id: str