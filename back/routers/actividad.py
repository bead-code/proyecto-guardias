"""
API Router para gestionar las operaciones CRUD de las actividades.

Este módulo define las rutas y funciones para manejar las operaciones CRUD de la entidad `Actividad` en la base de datos.

Rutas
-----

* **GET /actividad/{id}**: Obtiene una actividad por su ID.
* **GET /actividad/nombre/{nombre}**: Obtiene una actividad por su nombre.
* **GET /actividad/**: Obtiene todas las actividades.
* **POST /actividad/**: Crea una nueva actividad.
* **PUT /actividad/{id}**: Actualiza una actividad existente.
* **DELETE /actividad/{id}**: Elimina una actividad por su ID.

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
from dao import dao_actividad
from db.database import get_db, Session
from db.schemas import ActividadCreate, ActividadDTO, ActividadUpdate, ProfesorDTO
from security.oauth2 import get_current_profesor, check_admin_role
from utils.logger import logger

router = APIRouter(
    prefix="/actividad",
    tags=["actividad"],
)

@router.get(
    "/{id}",
    summary="Devuelve una actividad de la base de datos",
    description="Esta llamada devuelve una actividad en base al ID de la misma",
    response_description="La actividad de la base de datos",
    response_model=ActividadDTO,
    status_code=status.HTTP_200_OK
)
async def get_actividad_by_id(
        id: int,
        current_user: ProfesorDTO = Depends(check_admin_role),
        db: Session = Depends(get_db)
):
    """
    Obtiene una actividad por su ID.

    :param id: El ID de la actividad a buscar.
    :type id: int
    :param current_user: El usuario actual con rol de administrador.
    :type current_user: ProfesorDTO
    :param db: La sesión de la base de datos.
    :type db: Session
    :returns: La actividad encontrada.
    :rtype: ActividadDTO
    """
    logger.info(f"Request recibida de {current_user.username}: Obtener actividad con ID {id}")
    return dao_actividad.get_actividad_by_id(id, db)

@router.get(
    "/nombre/{nombre}",
    summary="Devuelve una actividad de la base de datos",
    description="Esta llamada devuelve una actividad en base al nombre de la misma",
    response_description="La actividad de la base de datos",
    response_model=ActividadDTO,
    status_code=status.HTTP_200_OK
)
async def get_actividad_by_nombre(
        nombre: str,
        current_user: ProfesorDTO = Depends(check_admin_role),
        db: Session = Depends(get_db)
):
    """
    Obtiene una actividad por su nombre.

    :param nombre: El nombre de la actividad a buscar.
    :type nombre: str
    :param current_user: El usuario actual con rol de administrador.
    :type current_user: ProfesorDTO
    :param db: La sesión de la base de datos.
    :type db: Session
    :returns: La actividad encontrada.
    :rtype: ActividadDTO
    """
    logger.info(f"Request recibida de {current_user.username}: Obtener actividad con nombre {nombre}")
    return dao_actividad.get_actividad_by_nombre(nombre, db)

@router.get(
    "/",
    summary="Devuelve todas las actividades de la base de datos",
    description="Esta llamada devuelve todas las actividades de la base de datos",
    response_description="Lista de todas las actividades de la base de datos",
    response_model=List[ActividadDTO],
    status_code=status.HTTP_200_OK
)
async def get_actividades(
        current_user: ProfesorDTO = Depends(check_admin_role),
        db: Session = Depends(get_db)
):
    """
    Obtiene todas las actividades activas.

    :param current_user: El usuario actual con rol de administrador.
    :type current_user: ProfesorDTO
    :param db: La sesión de la base de datos.
    :type db: Session
    :returns: Una lista de todas las actividades activas.
    :rtype: List[ActividadDTO]
    """
    logger.info(f"Request recibida de {current_user.username}: Obtener todas las actividades")
    return dao_actividad.get_actividades(db)

@router.post(
    "/",
    summary="Crea una actividad en la base de datos",
    description="Esta llamada crea una actividad en la base de datos",
    response_description="La actividad creada en la base de datos",
    response_model=ActividadDTO,
    status_code=status.HTTP_201_CREATED
)
async def create_actividad(
        request: ActividadCreate,
        current_user: ProfesorDTO = Depends(check_admin_role),
        db: Session = Depends(get_db)
):
    """
    Crea una nueva actividad.

    :param request: Los datos de la actividad a crear.
    :type request: ActividadCreate
    :param current_user: El usuario actual con rol de administrador.
    :type current_user: ProfesorDTO
    :param db: La sesión de la base de datos.
    :type db: Session
    :returns: La actividad creada.
    :rtype: ActividadDTO
    """
    logger.info(f"Request recibida de {current_user.username}: Crear actividad")
    return dao_actividad.create_actividad(request, db)

@router.put(
    "/{id}",
    summary="Actualiza una actividad en la base de datos",
    description="Esta llamada actualiza una actividad en la base de datos",
    response_description="La actividad de la base de datos",
    response_model=ActividadDTO,
    status_code=status.HTTP_200_OK
)
async def update_actividad(
        id: int, request: ActividadUpdate,
        current_user: ProfesorDTO = Depends(check_admin_role),
        db: Session = Depends(get_db)
):
    """
    Actualiza una actividad existente.

    :param id: El ID de la actividad a actualizar.
    :type id: int
    :param request: Los nuevos datos de la actividad.
    :type request: ActividadUpdate
    :param current_user: El usuario actual con rol de administrador.
    :type current_user: ProfesorDTO
    :param db: La sesión de la base de datos.
    :type db: Session
    :returns: La actividad actualizada.
    :rtype: ActividadDTO
    """
    logger.info(f"Request recibida de {current_user.username}: Actualizar actividad con ID {id}")
    return dao_actividad.update_actividad(id, request, db)

@router.delete(
    "/{id}",
    summary="Elimina una actividad de la base de datos",
    description="Esta llamada elimina una actividad en base al ID de la misma",
    status_code=status.HTTP_204_NO_CONTENT
)
async def delete_actividad(
        id: int,
        current_user: ProfesorDTO = Depends(get_current_profesor),
        db: Session = Depends(get_db)
):
    """
    Elimina (desactiva) una actividad por su ID.

    :param id: El ID de la actividad a eliminar.
    :type id: int
    :param current_user: El usuario actual.
    :type current_user: ProfesorDTO
    :param db: La sesión de la base de datos.
    :type db: Session
    """
    logger.info(f"Request recibida de {current_user.username}: Eliminar actividad con ID {id}")
    return dao_actividad.delete_actividad(id, db)

