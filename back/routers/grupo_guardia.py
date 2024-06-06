import logging
from typing import List

from fastapi import APIRouter, Depends
from starlette import status

from dao import dao_guardia, dao_grupo_guardia
from db.database import Session, get_db
from db.schemas import ProfesorDTO, CalendarioDTO

router = APIRouter(
    prefix="/grupo_guardia",
    tags=["grupo_guardia"]
)

@router.get('/', response_model=List[CalendarioDTO], status_code=status.HTTP_200_OK)
async def get_guardias_pendientes_by_grupo_guardia(id_tramo: int, dia: int, db: Session = Depends(get_db)):
    logging.info(f"Request recibida...")
    return dao_grupo_guardia.get_guardias_pendientes_by_grupo_guardia(id_tramo, dia, db)

@router.get('/{id_tramo}', response_model=List[CalendarioDTO], status_code=status.HTTP_200_OK)
async def get_guardias_asignadas_by_tramo(id_tramo: int, dia: int, db: Session = Depends(get_db)):
    logging.info(f"Request recibida...")
    return dao_grupo_guardia.get_guardias_pendientes_by_grupo_guardia(id_tramo,dia, db)
