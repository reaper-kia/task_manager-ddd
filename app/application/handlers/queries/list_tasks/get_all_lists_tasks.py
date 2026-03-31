from dataclasses import dataclass

from app.application.query.dto import ListTasksReadDTO
from app.application.query.list_tasks.get_all_lists_tasks import GetAllListsTasksQuery
from app.infra.repository.query.base import ListTasksQueryRepository

@dataclass(frozen=True)
class GetAllListsTasksQueryHandler:
   repo: ListTasksQueryRepository
   
   def handle(self, query: GetAllListsTasksQuery) -> list[ListTasksReadDTO]:
      return self.repo.get_all_lists()