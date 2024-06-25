"""
API Router para gestionar las operaciones CRUD de las clases.

Este módulo define las rutas y funciones para manejar las operaciones CRUD de la entidad `Clase` en la base de datos.

Rutas
-----

* **GET /clase/{id}**: Obtiene una clase por su ID.
* **GET /clase/nombre/{nombre}**: Obtiene una clase por su nombre.
* **GET /clase/**: Obtiene todas las clases.
* **POST /clase/**: Crea una nueva clase.
* **PUT /clase/{id}**: Actualiza una clase existente.
* **DELETE /clase/{id}**: Elimina una clase por su ID.

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
from dao import dao_clase
from db.database import Session, get_db
from db.schemas import ClaseDTO, ClaseCreate, ClaseUpdate, ProfesorDTO
from security.oauth2 import get_current_profesor, check_admin_role
from utils.logger import logger

router = APIRouter(
    prefix="/clase",
    tags=["clase"],
)

@router.get(
    "/{id}",
    summary="Devuelve una clase de la base de datos",
    description="Esta llamada devuelve una clase en base al ID de la misma",
    response_description="La clase de la base de datos",
    response_model=ClaseDTO,
    status_code=status.HTTP_200_OK)
def get_clase_by_id(
        id: int,
        current_user: ProfesorDTO = Depends(check_admin_role),
        db: Session = Depends(get_db)
):
    """
    Obtiene una clase por su ID.

    :param id: El ID de la clase a buscar.
    :type id: int
    :param current_user: El usuario actual con rol de administrador.
    :type current_user: ProfesorDTO
    :param db: La sesión de la base de datos.
    :type db: Session
    :returns: La clase encontrada.
    :rtype: ClaseDTO
    """
    logger.info(f"Request recibida de {current_user.username}: Obtener clase con ID {id}")
    return dao_clase.get_clase_by_id(id, db)

@router.get(
    "/nombre/{nombre}",
    summary="Devuelve una clase de la base de datos",
    description="Esta llamada devuelve una clase en base al nombre de la misma",
    response_description="La clase de la base de datos",
    response_model=ClaseDTO,
    status_code=status.HTTP_200_OK
)
def get_clase_by_nombre(
        nombre: str,
        current_user: ProfesorDTO = Depends(check_admin_role),
        db: Session = Depends(get_db)
):
    """
    Obtiene una clase por su nombre.

    :param nombre: El nombre de la clase a buscar.
    :type nombre: str
    :param current_user: El usuario actual con rol de administrador.
    :type current_user: ProfesorDTO
    :param db: La sesión de la base de datos.
    :type db: Session
    :returns: La clase encontrada.
    :rtype: ClaseDTO
    """
    logger.info(f"Request recibida de {current_user.username}: Obtener clase con nombre {nombre}")
    return dao_clase.get_clase_by_nombre(nombre, db)

@router.get(
    "/",
    summary="Devuelve todas las clases de la base de datos",
    description="Esta llamada devuelve todas las clases de la base de datos",
    response_description="Lista de todas las clases de la base de datos",
    response_model=List[ClaseDTO],
    status_code=status.HTTP_200_OK
)
def get_clases(
        current_user: ProfesorDTO = Depends(check_admin_role),
        db: Session = Depends(get_db)
):
    """
    Obtiene todas las clases activas.

    :param current_user: El usuario actual con rol de administrador.
    :type current_user: ProfesorDTO
    :param db: La sesión de la base de datos.
    :type db: Session
    :returns: Una lista de todas las clases activas.
    :rtype: List[ClaseDTO]
    """
    logger.info(f"Request recibida de {current_user.username}: Obtener todas las clases")
    return dao_clase.get_clases(db)

@router.post(
    "/",
    summary="Crea una clase en la base de datos",
    description="Esta llamada crea una clase en la base de datos",
    response_description="La clase creada en la base de datos",
    response_model=ClaseDTO,
    status_code=status.HTTP_201_CREATED
)
def create_clase(
        request: ClaseCreate,
        current_user: ProfesorDTO = Depends(check_admin_role),
        db: Session = Depends(get_db)
):
    """
    Crea una nueva clase.

    :param request: Los datos de la clase a crear.
    :type request: ClaseCreate
    :param current_user: El usuario actual con rol de administrador.
    :type current_user: ProfesorDTO
    :param db: La sesión de la base de datos.
    :type db: Session
    :returns: La clase creada.
    :rtype: ClaseDTO
    """
    logger.info(f"Request recibida de {current_user.username}: Crear clase con nombre {request.nombre}")
    return dao_clase.create_clase(request, db)

@router.put(
    "/{id}",
    summary="Actualiza una clase en la base de datos",
    description="Esta llamada actualiza una clase en la base de datos",
    response_description="La clase actualizada en la base de datos",
    response_model=ClaseDTO,
    status_code=status.HTTP_200_OK
)
def update_clase(
        id: int,
        request: ClaseUpdate,
        current_user: ProfesorDTO = Depends(check_admin_role),
        db: Session = Depends(get_db)
):
    """
    Actualiza una clase existente.

    :param id: El ID de la clase a actualizar.
    :type id: int
    :param request: Los nuevos datos de la clase.
    :type request: ClaseUpdate
    :param current_user: El usuario actual con rol de administrador.
    :type current_user: ProfesorDTO
    :param db: La sesión de la base de datos.
    :type db: Session
    :returns: La clase actualizada.
    :rtype: ClaseDTO
    """
    logger.info(f"Request recibida de {current_user.username}: Actualizar clase con ID {id}")
    return dao_clase.update_clase(id, request, db)

@router.delete(
    "/{id}",
    summary="Elimina una clase de la base de datos",
    description="Esta llamada elimina una clase de la base de datos",
    status_code=status.HTTP_204_NO_CONTENT
)
def delete_clase(
        id: int,
        current_user: ProfesorDTO = Depends(check_admin_role),
        db: Session = Depends(get_db)
):
    """
    Elimina (desactiva) una clase por su ID.

    :param id: El ID de la clase a eliminar.
    :type id: int
    :param current_user: El usuario actual con rol de administrador.
    :type current_user: ProfesorDTO
    :param db: La sesión de la base de datos.
    :type db: Session
    """
    logger.info(f"Request recibida de {current_user.username}: Eliminar clase con ID {id}")
    return dao_clase.delete_clase(id, db)