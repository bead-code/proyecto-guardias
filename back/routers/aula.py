from typing import List

from fastapi import APIRouter, Depends
from starlette import status

from dao import dao_aula
from db.database import Session, get_db
from db.schemas import AulaDTO, AulaUpdate, AulaCreate, ProfesorDTO
import logging

from security.oauth2 import get_current_profesor, check_admin_role
from utils.logger import logger

router = APIRouter(
    prefix="/aula",
    tags=["aula"],
)

@router.get(
    "/{id}",
    summary="Devuelve un aula de la base de datos",
    description="Esta llamada devuelve un aula en base al ID de la misma",
    response_description="El aula de la base de datos",
    response_model=AulaDTO,
    status_code=status.HTTP_200_OK
)
async def get_aula_by_id(
        id: int,
        current_user: ProfesorDTO = Depends(check_admin_role),
        db: Session = Depends(get_db)
):
    logger.info(f"Request recibida de {current_user.username}: Obtener aula con ID {id}")
    return dao_aula.get_aula_by_id(id, db)

@router.get(
    "/nombre/{nombre",
    summary="Devuelve un aula de la base de datos",
    description="Esta llamada devuelve un aula en base al nombre de la misma",
    response_description="El aula de la base de datos",
    response_model=AulaDTO,
    status_code=status.HTTP_200_OK
)
async def get_aula_by_nombre(
        nombre: str,
        current_user: ProfesorDTO = Depends(check_admin_role),
        db: Session = Depends(get_db)
):
    logger.info(f"Request recibida de {current_user.username}: Obtener aula con nombre {nombre}")
    return dao_aula.get_aula_by_nombre(nombre, db)

@router.get(
    "/",
    summary="Devuelve todas las aulas de la base de datos",
    description="Esta llamada devuelve todas las aulas de la base de datos",
    response_description="Lista de todas las aulas de la base de datos",
    response_model=List[AulaDTO],
    status_code=status.HTTP_200_OK)
async def get_aulas(
        current_user: ProfesorDTO = Depends(check_admin_role),
        db: Session = Depends(get_db)
):
    logger.info(f"Request recibida de {current_user.username}: Obtener todas las aulas")
    return dao_aula.get_aulas(db)

@router.post(
    "/",
    summary="Crea un aula en la base de datos",
    description="Esta llamada crea un aula en la base de datos",
    response_description="El aula creado en la base de datos",
    response_model=AulaDTO,
    status_code=status.HTTP_201_CREATED
)
async def create_aula(
        resquest: AulaCreate,
        current_user: ProfesorDTO = Depends(check_admin_role),
        db: Session = Depends(get_db)):
    logger.info(f"Request recibida de {current_user.username}: Crear aula con nombre {resquest.nombre}")
    return dao_aula.create_aula(resquest, db)


@router.put(
    "{id}",
    summary="Actualiza un aula de la base de datos",
    description="Esta llamada actualiza un aula en base al ID de la misma",
    response_description="El aula actualizado en la base de datos",
    response_model=AulaDTO,
    status_code=status.HTTP_200_OK
)
async def update_aula(
        id: int, request: AulaUpdate,
        current_user: ProfesorDTO = Depends(check_admin_role),
        db: Session = Depends(get_db)
):
    logger.info(f"Request recibida de {current_user.username}: Actualizar aula con ID {id}")
    return dao_aula.update_aula(id, request, db)

@router.delete(
    "/{id}",
    summary="Elimina un aula de la base de datos",
    description="Esta llamada elimina un aula en base al ID de la misma",
    status_code=status.HTTP_204_NO_CONTENT
)
async def delete_aula(
        id: int,
        current_user: ProfesorDTO = Depends(check_admin_role),
        db: Session = Depends(get_db)
):
    logger.info(f"Request recibida de {current_user.username}: Eliminar aula con ID {id}")
    return dao_aula.delete_aula(id, db)