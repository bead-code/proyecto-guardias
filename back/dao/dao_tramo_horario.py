from fastapi import HTTPException

from db.database import Session
from db.models import TramoHorario
from db.schemas import TramoHorarioCreate, TramoHorarioUpdate
import logging


def get_tramo_horario_by_id(id: int, db: Session):
    tramo = db.query(TramoHorario).filter(TramoHorario.id_tramo_horario == id).filter(TramoHorario.activo == True).first()
    if not tramo:
        raise HTTPException(status_code=404, detail="El tramo horario no existe en la base de datos")
    return tramo

def get_tramo_horario_by_nombre(nombre, db: Session):
    tramo = db.query(TramoHorario).filter(TramoHorario.nombre == nombre).filter(TramoHorario.activo == True).first()
    if not tramo:
        raise HTTPException(status_code=404, detail="El tramo horario no existe en la base de datos")
    return tramo

def get_tramos_horarios(db: Session):
    tramos = db.query(TramoHorario).filter(TramoHorario.activo == True).all()
    if not tramos:
        raise HTTPException(status_code=404, detail="No existen tramos horarios en la base de datos")
    return tramos

def create_tramo_horario(request: TramoHorarioCreate, db: Session):
    tramo = db.query(TramoHorario).filter(TramoHorario.nombre == request.nombre).first()
    if tramo:
        raise HTTPException(status_code=409, detail='El tramo horario ya existe en la base de datos')
    new_tramo = TramoHorario(
        nombre=request.nombre,
        hora_inicio=request.hora_inicio,
        hora_fin=request.hora_fin,
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
    tramo.activo = False
    try:
        db.commit()
        db.refresh(tramo)
    except Exception as e:
        db.rollback()
        raise HTTPException(status_code=500, detail=f"Error borrando el tramo de la base de datos: {str(e)}")

