from fastapi import HTTPException

from db.database import Session
from db.models import Clase
from db.schemas import ClaseCreate, ClaseUpdate
import logging


def get_clase_by_id(id: int, db: Session):
    clase = db.query(Clase).filter(Clase.id_clase == id).first()
    if not clase:
        raise HTTPException(status_code=404, detail="La clase no existe en la base de datos")
    return clase

def get_clase_by_nombre(nombre: str, db: Session):
    clase = db.query(Clase).filter(Clase.nombre == nombre).first()
    if not clase:
        raise HTTPException(status_code=404, detail="La clase no existe en la base de datos")
    return clase

def get_clases(db: Session):
    clases = db.query(Clase).all()
    if not clases:
        raise HTTPException(status_code=404, detail="No hay clases registradas en la base de datos")
    return clases

def create_clase(request: ClaseCreate, db: Session):
    clase = db.query(Clase).filter(Clase.nombre == request.nombre).first()
    if clase:
        raise HTTPException(status_code=409, detail="La clase ya existe en la base de datos")
    new_clase = Clase(
        nombre=request.nombre,
    )
    db.add(new_clase)
    try:
        db.commit()
        db.refresh(new_clase)
        return new_clase
    except Exception as e:
        db.rollback()
        logging.error(f"Error occurred: {str(e)}")
        raise HTTPException(status_code=500, detail=f"Error al insertar la clase en la BBDD: {str(e)}")

def update_clase(id: int, request: ClaseUpdate, db: Session):
    clase = get_clase_by_id(id, db)
    clase.nombre = request.nombre
    try:
        db.commit()
        db.refresh(clase)
        return clase
    except Exception as e:
        db.rollback()
        logging.error(f"Error occurred: {str(e)}")
        raise HTTPException(status_code=500, detail=f"Error al modificar la clase en la base de datos")

def delete_clase(id: int, db: Session):
    clase = get_clase_by_id(id, db)
    db.delete(clase)
    try:
        db.commit()
    except Exception as e:
        db.rollback()
        raise HTTPException(status_code=500, detail=f"Error borrando la clase de la base de datos: {str(e)}")

