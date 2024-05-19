from db.database import Session
from db.models import Aula, Curso, Asignatura
from generador_horarios.conversor_xml_to_df import parse_xml_to_dataframes
import pandas as pd
import logging

dataframes = parse_xml_to_dataframes()

df_asignaturas = dataframes.get('MATERIAS', pd.DataFrame())

def load_asignaturas_from_xml():
    db = Session()
    for index, asignatura in df_asignaturas.iterrows():
        new_asignatura = Asignatura(
                codigo= asignatura['D_MATERIAC'],
        )
        db.add(new_asignatura)
        try:
            logging.info("Insertando las asignaturas en la base de datos...")
            db.commit()
            db.refresh(new_asignatura)
        except Exception as e:
            db.rollback()
            logging.error(f"Error occurred: {str(e)}")