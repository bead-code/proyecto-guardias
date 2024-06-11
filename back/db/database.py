"""
Configuración de la base de datos y operaciones de mantenimiento.

Este módulo define la configuración de la base de datos y las funciones para manejar la sesión de la base de datos y las operaciones de truncado de tablas.

Funciones
---------

* **get_db**: Obtiene una sesión de la base de datos.
* **truncate_all_tables**: Elimina todos los datos de todas las tablas de la base de datos.

Excepciones
-----------

* **HTTPException**: Excepción levantada si ocurre algún error durante las operaciones de base de datos.

Dependencias
------------

* **Session**: La sesión de la base de datos.
* **engine**: El motor de la base de datos.
* **MetaData**: Metadata para reflejar las tablas de la base de datos.
* **text**: Para ejecutar consultas SQL sin procesar.
* **SQLAlchemyError**: Excepción de SQLAlchemy.
* **logging**: Para el registro de eventos y errores.
"""

from fastapi import HTTPException
from sqlalchemy import create_engine, MetaData, text
from sqlalchemy.exc import SQLAlchemyError
from sqlalchemy.orm import sessionmaker, declarative_base
import logging

# Configuración de la conexión a la base de datos
hostname = "localhost"
username = "root"
password = "1234"
port = 3306
database = "mydb"

engine = create_engine(
    f"mysql+pymysql://{username}:{password}@mariadb:{port}/{database}?charset=utf8mb4",
)

Session = sessionmaker(autocommit=False, autoflush=False, bind=engine)

Base = declarative_base()

def get_db():
    """
    Obtiene una sesión de la base de datos.

    :returns: La sesión de la base de datos.
    :rtype: Session
    """
    db = Session()
    try:
        yield db
    finally:
        db.close()

def truncate_all_tables():
    """
    Elimina todos los datos de todas las tablas de la base de datos.

    :raises HTTPException: Si ocurre un error al eliminar los datos de las tablas.
    """
    meta = MetaData()
    meta.reflect(bind=engine)
    Session.close_all()
    with engine.connect() as conn:
        trans = conn.begin()
        try:
            conn.execute(text('SET FOREIGN_KEY_CHECKS = 0;'))
            for table in reversed(meta.sorted_tables):
                conn.execute(text(f'TRUNCATE TABLE {table.name}'))
            conn.execute(text('SET FOREIGN_KEY_CHECKS = 1;'))
            trans.commit()
            logging.info("Todos los datos han sido eliminados de todas las tablas existentes.")
        except SQLAlchemyError as e:
            trans.rollback()
            logging.error(f"Error al eliminar los datos: {e}")
            raise HTTPException(status_code=500, detail="Error al eliminar los datos de las tablas")

