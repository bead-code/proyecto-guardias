"""
DAO para gestionar las operaciones de guardias.

Este módulo define las funciones para manejar las operaciones de la entidad `Guardia` en la base de datos.

Funciones
---------

* **get_guardia_by_id**: Obtiene una guardia por su ID.
* **get_guardia_by_fecha_tramo**: Obtiene la guardia de un profesor filtrada por fecha y tramo horario.
* **get_guardias**: Obtiene todas las guardias activas.
* **get_guardias_asignadas**: Obtiene todas las guardias asignadas.
* **get_guardias_pendientes**: Obtiene todas las guardias pendientes.
* **get_guardias_by_profesor**: Obtiene guardias asignadas a un profesor.
* **get_assignable_guardias**: Obtiene todas las guardias asignables a un profesor.
* **create_guardia**: Crea una nueva guardia.
* **assign_profesor_sustituto**: Asigna un profesor sustituto a una guardia.

Excepciones
-----------

* **HTTPException**: Excepción levantada si ocurre algún error durante las operaciones de base de datos.

Dependencias
------------

* **Session**: La sesión de la base de datos.
* **Calendario**: El modelo de datos del calendario.
* **Profesor**: El modelo de datos del profesor.
* **TramoHorario**: El modelo de datos del tramo horario.

"""
from datetime import date, time
from typing import Optional
from fastapi import HTTPException
from sqlalchemy import Date
from starlette import status
from db.database import Session
from db.models import Calendario, Profesor, TramoHorario
from utils.logger import logger


def get_guardia_by_id(id: int, db: Session):
    """
    Obtiene una guardia por su ID.

    :param id: El ID de la guardia a buscar.
    :type id: int
    :param db: La sesión de la base de datos.
    :type db: Session
    :returns: La guardia encontrada.
    :rtype: Calendario
    :raises HTTPException: Si la guardia no existe.
    """
    calendario = db.query(Calendario).filter(Calendario.id == id).filter(Calendario.ausencia == True).first()
    if not calendario:
        logger.error(f"La guardia con ID {id} no existe en la base de datos")
        raise HTTPException(
            status_code=status.HTTP_404_NOT_FOUND,
            detail="No se encontró la guardia"
        )
    logger.info(f"Guardia retornada exitosamente")
    return calendario

def get_guardia_by_fecha_tramo(id_profesor: int, fecha: date, id_tramo_horario: int, db: Session):
    """
    Obtiene la guardia de un profesor filtrada por fecha y tramo horario.

    :param id_profesor: El ID del profesor.
    :type id_profesor: int
    :param fecha: La fecha de la guardia.
    :type fecha: date
    :param id_tramo_horario: El ID del tramo horario.
    :type id_tramo_horario: int
    :param db: La sesión de la base de datos.
    :type db: Session
    :returns: La guardia encontrada.
    :rtype: Calendario
    :raises HTTPException: Si no hay guardias asignadas.
    """
    calendario = (
        db.query(Calendario)
        .filter(Calendario.id_profesor == id_profesor)
        .filter(Calendario.fecha == fecha)
        .filter(Calendario.id_tramo_horario == id_tramo_horario)
        .filter(Calendario.activo == True)
        .filter(Calendario.ausencia == True)
        .group_by(Calendario.id_profesor, Calendario.fecha, Calendario.id_tramo_horario)
        .first()
    )
    if not calendario:
        logger.error(f"No hay guardias asignadas para el profesor {id_profesor} en la fecha {fecha} y tramo horario {id_tramo_horario}")
        raise HTTPException(
            status_code=status.HTTP_404_NOT_FOUND,
            detail="No hay guardias asignadas a este tramo horario"
        )
    logger.info(f"Guardia retornada exitosamente")
    return calendario

def get_guardias(db: Session):
    """
    Obtiene todas las guardias activas.

    :param db: La sesión de la base de datos.
    :type db: Session
    :returns: Una lista de todas las guardias activas.
    :rtype: List[Calendario]
    """
    calendario = (
        db.query(Calendario)
        .filter(Calendario.ausencia == True)
        .filter(Calendario.activo == True)
        .group_by(Calendario.id_profesor, Calendario.fecha, Calendario.id_tramo_horario)
        .all()
    )
    if not calendario:
        logger.error("No hay guardias asignadas en la base de datos")
        raise HTTPException(
            status_code=status.HTTP_404_NOT_FOUND,
            detail="No hay guardias asignadas en la base de datos"
        )
    logger.info(f"Guardias retornadas exitosamente")
    return calendario

