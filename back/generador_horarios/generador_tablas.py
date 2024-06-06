from io import BytesIO

import pandas as pd
from anyio.streams import file
from sqlalchemy import insert
from sqlalchemy.exc import SQLAlchemyError

from db.database import Session, truncate_all_tables
from generador_horarios.conversor_xml_to_df import load_tables_from_path, load_tables_from_file, \
    load_calendario_from_file
from generador_horarios.generador_actividades import load_actividades_from_xml
from generador_horarios.generador_aulas import load_aulas_from_xml
from generador_horarios.generador_calendario import load_calendario
from generador_horarios.generador_clases import load_clases_from_xml
from generador_horarios.generador_cursos import load_cursos_from_xml
from generador_horarios.generador_profesores import load_profesores_from_xml
from generador_horarios.generador_roles import generar_roles
from generador_horarios.generador_tramos_horarios import load_tramos_horarios_from_xml


def generate_tables_from_path():
    generar_roles()
    load_profesores_from_xml(load_tables_from_path())
    load_aulas_from_xml(load_tables_from_path())
    load_cursos_from_xml(load_tables_from_path())
    load_actividades_from_xml(load_tables_from_path())
    load_tramos_horarios_from_xml(load_tables_from_path())
    load_clases_from_xml(load_tables_from_path())


def generate_tables_from_files(tablas: BytesIO, calendario: BytesIO):
    tablas_df = load_tables_from_file(tablas)
    calendario_df = load_calendario_from_file(calendario)
    truncate_all_tables()
    generar_roles()
    load_profesores_from_xml(tablas_df)
    load_aulas_from_xml(tablas_df)
    load_cursos_from_xml(tablas_df)
    load_actividades_from_xml(tablas_df)
    load_tramos_horarios_from_xml(tablas_df)
    load_clases_from_xml(tablas_df)
    load_calendario(calendario_df)