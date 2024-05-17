from fastapi import APIRouter, Depends, HTTPException, status
from sqlalchemy.orm import Session
from sqlalchemy.testing.plugin.plugin_base import logging
from dao import dao_profesor
from db.database import get_db
from db.schemas import ProfesorDb, ProfesorDTO
import logging

from security.oauth2 import get_current_profesor

router = APIRouter(
    prefix="/profesor",
    tags=["profesor"]
)


@router.post('/', status_code=status.HTTP_201_CREATED)
def create_profesor(request: ProfesorDb, db: Session = Depends(get_db)):
    logging.info(f"Request recibida: {request}")
    return dao_profesor.create_profesor(request, db)


@router.get('/',
            summary="Devuelve un profesor de la base de datos",
            description="Esta llamada devuelve un profesor en base al nick o el código del mismo",
            response_description = "El profesor de la base de datos",
            response_model=ProfesorDTO)
def get_profesor(current_user: ProfesorDTO = Depends(get_current_profesor), codigo: str = None, nick: str = None, db: Session = Depends(get_db)):
    logging.info(f"Request recibida..")
    if codigo:
        profesor = dao_profesor.get_profesor_by_codigo(codigo, db)
    elif nick:
        profesor = dao_profesor.get_profesor_by_nick(nick, db)
    else:
        raise HTTPException(status_code=400, detail="Debe proporcionar 'codigo' o 'nick'")

    return profesor

@router.delete("/{codigo}", status_code=status.HTTP_200_OK)
def delete_profesor(current_user: ProfesorDTO = Depends(get_current_profesor), codigo: str = None, db: Session = Depends(get_db)):
    if current_user.codigo == codigo:
        raise HTTPException(status_code=409, detail="No se puede eliminar al profesor autenticado actualmente")
    if not codigo:
        raise HTTPException(status_code=400, detail="Debe proporcionar 'codigo'")
    dao_profesor.delete_profesor(codigo, db)


