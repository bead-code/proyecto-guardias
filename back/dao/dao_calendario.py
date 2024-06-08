from datetime import datetime

from fastapi import HTTPException
from starlette import status

from db.database import Session
from db.models import Profesor, Actividad, Aula, Curso, Clase, Calendario, TramoHorario
from db.schemas import CalendarioCreate


def get_calendario_by_id(id: int, db: Session):
    calendario = db.query(Calendario).filter(Calendario.id == id).filter(Calendario.activo == True).first()
    if not calendario:
        raise HTTPException(status_code=status.HTTP_404_NOT_FOUND, detail='El registro no existe en el calendario actual')
    return calendario

def create_calendario(calendario: CalendarioCreate, db: Session,):
    db_profesor = db.query(Profesor).filter(Profesor.id_profesor == calendario.id_profesor).filter(Calendario.activo == True).first()
    if not db_profesor:
        raise HTTPException(status_code=status.HTTP_404_NOT_FOUND, detail="Profesor no registrado en la base de datos")
    if calendario.codigo_profesor_sustituto:
        db_profesor_sustituto = db.query(Profesor).filter(Profesor.id_profesor == calendario.id_profesor_sustituto).first()
        if not db_profesor_sustituto:
            raise HTTPException(status_code=status.HTTP_404_NOT_FOUND, detail="Profesor registrado no encontrado en la base de datos")

    db_actividad = db.query(Actividad).filter(Actividad.id_actividad == calendario.id_actividad).first()
    if not db_actividad:
        raise HTTPException(status_code=status.HTTP_404_NOT_FOUND, detail="Actividad no registrada en la base de datos")
    db_curso = db.query(Curso).filter(Curso.id_curso == calendario.id_curso).first()
    if not db_curso:
        raise HTTPException(status_code=status.HTTP_404_NOT_FOUND, detail="Curso no registrado en la base de datos")
    db_clase = db.query(Clase).filter(Clase.id_clase == calendario.id_clase).first()
    if not db_clase:
        raise HTTPException(status_code=status.HTTP_404_NOT_FOUND, detail="Clase no registrado en la base de datos")
    db_aula = db.query(Aula).filter(Aula.codigo == calendario.codigo_aula).first()
    if not db_aula:
        raise HTTPException(status_code=status.HTTP_404_NOT_FOUND, detail="Aula no registrada en la base de datos")

    db_calendario = Calendario(
        id_profesor=calendario.id_profesor,
        id_profesor_sustituto=calendario.id_profesor_sustituto,
        id_actividad=calendario.id_asignatura,
        id_clase=calendario.id_clase,
        id_aula=calendario.id_aula,
        fecha=calendario.fecha,
        dia=calendario.dia_semana,
        id_tramo_horario=calendario.id_tramo_horario,
        ausencia=calendario.ausencia
    )
    db.add(db_calendario)
    try:
        db.commit()
        db.refresh(db_calendario)
    except Exception as e:
        raise HTTPException(status_code=500, detail=f"Error al insertar al calendario en la base de datos: {str(e)}")
    return db_calendario


def get_calendario_by_id_profesor(id_profesor: int, db: Session):
    calendario = db.query(Calendario).filter(Profesor.id_profesor == id_profesor).filter(Calendario.activo == True).all()
    if not calendario:
        raise HTTPException(status_code=status.HTTP_404_NOT_FOUND, detail="Profesor no registrado en la base de datos")
    return calendario


def get_actual_calendario_by_id_profesor(id_profesor, db):
    current_day = datetime.now().weekday() + 1
    current_time = datetime.now().time()
    calendario = (db.query(Calendario)
             .filter(Calendario.id_profesor == id_profesor)
             .filter(Calendario.activo == True)
             .filter(Calendario.dia == current_day)
             .join(TramoHorario, Calendario.id_tramo_horario == TramoHorario.id_tramo_horario
                   .filter(TramoHorario.hora_inicio >= current_time)
                   .filter(TramoHorario.hora_fin <= current_time))).all()

    if not calendario:
        raise HTTPException(status_code=status.HTTP_404_NOT_FOUND, detail="No hay clases para el profesor en la hora actual")
    return calendario
