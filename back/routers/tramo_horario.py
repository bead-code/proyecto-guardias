"""
API Router para gestionar las operaciones CRUD de los tramos horarios.

Este módulo define las rutas y funciones para manejar las operaciones CRUD de la entidad `TramoHorario` en la base de datos.

Rutas
-----

* **GET /tramo_horario/{id}**: Obtiene un tramo horario por su ID.
* **GET /tramo_horario/nombre/{nombre}**: Obtiene un tramo horario por su nombre.
* **GET /tramo_horario/**: Obtiene todos los tramos horarios.
* **POST /tramo_horario/**: Crea un nuevo tramo horario.
* **PUT /tramo_horario/{id}**: Actualiza un tramo horario existente.
* **DELETE /tramo_horario/{id}**: Elimina un tramo horario por su ID.

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
from typing import List
from fastapi import APIRouter, Depends
from starlette import status
from starlette.status import HTTP_200_OK, HTTP_201_CREATED
from dao import dao_tramo_horario
from db.database import Session, get_db
from db.schemas import TramoHorarioDTO, TramoHorarioCreate, TramoHorarioUpdate, ProfesorDTO
from security.oauth2 import get_current_profesor, check_admin_role
from utils.logger import logger

router = APIRouter(
    prefix="/tramo_horario",
    tags=["tramo_horario"],
)

@router.get(
    "/{id}",
    summary="Devuelve un tramo horario de la base de datos",
    description="Esta llamada devuelve un tramo horario en base al ID del mismo",
    response_description="El tramo horario de la base de datos",
    response_model=TramoHorarioDTO,
    status_code=status.HTTP_200_OK)
async def get_tramo_horario_by_id(
        id: int,
        current_user: ProfesorDTO = Depends(check_admin_role),
        db: Session = Depends(get_db)
):
    """
    Obtiene un tramo horario por su ID.

    :param id: El ID del tramo horario a buscar.
    :type id: int
    :param current_user: El usuario actual con rol de administrador.
    :type current_user: ProfesorDTO
    :param db: La sesión de la base de datos.
    :type db: Session
    :returns: El tramo horario encontrado.
    :rtype: TramoHorarioDTO
    """
    logger.info(f"Request recibida de {current_user.username}: Obtener tramo horario con ID {id}")
    return dao_tramo_horario.get_tramo_horario_by_id(id, db)

@router.get(
    "/nombre/{nombre}",
    summary="Devuelve un tramo horario de la base de datos",
    description="Esta llamada devuelve un tramo horario en base al nombre del mismo",
    response_description="El tramo horario de la base de datos",
    response_model=TramoHorarioDTO,
    status_code=status.HTTP_200_OK
)
async def get_tramo_horario_by_nombre(
        nombre: str,
        current_user: ProfesorDTO = Depends(check_admin_role),
        db: Session = Depends(get_db)
):
    """
    Obtiene un tramo horario por su nombre.

    :param nombre: El nombre del tramo horario a buscar.
    :type nombre: str
    :param current_user: El usuario actual con rol de administrador.
    :type current_user: ProfesorDTO
    :param db: La sesión de la base de datos.
    :type db: Session
    :returns: El tramo horario encontrado.
    :rtype: TramoHorarioDTO
    """
    logger.info(f"Request recibida de {current_user.username}: Obtener tramo horario con nombre {nombre}")
    return dao_tramo_horario.get_tramo_horario_by_nombre(nombre, db)

@router.get(
    "/",
    summary="Devuelve todos los tramos horarios de la base de datos",
    description="Esta llamada devuelve todos los tramos horarios de la base de datos",
    response_description="Lista de todos los tramos horarios de la base de datos",
    response_model=List[TramoHorarioDTO],
    status_code=status.HTTP_200_OK)
async def get_tramos_horarios(
        current_user: ProfesorDTO = Depends(check_admin_role),
        db: Session = Depends(get_db)):
    """
    Obtiene todos los tramos horarios activos.

    :param current_user: El usuario actual con rol de administrador.
    :type current_user: ProfesorDTO
    :param db: La sesión de la base de datos.
    :type db: Session
    :returns: Una lista de todos los tramos horarios activos.
    :rtype: List[TramoHorarioDTO]
    """
    logger.info(f"Request recibida de {current_user.username}: Obtener todos los tramos horarios")
    return dao_tramo_horario.get_tramos_horarios(db)

@router.post(
    "/",
    summary="Crea un tramo horario en la base de datos",
    description="Esta llamada crea un tramo horario en la base de datos",
    response_description="El tramo horario creado en la base de datos",
    response_model=TramoHorarioDTO,
    status_code=HTTP_201_CREATED)
async def create_tramo_horario(
        request: TramoHorarioCreate,
        current_user: ProfesorDTO = Depends(check_admin_role),
        db: Session = Depends(get_db)
):
    """
    Crea un nuevo tramo horario.

    :param request: Los datos del tramo horario a crear.
    :type request: TramoHorarioCreate
    :param current_user: El usuario actual con rol de administrador.
    :type current_user: ProfesorDTO
    :param db: La sesión de la base de datos.
    :type db: Session
    :returns: El tramo horario creado.
    :rtype: TramoHorarioDTO
    """
    logger.info(f"Request recibida de {current_user.username}: Crear tramo horario con nombre {request.nombre}")
    return dao_tramo_horario.create_tramo_horario(request, db)

@router.put(
    "/{id}",
    summary="Actualiza un tramo horario en la base de datos",
    description="Esta llamada actualiza un tramo horario en la base de datos",
    response_description="El tramo horario actualizado en la base de datos",
    response_model=TramoHorarioDTO,
    status_code=status.HTTP_200_OK
)
async def update_tramo_horario(
        id: int,
        request: TramoHorarioUpdate,
        current_user: ProfesorDTO = Depends(check_admin_role),
        db: Session = Depends(get_db)
):
    """
    Actualiza un tramo horario existente.

    :param id: El ID del tramo horario a actualizar.
    :type id: int
    :param request: Los nuevos datos del tramo horario.
    :type request: TramoHorarioUpdate
    :param current_user: El usuario actual con rol de administrador.
    :type current_user: ProfesorDTO
    :param db: La sesión de la base de datos.
    :type db: Session
    :returns: El tramo horario actualizado.
    :rtype: TramoHorarioDTO
    """
    logger.info(f"Request recibida de {current_user.username}: Actualizar tramo horario con ID {id}")
    return dao_tramo_horario.update_tramo_horario(id, request, db)

@router.delete(
    "/{id}",
    summary="Elimina un tramo horario de la base de datos",
    description="Esta llamada elimina un tramo horario de la base de datos",
    status_code=status.HTTP_204_NO_CONTENT
)
async def delete_tramo_horario(
        id: int,
        current_user: ProfesorDTO = Depends(get_current_profesor),
        db: Session = Depends(get_db)
):
    """
    Elimina (desactiva) un tramo horario por su ID.

    :param id: El ID del tramo horario a eliminar.
    :type id: int
    :param current_user: El usuario actual.
    :type current_user: ProfesorDTO
    :param db: La sesión de la base de datos.
    :type db: Session
    """
    logger.info(f"Request recibida de {current_user.username}: Eliminar tramo horario con ID {id}")
    return dao_tramo_horario.delete_tramo_horario(id, db)

