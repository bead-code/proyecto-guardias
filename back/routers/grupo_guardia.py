import logging

from typing import List, Tuple, Dict

from fastapi import APIRouter, Depends, HTTPException
from starlette import status

from dao import dao_guardia, dao_grupo_guardia
from db.database import Session, get_db
from db.schemas import ProfesorDTO, CalendarioDTO

router = APIRouter(
    prefix="/grupo_guardia",
    tags=["grupo_guardia"]
)

@router.get('', response_model=List[ProfesorDTO], status_code=status.HTTP_200_OK)
async def get_grupo_guardia(id_tramo: int, dia: int, db: Session = Depends(get_db)):
    logging.info(f"Request recibida...")
    return dao_grupo_guardia.get_grupo_guardia(int(id_tramo), int(dia), db)


@router.get('', response_model=Dict[Tuple[int, int], List[ProfesorDTO]], status_code=status.HTTP_200_OK)
async def get_guardias(db: Session = Depends(get_db)):
    logging.info(f"Request recibida...")
    return dao_grupo_guardia.get_grupos_guardia(db)
