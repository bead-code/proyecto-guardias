"""
Módulo para generar todas las tablas necesarias para la base de datos a partir de datos XML.

Funciones
---------

* **generate_tables_from_path**: Genera todas las tablas necesarias a partir de datos XML en la ruta del proyecto.
* **generate_tables_from_files**: Genera todas las tablas necesarias a partir de archivos XML proporcionados.

"""

from io import BytesIO
from db.database import truncate_all_tables
from generador_calendario.conversor_xml_to_df import load_tables, load_calendario
from generador_calendario.generador_actividades import generate_actividades_from_dataframe
from generador_calendario.generador_aulas import generate_aulas_from_dataframe
from generador_calendario.generador_calendario import generate_calendario_from_dataframe
from generador_calendario.generador_clases import generate_clases_from_dataframe
from generador_calendario.generador_cursos import generate_cursos_from_dataframe
from generador_calendario.generador_profesores import generate_profesores_from_dataframe, generate_base_users
from generador_calendario.generador_roles import generate_roles
from generador_calendario.generador_tramos_horarios import generate_tramos_horarios_from_dataframe


def generate_tables_from_path():
    """
    Genera todas las tablas necesarias para la base de datos a partir de datos XML en la ruta del proyecto.

    Este método llama a funciones específicas para generar roles, profesores, aulas, cursos, actividades,
    tramos horarios y clases a partir de datos XML predeterminados.

    Ejemplo de uso:

    .. code-block:: python

        generate_tables_from_path()
    """
    # tablas_df = load_tables()
    # calendario_df = load_calendario()
    truncate_all_tables()
    generate_roles()
    generate_base_users()
    # generate_profesores_from_dataframe(tablas_df)
    # generate_aulas_from_dataframe(tablas_df)
    # generate_cursos_from_dataframe(tablas_df)
    # generate_actividades_from_dataframe(tablas_df)
    # generate_tramos_horarios_from_dataframe(tablas_df)
    # generate_clases_from_dataframe(tablas_df)
    # generate_calendario_from_dataframe(calendario_df)


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

    Ejemplo de uso:

    .. code-block:: python

        with open('path_to_tablas.xml', 'rb') as tablas_file, open('path_to_calendario.xml', 'rb') as calendario_file:
            generate_tables_from_files(BytesIO(tablas_file.read()), BytesIO(calendario_file.read()))
    """
    tablas_df = load_tables(tablas)
    calendario_df = load_calendario(calendario)
    truncate_all_tables()
    generate_roles()
    generate_profesores_from_dataframe(tablas_df)
    generate_aulas_from_dataframe(tablas_df)
    generate_cursos_from_dataframe(tablas_df)
    generate_actividades_from_dataframe(tablas_df)
    generate_tramos_horarios_from_dataframe(tablas_df)
    generate_clases_from_dataframe(tablas_df)
    generate_calendario_from_dataframe(calendario_df)

