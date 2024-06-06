from fastapi import HTTPException
from sqlalchemy import create_engine, MetaData, text
from sqlalchemy.exc import SQLAlchemyError
from sqlalchemy.orm import sessionmaker, declarative_base
import logging

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
    db = Session()
    try:
        yield db
    finally:
        db.close()


def truncate_all_tables():
    meta = MetaData()
    meta.reflect(bind=engine)
    with engine.connect() as conn:
        trans = conn.begin()
        try:
            conn.execute(text('SET FOREIGN_KEY_CHECKS = 0;'))
            for table in reversed(meta.sorted_tables):
                result = conn.execute(text(f"SHOW TABLES LIKE '{table.name}';")).fetchone()
                if result:
                    conn.execute(text(f'TRUNCATE TABLE {table.name}'))

            conn.execute(text('SET FOREIGN_KEY_CHECKS = 1;'))
            trans.commit()
            logging.info("Todos los datos han sido eliminados de todas las tablas existentes.")
        except SQLAlchemyError as e:
            trans.rollback()
            print(f"Error al eliminar los datos: {e}")
            raise HTTPException(status_code=500, detail="Error al eliminar los datos de las tablas")