from io import BytesIO

import pandas as pd
from anyio.streams import file
from sqlalchemy import insert
from sqlalchemy.exc import SQLAlchemyError

from db.database import Session, truncate_all_tables
from generador_calendario.conversor_xml_to_df import load_tables, load_calendario
from generador_calendario.generador_actividades import load_actividades_from_xml
from generador_calendario.generador_aulas import load_aulas_from_xml
from generador_calendario.generador_calendario import generate_calendario
from generador_calendario.generador_clases import load_clases_from_xml
from generador_calendario.generador_cursos import load_cursos_from_xml
from generador_calendario.generador_profesores import load_profesores_from_xml
from generador_calendario.generador_roles import generar_roles
from generador_calendario.generador_tramos_horarios import load_tramos_horarios_from_xml


def generate_tables():
    generar_roles()
    load_profesores_from_xml(load_tables())
    load_aulas_from_xml(load_tables())
    load_cursos_from_xml(load_tables())
    load_actividades_from_xml(load_tables())
    load_tramos_horarios_from_xml(load_tables())
    load_clases_from_xml(load_tables())


def generate_tables_from_files(tablas: BytesIO, calendario: BytesIO):
    tablas_df = load_tables(tablas)
    calendario_df = load_calendario(calendario)
    truncate_all_tables()
    generar_roles()
    load_profesores_from_xml(tablas_df)
    load_aulas_from_xml(tablas_df)
    load_cursos_from_xml(tablas_df)
    load_actividades_from_xml(tablas_df)
    load_tramos_horarios_from_xml(tablas_df)
    load_clases_from_xml(tablas_df)
    generate_calendario(calendario_df)