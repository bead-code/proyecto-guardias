"""
API Router para gestionar las operaciones CRUD de las aulas.

Este módulo define las rutas y funciones para manejar las operaciones CRUD de la entidad `Aula` en la base de datos.

Rutas
-----

* **GET /aula/{id}**: Obtiene un aula por su ID.
* **GET /aula/nombre/{nombre}**: Obtiene un aula por su nombre.
* **GET /aula/**: Obtiene todas las aulas.
* **POST /aula/**: Crea un nuevo aula.
* **PUT /aula/{id}**: Actualiza un aula existente.
* **DELETE /aula/{id}**: Elimina un aula por su ID.

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
from dao import dao_aula
from db.database import Session, get_db
from db.schemas import AulaDTO, AulaUpdate, AulaCreate, ProfesorDTO
from security.oauth2 import get_current_profesor, check_admin_role
from utils.logger import logger

router = APIRouter(
    prefix="/aula",
    tags=["aula"],
)

@router.get(
    "/{id}",
    summary="Devuelve un aula de la base de datos",
    description="Esta llamada devuelve un aula en base al ID de la misma",
    response_description="El aula de la base de datos",
    response_model=AulaDTO,
    status_code=status.HTTP_200_OK
)
async def get_aula_by_id(
        id: int,
        current_user: ProfesorDTO = Depends(check_admin_role),
        db: Session = Depends(get_db)
):
    """
    Obtiene un aula por su ID.

    :param id: ID del aula.
    :param current_user: Usuario autenticado con permisos de administrador.
    :param db: Sesión de la base de datos.
    :return: AulaDTO
    """
    logger.info(f"Request recibida de {current_user.username}: Obtener aula con ID {id}")
    return dao_aula.get_aula_by_id(id, db)


@router.get(
    "/nombre/{nombre}",
    summary="Devuelve un aula de la base de datos",
    description="Esta llamada devuelve un aula en base al nombre de la misma",
    response_description="El aula de la base de datos",
    response_model=AulaDTO,
    status_code=status.HTTP_200_OK
)
async def get_aula_by_nombre(
        nombre: str,
        current_user: ProfesorDTO = Depends(check_admin_role),
        db: Session = Depends(get_db)
):
    """
    Obtiene un aula por su nombre.

    :param nombre: Nombre del aula.
    :param current_user: Usuario autenticado con permisos de administrador.
    :param db: Sesión de la base de datos.
    :return: AulaDTO
    """
    logger.info(f"Request recibida de {current_user.username}: Obtener aula con nombre {nombre}")
    return dao_aula.get_aula_by_nombre(nombre, db)


@router.get(
    "/",
    summary="Devuelve todas las aulas de la base de datos",
    description="Esta llamada devuelve todas las aulas de la base de datos",
    response_description="Lista de todas las aulas de la base de datos",
    response_model=List[AulaDTO],
    status_code=status.HTTP_200_OK)
async def get_aulas(
        current_user: ProfesorDTO = Depends(check_admin_role),
        db: Session = Depends(get_db)
):
    """
    Obtiene todas las aulas.

    :param current_user: Usuario autenticado con permisos de administrador.
    :param db: Sesión de la base de datos.
    :return: List[AulaDTO]
    """
    logger.info(f"Request recibida de {current_user.username}: Obtener todas las aulas")
    return dao_aula.get_aulas(db)


@router.post(
    "/",
    summary="Crea un aula en la base de datos",
    description="Esta llamada crea un aula en la base de datos",
    response_description="El aula creado en la base de datos",
    response_model=AulaDTO,
    status_code=status.HTTP_201_CREATED
)
async def create_aula(
        request: AulaCreate,
        current_user: ProfesorDTO = Depends(check_admin_role),
        db: Session = Depends(get_db)):
    """
    Crea un nuevo aula.

    :param request: Datos para crear un nuevo aula.
    :param current_user: Usuario autenticado con permisos de administrador.
    :param db: Sesión de la base de datos.
    :return: AulaDTO
    """
    logger.info(f"Request recibida de {current_user.username}: Crear aula con nombre {request.nombre}")
    return dao_aula.create_aula(request, db)


@router.put(
    "{id}",
    summary="Actualiza un aula de la base de datos",
    description="Esta llamada actualiza un aula en base al ID de la misma",
    response_description="El aula actualizado en la base de datos",
    response_model=AulaDTO,
    status_code=status.HTTP_200_OK
)
async def update_aula(
        id: int, request: AulaUpdate,
        current_user: ProfesorDTO = Depends(check_admin_role),
        db: Session = Depends(get_db)
):
    """
    Actualiza un aula por su ID.

    :param id: ID del aula a actualizar.
    :param request: Datos actualizados del aula.
    :param current_user: Usuario autenticado con permisos de administrador.
    :param db: Sesión de la base de datos.
    :return: AulaDTO
    """
    logger.info(f"Request recibida de {current_user.username}: Actualizar aula con ID {id}")
    return dao_aula.update_aula(id, request, db)


@router.delete(
    "/{id}",
    summary="Elimina un aula de la base de datos",
    description="Esta llamada elimina un aula en base al ID de la misma",
    status_code=status.HTTP_204_NO_CONTENT
)
async def delete_aula(
        id: int,
        current_user: ProfesorDTO = Depends(check_admin_role),
        db: Session = Depends(get_db)
):
    """
    Elimina un aula por su ID.

    :param id: ID del aula a eliminar.
    :param current_user: Usuario autenticado con permisos de administrador.
    :param db: Sesión de la base de datos.
    """
    logger.info(f"Request recibida de {current_user.username}: Eliminar aula con ID {id}")
    return dao_aula.delete_aula(id, db)