from fastapi import APIRouter, Depends
from dao import dao_asignatura
from db.database import get_db, Session
from db.schemas import AsignaturaDb, AsignaturaDto
import logging

router = APIRouter(
    prefix="/asignatura",
    tags=["asignatura"],
)

@router.post("/", response_model=AsignaturaDb)
async def create_asignatura(request: AsignaturaDb, db: Session = Depends(get_db)):
    logging.info(f"Request recibida: {request}")
    return dao_asignatura.create_asignatura(request, db)


@router.get("/", response_model=AsignaturaDto)
async def get_asignatura_by_codigo(codigo: str, db: Session = Depends(get_db)):
    logging.info(f"Request recibida...")
    return dao_asignatura.get_asignatura_by_codigo(codigo, db)
