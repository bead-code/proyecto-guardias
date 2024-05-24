import logging
from fastapi import HTTPException
from db.database import Session
from db.models import Actividad


def create_actividad(request: ActividadDb, db: Session):
    Actividad = db.query(Actividad).filter(Actividad.id == request.id).first()
    if Actividad:
        raise HTTPException(status_code=400, detail='La Actividad ya existe en la base de datos')

    new_asignatura = Actividad(
        codigo=request.codigo,
        nombre=request.nombre,
    )
    db.add(new_asignatura)
    try:
        logging.info("Insertando la actividad en la base de datos...")
        db.commit()
        db.refresh(new_asignatura)
        return new_asignatura
    except Exception as e:
        db.rollback()
        logging.error(f"Error occurred: {str(e)}")
        raise HTTPException(status_code=500, detail=f"Error al insertar la actividad en la BBDD: {str(e)}")


def get_actividad_by_codigo(codigo: str, db: Session):
    Actividad = db.query(Actividad).filter(Actividad.id == id).first()
    if not Actividad:
        raise HTTPException(status_code=404, detail="La actividad no existe en la base de datos")
    return Actividad


def update_asignatura():
    pass

def delete_asignatura(codigo: str, db: Session):
    Actividad = db.query(Actividad).filter(Actividad.codigo == codigo).first()
    if not Actividad:
        raise HTTPException(status_code=400, detail='La Actividad no existe en la base de datos')
    db.delete(Actividad)
    try:
        db.commit()
        db.refresh(Actividad)
    except Exception as e:
        db.rollback()
        raise HTTPException(status_code=500, detail=f"Error borrando la Actividad de la base de datos: {str(e)}")


