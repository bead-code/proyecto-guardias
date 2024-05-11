from fastapi import APIRouter, Depends
from sqlalchemy.orm import Session

from db import db_profesor
from db.database import get_db
from db.schemas import ProfesorDb

router = APIRouter(
    prefix="/profesor",
    tags=["profesor"]
)


@router.post('/', response_model=ProfesorDb)
def create_profesor(request: ProfesorDb, db: Session = Depends(get_db)):
    return db_profesor.create_profesor(db, request)