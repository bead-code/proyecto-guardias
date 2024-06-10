from fastapi import HTTPException
from sqlalchemy.orm import Session
from db.models import Curso
from db.schemas import CursoCreate, CursoUpdate
import logging

def get_curso_by_id(id: int, db: Session):
    """
    Obtiene un curso por su ID.

    :param id: El ID del curso a buscar.
    :type id: int
    :param db: La sesión de la base de datos.
    :type db: Session
    :returns: El curso encontrado.
    :rtype: Curso
    :raises HTTPException: Si el curso no existe en la base de datos.
    """
    curso = db.query(Curso).filter(Curso.id_curso == id).filter(Curso.activo == True).first()
    if not curso:
        raise HTTPException(status_code=404, detail="El curso no existe en la base de datos")
    return curso

def get_curso_by_nombre(nombre: str, db: Session):
    """
    Obtiene un curso por su nombre.

    :param nombre: El nombre del curso a buscar.
    :type nombre: str
    :param db: La sesión de la base de datos.
    :type db: Session
    :returns: El curso encontrado.
    :rtype: Curso
    :raises HTTPException: Si el curso no existe en la base de datos.
    """
    curso = db.query(Curso).filter(Curso.nombre == nombre).filter(Curso.activo == True).first()
    if not curso:
        raise HTTPException(status_code=404, detail="El curso no existe en la base de datos")
    return curso

def get_cursos(db: Session):
    """
    Obtiene todos los cursos activos.

    :param db: La sesión de la base de datos.
    :type db: Session
    :returns: Una lista de todos los cursos activos.
    :rtype: List[Curso]
    :raises HTTPException: Si no existen cursos en la base de datos.
    """
    cursos = db.query(Curso).filter(Curso.activo == True).all()
    if not cursos:
        raise HTTPException(status_code=404, detail="No existen cursos en la base de datos")
    return cursos

def create_curso(request: CursoCreate, db: Session):
    """
    Crea un nuevo curso.

    :param request: Los datos del curso a crear.
    :type request: CursoCreate
    :param db: La sesión de la base de datos.
    :type db: Session
    :returns: El curso creado.
    :rtype: Curso
    :raises HTTPException: Si el curso ya existe o si ocurre un error al insertarlo.
    """
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
    """
    Actualiza un curso existente.

    :param id: El ID del curso a actualizar.
    :type id: int
    :param request: Los nuevos datos del curso.
    :type request: CursoUpdate
    :param db: La sesión de la base de datos.
    :type db: Session
    :returns: El curso actualizado.
    :rtype: Curso
    :raises HTTPException: Si ocurre un error al modificar el curso.
    """
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
    """
    Elimina (desactiva) un curso por su ID.

    :param id: El ID del curso a eliminar.
    :type id: int
    :param db: La sesión de la base de datos.
    :type db: Session
    :raises HTTPException: Si ocurre un error al eliminar el curso.
    """
    curso = get_curso_by_id(id, db)
    curso.activo = False
    try:
        db.commit()
        db.refresh(curso)
    except Exception as e:
        db.rollback()
        raise HTTPException(status_code=500, detail=f"Error al borrar al ciclo de la base de datos: {str(e)}")



