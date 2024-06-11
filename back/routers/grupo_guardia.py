"""
API Router para gestionar las operaciones CRUD de los grupos de guardia.

Este módulo define las rutas y funciones para manejar las operaciones CRUD de la entidad `GrupoGuardia` en la base de datos.

Rutas
-----

* **GET /grupo_guardia**: Obtiene un grupo de guardia por el ID del tramo y el día de la semana.
* **GET /grupo_guardia/all**: Obtiene todos los grupos de guardia.
* **GET /grupo_guardia/all**: Obtiene todos los grupos de guardia de un profesor por su ID (opcional).

Dependencias
------------

* **get_current_profesor**: Dependencia para obtener el profesor actual autenticado.
* **check_admin_role**: Dependencia para verificar que el usuario tenga un rol de administrador.
* **get_db**: Dependencia para obtener la sesión de la base de datos.

Dependencias Inyectadas
-----------------------

* **current_user**: El usuario actual autenticado (ProfesorDTO).
* **db**: La sesión de la base de datos (Session).

"""
from typing import List, Tuple, Dict, Optional
from fastapi import APIRouter, Depends
from starlette import status
from dao import dao_grupo_guardia
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
    """
    Obtiene un grupo de guardia por su ID de tramo y día de la semana.

    :param id_tramo: El ID del tramo horario.
    :type id_tramo: int
    :param dia: El día de la semana.
    :type dia: int
    :param current_user: El usuario actual.
    :type current_user: ProfesorDTO
    :param db: La sesión de la base de datos.
    :type db: Session
    :returns: Una lista de profesores en el grupo de guardia.
    :rtype: List[ProfesorDTO]
    """
    logger.info(f"Request recibida de {current_user.username}: Obtener grupo de guardia con ID tramo {id_tramo} y día {dia}")
    return dao_grupo_guardia.get_grupo_guardia(int(id_tramo), int(dia), db)

@router.get(
    '/all',
    summary="Devuelve todos los grupos de guardia de la base de datos",
    description="Esta llamada devuelve todos los grupos de guardia de la base de datos",
    response_description="Lista de todos los grupos de guardia de la base de datos",
    response_model=Dict[Tuple[int, int], List[ProfesorDTO]],
    status_code=status.HTTP_200_OK)
async def get_grupos_guardia(
        id_profesor: Optional[int] = None,
        current_user: ProfesorDTO = Depends(check_admin_role),
        db: Session = Depends(get_db)
):
    """
    Obtiene todos los grupos de guardia.

    :param id_profesor: El ID del profesor (opcional).
    :type id_profesor: Optional[int]
    :param current_user: El usuario actual con rol de administrador.
    :type current_user: ProfesorDTO
    :param db: La sesión de la base de datos.
    :type db: Session
    :returns: Un diccionario con los grupos de guardia, donde la clave es una tupla de (día, ID del tramo horario) y el valor es una lista de profesores.
    :rtype: Dict[Tuple[int, int], List[ProfesorDTO]]
    """
    if id_profesor is None:
        logger.info(f"Request recibida de {current_user.username}: Obtener todos los grupos de guardia")
        return dao_grupo_guardia.get_grupos_guardia(db)
    logger.info(f"Request recibida de {current_user.username}: Obtener todos los grupos de guardia del profesor con id: {id_profesor}")
    return dao_grupo_guardia.get_grupos_guardia_by_id_profesor(id_profesor, db)


