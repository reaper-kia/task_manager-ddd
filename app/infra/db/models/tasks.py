from typing import Optional
from sqlalchemy.orm import Mapped, mapped_column, relationship
from sqlalchemy import Boolean, ForeignKey, String

from app.domain.entities.tasks import ListTasks, Task
from app.domain.value_objects.tasks import Description, Title
from app.infra.db.session import Base


class ListTasksModel(Base):
   __tablename__ = "list_tasks"
   
   id: Mapped[str] = mapped_column(primary_key=True)
   title: Mapped[str] = mapped_column(String(255))
   description: Mapped[Optional[str]] = mapped_column(String(1023))
   tasks: Mapped[list["TaskModel"]] = relationship(back_populates="task_list", cascade="all, delete-orphan", lazy="selectin")
   
   @classmethod
   def from_entity(cls, list_tasks: ListTasks):
      model = cls(
         id=list_tasks.id,
         title=list_tasks.title.value,
         description=list_tasks.description.value if list_tasks.description else None,
      )
      model.tasks = [
         TaskModel.from_entity(list_tasks_id=list_tasks.id, task=task) for task in list_tasks.tasks
      ]
      return model
   
   
   def to_entity(self):
      return ListTasks(
         id=self.id,
         title=Title(self.title),
         description=Description(self.description) if self.description else None,
         tasks=[task.to_entity() for task in self.tasks]
      )


class TaskModel(Base):
   __tablename__ = "tasks"
   
   id: Mapped[str] = mapped_column(primary_key=True)
   title: Mapped[str] = mapped_column(String(255))
   description: Mapped[Optional[str]] = mapped_column(String(1023))
   is_complete: Mapped[bool] = mapped_column(Boolean)
      
   list_tasks_id: Mapped[str] = mapped_column(ForeignKey("list_tasks.id"))
   
   task_list: Mapped["ListTasksModel"] = relationship(
      back_populates="tasks"
   )
   
   def to_entity(self):
      return Task(
         id=self.id,
         title=Title(self.title),
         description=Description(self.description) if self.description else None,
         is_complete=self.is_complete,
      )
   
   @classmethod
   def from_entity(cls, list_tasks_id: str, task: Task):
      return cls(
         id=task.id,
         title=task.title.value,
         description=task.description.value if task.description else None,
         is_complete=task.is_complete,
         list_tasks_id=list_tasks_id,
      )