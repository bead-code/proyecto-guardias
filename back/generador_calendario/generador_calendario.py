import pandas as pd
from db.database import Session
from db.models import Calendario
from utils.logger import logger


def generate_calendario_from_dataframe(df_calendario: pd.DataFrame):
    """
    Genera entradas de calendario y las inserta en la base de datos.

    :param df_calendario: El DataFrame de pandas que contiene los datos del calendario.
    :type df_calendario: pd.DataFrame

    La función realiza los siguientes pasos:
    1. Crea una sesión de la base de datos.
    2. Itera sobre cada fila del DataFrame `df_calendario`.
    3. Crea un objeto `Calendario` para cada fila, asignando valores predeterminados si los datos están ausentes.
    4. Inserta todos los objetos `Calendario` en la base de datos.
    5. Maneja cualquier excepción que ocurra durante la inserción de datos.

    Ejemplo de uso:

    .. code-block:: python

        dataframes = pd.read_excel('path_to_excel_file.xlsx', sheet_name=None)
        df_calendario = dataframes['CALENDARIO']
        generate_calendario(df_calendario)
    """
    db = Session()
    calendarios = []

    for index, calendario in df_calendario.iterrows():
        new_calendario = Calendario(
            id_profesor=calendario['ID_PROFESOR'] if calendario['ID_PROFESOR'] is not None else 9999,
            id_profesor_sustituto=calendario.get('ID_PROFESOR_SUSTITUTO', 9999),
            id_actividad=calendario['ID_MATERIA'] if calendario['ID_MATERIA'] is not None else 65,
            id_curso=int(calendario['ID_CURSO']) if calendario['ID_CURSO'] is not None else 9999,
            id_clase=calendario['ID_CLASE'] if calendario['ID_CLASE'] is not None else 9999,
            id_aula=calendario['ID_AULA'] if calendario['ID_AULA'] is not None else 9999,
            dia=calendario['DIA'],
            fecha=calendario['FECHA'],
            id_tramo_horario=calendario['ID_TRAMO'] if calendario['ID_TRAMO'] is not None else 9999
        )
        calendarios.append(new_calendario)

    db.add_all(calendarios)

    try:
        db.commit()
        logger.info(f"Calendarios insertados -> {len(calendarios)}")
    except Exception as e:
        db.rollback()
        logger.error(f"Error occurred: {str(e)}")

