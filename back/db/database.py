from sqlalchemy import create_engine
from sqlalchemy.orm import sessionmaker, declarative_base

hostname = "localhost"
username = "root"
password = "1234"
port = 3306
database = "mydb"

engine = create_engine(
    f"mysql+pymysql://{username}:{password}@localhost:{port}/{database}?charset=utf8mb4",
    echo=True
)

Session = sessionmaker(autocommit=False, autoflush=False, bind=engine)

Base = declarative_base()

def get_db():
    db = Session()
    try:
        yield db
    finally:
        db.close()
