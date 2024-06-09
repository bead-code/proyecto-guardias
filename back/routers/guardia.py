import logging
from datetime import date, time
from typing import List, Optional

from fastapi import APIRouter, Depends, HTTPException
from starlette import status

from dao import dao_guardia
from db.database import Session, get_db
from db.schemas import CalendarioDTO, ProfesorDTO
from security.oauth2 import get_current_profesor, check_admin_role
from utils.logger import logger

router = APIRouter(
    prefix="/guardias",
    tags=["guardias"],
)


@router.get(
    "",
    summary="Devuelve todas las guardias de la base de datos",
    description="Esta llamada devuelve todas las guardias de la base de datos",
    response_description="Lista de todas las guardias de la base de datos",
    response_model=CalendarioDTO,
    status_code=status.HTTP_200_OK)
async def get_guardias_by_fecha_tramo_id_profesor(
        id_profesor: int,
        fecha: date,
        id_tramo_horario: int,
        current_user: ProfesorDTO = Depends(check_admin_role),
        db: Session = Depends(get_db)):
    logger.info(f"Request recibida de {current_user.username}: Obtener guardias con ID profesor {id_profesor}, fecha {fecha} y tramo horario {id_tramo_horario}")
    return dao_guardia.get_guardias_by_fecha_tramo(id_profesor, fecha, id_tramo_horario, db)

@router.get("/all", 
    summary="Devuelve todas las guardias de la base de datos",
    description="Esta llamada devuelve todas las guardias de la base de datos",
    response_description="Lista de todas las guardias de la base de datos",
    response_model=List[CalendarioDTO], 
    status_code=status.HTTP_200_OK)
async def get_guardias(db: Session = Depends(get_db)):
    logging.info(f"Request recibida....")
    return dao_guardia.get_guardias(db)

@router.get(
    "/asignadas",
    summary="Devuelve todas las guardias asignadas de la base de datos",
    description="Esta llamada devuelve todas las guardias asignadas de la base de datos",
    response_description="Lista de todas las guardias asignadas de la base de datos",
    response_model=List[CalendarioDTO],
    status_code=status.HTTP_200_OK)
async def get_guardias_asignadas(
        current_user: ProfesorDTO = Depends(check_admin_role),
        db: Session = Depends(get_db)
):
    logger.info(f"Request recibida de {current_user.username}: Obtener todas las guardias asignadas")
    return dao_guardia.get_guardias_asignadas(db)

@router.get(
    "/pendientes",
    summary="Devuelve todas las guardias pendientes de la base de datos",
    description="Esta llamada devuelve todas las guardias pendientes de la base de datos",
    response_description="Lista de todas las guardias pendientes de la base de datos",
    response_model=List[CalendarioDTO],
    status_code=status.HTTP_200_OK)
async def get_guardias_pendientes(
        current_user: ProfesorDTO = Depends(check_admin_role),
        db: Session = Depends(get_db)
):
    logger.info(f"Request recibida de {current_user.username}: Obtener todas las guardias pendientes")
    return dao_guardia.get_guardias_pendientes(db)

@router.get(
    "/{id_profesor}",
    summary="Devuelve todas las guardias de un profesor",
    description="Esta llamada devuelve todas las guardias de un profesor",
    response_description="Lista de todas las guardias de un profesor",
    response_model=List[CalendarioDTO],
    status_code=status.HTTP_200_OK)
async def get_guardias_by_profesor(
        id_profesor: int,
        current_user: ProfesorDTO = Depends(get_current_profesor),
        db: Session = Depends(get_db),
        date: Optional[date] = None):
    logger.info(f"Request recibida de {current_user.username}: Obtener guardias con ID profesor {id_profesor}")
    return dao_guardia.get_guardias_by_profesor(id_profesor, db, date)

@router.post(
    "",
    summary="Crea una guardia en la base de datos",
    description="Esta llamada crea una guardia en la base de datos",
    response_description="La guardia creada en la base de datos",
    response_model=List[CalendarioDTO],
    status_code=status.HTTP_200_OK
)
async def create_guardia(
        id_profesor: int,
        fecha_inicio: date,
        fecha_fin: date, hora_inicio:
        time, hora_fin: time,
        current_user: ProfesorDTO = Depends(check_admin_role),
        db: Session = Depends(get_db)):
    if fecha_inicio > fecha_fin:
        raise HTTPException(
            status_code=status.HTTP_400_BAD_REQUEST,
            detail="La fecha de inicio no puede ser mayor a la fecha de fin"
        )
    logger.info(f"Request recibida de {current_user.username}: Crear guardia con ID profesor {id_profesor}")
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
    if current_user.id_profesor != id_profesor_sustituto and current_user.rol.id_rol > 3  :
        raise HTTPException(
            status_code=status.HTTP_403_FORBIDDEN,
            detail="No tienes permisos para acceder a este recurso"
        )
    logging.info(f"Request recibida...")
    return dao_guardia.assign_profesor_sustituto(id, id_profesor_sustituto, db)