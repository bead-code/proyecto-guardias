"""
DAO para gestionar las operaciones CRUD de las clases.

Este módulo define las funciones para manejar las operaciones CRUD de la entidad `Clase` en la base de datos.

Funciones
---------

* **get_clase_by_id**: Obtiene una clase por su ID.
* **get_clase_by_nombre**: Obtiene una clase por su nombre.
* **get_clases**: Obtiene todas las clases activas.
* **create_clase**: Crea una nueva clase.
* **update_clase**: Actualiza una clase existente.
* **delete_clase**: Elimina (desactiva) una clase por su ID.

Excepciones
-----------

* **HTTPException**: Excepción levantada si ocurre algún error durante las operaciones de base de datos.

Dependencias
------------

* **Session**: La sesión de la base de datos.
* **Clase**: El modelo de datos de la clase.
* **ClaseCreate**: El esquema de datos para crear una clase.
* **ClaseUpdate**: El esquema de datos para actualizar una clase.

"""
from fastapi import HTTPException
from db.database import Session
from db.models import Clase
from db.schemas import ClaseCreate, ClaseUpdate
from utils.logger import logger


def get_clase_by_id(id: int, db: Session):
    """
    Obtiene una clase por su ID.

    :param id: El ID de la clase a buscar.
    :type id: int
    :param db: La sesión de la base de datos.
    :type db: Session
    :returns: La clase encontrada.
    :rtype: Clase
    :raises HTTPException: Si la clase no existe en la base de datos.
    """
    clase = db.query(Clase).filter(Clase.id_clase == id).filter(Clase.activo == True).first()
    if not clase:
        logger.error(f"La clase con ID {id} no existe en la base de datos")
        raise HTTPException(status_code=404, detail="La clase no existe en la base de datos")
    logger.info(f"Clase retornada exitosamente")
    return clase

def get_clase_by_nombre(nombre: str, db: Session):
    """
    Obtiene una clase por su nombre.

    :param nombre: El nombre de la clase a buscar.
    :type nombre: str
    :param db: La sesión de la base de datos.
    :type db: Session
    :returns: La clase encontrada.
    :rtype: Clase
    :raises HTTPException: Si la clase no existe en la base de datos.
    """
    clase = db.query(Clase).filter(Clase.nombre == nombre).filter(Clase.activo == True).first()
    if not clase:
        logger.error(f"La clase con nombre {nombre} no existe en la base de datos")
        raise HTTPException(status_code=404, detail="La clase no existe en la base de datos")
    logger.info(f"Clase retornada exitosamente")
    return clase

def get_clases(db: Session):
    """
    Obtiene todas las clases activas.

    :param db: La sesión de la base de datos.
    :type db: Session
    :returns: Una lista de todas las clases activas.
    :rtype: List[Clase]
    :raises HTTPException: Si no hay clases registradas en la base de datos.
    """
    clases = db.query(Clase).filter(Clase.activo == True).all()
    if not clases:
        logger.error("No hay clases registradas en la base de datos")
        raise HTTPException(status_code=404, detail="No hay clases registradas en la base de datos")
    logger.info("Clases retornadas exitosamente")
    return clases

def create_clase(request: ClaseCreate, db: Session):
    """
    Crea una nueva clase.

    :param request: Los datos de la clase a crear.
    :type request: ClaseCreate
    :param db: La sesión de la base de datos.
    :type db: Session
    :returns: La clase creada.
    :rtype: Clase
    :raises HTTPException: Si la clase ya existe o si ocurre un error al insertarla.
    """
    clase = db.query(Clase).filter(Clase.nombre == request.nombre).first()
    if clase:
        logger.error(f"La clase con nombre {request.nombre} ya existe en la base de datos")
        raise HTTPException(status_code=409, detail="La clase ya existe en la base de datos")
    new_clase = Clase(
        nombre=request.nombre,
    )
    db.add(new_clase)
    try:
        db.commit()
        db.refresh(new_clase)
        logger.info(f"Clase creada exitosamente")
        return new_clase
    except Exception as e:
        db.rollback()
        logger.error(f"Error occurred: {str(e)}")
        raise HTTPException(status_code=500, detail=f"Error al insertar la clase en la BBDD: {str(e)}")

def update_clase(id: int, request: ClaseUpdate, db: Session):
    """
    Actualiza una clase existente.

    :param id: El ID de la clase a actualizar.
    :type id: int
    :param request: Los nuevos datos de la clase.
    :type request: ClaseUpdate
    :param db: La sesión de la base de datos.
    :type db: Session
    :returns: La clase actualizada.
    :rtype: Clase
    :raises HTTPException: Si ocurre un error al modificar la clase.
    """
    clase = get_clase_by_id(id, db)
    clase.nombre = request.nombre
    try:
        db.commit()
        db.refresh(clase)
        logger.info(f"Clase actualizada exitosamente")
        return clase
    except Exception as e:
        db.rollback()
        logger.error(f"Error occurred: {str(e)}")
        raise HTTPException(status_code=500, detail=f"Error al modificar la clase en la base de datos")

def delete_clase(id: int, db: Session):
    """
    Elimina (desactiva) una clase por su ID.

    :param id: El ID de la clase a eliminar.
    :type id: int
    :param db: La sesión de la base de datos.
    :type db: Session
    :raises HTTPException: Si ocurre un error al eliminar la clase.
    """
    clase = get_clase_by_id(id, db)
    clase.activo = False
    try:
        db.commit()
        db.refresh(clase)
        logger.info(f"Clase eliminada exitosamente")
    except Exception as e:
        db.rollback()
        logger.error(f"Error occurred: {str(e)}")
        raise HTTPException(status_code=500, detail=f"Error borrando la clase de la base de datos: {str(e)}")



