from datetime import date
from typing import Optional

from fastapi import HTTPException
from sqlalchemy import Date
from starlette import status

from db.database import Session
from db.models import Calendario


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


def create_guardia(id_profesor: int, fecha_inicio: date, fecha_fin: date, db: Session):
    try:

        updated_rows = db.query(Calendario).filter(
            Calendario.id_profesor == id_profesor,
            Calendario.fecha >= fecha_inicio,
            Calendario.fecha <= fecha_fin
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