import logging
from fastapi import HTTPException
from db.database import Session
from db.models import Actividad
from db.schemas import ActividadCreate, ActividadUpdate

def get_actividad_by_id(id: int, db: Session):
    actividad = db.query(Actividad).filter(Actividad.id_actividad == id).first()
    if not actividad:
        raise HTTPException(status_code=404, detail="La actividad no existe en la base de datos")
    return actividad

def get_actividad_by_nombre(nombre: str, db: Session):
    actividad = db.query(Actividad).filter(Actividad.nombre == nombre).first()
    if not actividad:
        raise HTTPException(status_code=404, detail="La actividad no existe en la base de datos")
    return actividad

def get_actividades(db: Session):
    actividades = db.query(Actividad).all()
    if not actividades:
        raise HTTPException(status_code=404, detail="No hay actividades registradas la base de datos")
    return actividades

def create_actividad(request: ActividadCreate, db: Session):
    actividad = get_actividad_by_nombre(request.nombre, db)
    if actividad:
        raise HTTPException(status_code=409, detail='La actividad ya existe en la base de datos')

    new_actividad = Actividad(
        nombre=request.nombre,
    )
    db.add(new_actividad)
    try:
        logging.info("Insertando la actividad en la base de datos...")
        db.commit()
        db.refresh(new_actividad)
        return new_actividad
    except Exception as e:
        db.rollback()
        logging.error(f"Error occurred: {str(e)}")
        raise HTTPException(status_code=500, detail=f"Error al insertar la actividad en la BBDD: {str(e)}")


def update_actividad(id: int, request: ActividadUpdate, db: Session):
    actividad = get_actividad_by_id(id, db)
    if not actividad:
        raise HTTPException(status_code=404, detail="La actividad no existe en la base de datos")
    actividad.nombre = request.nombre
    try:
        db.commit()
        db.refresh(actividad)
        return actividad
    except Exception as e:
        db.rollback()
        logging.error(f"Error occurred: {str(e)}")
        raise HTTPException(status_code=500, detail=f"Error al modificar la actividad en la base de datos")

def delete_actividad(id: int, db: Session):
    actividad = db.query(Actividad).filter(Actividad.id_actividad == id).first()
    if not actividad:
        raise HTTPException(status_code=400, detail='La Actividad no existe en la base de datos')
    db.delete(actividad)
    try:
        db.commit()
        db.refresh(actividad)
    except Exception as e:
        db.rollback()
        raise HTTPException(status_code=500, detail=f"Error borrando la actividad de la base de datos: {str(e)}")


