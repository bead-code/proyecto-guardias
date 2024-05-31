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
                  .filter(Calendario.ausencia == True))
    if date:
        query = query.filter(Calendario.fecha == date)
    calendario = query.all()
    if not calendario:
        raise HTTPException(
            status_code=status.HTTP_404_NOT_FOUND,
            detail="No hay guardias asignadas a este profesor")
    return calendario