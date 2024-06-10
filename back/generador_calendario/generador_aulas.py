from typing import Dict
import pandas as pd
from db.database import Session
from db.models import Aula
from utils.logger import logger


def generate_aulas_from_dataframe(dataframes: Dict[str, pd.DataFrame]):
    """
    Carga aulas desde un DataFrame de pandas y las inserta en la base de datos.

    :param dataframes: El DataFrame de pandas que contiene los datos de las aulas.
    :type dataframes: pd.DataFrame

    La función realiza los siguientes pasos:
    1. Obtiene el DataFrame `DEPENDENCIAS` de los datos proporcionados.
    2. Crea un aula predeterminada "No aplica".
    3. Itera sobre cada fila del DataFrame para crear objetos `Aula`.
    4. Inserta todos los objetos `Aula` en la base de datos.
    5. Maneja cualquier excepción que ocurra durante la inserción de datos.

    Ejemplo de uso:

    .. code-block:: python

        dataframes = pd.read_excel('path_to_excel_file.xlsx', sheet_name=None)
        load_aulas_from_xml(dataframes)
    """
    df_aulas = dataframes.get('DEPENDENCIAS', pd.DataFrame())
    db = Session()
    aulas = []

    new_aula = Aula(
        id_aula=9999,
        nombre="No aplica"
    )
    aulas.append(new_aula)

    for index, aula in df_aulas.iterrows():
        new_aula = Aula(
            id_aula=aula["X_DEPENDENCIA"],
            nombre=aula['D_DEPENDENCIA']
        )
        aulas.append(new_aula)

    db.add_all(aulas)

    try:
        db.commit()
        logger.info(f"Aulas insertadas -> {len(aulas)}")
    except Exception as e:
        db.rollback()
        logger.error(f"Error occurred: {str(e)}")
