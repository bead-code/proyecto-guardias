from fastapi import HTTPException
from starlette import status

from db.database import Session
from db.models import Calendario, Profesor

id_actividad_guardia = 65


def get_grupo_guardia(id_tramo: int, dia: int, db: Session):
    profesor = (
        db.query(Profesor)
        .join(Calendario, Calendario.id_profesor == Profesor.id_profesor)
        .filter(Calendario.id_tramo_horario == id_tramo)
        .filter(Calendario.dia == dia)
        .filter(Calendario.activo == True)
        .filter(Calendario.id_actividad == id_actividad_guardia)
        .distinct()
        .all()
    )
    if not profesor:
        raise HTTPException(
            status_code=status.HTTP_404_NOT_FOUND,
            detail="No hay guardias asignadas a este grupo de guardia"
        )
    return profesor


def get_grupos_guardia(db: Session):
    resultados = (
        db.query(Calendario.dia, Calendario.id_tramo_horario, Profesor)
        .join(Profesor, Calendario.id_profesor == Profesor.id_profesor)
        .filter(Calendario.activo == True)
        .filter(Calendario.id_actividad == id_actividad_guardia)
        .all()
    )

    grupos_guardia = {}

    for dia, id_tramo_horario, profesor in resultados:
        if (dia, id_tramo_horario) not in grupos_guardia:
            grupos_guardia[(dia, id_tramo_horario)] = []
        grupos_guardia[(dia, id_tramo_horario)].append(profesor)

    return grupos_guardia