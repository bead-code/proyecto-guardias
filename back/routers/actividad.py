from fastapi import APIRouter, Depends
from dao import dao_actividad
from db.database import get_db, Session
from db.schemas import AsignaturaDb, AsignaturaDto
import logging

router = APIRouter(
    prefix="/actividad",
    tags=["actividad"],
)

@router.post("/", response_model=ActividadDb)
async def create_actividad(request: ActividadDb, db: Session = Depends(get_db)):
    logging.info(f"Request recibida: {request}")
    return dao_actividad.create_actividad(request, db)


@router.get("/", response_model=AsignaturaDto)
async def get_asignatura_by_codigo(codigo: str, db: Session = Depends(get_db)):
    logging.info(f"Request recibida...")
    return dao_actividad.get_actividad_by_id(codigo, db)
