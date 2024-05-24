from db.database import Session
from db.models import Actividad
from generador_horarios.conversor_xml_to_df import parse_xml_to_dataframes
import pandas as pd
import logging

dataframes = parse_xml_to_dataframes()

df_asignaturas = dataframes.get('MATERIAS', pd.DataFrame())
df_actividades = dataframes.get('ACTIVIDADES', pd.DataFrame())
df_asignaturas.rename(columns={"X_MATERIAOMG": "ID_ACTIVIDAD"}, inplace=True)
df_asignaturas.rename(columns={"D_MATERIAC": "NOMBRE_ACTIVIDAD"}, inplace=True)
df_actividades.rename(columns={"X_ACTIVIDAD": "ID_ACTIVIDAD"}, inplace=True)
df_actividades.rename(columns={"D_ACTIVIDAD": "NOMBRE_ACTIVIDAD"}, inplace=True)
df_actividades_def = pd.concat([df_asignaturas, df_actividades], ignore_index=True)
df_actividades_def = df_actividades_def[["ID_ACTIVIDAD", "NOMBRE_ACTIVIDAD"]]


def load_actividades_from_xml():
    db = Session()
    for index, actividad in df_actividades_def.iterrows():
        new_actividad = Actividad(
                id_actividad=actividad["ID_ACTIVIDAD"],
                nombre= actividad['NOMBRE_ACTIVIDAD']
        )
        db.add(new_actividad)
        try:
            logging.info("Insertando las actividades en la base de datos...")
            db.commit()
            db.refresh(new_actividad)
        except Exception as e:
            db.rollback()
            logging.error(f"Error occurred: {str(e)}")