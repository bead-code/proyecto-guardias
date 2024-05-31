from typing import Optional

from fastapi import HTTPException
from sqlalchemy import Date
from starlette import status
from db.database import Session
from db.models import Calendario


def get_guardias_pendientes_by_grupo_guardia(id_tramo: int, dia: int, db: Session):
    calendario = (db.query(Calendario)
                  .filter(Calendario.id_tramo_horario == id_tramo)
                  .filter(Calendario.dia == dia)
                  .filter(Calendario.ausencia == True)
                  .filter(Calendario.id_profesor_sustituto == 9999).all()
                  )
    if not calendario:
        raise HTTPException(
            status_code=status.HTTP_404_NOT_FOUND,
            detail="No hay guardias asignadas a este grupo de guardia"
        )
    return calendario

def get_guardias_asignadas_by_grupo_guardia(id_tramo: int, dia: int, db: Session):
    calendario = (db.query(Calendario)
                  .filter(Calendario.id_tramo_horario == id_tramo)
                  .filter(Calendario.dia == dia)
                  .filter(Calendario.ausencia == True)
                  .filter(Calendario.id_profesor_sustituto != 9999).all()
                  )
    if not calendario:
        raise HTTPException(
            status_code=status.HTTP_404_NOT_FOUND,
            detail="No hay guardias asignadas a este grupo de guardia"
        )
    return calendario
