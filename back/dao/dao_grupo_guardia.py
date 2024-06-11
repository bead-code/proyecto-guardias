from fastapi import HTTPException
from starlette import status
from db.database import Session
from db.models import Calendario, Profesor
from utils.logger import logger

id_actividad_guardia = 65

def get_grupo_guardia(id_tramo: int, dia: int, db: Session):
    """
    Obtiene el grupo de guardia asignado a un tramo horario y día específicos.

    :param id_tramo: El ID del tramo horario.
    :type id_tramo: int
    :param dia: El día de la semana (0-6, donde 0 es lunes y 6 es domingo).
    :type dia: int
    :param db: La sesión de la base de datos.
    :type db: Session
    :returns: Una lista de profesores asignados a la guardia en el tramo horario y día especificados.
    :rtype: List[Profesor]
    :raises HTTPException: Si no hay guardias asignadas a este grupo de guardia.
    """
    profesor = (
        db.query(Profesor)
        .join(Calendario, Calendario.id_profesor == Profesor.id_profesor)
        .filter(Calendario.id_tramo_horario == id_tramo)
        .filter(Calendario.dia == dia)
        .filter(Calendario.activo == True)
        .filter(Calendario.id_actividad == id_actividad_guardia)
        .distinct()
        .all()
    )
    if not profesor:
        logger.error("No hay guardias asignadas a este grupo de guardia")
        raise HTTPException(
            status_code=status.HTTP_404_NOT_FOUND,
            detail="No hay guardias asignadas a este grupo de guardia"
        )
    logger.info("Grupo de guardia retornado exitosamente")
    return profesor

def get_grupos_guardia(db: Session):
    """
    Obtiene todos los grupos de guardia.

    :param db: La sesión de la base de datos.
    :type db: Session
    :returns: Un diccionario donde las claves son tuplas (día, id_tramo_horario) y los valores son listas de profesores asignados a guardias.
    :rtype: dict
    """
    resultados = (
        db.query(Calendario.dia, Calendario.id_tramo_horario, Profesor)
        .join(Profesor, Calendario.id_profesor == Profesor.id_profesor)
        .filter(Calendario.activo == True)
        .filter(Calendario.id_actividad == id_actividad_guardia)
        .all()
    )
    if not resultados:
        logger.error("No hay grupos de guardia registrados en la base de datos")
        raise HTTPException(
            status_code=status.HTTP_404_NOT_FOUND,
            detail="No hay grupos de guardia registrados en la base de datos"
        )
    grupos_guardia = {}
    for dia, id_tramo_horario, profesor in resultados:
        if (dia, id_tramo_horario) not in grupos_guardia:
            grupos_guardia[(dia, id_tramo_horario)] = []
        grupos_guardia[(dia, id_tramo_horario)].append(profesor)
    logger.info("Grupos de guardia retornados exitosamente")
    return grupos_guardia

def get_grupos_guardia_by_id_profesor(id_profesor:int, db: Session):
    """
    Obtiene todos los grupos de guardia de un profesor.

    :param db: La sesión de la base de datos.
    :type db: Session
    :returns: Un diccionario donde las claves son tuplas (día, id_tramo_horario) y los valores son listas del profesor asignado a guardias.
    :rtype: dict
    """
    resultados = (
        db.query(Calendario.dia, Calendario.id_tramo_horario, Profesor)
        .join(Profesor, Calendario.id_profesor == Profesor.id_profesor)
        .filter(id_profesor == Profesor.id_profesor)
        .filter(Calendario.activo == True)
        .filter(Calendario.id_actividad == id_actividad_guardia)
        .all()
    )
    if not resultados:
        logger.error("No hay grupos de guardia registrados en la base de datos")
        raise HTTPException(
            status_code=status.HTTP_404_NOT_FOUND,
            detail="No hay grupos de guardia registrados en la base de datos"
        )
    grupos_guardia = {}
    for dia, id_tramo_horario, profesor in resultados:
        if (dia, id_tramo_horario) not in grupos_guardia:
            grupos_guardia[(dia, id_tramo_horario)] = []
        grupos_guardia[(dia, id_tramo_horario)].append(profesor)
    logger.info("Grupos de guardia retornados exitosamente")
    return grupos_guardia