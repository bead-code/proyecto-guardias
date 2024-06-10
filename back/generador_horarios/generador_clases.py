import logging
import pandas as pd
from db.database import Session
from db.models import Clase


def load_clases_from_xml(dataframes: pd.DataFrame):
    """
    Carga clases desde un DataFrame de pandas y las inserta en la base de datos.

    :param dataframes: El DataFrame de pandas que contiene los datos de las clases.
    :type dataframes: pd.DataFrame

    La función realiza los siguientes pasos:
    1. Obtiene el DataFrame `UNIDADES` de los datos proporcionados.
    2. Elimina las filas duplicadas basándose en la columna `X_UNIDAD`.
    3. Crea una clase predeterminada "No aplica".
    4. Itera sobre cada fila del DataFrame para crear objetos `Clase`.
    5. Inserta todos los objetos `Clase` en la base de datos.
    6. Maneja cualquier excepción que ocurra durante la inserción de datos.

    Ejemplo de uso:

    .. code-block:: python

        dataframes = pd.read_excel('path_to_excel_file.xlsx', sheet_name=None)
        load_clases_from_xml(dataframes)
    """
    df_clases = dataframes.get('UNIDADES', pd.DataFrame())
    df_clases.drop_duplicates(subset='X_UNIDAD', keep='first', inplace=True)
    db = Session()

    new_curso = Clase(
        id_clase=9999,
        nombre="No aplica"
    )
    db.add(new_curso)

    clases = []
    for index, curso in df_clases.iterrows():
        new_curso = Clase(
            id_clase=curso['X_UNIDAD'],
            nombre=curso['T_NOMBRE'],
        )
        clases.append(new_curso)

    db.add_all(clases)

    try:
        db.commit()
        logging.info(f"Clases insertadas -> {len(clases)}")
    except Exception as e:
        db.rollback()
        logging.error(f"Error occurred: {str(e)}")
