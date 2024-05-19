from db.database import Session
from db.models import Aula
from generador_horarios.conversor_xml_to_df import parse_xml_to_dataframes
import pandas as pd
import logging

dataframes = parse_xml_to_dataframes()

df_aulas = dataframes.get('DEPENDENCIAS', pd.DataFrame())

def cargar_aula_from_xml():
    db = Session()
    for index, aula in df_aulas.iterrows():
        new_aula = Aula(
            codigo=aula['D_DEPENDENCIA'],
        )
        db.add(new_aula)
        try:
            logging.info("Insertando el profesor en la base de datos...")
            db.commit()
            db.refresh(new_aula)
        except Exception as e:
            db.rollback()
            logging.error(f"Error occurred: {str(e)}")