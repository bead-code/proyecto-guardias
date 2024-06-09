from datetime import date, time
from typing import Optional

from fastapi import HTTPException
from sqlalchemy import Date
from starlette import status

from db.database import Session
from db.models import Calendario, Profesor, TramoHorario
import logging


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
        .first()
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
    return calendario

def get_guardias_asignadas(db: Session):
    calendario = (
        db.query(Calendario)
        .filter(Calendario.id_profesor_sustituto != 9999)
        .filter(Calendario.ausencia == True)
        .filter(Calendario.activo == True)
        .all()
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


def create_guardia(id_profesor: int, fecha_inicio: date, fecha_fin: date, hora_inicio: time,
                   hora_fin: time, db: Session):
    tramo_inicio = db.query(TramoHorario).filter(TramoHorario.hora_inicio <= hora_inicio,
                                                 TramoHorario.hora_fin > hora_inicio).first()
    tramo_fin = db.query(TramoHorario).filter(TramoHorario.hora_inicio <= hora_fin,
                                              TramoHorario.hora_fin > hora_fin).first()

    if not tramo_inicio or not tramo_fin:
        raise HTTPException(status_code=404, detail="Tramo horario no encontrado")

    try:
        update_query = db.query(Calendario).filter(
            Calendario.id_profesor == id_profesor,
            Calendario.fecha >= fecha_inicio,
            Calendario.fecha <= fecha_fin,
            Calendario.id_tramo_horario >= tramo_inicio.id_tramo_horario,
            Calendario.id_tramo_horario <= tramo_fin.id_tramo_horario
        ).update({Calendario.ausencia: True}, synchronize_session=False)
        db.commit()
    except Exception as e:
        db.rollback()
        raise HTTPException(status_code=500, detail=f"Error al actualizar el calendario en la base de datos: {str(e)}")

    if update_query == 0:
        raise HTTPException(status_code=404, detail="No se encontraron registros para actualizar")
    registros_actualizados = db.query(Calendario).filter(
        Calendario.id_profesor == id_profesor,
        Calendario.fecha >= fecha_inicio,
        Calendario.fecha <= fecha_fin,
        Calendario.id_tramo_horario >= tramo_inicio.id_tramo_horario,
        Calendario.id_tramo_horario <= tramo_fin.id_tramo_horario,
        Calendario.ausencia == True
    ).all()
    db.commit()
    return registros_actualizados

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