def get_guardias_asignadas(db: Session):
    """
    Obtiene todas las guardias asignadas.

    :param db: La sesión de la base de datos.
    :type db: Session
    :returns: Una lista de todas las guardias asignadas.
    :rtype: List[Calendario]
    """
    calendario = (
        db.query(Calendario)
        .filter(Calendario.id_profesor_sustituto != 9999)
        .filter(Calendario.ausencia == True)
        .filter(Calendario.activo == True)
        .group_by(Calendario.id_profesor, Calendario.fecha, Calendario.id_tramo_horario)
        .all()
    )
    if not calendario:
        logger.error("No hay guardias asignadas en la base de datos")
        raise HTTPException(
            status_code=status.HTTP_404_NOT_FOUND,
            detail="No hay guardias asignadas en la base de datos"
        )
    logger.info(f"Guardias retornadas exitosamente")
    return calendario

def get_guardias_pendientes(db: Session):
    """
    Obtiene todas las guardias pendientes.

    :param db: La sesión de la base de datos.
    :type db: Session
    :returns: Una lista de todas las guardias pendientes.
    :rtype: List[Calendario]
    """
    calendario = (
        db.query(Calendario)
        .filter(Calendario.id_profesor_sustituto == 9999)
        .filter(Calendario.ausencia == True)
        .filter(Calendario.activo == True)
        .group_by(Calendario.id_profesor, Calendario.fecha, Calendario.id_tramo_horario)
        .all()
    )
    if not calendario:
        logger.error("No hay guardias pendientes en la base de datos")
        raise HTTPException(
            status_code=status.HTTP_404_NOT_FOUND,
            detail="No hay guardias pendientes en la base de datos"
        )
    logger.info(f"Guardias retornadas exitosamente")
    return calendario

def get_guardias_by_profesor(id: int, db: Session, date: Optional[Date] = None):
    """
    Obtiene guardias asignadas a un profesor.

    :param id: El ID del profesor.
    :type id: int
    :param db: La sesión de la base de datos.
    :type db: Session
    :param date: La fecha de las guardias a buscar (opcional).
    :type date: Optional[Date]
    :returns: Una lista de guardias asignadas al profesor.
    :rtype: List[Calendario]
    :raises HTTPException: Si no hay guardias asignadas al profesor.
    """
    query = (db.query(Calendario)
             .filter(Calendario.id_profesor_sustituto == id)
             .filter(Calendario.ausencia == True)
             .filter(Calendario.activo == True)
             )
    if date:
        query = query.filter(Calendario.fecha == date)
    calendario = query.all()
    if not calendario:
        logger.error(f"No hay guardias asignadas al profesor {id}")
        raise HTTPException(
            status_code=status.HTTP_404_NOT_FOUND,
            detail="No hay guardias asignadas a este profesor")
    logger.info(f"Guardias retornadas exitosamente")
    return calendario

def get_assignable_guardias(id_profesor, db: Session):
    """
    Obtiene todas las guardias asignables a un profesor.

    :param current_user: El usuario actual.
    :type current_user: ProfesorDTO
    :param db: La sesión de la base de datos.
    :type db: Session
    :returns: Una lista de guardias asignables.
    :rtype: List[Calendario]
    :raises HTTPException: Si no hay guardias asignables.
    """
    guardias = get_guardias(db)
    for guardia in guardias:
        if not (
            db.query(Calendario)
            .filter(Calendario.id_profesor == id_profesor)
            .filter(Calendario.fecha == guardia.fecha)
            .filter(Calendario.id_tramo_horario == guardia.id_tramo_horario)
            .filter(Calendario.id_actividad == 65)
            .filter(Profesor.activo == True)
            .first()
        ):
            guardias.remove(guardia)
    if not guardias:
        logger.error("No hay guardias asignables en la base de datos")
        raise HTTPException(
            status_code=status.HTTP_404_NOT_FOUND,
            detail="No hay guardias asignables en la base de datos"
        )
    logger.info(f"Guardias asignables retornadas exitosamente")
    return guardias

