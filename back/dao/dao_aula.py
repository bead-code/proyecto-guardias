from fastapi import HTTPException

from db.database import Session
from db.models import Aula
from db.schemas import AulaCreate, AulaUpdate
import logging


def get_aula_by_id(id: int, db: Session):
    aula = db.query(Aula).filter_by(Aula.id_aula == id).first()
    if not aula:
        raise HTTPException(status_code=404, detail="El aula no existe en la base de datos")
    return aula


def get_aula_by_nombre(nombre: str, db: Session):
    aula = db.query(Aula).filter_by(Aula.nombre == nombre).first()
    if not aula:
        raise HTTPException(status_code=404, detail="El aula no existe en la base de datos")
    return aula

def get_aulas(db: Session):
    aulas = db.query(Aula).all()
    if not aulas:
        raise HTTPException(status_code=404, detail="No existe ningún aula en la base de datos")
    return aulas

def create_aula(request: AulaCreate, db: Session):
    aula = db.query(Aula).filter(Aula.id_aula == request.id ).first()
    if aula:
        raise HTTPException(status_code=400, detail='El aula ya existe en la base de datos')
    new_aula = Aula(
        nombre=request.nombre
    )
    db.add(new_aula)
    try:
        db.commit()
        db.refresh(new_aula)
    except Exception as e:
        db.rollback()
        raise HTTPException(status_code=500, detail=f"Error al insertar el aula en la BBDD: {str(e)}")

def update_aula(id: int, request: AulaUpdate, db: Session):
    aula = get_aula_by_id(id, db)
    if not aula:
        raise HTTPException(status_code=404, detail="El aula no existe en la base de datos")
    aula.nombre = request.nombre
    try:
        db.commit()
        db.refresh(aula)
    except Exception as e:
        db.rollback()
        logging.error(f"Error occurred: {str(e)}")
        raise HTTPException(status_code=500, detail=f"Error al modificar la aula en la base de datos")

def delete_aula(id:  int, db: Session):
    aula = db.query(Aula).filter(Aula.id_aula == id).delete()
    if not aula:
        raise HTTPException(status_code=404, detail='El aula no existe en la base de datos')
    db.delete(aula)
    try:
        db.commit()
        db.refresh(aula)
    except Exception as e:
        raise HTTPException(status_code=500, detail=f"Error al borrar el aula de la BBDD: {str(e)}")

