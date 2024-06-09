from datetime import date, time
from typing import List, Optional

from fastapi import APIRouter, Depends, HTTPException
import logging

from starlette import status

from dao import dao_guardia
from db.database import Session, get_db
from db.schemas import CalendarioDTO, ProfesorDTO
from security.oauth2 import get_current_profesor, check_roles_and_id

router = APIRouter(
    prefix="/guardias",
    tags=["guardias"],
)

@router.get("", response_model=CalendarioDTO, status_code=status.HTTP_200_OK)
async def get_guardias_by_fecha_tramo_id_profesor(id_profesor: int, fecha: date, id_tramo_horario: int, db: Session = Depends(get_db)):
    logging.info(f"Request recibida....")
    return dao_guardia.get_guardias_by_fecha_tramo(id_profesor, fecha, id_tramo_horario, db)

@router.get("/all", response_model=List[CalendarioDTO], status_code=status.HTTP_200_OK)
async def get_guardias(db: Session = Depends(get_db)):
    logging.info(f"Request recibida....")
    return dao_guardia.get_guardias(db)

@router.get("/asignadas", response_model=List[CalendarioDTO], status_code=status.HTTP_200_OK)
async def get_guardias_asignadas(db: Session = Depends(get_db)):
    logging.info(f"Request recibida....")
    return dao_guardia.get_guardias_asignadas(db)

@router.get("/pendientes", response_model=List[CalendarioDTO], status_code=status.HTTP_200_OK)
async def get_guardias_pendientes(db: Session = Depends(get_db)):
    logging.info(f"Request recibida....")
    return dao_guardia.get_guardias_pendientes(db)

@router.get("/{id_profesor}", response_model=List[CalendarioDTO], status_code=status.HTTP_200_OK)
async def get_guardias_by_profesor(id_profesor: int, db: Session = Depends(get_db), date: Optional[date] = None):
    logging.info(f"Request recibida....")
    return dao_guardia.get_guardias_by_profesor(id_profesor, db, date)

@router.post("", response_model=List[CalendarioDTO], status_code=status.HTTP_200_OK)
async def create_guardia(id_profesor: int, fecha_inicio: date, fecha_fin: date, hora_inicio: time, hora_fin: time, db: Session = Depends(get_db)):
    if fecha_inicio > fecha_fin:
        raise HTTPException(
            status_code=status.HTTP_400_BAD_REQUEST,
            detail="La fecha de inicio no puede ser mayor a la fecha de fin"
        )
    logging.info(f"Request recibida....")
    return dao_guardia.create_guardia(id_profesor, fecha_inicio, fecha_fin, hora_inicio, hora_fin,db)

@router.put(
    "/{id}",
    summary="Asigna un profesor sustituto a un calendario",
    description="Esta llamada asigna un profesor sustituto a un calendario",
    status_code=status.HTTP_200_OK
)
async def asignar_profesor_sustituto(
        id: int,
        id_profesor_sustituto: int,
        current_user: ProfesorDTO = Depends(get_current_profesor),
        db: Session = Depends(get_db)
):
    check_roles_and_id(current_user.id_profesor, current_user)
    logging.info(f"Request recibida...")
    return dao_guardia.assign_profesor_sustituto(id, id_profesor_sustituto, db)