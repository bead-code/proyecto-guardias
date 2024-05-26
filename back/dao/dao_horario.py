from fastapi import HTTPException
from starlette import status

from db.database import Session
from db.models import Profesor, Asignatura, Aula, Horario
from db.schemas import HorarioDb


def create_horario(horario: HorarioDb, db: Session,):
    db_profesor = db.query(Profesor).filter(Profesor.codigo == horario.codigo_profesor).first()
    if not db_profesor:
        raise HTTPException(status_code=status.HTTP_404_NOT_FOUND, detail="Profesor no registrado en la base de datos")
    if horario.codigo_profesor_sustituto:
        db_profesor_sustituto = db.query(Profesor).filter(Profesor.codigo == horario.codigo_profesor_sustituto).first()
        if not db_profesor_sustituto:
            raise HTTPException(status_code=status.HTTP_404_NOT_FOUND, detail="Profesor registrado no encontrado en la base de datos")

    db_asignatura = db.query(Asignatura).filter(Asignatura.codigo == horario.codigo_asignatura).first()
    if not db_asignatura:
        raise HTTPException(status_code=status.HTTP_404_NOT_FOUND, detail="Asignatura no registrada en la base de datos")

    db_aula = db.query(Aula).filter(Aula.codigo == horario.codigo_aula).first()
    if not db_aula:
        raise HTTPException(status_code=status.HTTP_404_NOT_FOUND, detail="Aula no registrada en la base de datos")

    db_horario = Horario(
        codigo_profesor=horario.codigo_profesor,
        codigo_profesor_sustituto=horario.codigo_profesor_sustituto,
        codigo_asignatura=horario.codigo_asignatura,
        codigo_aula=horario.codigo_aula,
        fecha=horario.fecha,
        dia_semana=horario.dia_semana,
        hora=horario.hora,
        ausencia=horario.ausencia
    )

    db.add(db_horario)
    try:
        db.commit()
        db.refresh(db_horario)
    except Exception as e:
        raise HTTPException(status_code=500, detail=f"Error al insertar al horario en la base de datos: {str(e)}")
    return db_horario


def get_horario_profesor(profesor_codidgo: str, db: Session):
    horario = db.query(Horario).filter(Profesor.codigo == profesor_codidgo)
    if not horario:
        raise HTTPException(status_code=status.HTTP_404_NOT_FOUND, detail="Profesor no registrado en la base de datos")
    return horario