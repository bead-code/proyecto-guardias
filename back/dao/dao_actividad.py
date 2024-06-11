from fastapi import HTTPException
from db.database import Session
from db.models import Actividad
from db.schemas import ActividadCreate, ActividadUpdate
from utils.logger import logger


def get_actividad_by_id(id: int, db: Session):
    """
    Obtiene una actividad por su ID.

    :param id: El ID de la actividad a buscar.
    :type id: int
    :param db: La sesión de la base de datos.
    :type db: Session
    :returns: La actividad encontrada.
    :rtype: Actividad
    :raises HTTPException: Si la actividad no existe en la base de datos.
    """
    actividad = db.query(Actividad).filter(Actividad.id_actividad == id).filter(Actividad.activo == True).first()
    if not actividad:
        logger.error(f"La actividad con ID {id} no existe en la base de datos")
        raise HTTPException(status_code=404, detail="La actividad no existe en la base de datos")
    logger.info(f"Actividad retornada exitosamente")
    return actividad

def get_actividad_by_nombre(nombre: str, db: Session):
    """
    Obtiene una actividad por su nombre.

    :param nombre: El nombre de la actividad a buscar.
    :type nombre: str
    :param db: La sesión de la base de datos.
    :type db: Session
    :returns: La actividad encontrada.
    :rtype: Actividad
    :raises HTTPException: Si la actividad no existe en la base de datos.
    """
    actividad = db.query(Actividad).filter(Actividad.nombre == nombre).filter(Actividad.activo == True).first()
    if not actividad:
        logger.error(f"La actividad con nombre {nombre} no existe en la base de datos")
        raise HTTPException(status_code=404, detail="La actividad no existe en la base de datos")
    logger.info(f"Actividad retornada exitosamente")
    return actividad

def get_actividades(db: Session):
    """
    Obtiene todas las actividades activas.

    :param db: La sesión de la base de datos.
    :type db: Session
    :returns: Una lista de todas las actividades activas.
    :rtype: List[Actividad]
    :raises HTTPException: Si no hay actividades registradas en la base de datos.
    """
    actividades = db.query(Actividad).filter(Actividad.activo == True).all()
    if not actividades:
        logger.error("No hay actividades registradas en la base de datos")
        raise HTTPException(status_code=404, detail="No hay actividades registradas en la base de datos")
    logger.info("Actividades retornadas exitosamente")
    return actividades

def create_actividad(request: ActividadCreate, db: Session):
    """
    Crea una nueva actividad.

    :param request: Los datos de la actividad a crear.
    :type request: ActividadCreate
    :param db: La sesión de la base de datos.
    :type db: Session
    :returns: La actividad creada.
    :rtype: Actividad
    :raises HTTPException: Si la actividad ya existe o si ocurre un error al insertarla.
    """
    actividad = db.query(Actividad).filter(Actividad.nombre == request.nombre).first()
    if actividad:
        logger.error(f"La actividad con nombre {request.nombre} ya existe en la base de datos")
        raise HTTPException(status_code=409, detail='La actividad ya existe en la base de datos')
    new_actividad = Actividad(
        nombre=request.nombre,
    )
    db.add(new_actividad)
    try:
        db.commit()
        db.refresh(new_actividad)
        logger.info("Actividad creada exitosamente")
        return new_actividad
    except Exception as e:
        db.rollback()
        logger.error(f"Error occurred: {str(e)}")
        raise HTTPException(status_code=500, detail=f"Error al insertar la actividad en la BBDD: {str(e)}")

def update_actividad(id: int, request: ActividadUpdate, db: Session):
    """
    Actualiza una actividad existente.

    :param id: El ID de la actividad a actualizar.
    :type id: int
    :param request: Los nuevos datos de la actividad.
    :type request: ActividadUpdate
    :param db: La sesión de la base de datos.
    :type db: Session
    :returns: La actividad actualizada.
    :rtype: Actividad
    :raises HTTPException: Si ocurre un error al modificar la actividad.
    """
    actividad = get_actividad_by_id(id, db)
    actividad.nombre = request.nombre
    try:
        db.commit()
        db.refresh(actividad)
        logger.info("Actividad actualizada exitosamente")
        return actividad
    except Exception as e:
        db.rollback()
        logger.error(f"Error occurred: {str(e)}")
        raise HTTPException(status_code=500, detail=f"Error al modificar la actividad en la base de datos")

def delete_actividad(id: int, db: Session):
    """
    Elimina (desactiva) una actividad por su ID.

    :param id: El ID de la actividad a eliminar.
    :type id: int
    :param db: La sesión de la base de datos.
    :type db: Session
    :raises HTTPException: Si ocurre un error al eliminar la actividad.
    """
    actividad = get_actividad_by_id(id, db)
    actividad.activo = False
    try:
        db.commit()
        db.refresh(actividad)
        logger.info("Actividad eliminada exitosamente")
    except Exception as e:
        db.rollback()
        logger.error(f"Error occurred: {str(e)}")
        raise HTTPException(status_code=500, detail=f"Error borrando la actividad de la base de datos: {str(e)}")



