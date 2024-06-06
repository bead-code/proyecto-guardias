from datetime import date
from typing import List, Optional

from fastapi import APIRouter, Depends
import logging

from starlette import status

from dao import dao_guardia
from db.database import Session, get_db
from db.schemas import CalendarioDTO

router = APIRouter(
    prefix="/guardias",
    tags=["guardias"],
)


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

@router.put("{id_profesor}", response_model=List[CalendarioDTO], status_code=status.HTTP_200_OK)
async def create_guardia(id_profesor: int, fecha_inicio: date, fecha_fin: date, db: Session = Depends(get_db)):
    logging.info(f"Request recibida....")
    return dao_guardia.create_guardia(id_profesor, fecha_inicio, fecha_fin, db)