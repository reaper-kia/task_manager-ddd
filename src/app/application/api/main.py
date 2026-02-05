from fastapi import FastAPI

def create_app() -> FastAPI:
   app = FastAPI(
      title="Task Manager",
      docs_url='/api/docs'
   )
   return app

app = create_app()