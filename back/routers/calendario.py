"""
API Router para gestionar las operaciones CRUD del calendario.

Este módulo define las rutas y funciones para manejar las operaciones CRUD de la entidad `Calendario` en la base de datos.

Rutas
-----

* **GET /calendario/{id}**: Obtiene un calendario por su ID.
* **GET /calendario/{profesor_id}**: Obtiene el calendario de un profesor por su ID.
* **GET /calendario/profesor/{profesor_id}**: Obtiene el calendario actual de un profesor.
* **POST /calendario/**: Crea un nuevo calendario.
* **POST /calendario/generar_calendario/**: Genera el calendario para el año actual a partir de los XML enviados.

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
from io import BytesIO
from typing import List
from fastapi import APIRouter, UploadFile, File, Depends, HTTPException
from starlette import status
from dao import dao_calendario
from db.database import Session, get_db
from db.schemas import CalendarioDTO, ProfesorDTO, CalendarioCreate
from generador_calendario.generador_tablas import generate_tables_from_files
from security.oauth2 import get_current_profesor, check_admin_role
from utils.logger import logger


router = APIRouter(
    prefix="/calendario",
    tags=["calendario"],
)


@router.get(
    "/{id}",
    summary="Devuelve un calendario de la base de datos",
    description="Esta llamada devuelve un calendario en base a su id",
    response_description="El calendario de la base de datos",
    response_model=CalendarioDTO,
    status_code=status.HTTP_200_OK
)
def get_calendario_by_id(
        id: int,
        current_user: ProfesorDTO = Depends(check_admin_role),
        db: Session = Depends(get_db)
):
    """
    Obtiene un calendario por su ID.

    :param id: ID del calendario.
    :param current_user: Usuario autenticado con permisos de administrador.
    :param db: Sesión de la base de datos.
    :return: CalendarioDTO
    """
    logger.info(f"Request recibida de {current_user.username}: Obtener calendario con ID {id}")
    return dao_calendario.get_calendario_by_id(id, db)


@router.get(
    "/{profesor_id}",
    summary="Devuelve el calendario de un profesor",
    description="Esta llamada devuelve el calendario de un profesor en base a su id",
    response_model=List[CalendarioDTO],
    status_code=status.HTTP_200_OK
)
async def get_calendario_by_id_profesor(
        profesor_id: int,
        current_user: ProfesorDTO = Depends(get_current_profesor),
        db: Session = Depends(get_db)
):
    """
    Obtiene el calendario de un profesor por su ID.

    :param profesor_id: ID del profesor.
    :param current_user: Usuario autenticado.
    :param db: Sesión de la base de datos.
    :return: List[CalendarioDTO]
    """
    if current_user.id != profesor_id and current_user.rol.id_rol > 3:
        raise HTTPException(status_code=403, detail="No tienes permisos para realizar esta acción")
    logger.info(f"Request recibida de {current_user.username}: Obtener calendario con ID profesor {profesor_id}")
    return dao_calendario.get_calendario_by_id_profesor(profesor_id, db)


@router.get(
    "/profesor/{profesor_id}",
    summary="Devuelve el calendario de un profesor en base a la hora actual",
    description="Esta llamada devuelve el calendario de un profesor en base a la hora actual",
    response_description="El calendario de la base de datos",
    response_model=List[CalendarioDTO],
    status_code=status.HTTP_200_OK
)
async def get_actual_calendario_by_id_profesor(
        profesor_id: int,
        current_user: ProfesorDTO = Depends(get_current_profesor),
        db: Session = Depends(get_db)
):
    """
    Obtiene el calendario actual de un profesor por su ID.

    :param profesor_id: ID del profesor.
    :param current_user: Usuario autenticado.
    :param db: Sesión de la base de datos.
    :return: List[CalendarioDTO]
    """
    if current_user.id != profesor_id and current_user.rol.id_rol > 3:
        raise HTTPException(status_code=403, detail="No tienes permisos para realizar esta acción")
    logger.info(f"Request recibida de {current_user.username}: Obtener calendario actual con ID profesor {profesor_id}")
    return dao_calendario.get_actual_calendario_by_id_profesor(profesor_id, db)


@router.post(
    "/",
    summary="Crea un calendario en la base de datos",
    description="Esta llamada crea un calendario en la base de datos",
    response_description="El calendario creado",
    response_model=CalendarioDTO,
    status_code=status.HTTP_201_CREATED
)
async def create_calendario(
        calendario: CalendarioCreate,
        current_user: ProfesorDTO = Depends(check_admin_role),
        db: Session = Depends(get_db)
):
    """
    Crea un nuevo calendario.

    :param calendario: Datos para crear un nuevo calendario.
    :param current_user: Usuario autenticado con permisos de administrador.
    :param db: Sesión de la base de datos.
    :return: CalendarioDTO
    """
    logger.info(f"Request recibida de {current_user.username}: Crear calendario con datos {calendario}")
    return dao_calendario.create_calendario(calendario, db)


@router.post(
    "/generar_calendario/",
    summary="Genera el calendario para el año actual a partir de los XML enviados",
    description="Esta llamada genera el calendario para el año actual a partir de los XML enviados",
    status_code=status.HTTP_200_OK
)
async def upload_tables(
        tablas: UploadFile = File(...),
        calendario: UploadFile = File(...),
        current_user: ProfesorDTO = Depends(get_current_profesor)
):
    """
    Genera el calendario para el año actual a partir de los archivos XML enviados.

    :param tablas: Archivo XML con las tablas.
    :param calenario: Archivo XML con el calendario.
    :param current_user: Usuario autenticado.
    :return: Mensaje de éxito.
    """
    if current_user.rol.id_rol != 1:
        raise HTTPException(status_code=403, detail="No tienes permisos para realizar esta acción")
    tablas_byte = await tablas.read()
    horarios_byte = await calendario.read()
    generate_tables_from_files(BytesIO(tablas_byte), BytesIO(horarios_byte))
    return {"message": "Horarios generados correctamente"}



