from sqlalchemy import create_engine, MetaData, text
from sqlalchemy.orm import sessionmaker, declarative_base

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
            # Deshabilitar las restricciones de claves foráneas
            conn.execute(text('SET FOREIGN_KEY_CHECKS = 0;'))

            # Truncar todas las tablas
            for table in reversed(meta.sorted_tables):
                conn.execute(text(f'TRUNCATE TABLE {table.name}'))

            # Habilitar las restricciones de claves foráneas
            conn.execute(text('SET FOREIGN_KEY_CHECKS = 1;'))

            trans.commit()
            print("Todos los datos han sido eliminados de todas las tablas.")
        except:
            trans.rollback()
            raise