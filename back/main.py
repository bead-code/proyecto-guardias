from fastapi import FastAPI
from routers import profesor
from db.database import Base, engine
from models import DbProfesor, DbRol

app = FastAPI()
app.include_router(profesor.router)


Base.metadata.create_all(bind=engine)
