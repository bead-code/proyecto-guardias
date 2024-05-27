import logging

from fastapi import HTTPException
from sqlalchemy.orm import Session

from db.models import Profesor, Rol
from db.schemas import ProfesorCreate, ProfesorUpdate


def get_profesor_by_id(id: id, db: Session):
    profesor = db.query(Profesor).filter(Profesor.id_profesor == id).first()
    if not profesor:
        raise HTTPException(status_code=404, detail="El profesor no existe en la base de datos")
    return profesor


def get_profesor_by_username(username: str, db: Session):
    profesor = db.query(Profesor).filter(Profesor.username == username).first()
    if not profesor:
        raise HTTPException(status_code=404, detail="El profesor no existe en la base de datos")
    return profesor


def get_profesores(db: Session):
    profesores = db.query(Profesor).all()
    if not profesores:
        raise HTTPException(status_code=404, detail="No hay profesores registrados en la base de datos")
    return profesores


def create_profesor(request: ProfesorCreate, db: Session, ):
    rol = db.query(Rol).filter(Rol.id == request.rol_id).first()
    if not rol:
        raise HTTPException(status_code=404, detail="Rol incorrecto")
    profesor = db.query(Profesor).filter(Profesor.username == request.username).first()
    if profesor:
        raise HTTPException(status_code=409, detail="El profesor ya existe en la BBDD")
    new_profesor = Profesor(
        username=request.username,
        nombre=request.nombre,
        id_rol=request.id_rol
    )

    db.add(new_profesor)
    try:
        logging.info("Insertando el profesor en la base de datos...")
        db.commit()
        db.refresh(new_profesor)
    except Exception as e:
        db.rollback()
        logging.error(f"Error occurred: {str(e)}")
        raise HTTPException(status_code=500, detail=f"Error al insertar al profesor en la base de datos: {str(e)}")

    return new_profesor

def update_profesor(id: int, request: ProfesorUpdate, db: Session):
    profesor = db.query(Profesor).filter(Profesor.id_profesor == id).first()
    if not profesor:
        raise HTTPException(status_code=404, detail="El profesor no existe en la base de datos")

    for key, value in request.dict(exclude_unset=True).items():
        setattr(profesor, key, value)
    try:
        db.commit()
        db.refresh(profesor)
    except Exception as e:
        db.rollback()
        logging.error(f"Error occurred: {str(e)}")
        raise HTTPException(status_code=500, detail=f"Error el profesor la aula en la base de datos")

def delete_profesor(id: int, db: Session):
    profesor = db.query(Profesor).filter(Profesor.id_profesor == id).first()
    if not profesor:
        raise HTTPException(status_code=404, detail="El profesor no existe en la base de datos")
    db.delete(profesor)
    try:
        db.commit()
        logging.info("Profesor insertado en la base de datos")
    except Exception as e:
        db.rollback()
        logging.error(f"Error occurred: {str(e)}")
        raise HTTPException(status_code=500, detail=f"Error al borrar el profesor de la base de datos: {str(e)}")