def create_guardia(id_profesor: int, fecha_inicio: date, fecha_fin: date, hora_inicio: time,
                   hora_fin: time, db: Session):
    """
    Crea una nueva guardia.

    :param id_profesor: El ID del profesor.
    :type id_profesor: int
    :param fecha_inicio: La fecha de inicio de la guardia.
    :type fecha_inicio: date
    :param fecha_fin: La fecha de fin de la guardia.
    :type fecha_fin: date
    :param hora_inicio: La hora de inicio de la guardia.
    :type hora_inicio: time
    :param hora_fin: La hora de fin de la guardia.
    :type hora_fin: time
    :param db: La sesión de la base de datos.
    :type db: Session
    :returns: Una lista de registros actualizados.
    :rtype: List[Calendario]
    :raises HTTPException: Si no se encontraron registros para actualizar o si ocurre un error al actualizar.
    """
    tramo_inicio = db.query(TramoHorario).filter(TramoHorario.hora_inicio <= hora_inicio).order_by(TramoHorario.hora_inicio.desc()).first()
    tramo_fin = db.query(TramoHorario).filter(TramoHorario.hora_fin >= hora_fin).order_by(TramoHorario.hora_fin.asc()).first()
    update_query = 0
    try:
        update_query += db.query(Calendario).filter(
            Calendario.id_profesor == id_profesor,
            Calendario.fecha == fecha_inicio,
            Calendario.id_tramo_horario >= tramo_inicio.id_tramo_horario
        ).update({Calendario.ausencia: True}, synchronize_session=False)
        update_query += db.query(Calendario).filter(
            Calendario.id_profesor == id_profesor,
            Calendario.fecha == fecha_fin,
            Calendario.id_tramo_horario <= tramo_fin.id_tramo_horario
        ).update({Calendario.ausencia: True}, synchronize_session=False)
        update_query += db.query(Calendario).filter(
            Calendario.id_profesor == id_profesor,
            Calendario.fecha > fecha_inicio,
            Calendario.fecha < fecha_fin
        ).update({Calendario.ausencia: True}, synchronize_session=False)
        db.commit()
        logger.info("Calendario actualizado exitosamente")
    except Exception as e:
        logger.error(f"Error al actualizar el calendario en la base de datos: {str(e)}")
        raise HTTPException(status_code=500, detail=f"Error al actualizar el calendario en la base de datos: {str(e)}")

    if update_query == 0:
        logger.error("No se encontraron registros para actualizar")
        raise HTTPException(status_code=404, detail="No se encontraron registros para actualizar")
    registros_actualizados = db.query(Calendario).filter(
        Calendario.id_profesor == id_profesor,
        Calendario.fecha >= fecha_inicio,
        Calendario.fecha <= fecha_fin,
        Calendario.id_tramo_horario >= tramo_inicio.id_tramo_horario,
        Calendario.id_tramo_horario <= tramo_fin.id_tramo_horario,
        Calendario.ausencia == True
    ).all()
    db.commit()
    logger.info("Registros actualizados retornados exitosamente")
    return registros_actualizados

def assign_profesor_sustituto(id_calendario: int, id_profesor_sustituto: int, db: Session):
    """
    Asigna un profesor sustituto a una guardia.

    :param id_calendario: El ID del registro del calendario.
    :type id_calendario: int
    :param id_profesor_sustituto: El ID del profesor sustituto.
    :type id_profesor_sustituto: int
    :param db: La sesión de la base de datos.
    :type db: Session
    :returns: El registro del calendario actualizado.
    :rtype: Calendario
    :raises HTTPException: Si el registro no se encuentra o si ocurre un error al actualizar.
    """
    db_calendario = db.query(Calendario).filter(Calendario.id_calendario == id_calendario).filter(Calendario.activo == True).first()
    if not db_calendario:
        logger.error(f"Registro con ID {id_calendario} no encontrado en el calendario")
        raise HTTPException(status_code=status.HTTP_404_NOT_FOUND, detail="Registro no encontrado en el calendario")
    db_profesor_sustituto = db.query(Profesor).filter(Profesor.id_profesor == id_profesor_sustituto).first()
    if not db_profesor_sustituto:
        logger.error(f"Profesor sustituto con ID {id_profesor_sustituto} no encontrado en la base de datos")
        raise HTTPException(status_code=status.HTTP_404_NOT_FOUND, detail="Profesor sustituto no encontrado en la base de datos")
    db_calendario.id_profesor_sustituto = id_profesor_sustituto
    try:
        db.commit()
        db.refresh(db_calendario)
        logger.info("Profesor sustituto asignado exitosamente")
        return db_calendario
    except Exception as e:
        logger.error(f"Error al actualizar el calendario en la base de datos: {str(e)}")
        raise HTTPException(status_code=500, detail=f"Error al actualizar el calendario en la base de datos: {str(e)}")










