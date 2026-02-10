from app.infra.db.session import Base, engine

from app.infra.db.models.tasks import ListTasksModel, TaskModel 

def init_db():
   Base.metadata.create_all(bind=engine)
   print(Base.metadata.tables.keys())  # проверка

if __name__ == "__main__":
   init_db()