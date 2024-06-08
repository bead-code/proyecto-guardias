import logging

import pandas as pd

from db.database import Session
from db.models import Actividad


def load_actividades_from_xml(dataframes: pd.DataFrame):
    df_asignaturas = dataframes.get('MATERIAS', pd.DataFrame())
    df_actividades_complementarias = dataframes.get("ACTIVIDADES", pd.DataFrame())
    df_asignaturas.rename(columns={"X_MATERIAOMG": "id_actividad", "D_MATERIAC": "nombre"}, inplace=True)
    df_actividades_complementarias.rename(columns={"X_ACTIVIDAD": "id_actividad", "D_ACTIVIDAD": "nombre"}, inplace=True)
    df_asignaturas = pd.concat([df_asignaturas, df_actividades_complementarias], ignore_index=True)
    db = Session()
    actividades = []
    for index, actividad in df_asignaturas.iterrows():
        new_actividad = Actividad(
            id_actividad=actividad['id_actividad'],
            nombre=actividad['nombre']
        )
        actividades.append(new_actividad)
    db.add_all(actividades)
    try:
        db.commit()
        logging.info(f"Actividades insertadas -> {len(actividades)}")
    except Exception as e:
        db.rollback()
        logging.error(f"Error occurred: {str(e)}")