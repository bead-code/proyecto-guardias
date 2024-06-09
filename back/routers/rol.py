import logging
from typing import List

from fastapi import APIRouter, Depends
from sqlalchemy.orm import Session
from starlette import status

from dao import dao_rol
from db.database import get_db
from db.schemas import RolCreate, RolDTO, ProfesorDTO, RolUpdate
from security.oauth2 import get_current_profesor
from utils.logger import logger

router = APIRouter(
    prefix="/rol",
    tags=["rol"]
)

@router.get(
    '/{id}',
    summary="Devuelve un rol de la base de datos",
    description="Esta llamada devuelve un rol en base al ID del mismo",
    response_description="El rol de la base de datos",
    response_model=RolDTO,
    status_code=status.HTTP_200_OK
)
async def get_roll_by_id(
        id: int, current_user: ProfesorDTO = Depends(get_current_profesor),
        db: Session = Depends(get_db)
):
    logger.info(f"Request recibida de {current_user.username}: Obtener rol con ID {id}")
    return dao_rol.get_rol_by_id(id, db)


@router.get(
    '/nombre/{nombre}',
    summary="Devuelve un rol de la base de datos",
    description="Esta llamada devuelve un rol en base al nombre del mismo",
    response_description="El rol de la base de datos",
    response_model=RolDTO,
    status_code=status.HTTP_200_OK)
async def get_roll_by_name(
        nombre: str,
        current_user: ProfesorDTO = Depends(get_current_profesor),
        db: Session = Depends(get_db)
):
    logger.info(f"Request recibida de {current_user.username}: Obtener rol con nombre {nombre}")
    return dao_rol.get_rol_by_nombre(nombre, db)

@router.get(
    '/',
    summary="Devuelve todos los roles de la base de datos",
    description="Esta llamada devuelve todos los roles de la base de datos",
    response_description="Lista de todos los roles de la base de datos",
    response_model=List[RolDTO],
    status_code=status.HTTP_200_OK)
async def get_roles(
        current_user: ProfesorDTO = Depends(get_current_profesor),
        db: Session = Depends(get_db)
):
    logger.info(f"Request recibida de {current_user.username}: Obtener todos los roles")
    return dao_rol.get_roles(db)

@router.post(
    '/',
    summary="Crea un rol en la base de datos",
    description="Esta llamada crea un rol en la base de datos",
    response_description="El rol creado en la base de datos",
    response_model=RolDTO,
    status_code=status.HTTP_201_CREATED
)
async def create_rol(request: RolCreate, current_user: ProfesorDTO = Depends(get_current_profesor), db: Session = Depends(get_db)):
    logger.info(f"Request recibida de {current_user.username}: Crear rol con nombre {request.nombre}")
    return dao_rol.create_rol(request, db)

@router.put(
    '/{id}',
    summary="Actualiza un rol en la base de datos",
    description="Esta llamada actualiza un rol en la base de datos",
    response_description="El rol actualizado en la base de datos",
    response_model=RolDTO,
    status_code=status.HTTP_200_OK
)
async def update_rol(
        id: int,
        request: RolUpdate,
        current_user: ProfesorDTO = Depends(get_current_profesor),
        db: Session = Depends(get_db)
):
    logger.info(f"Request recibida de {current_user.username}: Actualizar rol con ID {id}")
    return dao_rol.update_rol(id, request, db)


@router.delete(
    '/{id}',
    summary="Elimina un rol de la base de datos",
    description="Esta llamada elimina un rol en base al ID del mismo",
    status_code=status.HTTP_204_NO_CONTENT
)
async def delete_rol(
        id: int,
        current_user: ProfesorDTO = Depends(get_current_profesor),
        db: Session = Depends(get_db)
):
    logger.info(f"Request recibida de {current_user.username}: Eliminar rol con ID {id}")
    return dao_rol.delete_rol(id, db)