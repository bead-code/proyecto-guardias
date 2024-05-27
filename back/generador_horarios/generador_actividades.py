import logging

import pandas as pd

from db.database import Session
from db.models import Actividad


def load_actividades_from_xml(dataframes: pd.DataFrame):
    df_asignaturas = dataframes.get('MATERIAS', pd.DataFrame())
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
        db.commit()
        logging.info(f"Actividades insertadas -> {len(actividades)}")
    except Exception as e:
        db.rollback()
        logging.error(f"Error occurred: {str(e)}")
