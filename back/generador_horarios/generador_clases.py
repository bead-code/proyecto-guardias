import logging

import pandas as pd

from db.database import Session
from db.models import Clase
from generador_horarios.conversor_xml_to_df import parse_xml_to_dataframes

dataframes = parse_xml_to_dataframes()

df_clases = dataframes.get('UNIDADES', pd.DataFrame())

def load_clases_from_xml():
    db = Session()
    new_clase = Clase(
        id_clase=9999,
        nombre="No aplica"
    )
    db.add(new_clase)
    for index, curso in df_clases.iterrows():
        new_curso = Clase(
            id_clase=curso['X_UNIDAD'],
            nombre=curso['T_NOMBRE'],
        )

        db.add(new_curso)
        try:
            logging.info("Insertando los profesores en la base de datos...")
            db.commit()
            db.refresh(new_curso)
        except Exception as e:
            db.rollback()
            logging.error(f"Error occurred: {str(e)}")