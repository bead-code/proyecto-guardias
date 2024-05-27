import logging
from datetime import time
import pandas as pd
from db.database import Session
from db.models import TramoHorario


def minutos_a_hora(minutos):
    minutos = int(minutos)
    horas = minutos // 60
    minutos_restantes = minutos % 60
    return time(horas, minutos_restantes)


def load_tramos_horarios_from_xml(dataframes: pd.DataFrame):
    df_tramo = dataframes.get('TRAMOS_HORARIOS', pd.DataFrame())
    db = Session()
    tramos=[]
    new_tramo = TramoHorario(
        id_tramo_horario=9999,
        nombre="No aplica"
    )
    tramos.append(new_tramo)
    for index, tramo in df_tramo.iterrows():
        new_hora = TramoHorario(
            id_tramo_horario=tramo["X_TRAMO"],
            nombre=tramo["T_HORCEN"],
            hora_inicio=minutos_a_hora(tramo["N_INICIO"]),
            hora_fin=minutos_a_hora(tramo["N_FIN"])
        )
        tramos.append(new_hora)
    db.add_all(tramos)
    try:
        db.commit()
        logging.info(f"Tramos horarios insertados -> {len(tramos)}")
    except Exception as e:
        db.rollback()
        logging.error(f"Error occurred: {str(e)}")