"""
Módulo para generar tramos horarios desde un DataFrame y almacenarlos en la base de datos.

Funciones
---------

* **minutos_a_hora**: Convierte una cantidad de minutos a un objeto de hora.
* **generate_tramos_horarios_from_dataframe**: Carga tramos horarios desde un DataFrame y los inserta en la base de datos.

"""

from datetime import time
from typing import Dict
import pandas as pd
from db.database import Session
from db.models import TramoHorario
from utils.logger import logger


def minutos_a_hora(minutos: int) -> time:
    """
    Convierte una cantidad de minutos a un objeto de hora.

    :param minutos: La cantidad de minutos a convertir.
    :type minutos: int
    :returns: Un objeto de tiempo representando la hora y los minutos.
    :rtype: time
    """
    minutos = int(minutos)
    horas = minutos // 60
    minutos_restantes = minutos % 60
    return time(horas, minutos_restantes)


def generate_tramos_horarios_from_dataframe(dataframes: Dict[str, pd.DataFrame]):
    """
    Carga tramos horarios desde un DataFrame de pandas y los inserta en la base de datos.

    :param dataframes: Un diccionario que contiene los DataFrames de pandas con los datos de los tramos horarios.
    :type dataframes: Dict[str, pd.DataFrame]

    La función realiza los siguientes pasos:
    1. Obtiene el DataFrame `TRAMOS_HORARIOS` de los datos proporcionados.
    2. Crea un tramo horario predeterminado "No aplica".
    3. Itera sobre cada fila del DataFrame para crear objetos `TramoHorario`.
    4. Inserta todos los objetos `TramoHorario` en la base de datos.
    5. Maneja cualquier excepción que ocurra durante la inserción de datos.

    Ejemplo de uso:

    .. code-block:: python

        dataframes = pd.read_excel('path_to_excel_file.xlsx', sheet_name=None)
        generate_tramos_horarios_from_dataframe(dataframes)
    """
    df_tramo = dataframes.get('TRAMOS_HORARIOS', pd.DataFrame())
    db = Session()
    tramos = []

    new_tramo = TramoHorario(
        id_tramo_horario=9999,
        nombre="No aplica"
    )
    tramos.append(new_tramo)

    for index, tramo in df_tramo.iterrows():
        new_hora = TramoHorario(
            id_tramo_horario=tramo["X_TRAMO"],
            nombre=tramo["T_HORCEN"],
            hora_inicio=minutos_a_hora(tramo["N_INICIO"]),
            hora_fin=minutos_a_hora(tramo["N_FIN"])
        )
        tramos.append(new_hora)

    db.add_all(tramos)
    try:
        db.commit()
        logger.info(f"Tramos horarios insertados -> {len(tramos)}")
    except Exception as e:
        db.rollback()
        logger.error(f"Error occurred: {str(e)}")

