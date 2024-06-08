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

@router.get('/{identificador}', response_model=List[ProfesorDTO], status_code=status.HTTP_200_OK)
async def get_grupo_guardia(identificador: str, db: Session = Depends(get_db)):
    logging.info(f"Request recibida...")
    try:
        id_tramo, dia = identificador.split('-')
        return dao_grupo_guardia.get_grupo_guardia(int(id_tramo), int(dia), db)
    except Exception as e:
        raise HTTPException(
            status_code=status.HTTP_400_BAD_REQUEST,
            detail="Error en la solicitud"
        )

@router.get('', response_model=Dict[Tuple[int, int], List[ProfesorDTO]], status_code=status.HTTP_200_OK)
async def get_guardias(db: Session = Depends(get_db)):
    logging.info(f"Request recibida...")
    return dao_grupo_guardia.get_grupos_guardia(db)
