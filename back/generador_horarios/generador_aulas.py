import logging

import pandas as pd

from db.database import Session
from db.models import Aula


def load_aulas_from_xml(dataframes = pd.DataFrame()):
    df_aulas = dataframes.get('DEPENDENCIAS', pd.DataFrame())
    db = Session()
    new_aula = Aula(
        id_aula=9999,
        nombre="No aplica"
    )
    db.add(new_aula)
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