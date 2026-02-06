import pytest

from app.domain.entities.tasks import ListTasks, Task
from app.domain.exceptions.tasks import EmptyTextException, TextToLongException
from app.domain.value_objects.tasks import Title

def test_create_task():
   task1 = Task.create(title=Title('task1'))
   task2 = Task.create(title=Title('task1'))
   
   task_list = ListTasks(title=Title('list1'))
   
   task_list.add_task(task1)
   task_list.add_task(task2)
   
   assert len(task_list.tasks) == 2
   assert task_list.get_task(task1.id).id == task1.id


def test_remove_task():
   task1 = Task.create(title=Title('task1'))
   task2 = Task.create(title=Title('task1'))
   
   task_list = ListTasks(title=Title('list1'))
   
   task_list.add_task(task1)
   task_list.add_task(task2)
   
   task_list.remove_task(task2.id)
   
   assert len(task_list.tasks) == 1
   assert task_list.get_task(task1.id).id == task1.id

def test_empty_text():
   with pytest.raises(EmptyTextException):
      task = Task.create(title=Title(''))

def test_test_to_long_exception():
   with pytest.raises(TextToLongException):
      task = Task.create(title=Title('a'*300))