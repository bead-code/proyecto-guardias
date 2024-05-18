from fastapi import HTTPException

from db.database import Session
from db.models import Aula
from db.schemas import AulaDb


def create_aula(request: AulaDb, db: Session):
    aula = db.query(Aula).filter(Aula.codigo == request.codigo).first()
    if aula:
        raise HTTPException(status_code=400, detail='El aula ya existe en la base de datos')
    new_aula = Aula(
        codigo=request.codigo,
        nombre=request.nombre
    )
    db.add(new_aula)
    try:
        db.commit()
        db.refresh(new_aula)
    except Exception as e:
        db.rollback()
        raise HTTPException(status_code=500, detail=f"Error al insertar el aula en la BBDD: {str(e)}")

def get_aula_by_codigo(codigo:str, db: Session):
    return db.query(Aula).filter(Aula.codigo == codigo).first()

def update_aula():
    pass

def delete_aula(codigo:str, db: Session):
    aula = db.query(Aula).filter(Aula.codigo == codigo).delete()
    if not aula:
        raise HTTPException(status_code=404, detail='El aula no existe en la base de datos')
    db.delete(aula)
    try:
        db.commit()
        db.refresh(aula)
    except Exception as e:
        raise HTTPException(status_code=500, detail=f"Error al borrar el aula de la BBDD: {str(e)}")

