import logging

from fastapi import HTTPException
from db.database import Session
from db.models import Rol
from db.schemas import RolCreate, RolUpdate


def get_rol_by_id(id: int, db: Session):
    rol = db.query(Rol).filter(Rol.id_rol == id).first()
    if not rol:
        raise HTTPException(status_code=404, detail='El rol no existe en la base de datos')
    return rol


def get_rol_by_nombre(nombre: str, db: Session):
    rol = db.query(Rol).filter(Rol.nombre == nombre).first()
    if not rol:
        raise HTTPException(status_code=404, detail='El rol no existe en la base de datos')
    return rol


def get_roles(db: Session):
    roles = db.query(Rol).all()
    if not roles:
        raise HTTPException(status_code=404, detail='No hay roles registrados en la base de datos')
    return roles


def create_rol(request: RolCreate, db: Session):
    rol = db.query(Rol).filter(Rol.nombre == request.nombre).first()
    if rol:
        raise HTTPException(status_code=409, detail='El rol ya existe en la base de datos')
    new_rol = Rol(
        nombre=request.nombre
    )
    db.add(new_rol)
    try:
        db.commit()
        db.refresh(new_rol)
        return new_rol
    except Exception as e:
        db.rollback()
        logging.error(f"Error occurred: {str(e)}")
        raise HTTPException(status_code=500, detail=f"Error al insertar el rol en la BBDD: {str(e)}")


def update_rol(id: int, request: RolUpdate, db: Session):
    rol = get_rol_by_id(id, db)
    rol.nombre = request.nombre
    try:
        db.commit()
        db.refresh(rol)
        return rol
    except Exception as e:
        db.rollback()
        logging.error(f"Error occurred: {str(e)}")
        raise HTTPException(status_code=500, detail=f"Error al modificar el rol en la base de datos")


def delete_rol(id: int, db: Session):
    rol = get_rol_by_id(id, db)
    db.delete(rol)
    try:
        db.commit()
        db.refresh(rol)
    except Exception as e:
        db.rollback()
        logging.error(f"Error occurred: {str(e)}")
        raise HTTPException(status_code=500, detail=f"Error al borrar el rol de la base de datos: {str(e)}")