from typing import List

from fastapi import APIRouter, Depends
from sqlalchemy.orm import Session
from starlette import status

from dao import dao_rol
from db.database import get_db
from db.schemas import RolCreate, RolDTO
import logging

router = APIRouter(
    prefix="/rol",
    tags=["rol"]
)

@router.get('/{id}', response_model=RolDTO, status_code=status.HTTP_200_OK)
async def get_roll_by_id(id: int, db: Session = Depends(get_db)):
    logging.info(f"Request recibida...")
    return dao_rol.get_rol_by_id(id, db)

@router.get('/nombre/{nombre}', response_model=RolDTO, status_code=status.HTTP_200_OK)
async def get_roll_by_name(nombre: str, db: Session = Depends(get_db)):
    logging.info(f"Request recibida...")
    return dao_rol.get_rol_by_nombre(nombre, db)

@router.get('/', response_model=List[RolDTO], status_code=status.HTTP_200_OK)
async def get_roles(db: Session = Depends(get_db)):
    logging.info(f"Request recibida...")
    return dao_rol.get_roles(db)

@router.post('/', response_model=RolDTO, status_code=status.HTTP_201_CREATED)
async def create_rol(request: RolCreate, db: Session = Depends(get_db)):
    logging.info(f"Request recibida...")
    return dao_rol.create_rol(request, db)

@router.put('/{id}', response_model=RolDTO, status_code=status.HTTP_200_OK)
async def update_rol(id: int, request: RolCreate, db: Session = Depends(get_db)):
    logging.info(f"Request recibida...")
    return dao_rol.update_rol(id, request, db)


@router.delete('/{id}', status_code=status.HTTP_204_NO_CONTENT)
async def delete_rol(id: int, db: Session = Depends(get_db)):
    logging.info(f"Request recibida...")
    return dao_rol.delete_rol(id, db)