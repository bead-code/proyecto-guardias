from fastapi import HTTPException

from db.database import Session
from db.models import Rol
from db.schemas import RolDto, RolDb
import logging


def create_rol(request: RolDb, db: Session):
    new_rol = Rol(
        codigo=request.codigo
    )
    db.add(new_rol)
    db.commit()
    db.refresh(new_rol)
    return new_rol


def get_rol_by_codigo(codigo:str, db: Session):
    rol = db.query(Rol).filter(Rol.codigo == codigo).first()
    if not rol:
        raise HTTPException(status_code=404, detail='El rol no existe en la base de datos')
    return rol

def update_rol(request: RolDb, db: Session):
    pass

def delete_rol(codigo: str, db: Session):
    rol = db.query(RolDb).filter(RolDb.codigo == codigo).first()
    if not rol:
        raise HTTPException(status_code=404, detail="El rol no existe en la base de datos")
    db.delete(rol)
    try:
        db.commit()
        db.refresh(rol)
    except Exception as e:
        db.rollback()
        logging.error(f"Error occurred: {str(e)}")
        raise HTTPException(status_code=500, detail=f"Error al borrar el rol de la base de datos: {str(e)}")