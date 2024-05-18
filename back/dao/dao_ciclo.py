from fastapi import HTTPException
from sqlalchemy.orm import Session
from db.models import Ciclo
from db.schemas import CicloDb


def create_ciclo(request: CicloDb, db: Session):
    ciclo = db.query(Ciclo).filter(Ciclo.codigo == request.codigo).first()
    if ciclo:
        raise HTTPException(status_code=409, detail="El ciclo ya existe en la base de datos")
    new_ciclo = Ciclo(
        codigo=request.codigo,
        nombre=request.nombre
    )
    db.add(new_ciclo)
    try:
        db.commit()
        db.refresh(new_ciclo)
        return new_ciclo
    except Exception as e:
        db.rollback()
        raise HTTPException(status_code=500, detail=f"Error al insertar al ciclo en la base de datos: {str(e)}")



def get_ciclo_by_codigo(codigo: str, db: Session):
    ciclo = db.query(Ciclo).filter(Ciclo.codigo == codigo).first()
    if not ciclo:
        raise HTTPException(status_code=404, detail="Ciclo no encontrado")
    return ciclo

def update_ciclo():
    pass

def delete_ciclo(codigo: str, db: Session):
    ciclo = db.query(Ciclo).filter(Ciclo.codigo == codigo).first()
    if not ciclo:
        raise HTTPException(status_code=404, detail="Ciclo no encontrado")
    db.delete(ciclo)
    try:
        db.commit()
        db.refresh(ciclo)
    except Exception as e:
        db.rollback()
        raise HTTPException(status_code=500, detail=f"Error al borrar al ciclo de la base de datos: {str(e)}")


