from dataclasses import dataclass
from sqlalchemy import Date, ForeignKey, Table
from sqlalchemy.orm import Mapped, mapped_column, relationship
from datetime import date

from app.domain.entities.days import Calendar, Day
from app.infra.db.models.tasks import ListTasksModel
from app.infra.db.session import Base


@dataclass
class CalendarModel(Base):
   __tablename__ = "calendars"
   
   id: Mapped[str] = mapped_column(primary_key=True)
   days: list['DayModel'] = relationship(cascade='all, delete-orphan', lazy='selectin')
   
   @classmethod
   def from_entity(cls, calendar: Calendar):
      return cls(
         id= calendar.id,
         days=[
            DayModel.from_entity(day) for day in calendar.days 
         ]
      )
   
   
@dataclass
class DayModel(Base):
   __tablename__ = "days"
   
   date: Mapped[Date] = mapped_column(primary_key=True)
   calendar_id: Mapped[str] = mapped_column(
      ForeignKey("calendars.id"),
      primary_key=True
      )
   
   list_tasks_ids: Mapped[list[str]] = relationship(
      cascade='all, delete-orphan',
      lazy='selectin',
      back_populates="days"
   )
   
   @classmethod
   def from_entity(cls, day: Day):
      return cls(
         date=day.date,
         calendar_id=day.calendar_id,
         list_tasks_ids=day.list_tasks_ids.copy()
      )