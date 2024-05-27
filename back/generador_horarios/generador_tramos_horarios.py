from datetime import time

import pandas as pd
from generador_horarios.conversor_xml_to_df import parse_xml_to_dataframes
from db.database import Session
from db.models import TramoHorario
import logging


dataframes = parse_xml_to_dataframes()
df_tramo = dataframes.get('TRAMOS_HORARIOS', pd.DataFrame())

def minutos_a_hora(minutos):
    minutos = int(minutos)
    horas = minutos // 60
    minutos_restantes = minutos % 60
    return time(horas, minutos_restantes)

def load_tramos_horarios_from_xml():
    db = Session()
    tramos=[]
    new_tramo = TramoHorario(
        id_tramo_horario=9999,
        nombre="No aplica"
    )
    db.add(new_tramo)
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
        logging.info("Insertando las horas en la base de datos...")
        db.commit()
        db.refresh(tramos)
    except Exception as e:
        db.rollback()
        logging.error(f"Error occurred: {str(e)}")