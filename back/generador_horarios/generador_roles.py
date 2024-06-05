from db.database import Session
from db.models import Rol

roles = {
    1: "ADMIN",
    2: "DIRECTOR",
    3: "JEFE_DE_ESTUDIOS",
    4: "PROFESOR"
}


def generar_roles():
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
