from typing import List
from fastapi import APIRouter, Depends, HTTPException, status
from sqlalchemy.orm import Session
from sqlalchemy.testing.plugin.plugin_base import logging
from dao import dao_profesor
from db.database import get_db
from db.schemas import ProfesorDTO, ProfesorCreate, ProfesorUpdate
from security.oauth2 import get_current_profesor
import logging

router = APIRouter(
    prefix="/profesor",
    tags=["profesor"]
)

@router.get('/{id}',
            summary="Devuelve un profesor de la base de datos",
            description="Esta llamada devuelve un profesor en base al nick o el código del mismo",
            response_description="El profesor de la base de datos",
            response_model=ProfesorDTO,
            status_code=status.HTTP_200_OK)
def get_profesor(id: int, current_user: ProfesorDTO = Depends(get_current_profesor), db: Session = Depends(get_db)):
    logging.info(f"Request recibida....")
    return dao_profesor.get_profesor_by_id(id, db)


@router.get('/username/{username}', response_model=ProfesorDTO, status_code=status.HTTP_200_OK)
def get_profesor_by_nombre(username: str, current_user: ProfesorDTO = Depends(get_current_profesor), db: Session = Depends(get_db)):
    logging.info("Request recibida..")
    return dao_profesor.get_profesor_by_username(username, db)


@router.get('/',  response_model=List[ProfesorDTO], status_code=status.HTTP_200_OK)
def get_profesores(current_user: ProfesorDTO = Depends(get_current_profesor), db: Session = Depends(get_db)):
    logging.info("Request recibida..")
    return dao_profesor.get_profesores(db)

@router.post('/',  response_model=ProfesorDTO, status_code=status.HTTP_201_CREATED)
def create_profesor(request: ProfesorCreate, current_user: ProfesorDTO = Depends(get_current_profesor), db: Session = Depends(get_db)):
    logging.info("Request recibida: {request}")
    return dao_profesor.create_profesor(request, db)

@router.put('/{id}', response_model = ProfesorDTO, status_code=status.HTTP_200_OK)
def update_profesor(id: int, request: ProfesorUpdate, current_user: ProfesorDTO = Depends(get_current_profesor), db: Session = Depends(get_db)):
    logging.info("Request recibida: {request}")
    return dao_profesor.update_profesor(id, request, db)


@router.delete("/{id}", response_model= ProfesorDTO, status_code=status.HTTP_200_OK)
def delete_profesor(current_user: ProfesorDTO = Depends(get_current_profesor), codigo: str = None, db: Session = Depends(get_db)):
    if current_user.id == id:
        raise HTTPException(status_code=409, detail="No se puede eliminar al profesor autenticado actualmente")
    if not codigo:
        raise HTTPException(status_code=400, detail="Debe proporcionar 'codigo'")
    dao_profesor.delete_profesor(id, db)


