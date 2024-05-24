import logging

import pandas as pd

from db.database import Session
from db.models import Aula
from generador_horarios.conversor_xml_to_df import parse_xml_to_dataframes

dataframes = parse_xml_to_dataframes()

df_aulas = dataframes.get('DEPENDENCIAS', pd.DataFrame())

def load_aulas_from_xml():
    db = Session()
    for index, aula in df_aulas.iterrows():
        new_aula = Aula(
            id_aula=aula["X_DEPENDENCIA"],
            nombre=aula['D_DEPENDENCIA']
        )
        db.add(new_aula)
        try:
            logging.info("Insertando las aulas en la base de datos...")
            db.commit()
            db.refresh(new_aula)
        except Exception as e:
            db.rollback()
            logging.error(f"Error occurred: {str(e)}")