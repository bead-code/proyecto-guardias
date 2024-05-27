from fastapi import HTTPException

from db.database import Session
from db.models import TramoHorario
from db.schemas import TramoHorarioCreate, TramoHorarioUpdate
import logging


def get_tramo_horario_by_id(id: int, db: Session):
    tramo = db.query(TramoHorario).filter(TramoHorario.id_tramo_horario == id).first()
    if not tramo:
        raise HTTPException(status_code=404, detail="El tramo horario no existe en la base de datos")
    return tramo

def get_tramo_horario_by_nombre(nombre, db: Session):
    tramo = db.query(TramoHorario).filter(TramoHorario.nombre == nombre).first()
    if not tramo:
        raise HTTPException(status_code=404, detail="El tramo horario no existe en la base de datos")
    return tramo

def get_tramos_horarios(db: Session):
    tramos = db.query(TramoHorario).all()
    if not tramos:
        raise HTTPException(status_code=404, detail="No existen tramos horarios en la base de datos")
    return tramos

def create_tramo_horario(request: TramoHorarioCreate, db: Session):
    tramo = get_tramo_horario_by_nombre(request.nombre, db)
    if tramo:
        raise HTTPException(status_code=409, detail='El tramo horario ya existe en la base de datos')
    new_tramo = TramoHorario(
        nombre=request.nombre,
    )
    db.add(new_tramo)
    try:
        db.commit()
        db.refresh(new_tramo)
        return new_tramo
    except Exception as e:
        db.rollback()
        logging.error(f"Error occurred: {str(e)}")
        raise HTTPException(status_code=500, detail=f"Error al insertar el tramo horario en la BBDD: {str(e)}")

def update_tramo_horario(id: int, request: TramoHorarioUpdate, db: Session):
    tramo = get_tramo_horario_by_id(id, db)
    if not tramo:
        raise HTTPException(status_code=404, detail="El tramo horario no existe en la base de datos")
    tramo.nombre = request.nombre
    try:
        db.commit()
        db.refresh(tramo)
        return tramo
    except Exception as e:
        db.rollback()
        logging.error(f"Error occurred: {str(e)}")
        raise HTTPException(status_code=500, detail=f"Error al modificar el tramo en la base de datos")

def delete_tramo_horario(id: int, db: Session):
    tramo = get_tramo_horario_by_id(id, db)
    if not tramo:
        raise HTTPException(status_code=404, detail="El tramo horario no existe en la base de datos")
    db.delete(tramo)
    try:
        db.commit()
        db.refresh(tramo)
    except Exception as e:
        db.rollback()
        raise HTTPException(status_code=500, detail=f"Error borrando el tramo de la base de datos: {str(e)}")

