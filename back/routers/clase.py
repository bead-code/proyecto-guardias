from typing import List

from fastapi import APIRouter, Depends
from starlette import status
from dao import dao_clase
from db.database import Session, get_db
from db.schemas import ClaseDTO, ClaseCreate, ClaseUpdate, ProfesorDTO
from security.oauth2 import get_current_profesor, check_admin_role
from utils.logger import logger

router = APIRouter(
    prefix="/clase",
    tags=["clase"],
)


@router.get(
    "/{id}",
    summary="Devuelve una clase de la base de datos",
    description="Esta llamada devuelve una clase en base al ID de la misma",
    response_description="La clase de la base de datos",
    response_model=ClaseDTO,
    status_code=status.HTTP_200_OK)
def get_clase_by_id(
        id: int,
        current_user: ProfesorDTO = Depends(check_admin_role),
        db: Session = Depends(get_db)
):

    return dao_clase.get_clase_by_id(id, db)


@router.get(
    "/nombre/{nombre}",
    summary="Devuelve una clase de la base de datos",
    description="Esta llamada devuelve una clase en base al nombre de la misma",
    response_description="La clase de la base de datos",
    response_model=ClaseDTO,
    status_code=status.HTTP_200_OK
)
def get_clase_by_nombre(
        nombre: str,
        current_user: ProfesorDTO = Depends(check_admin_role),
        db: Session = Depends(get_db)
):
    logger.info(f"Request recibida de {current_user.username}: Obtener clase con nombre {nombre}")
    return dao_clase.get_clase_by_nombre(nombre, db)


@router.get(
    "/",
    summary="Devuelve todas las clases de la base de datos",
    description="Esta llamada devuelve todas las clases de la base de datos",
    response_description="Lista de todas las clases de la base de datos",
    response_model=List[ClaseDTO],
    status_code=status.HTTP_200_OK
)
def get_clases(
        current_user: ProfesorDTO = Depends(check_admin_role),
        db: Session = Depends(get_db)):
    logger.info(f"Request recibida de {current_user.username}: Obtener todas las clases")
    return dao_clase.get_clases(db)


@router.post(
    "/",
    summary="Crea una clase en la base de datos",
    description="Esta llamada crea una clase en la base de datos",
    response_description="La clase creada en la base de datos",
    response_model=ClaseDTO,
    status_code=status.HTTP_200_OK
)
def create_clase(
        request: ClaseCreate,
        current_user: ProfesorDTO = Depends(check_admin_role),
        db: Session = Depends(get_db)
):
    logger.info(f"Request recibida de {current_user.username}: Crear clase con nombre {request.nombre}")
    return dao_clase.create_clase(request, db)


@router.put(
    "/{id}",
    summary="Actualiza una clase en la base de datos",
    description="Esta llamada actualiza una clase en la base de datos",
    response_description="La clase actualizada en la base de datos",
    response_model=ClaseDTO,
    status_code=status.HTTP_200_OK
)
def update_clase(
        id: int,
        request: ClaseUpdate,
        current_user: ProfesorDTO = Depends(check_admin_role),
        db: Session = Depends(get_db)
):
    logger.info(f"Request recibida de {current_user.username}: Actualizar clase con ID {id}")
    return dao_clase.update_clase(id, request, db)


@router.delete(
    "/{id}",
    summary="Elimina una clase de la base de datos",
    description="Esta llamada elimina una clase de la base de datos",
    status_code=status.HTTP_204_NO_CONTENT
)
def delete_clase(
        id: int,
        current_user: ProfesorDTO = Depends(check_admin_role),
        db: Session = Depends(get_db)
):
    logger.info(f"Request recibida de {current_user.username}: Eliminar clase con ID {id}")
    return dao_clase.delete_clase(id, db)
