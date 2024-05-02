from fastapi import HTTPException
from sqlalchemy.orm import Session
from models.profesor import DbProfesor



def get_profesor(db: Session, nick: str):
    profesor = db.query(DbProfesor).filter(DbProfesor.nick == nick).first()
    if not profesor:
        raise HTTPException(status_code=404, detail="Profesor no encontrado")
    return profesor