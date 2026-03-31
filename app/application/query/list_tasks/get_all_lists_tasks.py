from dataclasses import dataclass

@dataclass(frozen=True)
class GetAllListsTasksQuery:
   limit: int
   offset: int