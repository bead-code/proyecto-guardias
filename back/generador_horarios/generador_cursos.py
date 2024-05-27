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
    cursos = []
    for index, curso in df_cursos.iterrows():
        new_curso = Curso(
            id_curso=curso['X_OFERTAMATRIG'],
            nombre=curso['D_OFERTAMATRIG'],
        )
        cursos.append(new_curso)
    db.add_all(cursos)
    try:
        db.commit()
        logging.info(f"Cursos insertados -> {len(cursos)}")
    except Exception as e:
        db.rollback()
        logging.error(f"Error occurred: {str(e)}")