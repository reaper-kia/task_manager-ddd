from dataclasses import dataclass
from sqlalchemy import select
from sqlalchemy.orm import Session

from app.domain.entities.days import Calendar
from app.infra.db.models.calendar import CalendarModel
from app.infra.repository.base import CalendarRepository

@dataclass 
class SQLAlchemyCalendarRepository(CalendarRepository):
   session: Session
   
   def save(self, calendar: Calendar):
      model = self.session.get(CalendarModel, calendar.id)
      
      if model is None:
         self.session.add(Calendar.from_entity(calendar))
      
      