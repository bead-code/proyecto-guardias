from fastapi import HTTPException
from db.database import Session
from db.models import Asignatura
from db.schemas import AsignaturaDb
import logging


def create_asignatura(request: AsignaturaDb, db: Session):
    asignatura = db.query(Asignatura).filter(Asignatura.codigo == request.codigo).first()
    if asignatura:
        raise HTTPException(status_code=400, detail='La asignatura ya existe en la base de datos')

    new_asignatura = Asignatura(
        codigo=request.codigo,
        nombre=request.nombre,
    )
    db.add(new_asignatura)
    try:
        logging.info("Insertando el asignaturar en la base de datos...")
        db.commit()
        db.refresh(new_asignatura)
        return new_asignatura
    except Exception as e:
        db.rollback()
        logging.error(f"Error occurred: {str(e)}")
        raise HTTPException(status_code=500, detail=f"Error al insertar la asignatura en la BBDD: {str(e)}")


def get_asignatura_by_codigo(codigo: str, db: Session):
    asignatura = db.query(Asignatura).filter(Asignatura.codigo == codigo).first()
    if not asignatura:
        raise HTTPException(status_code=404, detail="La asignatura no existe en la base de datos")
    return asignatura


def update_asignatura():
    pass

def delete_asignatura(codigo: str, db: Session):
    asignatura = db.query(Asignatura).filter(Asignatura.codigo == codigo).first()
    if not asignatura:
        raise HTTPException(status_code=400, detail='La asignatura no existe en la base de datos')
    db.delete(asignatura)
    try:
        db.commit()
        db.refresh(asignatura)
    except Exception as e:
        db.rollback()
        raise HTTPException(status_code=500, detail=f"Error borrando la asignatura de la base de datos: {str(e)}")


