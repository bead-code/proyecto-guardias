from sqlalchemy import Column, String, Integer, Date, Enum, Boolean, ForeignKey
from sqlalchemy.orm import relationship

from database import Base

class Profesor(Base):
    __tablename__ = 'profesores'
    id = Column(String(64), primary_key=True, index=True)
    hashed_password = Column(String)
    nick = Column(String(64))
    color = Column(String(7))
    rol = Column(String(15))
    horarios = relationship("Horario", back_populates="profesor")

class Rol(Base):
    __tablename__ = 'roles'
    codigo = Column(String(15), primary_key=True, index=True)
    nombre = Column(String(64))

class Ciclo(Base):
    __tablename__ = 'ciclos'
    codigo = Column(String(15), primary_key=True, index=True)
    nombre = Column(String(64))
    asignaturas = relationship("Asignatura", back_populates="ciclo")

class Asignatura(Base):
    __tablename__ = 'asignaturas'
    codigo = Column(String(15), primary_key=True, index=True)
    codigo_ciclo = Column(String(15), ForeignKey('ciclos.codigo'))
    nombre = Column(String(64))
    aula = Column(String(15))
    ciclo = relationship("Ciclo", back_populates="asignaturas")
    horarios = relationship("Horario", back_populates="asignatura")

class Aula(Base):
    __tablename__ = 'aulas'
    codigo = Column(String(15), primary_key=True)
    nombre = Column(String(64))
    horarios = relationship("Horario", back_populates="aula")

class Horario(Base):
    __tablename__ = 'horario'
    id = Column(Integer, primary_key=True, index=True, autoincrement=True)
    id_profesor = Column(String(64), ForeignKey('profesores.id'))
    id_profesor_sustituto = Column(String(64), ForeignKey('profesores.id'))
    id_asignatura = Column(String(15), ForeignKey('asignaturas.codigo'))
    id_aula = Column(String(15), ForeignKey('aulas.codigo'))
    fecha = Column(Date)
    dia_semana = Column(Enum("1", "2", "3", "4", "5", "6", "7", "8", "9", "10", "11", "12", "13", "14"))
    ausencia = Column(Boolean, default=False)
    # Relaciones
    profesor = relationship("Profesor", back_populates="horarios")
    profesor_sustituto = relationship("Profesor")
    asignatura = relationship("Asignatura", back_populates="horarios")
    aula = relationship("Aula", back_populates="horarios")
