"""
API Router para gestionar las operaciones CRUD de los profesores.

Este módulo define las rutas y funciones para manejar las operaciones CRUD de la entidad `Profesor` en la base de datos.

Rutas
-----

* **GET /profesor/all**: Obtiene todos los profesores de la base de datos.
* **GET /profesor/disponible**: Obtiene todos los profesores disponibles en una fecha y tramo horario específicos.
* **GET /profesor/{id}**: Obtiene un profesor por su ID.
* **POST /profesor/**: Crea un nuevo profesor.
* **PUT /profesor/{id}**: Actualiza un profesor existente.
* **DELETE /profesor/{id}**: Elimina un profesor por su ID.

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
from datetime import date
from typing import List
from fastapi import APIRouter, Depends, HTTPException, status
from sqlalchemy.orm import Session
from dao import dao_profesor
from db.database import get_db
from db.schemas import ProfesorDTO, ProfesorCreate, ProfesorUpdate
from security.oauth2 import get_current_profesor, check_admin_role
from utils.logger import logger

router = APIRouter(
    prefix="/profesor",
    tags=["profesor"]
)


@router.get(
    '/all',
    summary="Devuelve todos los profesores de la base de datos",
    description="Esta llamada devuelve todos los profesores de la base de datos",
    response_description="Lista de todos los profesores de la base de datos",
    response_model=List[ProfesorDTO],
    status_code=status.HTTP_200_OK
)
def get_profesores(
        current_user: ProfesorDTO = Depends(check_admin_role),
        db: Session = Depends(get_db)
):
    """
    Obtiene todos los profesores activos.

    :param current_user: El usuario actual con rol de administrador.
    :type current_user: ProfesorDTO
    :param db: La sesión de la base de datos.
    :type db: Session
    :returns: Una lista de todos los profesores activos.
    :rtype: List[ProfesorDTO]
    """
    logger.info(f"Request recibida de {current_user.username}: Obtener todos los profesores")
    return dao_profesor.get_profesores(db)


@router.get(
    '/disponible',
    summary="Devuelve todos los profesores disponibles en una fecha y tramo horario",
    description="Esta llamada devuelve todos los profesores disponibles en una fecha y tramo horario",
    response_description="Lista de todos los profesores disponibles en una fecha y tramo horario",
    status_code=status.HTTP_200_OK
)
def get_profesores_disponibles_by_id_calendario(
        fecha: date,
        id_tramo_horario: int,
        current_user: ProfesorDTO = Depends(check_admin_role),
        db: Session = Depends(get_db)
):
    """
    Obtiene todos los profesores disponibles en una fecha y tramo horario específicos.

    :param fecha: La fecha en la que se desea buscar profesores disponibles.
    :type fecha: date
    :param id_tramo_horario: El ID del tramo horario en el que se desea buscar profesores disponibles.
    :type id_tramo_horario: int
    :param current_user: El usuario actual con rol de administrador.
    :type current_user: ProfesorDTO
    :param db: La sesión de la base de datos.
    :type db: Session
    :returns: Una lista de todos los profesores disponibles en la fecha y tramo horario especificados.
    :rtype: List[ProfesorDTO]
    """
    logger.info(f"Request recibida de {current_user.username}: Obtener profesores disponibles en fecha {fecha} y "
                f"tramo horario {id_tramo_horario}")
    return dao_profesor.get_profesores_disponibles_by_id_calendario(fecha, id_tramo_horario, db)


@router.get(
    '/{id}',
    summary="Devuelve un profesor de la base de datos",
    description="Esta llamada devuelve un profesor en base al ID del mismo",
    response_description="El profesor de la base de datos",
    response_model=ProfesorDTO,
    status_code=status.HTTP_200_OK
)
def get_profesor_by_id(
        id: int,
        current_user: ProfesorDTO = Depends(get_current_profesor),
        db: Session = Depends(get_db)
):
    """
    Obtiene un profesor por su ID.

    :param id: El ID del profesor a buscar.
    :type id: int
    :param current_user: El usuario actual.
    :type current_user: ProfesorDTO
    :param db: La sesión de la base de datos.
    :type db: Session
    :returns: El profesor encontrado.
    :rtype: ProfesorDTO
    :raises HTTPException: Si el usuario actual no tiene permisos para acceder a este recurso.
    """
    logger.info(f"Request recibida de {current_user.username}: Obtener profesor con ID {id}")
    if current_user.id_profesor != id and current_user.rol.id_rol > 3:
        raise HTTPException(status_code=403, detail="No tienes permisos para acceder a este recurso")
    return dao_profesor.get_profesor_by_id(id, db)


@router.post(
    '/',
    summary="Crea un profesor en la base de datos",
    description="Esta llamada crea un profesor en la base de datos",
    response_description="El profesor creado",
    response_model=ProfesorDTO,
    status_code=status.HTTP_201_CREATED
)
def create_profesor(
        request: ProfesorCreate,
        current_user: ProfesorDTO = Depends(check_admin_role),
        db: Session = Depends(get_db)
):
    """
    Crea un nuevo profesor.

    :param request: Los datos del profesor a crear.
    :type request: ProfesorCreate
    :param current_user: El usuario actual con rol de administrador.
    :type current_user: ProfesorDTO
    :param db: La sesión de la base de datos.
    :type db: Session
    :returns: El profesor creado.
    :rtype: ProfesorDTO
    """
    logger.info(f"Request recibida de {current_user.username}: Crear profesor con datos {request}")
    return dao_profesor.create_profesor(request, db)


@router.put(
    '/{id}',
    summary="Actualiza un profesor en la base de datos",
    description="Esta llamada actualiza un profesor en la base de datos",
    response_description="El profesor actualizado",
    response_model=ProfesorDTO,
    status_code=status.HTTP_200_OK
)
def update_profesor(
        id: int,
        request: ProfesorUpdate,
        current_user: ProfesorDTO = Depends(get_current_profesor),
        db: Session = Depends(get_db)
):
    """
    Actualiza un profesor existente.

    :param id: El ID del profesor a actualizar.
    :type id: int
    :param request: Los nuevos datos del profesor.
    :type request: ProfesorUpdate
    :param current_user: El usuario actual.
    :type current_user: ProfesorDTO
    :param db: La sesión de la base de datos.
    :type db: Session
    :returns: El profesor actualizado.
    :rtype: ProfesorDTO
    :raises HTTPException: Si el usuario actual no tiene permisos para acceder a este recurso.
    """
    if current_user.id_profesor != id and current_user.rol.id_rol > 3:
        raise HTTPException(status_code=403, detail="No tienes permisos para acceder a este recurso")
    logger.info(f"Request recibida de {current_user.username}: Actualizar profesor con ID {id} con datos {request}")
    return dao_profesor.update_profesor(id, request, db)


@router.delete(
    "/{id}",
    summary="Elimina un profesor de la base de datos",
    description="Esta llamada elimina un profesor de la base de datos",
    status_code=status.HTTP_204_NO_CONTENT)
def delete_profesor(
        id: int,
        current_user: ProfesorDTO = Depends(get_current_profesor),
        db: Session = Depends(get_db)
):
    """
    Elimina (desactiva) un profesor por su ID.

    :param id: El ID del profesor a eliminar.
    :type id: int
    :param current_user: El usuario actual.
    :type current_user: ProfesorDTO
    :param db: La sesión de la base de datos.
    :type db: Session
    :raises HTTPException: Si el usuario actual intenta eliminarse a sí mismo.
    """
    logger.info(f"Request recibida de {current_user.username}: Eliminar profesor con ID {id}")
    if current_user.id_profesor == id:
        raise HTTPException(status_code=409, detail="No se puede eliminar al profesor autenticado actualmente")
    dao_profesor.delete_profesor(id, db)
