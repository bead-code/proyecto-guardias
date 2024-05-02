from sqlalchemy import Column, Integer, String
from db.database import Base


class Prueba(Base):
    __tablename__ = 'prueba'
    id = Column(Integer, primary_key=True)
    nombre = Column(String(50), nullable=False)