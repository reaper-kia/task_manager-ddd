from app.application.command.list_tasks.add_task_to_list import AddTaskToListCommand
from app.application.command.list_tasks.complete_task import CompleteTaskCommand
from app.application.command.list_tasks.create_list_tasks import CreateListTasksCommand
from app.application.command.list_tasks.delete_list_tasks import DeleteListTasksCommand
from app.application.command.list_tasks.delete_task import DeleteTaskCommand
from app.application.handlers.commands.list_tasks.add_task_to_list import AddTaskToListCommandHandler
from app.application.handlers.commands.list_tasks.complete_task import CompleteTaskCommandHandler
from app.application.handlers.commands.list_tasks.create_list_tasks import CreateListTasksCommandHandler


from app.application.handlers.commands.list_tasks.delete_list_tasks import DeleteListTasksCommandHandler
from app.application.handlers.commands.list_tasks.delete_task import DeleteTaskCommandHandler
from app.application.handlers.queries.list_tasks.get_all_lists_tasks import GetAllListsTasksQueryHandler
from app.application.handlers.queries.list_tasks.get_list_tasks import GetListTasksQueryHandler
from app.application.mediator.mediator import Mediator
from app.application.query.list_tasks.get_all_lists_tasks import GetAllListsTasksQuery
from app.application.query.list_tasks.get_list_tasks import GetListTasksQuery


def build_mediator(uow_factory, query_repo) -> Mediator:
   mediator = Mediator(handlers={})
   
   #COMMAND
   mediator.register(AddTaskToListCommand, AddTaskToListCommandHandler(uow_factory))
   mediator.register(CompleteTaskCommand, CompleteTaskCommandHandler(uow_factory))
   mediator.register(CreateListTasksCommand, CreateListTasksCommandHandler(uow_factory))
   mediator.register(DeleteTaskCommand, DeleteTaskCommandHandler(uow_factory))
   mediator.register(DeleteListTasksCommand, DeleteListTasksCommandHandler(uow_factory))
   #QUERY
   mediator.register(GetAllListsTasksQuery, GetAllListsTasksQueryHandler(query_repo))
   mediator.register(GetListTasksQuery, GetListTasksQueryHandler(query_repo))
   
   
   return mediator