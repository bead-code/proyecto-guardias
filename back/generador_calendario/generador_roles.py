"""
Módulo para generar roles predeterminados en la base de datos.

Funciones
---------

* **generate_roles**: Genera roles predeterminados en la base de datos.

"""

from db.database import Session
from db.models import Rol

# Diccionario que define los roles predeterminados
roles = {
    1: "ADMIN",
    2: "DIRECTOR",
    3: "JEFE_DE_ESTUDIOS",
    4: "PROFESOR"
}

def generate_roles():
    """
    Genera roles predeterminados en la base de datos.

    Esta función crea una lista de roles predeterminados y los inserta en la base de datos.
    Si ocurre un error durante la inserción, la transacción es revertida.

    Los roles generados son:
    - ADMIN
    - DIRECTOR
    - JEFE_DE_ESTUDIOS
    - PROFESOR

    Ejemplo de uso:

    .. code-block:: python

        generate_roles()
    """
    db = Session()
    lista_roles = []
    for id, role in roles.items():
        new_rol = Rol(
            id_rol=id,
            nombre=role,
        )
        lista_roles.append(new_rol)

    db.add_all(lista_roles)
    try:
        db.commit()
    except Exception as e:
        db.rollback()
        raise e


