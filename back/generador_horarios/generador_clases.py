import logging

import pandas as pd

from db.database import Session
from db.models import Clase


def load_clases_from_xml(dataframes: pd.DataFrame):
    df_clases = dataframes.get('UNIDADES', pd.DataFrame())
    df_clases.drop_duplicates(subset='X_UNIDAD', keep='first', inplace=True)
    db = Session()
    new_curso = Clase(
        id_clase=9999,
        nombre="No aplica"
    )
    db.add(new_curso)
    clases = []
    for index, curso in df_clases.iterrows():
        new_curso = Clase(
            id_clase=curso['X_UNIDAD'],
            nombre=curso['T_NOMBRE'],
        )

        clases.append(new_curso)
    db.add_all(clases)
    try:
        db.commit()
        logging.info(f"Clases insertados -> {len(clases)}")
    except Exception as e:
        db.rollback()
        logging.error(f"Error occurred: {str(e)}")