from fastapi import APIRouter, Depends

from app.application.api.deps import get_mediator
from app.application.api.schemas.list_tasks.list_tasks import CreateListTasksRequest, GetAllListsTasksRequest, ListTasksResponse
from app.application.api.schemas.list_tasks.tasks import AddTaskRequest, CompleteTaskRequest, DeleteTaskRequest, TaskResponse
from app.application.command.list_tasks.add_task_to_list import AddTaskToListCommand
from app.application.command.list_tasks.complete_task import CompleteTaskCommand
from app.application.command.list_tasks.create_list_tasks import CreateListTasksCommand
from app.application.command.list_tasks.delete_list_tasks import DeleteListTasksCommand
from app.application.command.list_tasks.delete_task import DeleteTaskCommand
from app.application.mediator.mediator import Mediator
from app.application.query.list_tasks.get_all_lists_tasks import GetAllListsTasksQuery
from app.application.query.list_tasks.get_list_tasks import GetListTasksQuery

router = APIRouter(
   prefix='/list_tasks',
   tags=['List Tasks']
)

@router.post('/')
def crete_list_tasks(
   data: CreateListTasksRequest,
   mediator: Mediator = Depends(get_mediator)
):
   list_tasks = mediator.send(CreateListTasksCommand(
      title=data.title,
      description=data.description,
   ))
   
   return ListTasksResponse(
      id=list_tasks.id,
      title=list_tasks.title.value,
      description=list_tasks.description.value if list_tasks.description else None,
      tasks=[
         TaskResponse(
            id=task.id,
            title=task.title.value,
            description=task.description.value if task.description else None,
            list_tasks_id=list_tasks.id
        )
        for task in list_tasks.tasks
      ]
             
   )

@router.post('/add_task')
def add_task_to_list(
   data: AddTaskRequest,
   mediator: Mediator = Depends(get_mediator)
):
   if mediator.send(AddTaskToListCommand(
      id_list=data.list_id,
      title_task=data.title,
      description_task=data.description if data.description else None,
   )):
      return {'opertion': 'success'}

@router.post('/complete_task')
def complete_task(
   data: CompleteTaskRequest,
   mediator: Mediator = Depends(get_mediator),
):
   list_tasks = mediator.send(CompleteTaskCommand(
      list_id=data.list_id,
      task_id=data.task_id,
   ))
   return ListTasksResponse(
      id=list_tasks.id,
      title=list_tasks.title.value,
      description=list_tasks.description.value if list_tasks.description else None,
      tasks=[
         TaskResponse.from_entity(task, data.list_id) for task in list_tasks.tasks
      ]
   )
   
@router.get('/get_all')
def get_all_lists_tasks(
   limit: int = 50,
   offset: int = 0,
   mediator: Mediator = Depends(get_mediator),
):
   lists_tasks = mediator.send(GetAllListsTasksQuery(
      limit=limit,
      offset=offset,
   ))
   return lists_tasks

@router.get('/get_by_id')
def get_list_by_id(
   list_tasks_id: str,
   mediator: Mediator = Depends(get_mediator)
):
   list_task = mediator.send(GetListTasksQuery(
      list_tasks_id
   ))
   return list_task

@router.delete('/delete_task')
def delete_task(
   data: DeleteTaskRequest,
   mediator: Mediator = Depends(get_mediator),
):
   if mediator.send(DeleteTaskCommand(
      list_id=data.list_id,
      task_id=data.task_id,
   )):
      return {'opertion': 'success'}

@router.delete('/list')
def delete_list_tasks(
   list_tasks_id: str,
   mediator: Mediator = Depends(get_mediator),
): 
   if mediator.send(DeleteListTasksCommand(
      list_id=list_tasks_id
   )):
      return {'opertion': 'success'}