from dataclasses import dataclass
from typing import Callable
from sqlalchemy import select
from sqlalchemy.orm import Session

from app.infra.db.models.calendar import CalendarModel
from app.infra.repository.query.base import CalendarQueryRepository

@dataclass 
class SQLAlchemyCalendarQueryRepository(CalendarQueryRepository):
   session: Session
   
   def get_by_user_id(self, user_id: str):
      model = self.session.execute(select(CalendarModel)).where(CalendarModel.id == user_id)
      result = model.scalars().first()
      return result.to_dto()