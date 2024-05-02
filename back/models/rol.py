from sqlalchemy import Column, Integer, String
from sqlalchemy.orm import relationship
from db.database import Base


class DbRol(Base):
    __tablename__ = "roles"
    id = Column(Integer, primary_key=True)
    nombre = Column(String(50))
    profesores = relationship("DbProfesor", back_populates="rol")