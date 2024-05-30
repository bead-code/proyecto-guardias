import logging
from typing import List

from fastapi import APIRouter, Depends

from dao import dao_tramo_horario
from db.database import Session, get_db
from db.schemas import TramoHorarioDTO, TramoHorarioCreate, TramoHorarioUpdate, ProfesorDTO
from security.oauth2 import get_current_profesor

router = APIRouter(
    prefix="/tramo_horario",
    tags=["tramo_horario"],
)


@router.get("/{id}", response_model=TramoHorarioDTO, status_code=200)
async def get_tramo_horario_by_id(id: int, current_user: ProfesorDTO = Depends(get_current_profesor), db: Session = Depends(get_db)):
    logging.info(f"Request recibida...")
    return dao_tramo_horario.get_tramo_horario_by_id(id, db)


@router.get("/nombre/{nombre}", response_model=TramoHorarioDTO, status_code=200)
async def get_tramo_horario_by_nombre(nombre: str, current_user: ProfesorDTO = Depends(get_current_profesor), db: Session = Depends(get_db)):
    logging.info(f"Request recibida...")
    return dao_tramo_horario.get_tramo_horario_by_nombre(nombre, db)


@router.get("/", response_model=List[TramoHorarioDTO], status_code=200)
async def get_tramo_horarios(current_user: ProfesorDTO = Depends(get_current_profesor), db: Session = Depends(get_db)):
    logging.info(f"Request recibida...")
    return dao_tramo_horario.get_tramos_horarios(db)


@router.post("/", response_model=TramoHorarioDTO, status_code=200)
async def create_tramo_horario(request: TramoHorarioCreate, current_user: ProfesorDTO = Depends(get_current_profesor), db: Session = Depends(get_db)):
    logging.info(f"Request recibida...")
    return dao_tramo_horario.create_tramo_horario(request, db)


@router.put("/{id}", response_model=TramoHorarioDTO, status_code=200)
async def update_tramo_horario(id: int, request: TramoHorarioUpdate, current_user: ProfesorDTO = Depends(get_current_profesor), db: Session = Depends(get_db)):
    logging.info(f"Request recibida...")
    return dao_tramo_horario.update_tramo_horario(id, request, db)


@router.delete("/{id}", status_code=200)
async def delte_tramo_horario(id: int, current_user: ProfesorDTO = Depends(get_current_profesor), db: Session = Depends(get_db)):
    logging.info(f"Request recibida...")
    return dao_tramo_horario.delete_tramo_horario(id, db)
