"""
DAO para gestionar las operaciones CRUD de los profesores.

Este módulo define las funciones para manejar las operaciones CRUD de la entidad `Profesor` en la base de datos.

Funciones
---------

* **get_profesor_by_id**: Obtiene un profesor por su ID.
* **get_profesor_by_username**: Obtiene un profesor por su nombre de usuario.
* **get_profesores**: Obtiene todos los profesores activos.
* **get_profesores_disponibles_by_id_calendario**: Obtiene los profesores disponibles en un tramo horario específico.
* **create_profesor**: Crea un nuevo profesor.
* **update_profesor**: Actualiza un profesor existente.
* **delete_profesor**: Elimina (desactiva) un profesor por su ID.

Excepciones
-----------

* **HTTPException**: Excepción levantada si ocurre algún error durante las operaciones de base de datos.

Dependencias
------------

* **Session**: La sesión de la base de datos.
* **Profesor**: El modelo de datos del profesor.
* **Rol**: El modelo de datos del rol.
* **Calendario**: El modelo de datos del calendario.
* **ProfesorCreate**: Esquema para la creación de un profesor.
* **ProfesorUpdate**: Esquema para la actualización de un profesor.
"""
from fastapi import HTTPException
from db.database import Session
from db.models import Profesor, Rol, Calendario
from db.schemas import ProfesorCreate, ProfesorUpdate
from datetime import date
from utils.logger import logger


def get_profesor_by_id(id: int, db: Session):
    """
    Obtiene un profesor por su ID.

    :param id: El ID del profesor a buscar.
    :type id: int
    :param db: La sesión de la base de datos.
    :type db: Session
    :returns: El profesor encontrado.
    :rtype: Profesor
    :raises HTTPException: Si el profesor no existe en la base de datos.
    """
    profesor = db.query(Profesor).filter(Profesor.id_profesor == id).filter(Profesor.activo == True).first()
    if not profesor:
        logger.error(f"El profesor con ID {id} no existe en la base de datos")
        raise HTTPException(status_code=404, detail="El profesor no existe en la base de datos")
    logger.info(f"Profesor retornado existosamente")
    return profesor

def get_profesor_by_username(username: str, db: Session):
    """
    Obtiene un profesor por su nombre de usuario.

    :param username: El nombre de usuario del profesor a buscar.
    :type username: str
    :param db: La sesión de la base de datos.
    :type db: Session
    :returns: El profesor encontrado.
    :rtype: Profesor
    :raises HTTPException: Si el profesor no existe en la base de datos.
    """
    profesor = db.query(Profesor).filter(Profesor.username == username).filter(Profesor.activo == True).first()
    if not profesor:
        logger.info(f"El profesor con username {username} no existe en la base de datos")
        raise HTTPException(status_code=404, detail="El profesor no existe en la base de datos")
    logger.info(f"Profesor retornado exitosamente")
    return profesor

def get_profesores(db: Session):
    """
    Obtiene todos los profesores activos.

    :param db: La sesión de la base de datos.
    :type db: Session
    :returns: Una lista de todos los profesores activos.
    :rtype: List[Profesor]
    :raises HTTPException: Si no hay profesores registrados en la base de datos.
    """
    profesores = db.query(Profesor).filter(Profesor.activo == True).all()
    if not profesores:
        logger.error("No hay profesores registrados en la base de datos")
        raise HTTPException(status_code=404, detail="No hay profesores registrados en la base de datos")
    logger.info(f"Profesores retornados existosamente")
    return profesores

