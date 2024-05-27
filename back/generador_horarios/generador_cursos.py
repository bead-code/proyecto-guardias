import logging

import pandas as pd
from db.database import Session
from db.models import Curso


def load_cursos_from_xml(dataframes: pd.DataFrame):
    df_cursos = dataframes.get('CURSOS_DEL_CENTRO', pd.DataFrame())
    db = Session()
    new_curso = Curso(
        id_curso=9999,
        nombre="No aplica"
    )
    db.add(new_curso)
    for index, curso in df_cursos.iterrows():
        new_curso = Curso(
            id_curso=curso['X_OFERTAMATRIG'],
            nombre=curso['D_OFERTAMATRIG'],
        )
        db.add(new_curso)
        try:
            logging.info("Insertando los cursos en la base de datos...")
            db.commit()
            db.refresh(new_curso)
        except Exception as e:
            db.rollback()
            logging.error(f"Error occurred: {str(e)}")