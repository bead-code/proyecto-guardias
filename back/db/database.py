from sqlalchemy import create_engine
from sqlalchemy.orm import sessionmaker
from sqlalchemy.ext.declarative import declarative_base

# Definición de variables para la BBDD
hostname = "localhost"
username = "root"
password = "1234"
port = 3306
database = "mydb"

# Si usas PyMySQL como adaptador
engine = create_engine(
    f"mysql+pymysql://{username}:{password}@mariadb:{port}/{database}"
)

Session = sessionmaker(autocommit=False, autoflush=False, bind=engine)

Base = declarative_base()

def get_db():
    db = Session()
    try:
        yield db
    finally:
        db.close()
