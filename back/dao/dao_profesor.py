from fastapi import HTTPException
from sqlalchemy.orm import Session
from db.models import Profesor, Rol
from db.schemas import ProfesorDb
from security.hash import Hash
import logging


def create_profesor(request: ProfesorDb, db: Session,):

    rol = db.query(Rol).filter(Rol.codigo == request.rol_codigo).first()
    if not rol:
        raise HTTPException(status_code=404, detail="Rol incorrecto")

    profesor = db.query(Profesor).filter(Profesor.codigo == request.codigo).first()
    if profesor:
        raise HTTPException(status_code=409, detail="El profesor ya existe en la BBDD")


    new_profesor = Profesor(
        codigo=request.codigo,
        password=Hash.argon2(request.password),
        nick=request.nick,
        color=request.color,
        rol_codigo=request.rol_codigo
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


def get_profesor_by_codigo(codigo: str, db: Session):
    profesor = db.query(Profesor).filter(Profesor.codigo == codigo).first()
    if not profesor:
        raise HTTPException(status_code=404, detail="Profesor no encontrado")
    return profesor

def get_profesor_by_nick(nick: str, db: Session):
    profesor = db.query(Profesor).filter(Profesor.nick == nick).first()
    if not profesor:
        raise HTTPException(status_code=404, detail="Profesor no encontrado")
    return profesor

def update_profesor():
    pass

def delete_profesor(codigo: str, db: Session):
    profesor = db.query(Profesor).filter(Profesor.codigo == codigo).first()
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


