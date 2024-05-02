from sqlalchemy import Column, Integer, String, ForeignKey
from sqlalchemy.orm import relationship
from db.database import Base

class DbProfesor(Base):
    __tablename__ = 'profesores'
    id = Column(Integer, primary_key=True, index=True)
    nick = Column(String(50), unique=True, nullable=False)
    color = Column(String(20), nullable=False)
    rol_id = Column(Integer, ForeignKey('roles.id'))
    rol = relationship("DbRol", back_populates="profesores")

