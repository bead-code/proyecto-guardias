import logging
from fastapi import HTTPException
from db.database import Session
from db.models import Aula
from db.schemas import AulaCreate, AulaUpdate

def get_aula_by_id(id: int, db: Session):
    """
    Obtiene un aula por su ID.

    :param id: El ID del aula a buscar.
    :type id: int
    :param db: La sesión de la base de datos.
    :type db: Session
    :returns: El aula encontrada.
    :rtype: Aula
    :raises HTTPException: Si el aula no existe en la base de datos.
    """
    aula = db.query(Aula).filter(Aula.id_aula == id).filter(Aula.activo == True).first()
    if not aula:
        raise HTTPException(status_code=404, detail="El aula no existe en la base de datos")
    return aula

def get_aula_by_nombre(nombre: str, db: Session):
    """
    Obtiene un aula por su nombre.

    :param nombre: El nombre del aula a buscar.
    :type nombre: str
    :param db: La sesión de la base de datos.
    :type db: Session
    :returns: El aula encontrada.
    :rtype: Aula
    :raises HTTPException: Si el aula no existe en la base de datos.
    """
    aula = db.query(Aula).filter(Aula.nombre == nombre).filter(Aula.activo == True).first()
    if not aula:
        raise HTTPException(status_code=404, detail="El aula no existe en la base de datos")
    return aula

def get_aulas(db: Session):
    """
    Obtiene todas las aulas activas.

    :param db: La sesión de la base de datos.
    :type db: Session
    :returns: Una lista de todas las aulas activas.
    :rtype: List[Aula]
    :raises HTTPException: Si no existen aulas en la base de datos.
    """
    aulas = db.query(Aula).filter(Aula.activo == True).all()
    if not aulas:
        raise HTTPException(status_code=404, detail="No existe ningún aula en la base de datos")
    return aulas

def create_aula(request: AulaCreate, db: Session):
    """
    Crea un nuevo aula.

    :param request: Los datos del aula a crear.
    :type request: AulaCreate
    :param db: La sesión de la base de datos.
    :type db: Session
    :returns: El aula creada.
    :rtype: Aula
    :raises HTTPException: Si el aula ya existe o si ocurre un error al insertarla.
    """
    aula = db.query(Aula).filter(Aula.nombre == request.nombre).filter(Aula.activo == True).first()
    if aula:
        raise HTTPException(status_code=409, detail='El aula ya existe en la base de datos')
    new_aula = Aula(
        nombre=request.nombre
    )
    db.add(new_aula)
    try:
        db.commit()
        db.refresh(new_aula)
        return new_aula
    except Exception as e:
        db.rollback()
        raise HTTPException(status_code=500, detail=f"Error al insertar el aula en la BBDD: {str(e)}")

def update_aula(id: int, request: AulaUpdate, db: Session):
    """
    Actualiza un aula existente.

    :param id: El ID del aula a actualizar.
    :type id: int
    :param request: Los nuevos datos del aula.
    :type request: AulaUpdate
    :param db: La sesión de la base de datos.
    :type db: Session
    :returns: El aula actualizada.
    :rtype: Aula
    :raises HTTPException: Si ocurre un error al modificar el aula.
    """
    aula = get_aula_by_id(id, db)
    aula.nombre = request.nombre
    try:
        db.commit()
        db.refresh(aula)
        return aula
    except Exception as e:
        db.rollback()
        logging.error(f"Error occurred: {str(e)}")
        raise HTTPException(status_code=500, detail=f"Error al modificar la aula en la base de datos")

def delete_aula(id: int, db: Session):
    """
    Elimina (desactiva) un aula por su ID.

    :param id: El ID del aula a eliminar.
    :type id: int
    :param db: La sesión de la base de datos.
    :type db: Session
    :raises HTTPException: Si ocurre un error al eliminar el aula.
    """
    aula = db.query(Aula).filter(Aula.id_aula == id).first()
    aula.activo = False
    try:
        db.commit()
        db.refresh(aula)
    except Exception as e:
        db.rollback()
        raise HTTPException(status_code=500, detail=f"Error al borrar el aula de la BBDD: {str(e)}")


