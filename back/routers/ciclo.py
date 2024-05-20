from fastapi import APIRouter, Depends
from sqlalchemy.orm import Session
from dao import dao_curso
from db.database import get_db
from db.schemas import CicloDb, CicloDto
import logging

logging.basicConfig(level=logging.INFO)

router = APIRouter(
    prefix="/ciclo",
    tags=["ciclo"],
)

@router.post("/", response_model=CicloDb)
async def create_ciclo(request: CicloDb, db:Session = Depends(get_db)):
    logging.info(f"Request recibida: {request}")
    return dao_curso.create_curso(request, db)

@router.get("/{codigo}", response_model=CicloDto)
async def get_ciclo(codigo: str, db:Session = Depends(get_db)):
    logging.info(f"Request recibida....")
    return dao_curso.get_curso_by_codigo(codigo, db)