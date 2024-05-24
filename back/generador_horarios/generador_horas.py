import pandas as pd
from generador_horarios.conversor_xml_to_df import parse_xml_to_dataframes
from db.database import Session
from db.models import Hora
import logging


dataframes = parse_xml_to_dataframes()
df_horas = dataframes.get('TRAMOS_HORARIOS', pd.DataFrame())

def minutos_a_hora(minutos):
    horas = minutos // 60
    minutos_restantes = minutos % 60
    return f"{horas:02}:{minutos_restantes:02}"

def load_horas_from_xml():
    db = Session()
    horas=[]
    for index, hora in df_horas.iterrows():
        new_hora = Hora(
            id_hora=hora["ID_HORA"],
            tramo=hora["T_HORCEN"],
            hora_inicio=minutos_a_hora(hora["N_INICIO"]),
            hora_fin=minutos_a_hora(hora["N_FIN"])
        )
        horas.append(new_hora)
    db.add_all(horas)
    try:
        logging.info("Insertando las horas en la base de datos...")
        db.commit()
        db.refresh(horas)
    except Exception as e:
        db.rollback()
        logging.error(f"Error occurred: {str(e)}")