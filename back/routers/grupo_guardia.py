from typing import List, Tuple, Dict
from fastapi import APIRouter, Depends
from starlette import status
from dao import  dao_grupo_guardia
from db.database import Session, get_db
from db.schemas import ProfesorDTO
from security.oauth2 import get_current_profesor, check_admin_role
from utils.logger import logger

router = APIRouter(
    prefix="/grupo_guardia",
    tags=["grupo_guardia"]
)

@router.get(
    '',
    summary="Devuelve un grupo de guardia de la base de datos",
    description="Esta llamada devuelve un grupo de guardia en base al ID del tramo y el día de la semana",
    response_description="El grupo de guardia de la base de datos",
    response_model=List[ProfesorDTO],
    status_code=status.HTTP_200_OK)
async def get_grupo_guardia(
        id_tramo: int,
        dia: int,
        current_user: ProfesorDTO = Depends(get_current_profesor),
        db: Session = Depends(get_db)):
    logger.info(f"Request recibida de {current_user.username}: Obtener grupo de guardia con ID tramo {id_tramo} y día {dia}")
    return dao_grupo_guardia.get_grupo_guardia(int(id_tramo), int(dia), db)


@router.get(
    '/all',
    summary="Devuelve todos los grupos de guardia de la base de datos",
    description="Esta llamada devuelve todos los grupos de guardia de la base de datos",
    response_description="Lista de todos los grupos de guardia de la base de datos",
    response_model=Dict[Tuple[int, int],List[ProfesorDTO]],
    status_code=status.HTTP_200_OK)
async def get_grupo_guardias(
        current_user: ProfesorDTO = Depends(check_admin_role),
        db: Session = Depends(get_db)
):
    logger.info(f"Request recibida de {current_user.username}: Obtener todos los grupos de guardia")
    return dao_grupo_guardia.get_grupos_guardia(db)
