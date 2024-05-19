from db.database import Session
from db.models import Aula, Curso
from generador_horarios.conversor_xml_to_df import parse_xml_to_dataframes
import pandas as pd
import logging

dataframes = parse_xml_to_dataframes()

df_cursos = dataframes.get('CURSOS_DEL_CENTRO', pd.DataFrame())

def load_cursos_from_xml():
    db = Session()
    for index, curso in df_cursos.iterrows():
        new_curso = Curso(
            codigo=  curso['D_OFERTAMATRIG'],
        )
        db.add(new_curso)
        try:
            logging.info("Insertando los profesores en la base de datos...")
            db.commit()
            db.refresh(new_curso)
        except Exception as e:
            db.rollback()
            logging.error(f"Error occurred: {str(e)}")