from typing import Dict
import pandas as pd
from db.database import Session
from db.models import Profesor
from security.hash import Hash
from utils.logger import logger


def generate_profesores_from_dataframe(dataframes: Dict[str, pd.DataFrame]):
    """
    Carga profesores desde un DataFrame de pandas y los inserta en la base de datos.

    :param dataframes: El DataFrame de pandas que contiene los datos de los profesores.
    :type dataframes: pd.DataFrame

    La función realiza los siguientes pasos:
    1. Obtiene el DataFrame `EMPLEADOS` de los datos proporcionados.
    2. Asigna roles específicos a algunos profesores basándose en sus nombres completos.
    3. Formatea el nombre completo de cada profesor combinando su nombre y apellidos.
    4. Asigna un rol predeterminado de 4 (PROFESOR) a aquellos profesores que no tienen un rol específico.
    5. Crea objetos `Profesor` para un profesor "No asignado" y un usuario admin.
    6. Itera sobre cada fila del DataFrame para crear objetos `Profesor`.
    7. Inserta todos los objetos `Profesor` en la base de datos.
    8. Maneja cualquier excepción que ocurra durante la inserción de datos.

    Ejemplo de uso:

    .. code-block:: python

        dataframes = pd.read_excel('path_to_excel_file.xlsx', sheet_name=None)
        load_profesores_from_xml(dataframes)
    """
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
        df_profesores['NOMBRE_COMPLETO'] = df_profesores.apply(
            lambda row: ' '.join(filter(None, [row['NOMBRE'], row['APELLIDO1'], row['APELLIDO2']])), axis=1)
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
            id_profesor=profesor['X_EMPLEADO'],
            nombre=profesor['NOMBRE_COMPLETO'],
            id_rol=profesor["ROL"]
        )
        profesores.append(new_profesor)

    db.add_all(profesores)

    try:
        db.commit()
        logger.info(f"Profesores insertados -> {len(profesores)}")
    except Exception as e:
        db.rollback()
        logger.error(f"Error occurred: {str(e)}")
