import pandas as pd
from generador_horarios.conversor_xml_to_df import parse_xml_to_dataframes
from db.database import Session
from db.models import Profesor
import logging

dataframes = parse_xml_to_dataframes()

df_profesores = dataframes.get('EMPLEADOS', pd.DataFrame())
jefes_de_estudio = {
    'M. Belén Aguilar Aguilar': 'admin',
    'Mario Lobo Del Olmo': 'admin',
    'Rosalina Ugidos Valdueza': 'admin',
    'Mariano Iglesias Molina': 'admin',
    'Paula Pereira Fernández': 'admin',
    'Isabel La Parra Casado': 'admin'
}

if not df_profesores.empty:
    df_profesores['NOMBRE_COMPLETO'] = df_profesores['NOMBRE'] + ' ' + df_profesores['APELLIDO1'] + ' ' + df_profesores[
        'APELLIDO2']
    df_profesores['ROL'] = df_profesores['NOMBRE_COMPLETO'].apply(lambda x: jefes_de_estudio.get(x, 'profesor'))
    df_profesores.drop(columns=['X_EMPLEADO', 'F_TOMAPOS', 'D_PUESTO', 'NOMBRE', 'APELLIDO1', 'APELLIDO2'],
                       inplace=True)

def cargar_profesor_from_xml():
    db = Session()
    for index, profesor in df_profesores.iterrows():
        new_profesor = Profesor(
            codigo=profesor['NOMBRE_COMPLETO'],
            rol_codigo=profesor["ROL"]
        )
        db.add(new_profesor)
        try:
            logging.info("Insertando el profesor en la base de datos...")
            db.commit()
            db.refresh(new_profesor)
        except Exception as e:
            db.rollback()
            logging.error(f"Error occurred: {str(e)}")







