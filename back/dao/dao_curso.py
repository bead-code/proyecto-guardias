from fastapi import HTTPException
from sqlalchemy.orm import Session
from db.models import Curso
from db.schemas import CursoCreate, CursoUpdate
import logging


def get_curso_by_id(id: int, db: Session):
    curso = db.query(Curso).filter(Curso.id_curso == id).filter(Curso.activo == True).first()
    if not curso:
        raise HTTPException(status_code=404, detail="El curso no existe en la base de datos")
    return curso

def get_curso_by_nombre(nombre: str, db: Session):
    curso = db.query(Curso).filter(Curso.nombre == nombre).filter(Curso.activo == True).first()
    if not curso:
        raise HTTPException(status_code=404, detail="El curso no existe en la base de datos")
    return curso

def get_cursos(db: Session):
    cursos = db.query(Curso).filter(Curso.activo == True).all()
    if not cursos:
        raise HTTPException(status_code=404, detail="No existen cursos en la base de datos")
    return cursos

def create_curso(request: CursoCreate, db: Session):
    curso = db.query(Curso).filter(Curso.nombre == request.nombre).first()
    if curso:
        raise HTTPException(status_code=409, detail="El curso ya existe en la base de datos")
    new_curso = Curso(
        nombre=request.nombre
    )
    db.add(new_curso)
    try:
        db.commit()
        db.refresh(new_curso)
        return new_curso
    except Exception as e:
        db.rollback()
        logging.error(f"Error occurred: {str(e)}")
        raise HTTPException(status_code=500, detail=f"Error al insertar al ciclo en la base de datos: {str(e)}")

def update_curso(id: int, request: CursoUpdate, db: Session):
    curso = get_curso_by_id(id, db)
    curso.nombre = request.nombre
    try:
        db.commit()
        db.refresh(curso)
        return curso
    except Exception as e:
        db.rollback()
        logging.error(f"Error occurred: {str(e)}")
        raise HTTPException(status_code=500, detail=f"Error al modificar la actividad en la base de datos")


def delete_curso(id: int, db: Session):
    curso = get_curso_by_id(id, db)
    curso.activo = False
    try:
        db.commit()
        db.refresh(curso)
    except Exception as e:
        db.rollback()
        raise HTTPException(status_code=500, detail=f"Error al borrar al ciclo de la base de datos: {str(e)}")


