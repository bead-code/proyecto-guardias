import pandas as pd

from db.database import Session
from db.models import Calendario
import logging


def load_calendario(df_calendario=pd.DataFrame()):
    db = Session()
    calendarios = []
    for index, calendario in df_calendario.iterrows():
        new_calendario = Calendario(
            id_profesor=calendario['ID_PROFESOR'] if calendario['ID_PROFESOR'] is not None else 9999,
            id_profesor_sustituto=calendario['ID_PROFESOR_SUSTITUTO'] if calendario.get(
                'ID_PROFESOR_SUSTITUTO') is not None else 9999,
            id_actividad=calendario['ID_ACTIVIDAD'] if calendario['ID_ACTIVIDAD'] is not None else 9999,
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
        logging.info(f"Calendarios insertados -> {len(calendarios)}")
    except Exception as e:
        db.rollback()
