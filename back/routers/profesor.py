import logging
from typing import List

from fastapi import APIRouter, Depends, HTTPException, status
from sqlalchemy.orm import Session
from sqlalchemy.testing.plugin.plugin_base import logging

from dao import dao_profesor
from db.database import get_db
from db.schemas import ProfesorDTO, ProfesorCreate, ProfesorUpdate
from security.oauth2 import get_current_profesor, check_roles, check_roles_and_id, check_delete

router = APIRouter(
    prefix="/profesor",
    tags=["profesor"]
)


@router.get(
    '/{id}',
    summary="Devuelve un profesor de la base de datos",
    description="Esta llamada devuelve un profesor en base al nick o el código del mismo",
    response_description="El profesor de la base de datos",
    response_model=ProfesorDTO,
    status_code=status.HTTP_200_OK
)
def get_profesor(
        id: int,
        current_user: ProfesorDTO = Depends(get_current_profesor),
        db: Session = Depends(get_db)
):
    check_roles_and_id(id, current_user)
    logging.info(f"Request recibida....")
    return dao_profesor.get_profesor_by_id(id, db)


@router.get(
    '/',
    summary="Devuelve todos los profesores de la base de datos",
    description="Esta llamada devuelve todos los profesores de la base de datos",
    response_description="Lista de todos los profesores de la base de datos",
    response_model=List[ProfesorDTO],
    status_code=status.HTTP_200_OK
)
def get_profesores(
        current_user: ProfesorDTO = Depends(get_current_profesor),
        db: Session = Depends(get_db)
):
    check_roles(current_user)
    logging.info("Request recibida..")
    return dao_profesor.get_profesores(db)

@router.post(
    '/',
    summary="Crea un profesor en la base de datos",
    description="Esta llamada crea un profesor en la base de datos",
    response_description="El profesor creado",
    response_model=ProfesorDTO,
    status_code=status.HTTP_201_CREATED
)
def create_profesor(
        request: ProfesorCreate,
        current_user: ProfesorDTO = Depends(get_current_profesor),
        db: Session = Depends(get_db)
):
    check_roles(current_user)
    logging.info("Request recibida: {request}")
    return dao_profesor.create_profesor(request, db)

@router.put(
    '/{id}',
    summary="Actualiza un profesor en la base de datos",
    description="Esta llamada actualiza un profesor en la base de datos",
    response_description="El profesor actualizado",
    response_model = ProfesorDTO,
    status_code=status.HTTP_200_OK
)
def update_profesor(
        id: int, request: ProfesorUpdate,
        current_user: ProfesorDTO = Depends(get_current_profesor),
        db: Session = Depends(get_db)
):
    check_roles_and_id(id, current_user)
    logging.info("Request recibida: {request}")
    return dao_profesor.update_profesor(id, request, db)


@router.delete(
    "/{id}",
    summary="Elimina un profesor de la base de datos",
    description="Esta llamada elimina un profesor de la base de datos",
    status_code=status.HTTP_204_NO_CONTENT)
def delete_profesor(
        id: int,
        current_user: ProfesorDTO = Depends(get_current_profesor),
        db: Session = Depends(get_db)
):
    check_delete(id, current_user)
    if current_user.id_profesor == id:
        raise HTTPException(status_code=409, detail="No se puede eliminar al profesor autenticado actualmente")
    dao_profesor.delete_profesor(id, db)


