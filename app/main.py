from fastapi import FastAPI
from .routers import todo


from app.database import Base, engine
from app import models

app = FastAPI(title="ToDo API")

app.include_router(todo.router)



Base.metadata.create_all(bind=engine)
