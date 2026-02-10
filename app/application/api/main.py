from fastapi import FastAPI

from app.application.api.list_tasks.list_tasks import router as list_tasks_router

def create_app() -> FastAPI:
   app = FastAPI(
      title="Task Manager",
      docs_url='/api/docs'
   )
   app.include_router(list_tasks_router)
   
   return app

app = create_app()