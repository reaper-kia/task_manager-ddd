from dataclasses import dataclass

from app.application.query.dto import ListTasksReadDTO
from app.application.query.list_tasks.get_list_tasks import GetListTasksQuery
from app.infra.repository.query.base import ListTasksQueryRepository

@dataclass(frozen=True)
class GetListTasksQueryHandler:
   repo: ListTasksQueryRepository
   
   def handle(self, query: GetListTasksQuery) -> ListTasksReadDTO:
      return self.repo.get_by_id(query.list_tasks_id)