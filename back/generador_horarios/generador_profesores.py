import logging

import pandas as pd
from db.database import Session
from db.models import Profesor
from security.hash import Hash

def load_profesores_from_xml(dataframes: pd.DataFrame):
    profesores = []
    df_profesores = dataframes.get('EMPLEADOS', pd.DataFrame())
    jefes_de_estudio = {
        'M.Belén Aguilar Aguilar': 2,
        'Mario Lobo Del Olmo': 3,
        'Rosalina Ugidos Valdueza': 3,
        'Mariano Iglesias Molina': 3,
        'Paula Pereira Fernández': 3,
        'Isabel La Parra Casado': 3
    }

    if not df_profesores.empty:
        df_profesores['NOMBRE_COMPLETO'] = df_profesores.apply(lambda row: ' '.join(filter(None, [row['NOMBRE'], row['APELLIDO1'], row['APELLIDO2']])), axis=1)
        df_profesores['ROL'] = df_profesores['NOMBRE_COMPLETO'].apply(lambda x: jefes_de_estudio.get(x, 4))
        df_profesores = df_profesores[["X_EMPLEADO", "NOMBRE_COMPLETO", "ROL"]]
        df_profesores.loc[:, 'X_EMPLEADO'] = df_profesores['X_EMPLEADO'].astype(int)
    db = Session()
    new_profesor = Profesor(
        id_profesor=9999,
        nombre="No asignado",
        id_rol=4
    )
    profesores.append(new_profesor)
    new_profesor = Profesor(
        id_profesor=1,
        username="admin",
        nombre="admin",
        password=Hash.argon2("1234"),
        id_rol=1
    )
    profesores.append(new_profesor)
    for index, profesor in df_profesores.iterrows():
        new_profesor = Profesor(
            id_profesor = profesor['X_EMPLEADO'],
            nombre=profesor['NOMBRE_COMPLETO'],
            id_rol=profesor["ROL"]
        )
        profesores.append(new_profesor)
    db.add_all(profesores)
    try:
        db.commit()
        logging.info(f"Profesores insertados -> {len(profesores)}")
    except Exception as e:
        db.rollback()
        logging.error(f"Error occurred: {str(e)}")







