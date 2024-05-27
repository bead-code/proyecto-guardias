from typing import List

from fastapi import APIRouter, Depends
from starlette import status

from dao import dao_aula
from db.database import Session, get_db
from db.schemas import AulaDTO, AulaUpdate, AulaCreate
import logging

router = APIRouter(
    prefix="/aula",
    tags=["aula"],
)

@router.get("/{id}", response_model=AulaDTO, status_code=status.HTTP_200_OK)
async def get_aula_by_id(id: int, db: Session = Depends(get_db)):
    logging.info(f"Request recibida...")
    return dao_aula.get_aula_by_id(id, db)

@router.get("/{nombre", response_model=AulaDTO, status_code=status.HTTP_200_OK)
async def get_aula_by_nombre(nombre: str, db: Session = Depends(get_db)):
    logging.info(f"Request recibida...")
    return dao_aula.get_aula_by_nombre(nombre, db)

@router.post("/", response_model=AulaDTO, status_code=status.HTTP_201_CREATED)
async def create_aula(resquest: AulaCreate, db: Session = Depends(get_db)):
    logging.info(f"Request recibida...")
    return dao_aula.create_aula(resquest, db)

@router.get("/", response_model=List[AulaDTO], status_code=status.HTTP_200_OK)
async def get_aulas(db: Session = Depends(get_db)):
    logging.info(f"Request recibida...")
    return dao_aula.get_aulas(db)
@router.put("{id}", response_model=AulaDTO, status_code=status.HTTP_200_OK)
async def update_aula(id: int, request: AulaUpdate, db: Session = Depends(get_db)):
    logging.info(f"Request recibida...")
    return dao_aula.update_aula(id, request, db)

@router.delete("/{id}", status_code=status.HTTP_204_NO_CONTENT)
async def delete_aula(id: int, db: Session = Depends(get_db)):
    logging.info(f"Request recibida...")
    return dao_aula.delete_aula(id, db)