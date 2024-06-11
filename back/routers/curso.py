from typing import List
from fastapi import APIRouter, Depends
from sqlalchemy.orm import Session
from starlette import status
from dao import dao_curso
from db.database import get_db
from db.schemas import CursoDTO, CursoCreate, CursoUpdate, ProfesorDTO
from security.oauth2 import get_current_profesor, check_admin_role
from utils.logger import logger

router = APIRouter(
    prefix="/curso",
    tags=["curso"],
)

@router.get(
    "/{id}",
    summary="Devuelve un curso de la base de datos",
    description="Esta llamada devuelve un curso en base al ID del mismo",
    response_description="El curso de la base de datos",
    response_model=CursoDTO,
    status_code=status.HTTP_200_OK)
async def get_curso_by_id(
        id: int,
        current_user: ProfesorDTO = Depends(check_admin_role),
        db: Session = Depends(get_db)
):
    """
    Obtiene un curso por su ID.

    :param id: El ID del curso a buscar.
    :type id: int
    :param current_user: El usuario actual con rol de administrador.
    :type current_user: ProfesorDTO
    :param db: La sesión de la base de datos.
    :type db: Session
    :returns: El curso encontrado.
    :rtype: CursoDTO
    """
    logger.info(f"Request recibida de {current_user.username}: Obtener curso con ID {id}")
    return dao_curso.get_curso_by_id(id, db)

@router.get(
    "/nombre/{nombre}",
    summary="Devuelve un curso de la base de datos",
    description="Esta llamada devuelve un curso en base al nombre del mismo",
    response_description="El curso de la base de datos",
    response_model=CursoDTO,
    status_code=status.HTTP_200_OK
)
async def get_curso_by_nombre(
        nombre: str,
        current_user: ProfesorDTO = Depends(check_admin_role),
        db: Session = Depends(get_db)
):
    """
    Obtiene un curso por su nombre.

    :param nombre: El nombre del curso a buscar.
    :type nombre: str
    :param current_user: El usuario actual con rol de administrador.
    :type current_user: ProfesorDTO
    :param db: La sesión de la base de datos.
    :type db: Session
    :returns: El curso encontrado.
    :rtype: CursoDTO
    """
    logger.info(f"Request recibida de {current_user.username}: Obtener curso con nombre {nombre}")
    return dao_curso.get_curso_by_nombre(nombre, db)

@router.get(
    "/",
    summary="Devuelve todos los cursos de la base de datos",
    description="Esta llamada devuelve todos los cursos de la base de datos",
    response_description="Lista de todos los cursos de la base de datos",
    response_model=List[CursoDTO],
    status_code=status.HTTP_200_OK)
async def get_cursos(
        current_user: ProfesorDTO = Depends(check_admin_role),
        db: Session = Depends(get_db)
):
    """
    Obtiene todos los cursos activos.

    :param current_user: El usuario actual con rol de administrador.
    :type current_user: ProfesorDTO
    :param db: La sesión de la base de datos.
    :type db: Session
    :returns: Una lista de todos los cursos activos.
    :rtype: List[CursoDTO]
    """
    logger.info(f"Request recibida de {current_user.username}: Obtener todos los cursos")
    return dao_curso.get_cursos(db)

@router.post(
    "/",
    summary="Crea un curso en la base de datos",
    description="Esta llamada crea un curso en la base de datos",
    response_description="El curso creado en la base de datos",
    response_model=CursoDTO,
    status_code=status.HTTP_201_CREATED
)
async def create_curso(
        request: CursoCreate,
        current_user: ProfesorDTO = Depends(check_admin_role),
        db: Session = Depends(get_db)
):
    """
    Crea un nuevo curso.

    :param request: Los datos del curso a crear.
    :type request: CursoCreate
    :param current_user: El usuario actual con rol de administrador.
    :type current_user: ProfesorDTO
    :param db: La sesión de la base de datos.
    :type db: Session
    :returns: El curso creado.
    :rtype: CursoDTO
    """
    logger.info(f"Request recibida de {current_user.username}: Crear curso con nombre {request.nombre}")
    return dao_curso.create_curso(request, db)

@router.put(
    "/{id}",
    summary="Actualiza un curso en la base de datos",
    description="Esta llamada actualiza un curso en la base de datos",
    response_description="El curso actualizado en la base de datos",
    response_model=CursoDTO,
    status_code=status.HTTP_200_OK
)
async def update_curso(
        id: int,
        request: CursoUpdate,
        current_user: ProfesorDTO = Depends(check_admin_role),
        db: Session = Depends(get_db)
):
    """
    Actualiza un curso existente.

    :param id: El ID del curso a actualizar.
    :type id: int
    :param request: Los nuevos datos del curso.
    :type request: CursoUpdate
    :param current_user: El usuario actual con rol de administrador.
    :type current_user: ProfesorDTO
    :param db: La sesión de la base de datos.
    :type db: Session
    :returns: El curso actualizado.
    :rtype: CursoDTO
    """
    logger.info(f"Request recibida de {current_user.username}: Actualizar curso con ID {id}")
    return dao_curso.update_curso(id, request, db)

@router.delete(
    "/{id}",
    summary="Elimina un curso de la base de datos",
    description="Esta llamada elimina un curso en base a su ID",
    status_code=status.HTTP_204_NO_CONTENT
)
async def delete_curso(
        id: int,
        current_user: ProfesorDTO = Depends(check_admin_role),
        db: Session = Depends(get_db)
):
    """
    Elimina (desactiva) un curso por su ID.

    :param id: El ID del curso a eliminar.
    :type id: int
    :param current_user: El usuario actual con rol de administrador.
    :type current_user: ProfesorDTO
    :param db: La sesión de la base de datos.
    :type db: Session
    """
    logger.info(f"Request recibida de {current_user.username}: Eliminar curso con ID {id}")
    return dao_curso.delete_curso(id, db)


