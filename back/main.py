from fastapi import FastAPI
import models
from database import Base, engine

app = FastAPI()

Base.metadata.create_all(bind=engine)
