from datetime import date
from typing import Optional

from fastapi import HTTPException
from sqlalchemy import Date
from starlette import status

from db.database import Session
from db.models import Calendario, Profesor


def get_guardia_by_id(id: int, db: Session):
    calendario = db.query(Calendario).filter(Calendario.id == id).filter(Calendario.ausencia == True).first()
    if not calendario:
        raise HTTPException(
            status_code=status.HTTP_404_NOT_FOUND,
            detail="No se encontró la guardia"
        )
    return calendario

def get_guardias_by_fecha_tramo(id_profesor, fecha, id_tramo_horario, db):
    calendario = (
        db.query(Calendario)
        .filter(Calendario.id_profesor == id_profesor)
        .filter(Calendario.fecha == fecha)
        .filter(Calendario.id_tramo_horario == id_tramo_horario)
        .filter(Calendario.activo == True)
        .filter(Calendario.ausencia == True)
        .all()
    )
    if not calendario:
        raise HTTPException(
            status_code=status.HTTP_404_NOT_FOUND,
            detail="No hay guardias asignadas a este tramo horario"
        )
    return calendario

def get_guardias(db: Session):
    calendario = (
        db.query(Calendario)
        .filter(Calendario.ausencia == True)
        .filter(Calendario.activo == True)
        .all()
    )
    if not calendario:
        raise HTTPException(
            status_code=status.HTTP_404_NOT_FOUND,
            detail="No hay guardias en el calendario"
        )
    return calendario

def get_guardias_asignadas(db: Session):
    calendario = (
        db.query(Calendario)
        .filter(Calendario.id_profesor_sustituto != 9999)
        .filter(Calendario.ausencia == True)
        .filter(Calendario.activo == True)
        .all()
    )
    if not calendario:
        raise HTTPException(
            status_code=status.HTTP_404_NOT_FOUND,
            detail="No hay guardias cubiertas"
        )
    return calendario

def get_guardias_pendientes(db: Session):
    calendario = (
        db.query(Calendario)
        .filter(Calendario.id_profesor_sustituto == 9999)
        .filter(Calendario.ausencia == True)
        .filter(Calendario.activo == True)
        .all()
    )
    if not calendario:
        raise HTTPException(
            status_code=status.HTTP_404_NOT_FOUND,
            detail="No hay guardias sin cubrir"
        )
    return calendario


def get_guardias_by_profesor(id: int, db: Session, date: Optional[Date] = None):
    query = (db.query(Calendario)
             .filter(Calendario.id_profesor_sustituto == id)
             .filter(Calendario.ausencia == True)
             .filter(Calendario.activo == True)
             )
    if date:
        query = query.filter(Calendario.fecha == date)
    calendario = query.all()
    if not calendario:
        raise HTTPException(
            status_code=status.HTTP_404_NOT_FOUND,
            detail="No hay guardias asignadas a este profesor")
    return calendario


def create_guardia(id_profesor: int, fecha_inicio: date, id_tramo_horario: id, fecha_fin: date, db: Session):
    try:
        updated_rows = db.query(Calendario).filter(
            Calendario.id_profesor == id_profesor,
            Calendario.fecha >= fecha_inicio,
            Calendario.fecha <= fecha_fin,
            Calendario.id_tramo_horario == id_tramo_horario
        ).update({"ausencia": True}, synchronize_session='fetch')
        if updated_rows == 0:
            raise HTTPException(status_code=404, detail="No se encontraron registros para actualizar")

        updated_schedules = db.query(Calendario).filter(
            Calendario.id_profesor == id_profesor,
            Calendario.fecha >= fecha_inicio,
            Calendario.fecha <= fecha_fin,
            Calendario.ausencia == True
        ).all()

        db.commit()

    except Exception as e:
        db.rollback()
        raise HTTPException(status_code=500, detail=str(e))

    return updated_schedules

def assign_profesor_sustituto(id_calendario: int, id_profesor_sustituto: int, db: Session):
    db_calendario = db.query(Calendario).filter(Calendario.id_calendario == id_calendario).filter(Calendario.activo == True).first()
    if not db_calendario:
        raise HTTPException(status_code=status.HTTP_404_NOT_FOUND, detail="Registro no encontrado en el calendario")
    db_profesor_sustituto = db.query(Profesor).filter(Profesor.id_profesor == id_profesor_sustituto).first()
    if not db_profesor_sustituto:
        raise HTTPException(status_code=status.HTTP_404_NOT_FOUND, detail="Profesor sustituto no encontrado en la base de datos")
    db_calendario.id_profesor_sustituto = id_profesor_sustituto
    try:
        db.commit()
    except Exception as e:
        raise HTTPException(status_code=500, detail=f"Error al actualizar el calendario en la base de datos: {str(e)}")
    return db_calendario


