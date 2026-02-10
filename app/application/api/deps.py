from typing import Callable

from fastapi import Depends
from sqlalchemy.orm import Session

from app.application.mediator.mediator import Mediator
from app.application.mediator.register import build_mediator
from app.infra.db.session import SessionLocal
from app.infra.repository.query.sqlalchemy import SQLAlchemyListTasksQueryRepository
from app.infra.uow.sqlalchemy import SQLAlchemyUnitOfWork


def get_uow_factory() -> Callable[[], SQLAlchemyUnitOfWork]:
   return lambda: SQLAlchemyUnitOfWork(SessionLocal)

def get_db_session():
   session = SessionLocal()
   try:
      yield session
   finally:
      session.close()

def get_mediator(
   session: Session = Depends(get_db_session)
) -> Mediator:
   query_repo = SQLAlchemyListTasksQueryRepository(session)
   uow_factory = get_uow_factory()
   
   mediator = build_mediator(uow_factory, query_repo)
   return mediator