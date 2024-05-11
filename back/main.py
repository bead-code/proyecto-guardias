from fastapi import FastAPI
from db.database import Base, engine
from routers import profesor

app = FastAPI()
app.include_router(profesor.router)
Base.metadata.create_all(bind=engine)

