import logging

from fastapi import HTTPException

from db.database import Session
from db.models import Aula
from db.schemas import AulaCreate, AulaUpdate


def get_aula_by_id(id: int, db: Session):
    aula = db.query(Aula).filter(Aula.id_aula == id).filter(Aula.activo == True).first()
    if not aula:
        raise HTTPException(status_code=404, detail="El aula no existe en la base de datos")
    return aula


def get_aula_by_nombre(nombre: str, db: Session):
    aula = db.query(Aula).filter(Aula.nombre == nombre).filter(Aula.activo == True).first()
    if not aula:
        raise HTTPException(status_code=404, detail="El aula no existe en la base de datos")
    return aula

def get_aulas(db: Session):
    aulas = db.query(Aula).filter(Aula.activo == True).all()
    if not aulas:
        raise HTTPException(status_code=404, detail="No existe ningún aula en la base de datos")
    return aulas

def create_aula(request: AulaCreate, db: Session):
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

def delete_aula(id:  int, db: Session):
    aula = db.query(Aula).filter(Aula.id_aula == id).first()
    aula.activo = False
    try:
        db.commit()
        db.refresh(aula)
    except Exception as e:
        db.rollback()
        raise HTTPException(status_code=500, detail=f"Error al borrar el aula de la BBDD: {str(e)}")

