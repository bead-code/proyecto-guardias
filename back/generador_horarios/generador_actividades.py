import logging

import pandas as pd

from db.database import Session
from db.models import Actividad
from generador_horarios.conversor_xml_to_df import parse_xml_to_dataframes

dataframes = parse_xml_to_dataframes()

df_asignaturas = dataframes.get('MATERIAS', pd.DataFrame())

def load_actividades_from_xml():
    db = Session()
    actividades = []
    new_actividad = Actividad(
        id_actividad = 9999,
        nombre = "actividad complementaria"
    )
    db.add(new_actividad)
    for index, actividad in df_asignaturas.iterrows():
        new_actividad = Actividad(
            id_actividad=actividad['X_MATERIAOMG'],
            nombre=actividad['D_MATERIAC']
        )
        actividades.append(new_actividad)
    db.add_all(actividades)
    try:
        logging.info("Insertando las actividades en la base de datos...")
        db.commit()
    except Exception as e:
        db.rollback()
        logging.error(f"Error occurred: {str(e)}")
