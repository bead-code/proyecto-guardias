"""
DAO para gestionar las operaciones CRUD de los tramos horarios.

Este módulo define las funciones para manejar las operaciones CRUD de la entidad `TramoHorario` en la base de datos.

Funciones
---------

* **get_tramo_horario_by_id**: Obtiene un tramo horario por su ID.
* **get_tramo_horario_by_nombre**: Obtiene un tramo horario por su nombre.
* **get_tramos_horarios**: Obtiene todos los tramos horarios activos.
* **create_tramo_horario**: Crea un nuevo tramo horario.
* **update_tramo_horario**: Actualiza un tramo horario existente.
* **delete_tramo_horario**: Elimina (desactiva) un tramo horario por su ID.

Excepciones
-----------

* **HTTPException**: Excepción levantada si ocurre algún error durante las operaciones de base de datos.

Dependencias
------------

* **Session**: La sesión de la base de datos.
* **TramoHorario**: El modelo de datos del tramo horario.
* **TramoHorarioCreate**: Esquema para la creación de un tramo horario.
* **TramoHorarioUpdate**: Esquema para la actualización de un tramo horario.
"""
from fastapi import HTTPException
from db.database import Session
from db.models import TramoHorario
from db.schemas import TramoHorarioCreate, TramoHorarioUpdate
from utils.logger import logger


def get_tramo_horario_by_id(id: int, db: Session):
    """
    Obtiene un tramo horario por su ID.

    :param id: El ID del tramo horario a buscar.
    :type id: int
    :param db: La sesión de la base de datos.
    :type db: Session
    :returns: El tramo horario encontrado.
    :rtype: TramoHorario
    :raises HTTPException: Si el tramo horario no existe.
    """
    tramo = db.query(TramoHorario).filter(TramoHorario.id_tramo_horario == id).filter(TramoHorario.activo == True).first()
    if not tramo:
        logger.error(f"El tramo horario con ID {id} no existe en la base de datos")
        raise HTTPException(status_code=404, detail="El tramo horario no existe en la base de datos")
    logger.info(f"Tramo horario retornado exitosamente")
    return tramo

def get_tramo_horario_by_nombre(nombre: str, db: Session):
    """
    Obtiene un tramo horario por su nombre.

    :param nombre: El nombre del tramo horario a buscar.
    :type nombre: str
    :param db: La sesión de la base de datos.
    :type db: Session
    :returns: El tramo horario encontrado.
    :rtype: TramoHorario
    :raises HTTPException: Si el tramo horario no existe.
    """
    tramo = db.query(TramoHorario).filter(TramoHorario.nombre == nombre).filter(TramoHorario.activo == True).first()
    if not tramo:
        logger.error(f"El tramo horario con nombre {nombre} no existe en la base de datos")
        raise HTTPException(status_code=404, detail="El tramo horario no existe en la base de datos")
    logger.info(f"Tramo horario retornado exitosamente")
    return tramo

def get_tramos_horarios(db: Session):
    """
    Obtiene todos los tramos horarios activos.

    :param db: La sesión de la base de datos.
    :type db: Session
    :returns: Una lista de todos los tramos horarios activos.
    :rtype: List[TramoHorario]
    :raises HTTPException: Si no hay tramos horarios registrados.
    """
    tramos = db.query(TramoHorario).filter(TramoHorario.activo == True).all()
    if not tramos:
        logger.error("No existen tramos horarios en la base de datos")
        raise HTTPException(status_code=404, detail="No existen tramos horarios en la base de datos")
    logger.info("Tramos horarios retornados exitosamente")
    return tramos

def create_tramo_horario(request: TramoHorarioCreate, db: Session):
    """
    Crea un nuevo tramo horario.

    :param request: Los datos del tramo horario a crear.
    :type request: TramoHorarioCreate
    :param db: La sesión de la base de datos.
    :type db: Session
    :returns: El tramo horario creado.
    :rtype: TramoHorario
    :raises HTTPException: Si el tramo horario ya existe o si ocurre un error al insertarlo.
    """
    tramo = db.query(TramoHorario).filter(TramoHorario.nombre == request.nombre).first()
    if tramo:
        logger.error(f"El tramo horario con nombre {request.nombre} ya existe en la base de datos")
        raise HTTPException(status_code=409, detail='El tramo horario ya existe en la base de datos')
    new_tramo = TramoHorario(
        nombre=request.nombre,
        hora_inicio=request.hora_inicio,
        hora_fin=request.hora_fin,
    )
    db.add(new_tramo)
    try:
        db.commit()
        db.refresh(new_tramo)
        logger.info(f"Tramo horario insertado exitosamente")
        return new_tramo
    except Exception as e:
        db.rollback()
        logger.error(f"Error occurred: {str(e)}")
        raise HTTPException(status_code=500, detail=f"Error al insertar el tramo horario en la BBDD: {str(e)}")

def update_tramo_horario(id: int, request: TramoHorarioUpdate, db: Session):
    """
    Actualiza un tramo horario existente.

    :param id: El ID del tramo horario a actualizar.
    :type id: int
    :param request: Los nuevos datos del tramo horario.
    :type request: TramoHorarioUpdate
    :param db: La sesión de la base de datos.
    :type db: Session
    :returns: El tramo horario actualizado.
    :rtype: TramoHorario
    :raises HTTPException: Si ocurre un error al modificar el tramo horario.
    """
    tramo = get_tramo_horario_by_id(id, db)
    tramo.nombre = request.nombre
    try:
        db.commit()
        db.refresh(tramo)
        logger.info(f"Tramo horario actualizado exitosamente")
        return tramo
    except Exception as e:
        db.rollback()
        logger.error(f"Error occurred: {str(e)}")
        raise HTTPException(status_code=500, detail=f"Error al modificar el tramo en la base de datos")

def delete_tramo_horario(id: int, db: Session):
    """
    Elimina (desactiva) un tramo horario por su ID.

    :param id: El ID del tramo horario a eliminar.
    :type id: int
    :param db: La sesión de la base de datos.
    :type db: Session
    :raises HTTPException: Si ocurre un error al eliminar el tramo horario.
    """
    tramo = get_tramo_horario_by_id(id, db)
    tramo.activo = False
    try:
        db.commit()
        db.refresh(tramo)
        logger.info(f"Tramo horario eliminado exitosamente")
    except Exception as e:
        db.rollback()
        logger.error(f"Error occurred: {str(e)}")
        raise HTTPException(status_code=500, detail=f"Error borrando el tramo de la base de datos: {str(e)}")

