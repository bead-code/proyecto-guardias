"""
Módulo para cargar actividades desde DataFrames y guardarlas en la base de datos.

Funciones
---------

* **generate_actividades_from_dataframe**: Carga actividades desde un DataFrame de pandas y las inserta en la base de datos.

"""

from typing import Dict
import pandas as pd
from db.database import Session
from db.models import Actividad
from utils.logger import logger


def generate_actividades_from_dataframe(dataframes: Dict[str, pd.DataFrame]):
    """
    Carga actividades desde un DataFrame de pandas y las inserta en la base de datos.

    :param dataframes: Un diccionario que contiene los DataFrames de pandas con los datos de las actividades.
    :type dataframes: dict[str, pd.DataFrame]

    La función realiza los siguientes pasos:

    1. Obtiene los DataFrames `MATERIAS` y `ACTIVIDADES` de los datos proporcionados.
    2. Renombra las columnas relevantes en ambos DataFrames para que sean consistentes.
    3. Combina ambos DataFrames en uno solo.
    4. Itera sobre cada fila del DataFrame combinado para crear objetos `Actividad`.
    5. Inserta todos los objetos `Actividad` en la base de datos.
    6. Maneja cualquier excepción que ocurra durante la inserción de datos.

    Ejemplo de uso:

    .. code-block:: python

        dataframes = pd.read_excel('path_to_excel_file.xlsx', sheet_name=None)
        generate_actividades_from_dataframe(dataframes)
    """
    df_asignaturas = dataframes.get('MATERIAS', pd.DataFrame())
    df_actividades_complementarias = dataframes.get("ACTIVIDADES", pd.DataFrame())

    df_asignaturas.rename(columns={"X_MATERIAOMG": "id_actividad", "D_MATERIAC": "nombre"}, inplace=True)
    df_actividades_complementarias.rename(columns={"X_ACTIVIDAD": "id_actividad", "D_ACTIVIDAD": "nombre"},
                                          inplace=True)

    df_asignaturas = pd.concat([df_asignaturas, df_actividades_complementarias], ignore_index=True)

    db = Session()
    actividades = []

    for index, actividad in df_asignaturas.iterrows():
        new_actividad = Actividad(
            id_actividad=actividad['id_actividad'],
            nombre=actividad['nombre']
        )
        actividades.append(new_actividad)

    db.add_all(actividades)

    try:
        db.commit()
        logger.info(f"Actividades insertadas -> {len(actividades)}")
    except Exception as e:
        db.rollback()
        logger.error(f"Error occurred: {str(e)}")

