from enum import Enum as PyEnum

from sqlalchemy import Column, String, Integer, Date, Enum as SQLAlchemyEnum, Boolean, ForeignKey, Time
from sqlalchemy.orm import relationship, backref

from db.database import Base
from security.hash import Hash

class Rol(Base):
    __tablename__ = 'roles'
    id_rol = Column(Integer, primary_key=True)
    nombre = Column(String(64))
    profesores = relationship("Profesor", back_populates="rol")

class Profesor(Base):
    __tablename__ = 'profesores'
    id_profesor = Column(Integer, primary_key=True)
    username = Column(String(64), unique=True)
    password = Column(String(255), nullable=False, default=Hash.argon2("Sampedro.1234"))
    nombre = Column(String(64))
    password_temporal = Column(Boolean, nullable=False, default=True)
    color = Column(String(64), server_default="#FFFFFF")
    id_rol = Column(Integer, ForeignKey('roles.id_rol'), nullable=False)
    rol = relationship("Rol", back_populates="profesores")
    calendario = relationship("Calendario", back_populates="profesor", foreign_keys="[Calendario.id_profesor]")
    calendario_sustituto = relationship("Calendario", back_populates="profesor_sustituto", foreign_keys="[Calendario.id_profesor_sustituto]")

class Curso(Base):
    __tablename__ = 'cursos'
    id_curso = Column(Integer, primary_key=True)
    nombre = Column(String(255))
    calendario = relationship("Calendario", back_populates="curso")

class Clase(Base):
    __tablename__ = 'clases'
    id_clase = Column(Integer, primary_key=True)
    nombre = Column(String(64), index=True, unique=True)
    calendario = relationship("Calendario", back_populates="clase")

class Actividad(Base):
    __tablename__ = 'actividades'
    id_actividad = Column(Integer, primary_key=True)
    nombre = Column(String(255))
    calendario = relationship("Calendario", back_populates="actividad")

class Aula(Base):
    __tablename__ = 'aulas'
    id_aula = Column(Integer, primary_key=True)
    nombre = Column(String(64), index=True, unique=True)
    calendario = relationship("Calendario", back_populates="aula")

class TramoHorario(Base):
    __tablename__ = 'tramos_horarios'
    id_tramo_horario = Column(Integer, primary_key=True)
    nombre = Column(String(64), index=True, unique=True)
    hora_inicio = Column(Time)
    hora_fin = Column(Time)
    calendario = relationship("Calendario", back_populates="tramo_horario")

class Calendario(Base):
    __tablename__ = 'calendario'
    id = Column(Integer, primary_key=True, index=True, autoincrement=True)
    id_profesor = Column(Integer, ForeignKey('profesores.id_profesor'), nullable=False)
    id_profesor_sustituto = Column(Integer, ForeignKey('profesores.id_profesor'), nullable=True)
    id_actividad = Column(Integer, ForeignKey('actividades.id_actividad'), nullable=False)
    id_curso = Column(Integer, ForeignKey("cursos.id_curso"), nullable=False)
    id_clase = Column(Integer, ForeignKey("clases.id_clase"), nullable=False)
    id_aula = Column(Integer, ForeignKey('aulas.id_aula'), nullable=False)
    fecha = Column(Date, nullable=False)
    dia = Column(Integer, nullable=True)
    id_tramo_horario = Column(Integer, ForeignKey("tramos_horarios.id_tramo_horario"), nullable=False)
    ausencia = Column(Boolean, default=False)
    profesor = relationship("Profesor", back_populates="calendario", foreign_keys=[id_profesor])
    profesor_sustituto = relationship("Profesor", back_populates="calendario_sustituto", foreign_keys=[id_profesor_sustituto])
    actividad = relationship("Actividad", back_populates="calendario")
    curso = relationship("Curso", back_populates="calendario")
    clase = relationship("Clase", back_populates="calendario")
    aula = relationship("Aula", back_populates="calendario")
    tramo_horario = relationship("TramoHorario", back_populates="calendario")
