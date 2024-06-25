"""
DAO para gestionar las operaciones CRUD de los roles.

Este módulo define las funciones para manejar las operaciones CRUD de la entidad `Rol` en la base de datos.

Funciones
---------

* **get_rol_by_id**: Obtiene un rol por su ID.
* **get_rol_by_nombre**: Obtiene un rol por su nombre.
* **get_roles**: Obtiene todos los roles activos.
* **create_rol**: Crea un nuevo rol.
* **update_rol**: Actualiza un rol existente.
* **delete_rol**: Elimina (desactiva) un rol por su ID.

Excepciones
-----------

* **HTTPException**: Excepción levantada si ocurre algún error durante las operaciones de base de datos.

Dependencias
------------

* **Session**: La sesión de la base de datos.
* **Rol**: El modelo de datos del rol.
* **RolCreate**: Esquema para la creación de un rol.
* **RolUpdate**: Esquema para la actualización de un rol.
"""
from fastapi import HTTPException
from db.database import Session
from db.models import Rol
from db.schemas import RolCreate, RolUpdate
from utils.logger import logger


def get_rol_by_id(id: int, db: Session):
    """
    Obtiene un rol por su ID.

    :param id: El ID del rol a buscar.
    :type id: int
    :param db: La sesión de la base de datos.
    :type db: Session
    :returns: El rol encontrado.
    :rtype: Rol
    :raises HTTPException: Si el rol no existe en la base de datos.
    """
    rol = db.query(Rol).filter(Rol.id_rol == id).filter(Rol.activo == True).first()
    if not rol:
        logger.error(f"El rol con ID {id} no existe en la base de datos")
        raise HTTPException(status_code=404, detail='El rol no existe en la base de datos')
    logger.info(f"Rol retornado exitosamente")
    return rol

def get_rol_by_nombre(nombre: str, db: Session):
    """
    Obtiene un rol por su nombre.

    :param nombre: El nombre del rol a buscar.
    :type nombre: str
    :param db: La sesión de la base de datos.
    :type db: Session
    :returns: El rol encontrado.
    :rtype: Rol
    :raises HTTPException: Si el rol no existe en la base de datos.
    """
    rol = db.query(Rol).filter(Rol.nombre == nombre).filter(Rol.activo == True).first()
    if not rol:
        logger.error(f"El rol con nombre {nombre} no existe en la base de datos")
        raise HTTPException(status_code=404, detail='El rol no existe en la base de datos')
    logger.info(f"Rol retornado exitosamente")
    return rol

def get_roles(db: Session):
    """
    Obtiene todos los roles activos.

    :param db: La sesión de la base de datos.
    :type db: Session
    :returns: Una lista de todos los roles activos.
    :rtype: List[Rol]
    :raises HTTPException: Si no hay roles registrados en la base de datos.
    """
    roles = db.query(Rol).filter(Rol.activo == True).all()
    if not roles:
        logger.error("No hay roles registrados en la base de datos")
        raise HTTPException(status_code=404, detail='No hay roles registrados en la base de datos')
    logger.info("Roles retornados exitosamente")
    return roles

def create_rol(request: RolCreate, db: Session):
    """
    Crea un nuevo rol.

    :param request: Los datos del rol a crear.
    :type request: RolCreate
    :param db: La sesión de la base de datos.
    :type db: Session
    :returns: El rol creado.
    :rtype: Rol
    :raises HTTPException: Si el rol ya existe o si ocurre un error al insertarlo.
    """
    rol = db.query(Rol).filter(Rol.nombre == request.nombre).first()
    if rol:
        logger.error(f"El rol con nombre {request.nombre} ya existe en la base de datos")
        raise HTTPException(status_code=409, detail='El rol ya existe en la base de datos')
    new_rol = Rol(
        nombre=request.nombre
    )
    db.add(new_rol)
    try:
        db.commit()
        db.refresh(new_rol)
        logger.info(f"Rol creado exitosamente")
        return new_rol
    except Exception as e:
        db.rollback()
        logger.error(f"Error occurred: {str(e)}")
        raise HTTPException(status_code=500, detail=f"Error al insertar el rol en la BBDD: {str(e)}")

def update_rol(id: int, request: RolUpdate, db: Session):
    """
    Actualiza un rol existente.

    :param id: El ID del rol a actualizar.
    :type id: int
    :param request: Los nuevos datos del rol.
    :type request: RolUpdate
    :param db: La sesión de la base de datos.
    :type db: Session
    :returns: El rol actualizado.
    :rtype: Rol
    :raises HTTPException: Si ocurre un error al modificar el rol.
    """
    rol = get_rol_by_id(id, db)
    rol.nombre = request.nombre
    try:
        db.commit()
        db.refresh(rol)
        logger.info(f"Rol actualizado exitosamente")
        return rol
    except Exception as e:
        db.rollback()
        logger.error(f"Error occurred: {str(e)}")
        raise HTTPException(status_code=500, detail=f"Error al modificar el rol en la base de datos")

def delete_rol(id: int, db: Session):
    """
    Elimina (desactiva) un rol por su ID.

    :param id: El ID del rol a eliminar.
    :type id: int
    :param db: La sesión de la base de datos.
    :type db: Session
    :raises HTTPException: Si ocurre un error al eliminar el rol.
    """
    rol = get_rol_by_id(id, db)
    rol.activo = False
    try:
        db.commit()
        db.refresh(rol)
        logger.info(f"Rol eliminado exitosamente")
    except Exception as e:
        db.rollback()
        logger.error(f"Error occurred: {str(e)}")
        raise HTTPException(status_code=500, detail=f"Error al borrar el rol de la base de datos: {str(e)}")

