from typing import Dict
import pandas as pd
from db.database import Session
from db.models import Curso
from utils.logger import logger


def generate_cursos_from_dataframe(dataframes: Dict[str, pd.DataFrame]):
    """
    Carga cursos desde un DataFrame de pandas y los inserta en la base de datos.

    :param dataframes: El DataFrame de pandas que contiene los datos de los cursos.
    :type dataframes: pd.DataFrame

    La función realiza los siguientes pasos:
    1. Obtiene el DataFrame `CURSOS_DEL_CENTRO` de los datos proporcionados.
    2. Crea un curso predeterminado "No aplica".
    3. Itera sobre cada fila del DataFrame para crear objetos `Curso`.
    4. Inserta todos los objetos `Curso` en la base de datos.
    5. Maneja cualquier excepción que ocurra durante la inserción de datos.

    Ejemplo de uso:

    .. code-block:: python

        dataframes = pd.read_excel('path_to_excel_file.xlsx', sheet_name=None)
        load_cursos_from_xml(dataframes)
    """
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
        logger.info(f"Cursos insertados -> {len(cursos)}")
    except Exception as e:
        db.rollback()
        logger.error(f"Error occurred: {str(e)}")
