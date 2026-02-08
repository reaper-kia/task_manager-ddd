from dataclasses import dataclass
from datetime import date

from app.infra.db.models.calendar import CalendarModel, DayModel

@dataclass(frozen=True)
class CalendarReadDTO:
   id: str
   days: list["DayReadDTO"]
   
   @classmethod
   def to_dto(cls, model: CalendarModel):
      return cls(
         id=model.id,
         days=[
            DayReadDTO.to_dto(day) for day in model.days
         ]
      )
      

   
@dataclass(frozen=True)
class DayReadDTO:
   date: date
   list_tasks_ids: list[str]
   
   calendar_id: str
   
   @classmethod
   def to_dto(cls, model: DayModel):
      return cls(
         date=model.date,
         list_tasks_ids=model.list_tasks_ids.copy(),
         calendar_id=model.calendar_id,
      )