def get_profesores_disponibles_by_id_calendario(fecha: date, id_tramo_horario: int, db: Session):
    """
    Obtiene los profesores disponibles en un tramo horario específico.

    :param fecha: La fecha del tramo horario.
    :type fecha: date
    :param id_tramo_horario: El ID del tramo horario.
    :type id_tramo_horario: int
    :param db: La sesión de la base de datos.
    :type db: Session
    :returns: Una lista de profesores disponibles.
    :rtype: List[Profesor]
    :raises HTTPException: Si no hay profesores disponibles en el tramo horario.
    """
    profesores = (
        db.query(Profesor)
        .join(Calendario, Calendario.id_profesor == Profesor.id_profesor)
        .filter(Calendario.fecha == fecha)
        .filter(Calendario.id_tramo_horario == id_tramo_horario)
        .filter(Calendario.id_actividad == 65)
        .filter(Profesor.activo == True)
        .all()
    )
    if not profesores:
        logger.error("No hay profesores disponibles en este tramo horario")
        raise HTTPException(status_code=404, detail="No hay profesores disponibles en este tramo horario")
    logger.info("Profesores disponibles retornados existosamente")
    return profesores

def create_profesor(request: ProfesorCreate, db: Session):
    """
    Crea un nuevo profesor.

    :param request: Los datos del profesor a crear.
    :type request: ProfesorCreate
    :param db: La sesión de la base de datos.
    :type db: Session
    :returns: El profesor creado.
    :rtype: Profesor
    :raises HTTPException: Si el rol es incorrecto, el profesor ya existe o si ocurre un error al insertarlo.
    """
    rol = db.query(Rol).filter(Rol.id == request.rol_id).filter(Profesor.activo == True).first()
    if not rol:
        logger.error("Rol incorrecto")
        raise HTTPException(status_code=404, detail="Rol incorrecto")
    profesor = db.query(Profesor).filter(Profesor.username == request.username).filter(Profesor.activo == True).first()
    if profesor:
        logger.error("El profesor ya existe en la BBDD")
        raise HTTPException(status_code=409, detail="El profesor ya existe en la BBDD")
    new_profesor = Profesor(
        username=request.username,
        nombre=request.nombre,
        id_rol=request.id_rol
    )

    db.add(new_profesor)
    try:
        logger.info("Insertando el profesor en la base de datos...")
        db.commit()
        db.refresh(new_profesor)
    except Exception as e:
        db.rollback()
        logger.error(f"Error occurred: {str(e)}")
        raise HTTPException(status_code=500, detail=f"Error al insertar al profesor en la base de datos: {str(e)}")

    return new_profesor

def update_profesor(id: int, request: ProfesorUpdate, db: Session):
    """
    Actualiza un profesor existente.

    :param id: El ID del profesor a actualizar.
    :type id: int
    :param request: Los nuevos datos del profesor.
    :type request: ProfesorUpdate
    :param db: La sesión de la base de datos.
    :type db: Session
    :returns: El profesor actualizado.
    :rtype: Profesor
    :raises HTTPException: Si ocurre un error al modificar el profesor.
    """
    profesor = get_profesor_by_id(id, db)
    for key, value in request.dict(exclude_unset=True).items():
        setattr(profesor, key, value)
    try:
        db.commit()
        db.refresh(profesor)
        logger.info("Profesor actualizado en la base de datos")
        return profesor
    except Exception as e:
        db.rollback()
        logger.error(f"Error occurred: {str(e)}")
        raise HTTPException(status_code=400)

def delete_profesor(id: int, db: Session):
    """
    Elimina (desactiva) un profesor por su ID.

    :param id: El ID del profesor a eliminar.
    :type id: int
    :param db: La sesión de la base de datos.
    :type db: Session
    :raises HTTPException: Si ocurre un error al eliminar el profesor.
    """
    profesor = get_profesor_by_id(id, db)
    profesor.activo = False
    calendarios = db.query(Calendario).filter(Calendario.id_profesor == id).filter(Calendario.fecha > date.today()).all()
    if not calendarios:
        logger.error("No hay calendarios asociados al profesor")
    for calendario in calendarios:
        calendario.activo = False
    try:
        db.commit()
        logger.info("Profesor borrado en la base de datos")
    except Exception as e:
        db.rollback()
        logger.error(f"Error occurred: {str(e)}")
        raise HTTPException(status_code=500, detail=f"Error al borrar el profesor de la base de datos: {str(e)}")


