from io import BytesIO

import pandas as pd
from anyio.streams import file
from sqlalchemy import insert
from sqlalchemy.exc import SQLAlchemyError

from db.database import Session, truncate_all_tables
from generador_horarios.conversor_xml_to_df import load_tables, load_calendario
from generador_horarios.generador_actividades import load_actividades_from_xml
from generador_horarios.generador_aulas import load_aulas_from_xml
from generador_horarios.generador_calendario import generate_calendario
from generador_horarios.generador_clases import load_clases_from_xml
from generador_horarios.generador_cursos import load_cursos_from_xml
from generador_horarios.generador_profesores import load_profesores_from_xml
from generador_horarios.generador_roles import generar_roles
from generador_horarios.generador_tramos_horarios import load_tramos_horarios_from_xml


def generate_tables():
    """
    Genera todas las tablas necesarias para la base de datos a partir de datos XML predeterminados.

    Este método llama a funciones específicas para generar roles, profesores, aulas, cursos, actividades,
    tramos horarios y clases a partir de datos XML predeterminados.
    """
    generar_roles()
    load_profesores_from_xml(load_tables())
    load_aulas_from_xml(load_tables())
    load_cursos_from_xml(load_tables())
    load_actividades_from_xml(load_tables())
    load_tramos_horarios_from_xml(load_tables())
    load_clases_from_xml(load_tables())


def generate_tables_from_files(tablas: BytesIO, calendario: BytesIO):
    """
    Genera todas las tablas necesarias para la base de datos a partir de archivos XML proporcionados.

    Este método carga los datos de los archivos XML proporcionados y llama a funciones específicas
    para generar roles, profesores, aulas, cursos, actividades, tramos horarios y clases,
    y luego genera el calendario a partir de los datos proporcionados.

    :param tablas: Un archivo de bytes que contiene los datos de las tablas en formato XML.
    :type tablas: BytesIO
    :param calendario: Un archivo de bytes que contiene los datos del calendario en formato XML.
    :type calendario: BytesIO
    """
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