from db.database import Session
from db.models import Calendario, Curso, Profesor
from generador_horarios.conversor_xml_to_df import parse_calendario_to_dataframe

df_calendario = parse_calendario_to_dataframe()

def load_calendario_from_xml():
    df_calendario = parse_calendario_to_dataframe()
    db = Session()
    profesores_validos = {profesor.id_profesor for profesor in db.query(Profesor).all()}
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
        db.add(new_calendario)
        try:
            db.commit()
            print("Datos insertados correctamente en la base de datos.")
        except Exception as e:
            db.rollback()
            print(new_calendario.id_profesor)
            print(f"Error occurred: {e}")
