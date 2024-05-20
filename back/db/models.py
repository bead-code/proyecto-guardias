from enum import Enum as PyEnum

from sqlalchemy import Column, String, Integer, Date, Enum as SQLAlchemyEnum, Boolean, ForeignKey

from db.database import Base
from security.hash import Hash


class DiaSemanaEnum(PyEnum):
    LUNES = 1
    MARTES = 3
    MIERCOLES = 3
    JUEVES = 4
    VIERNES = 5


class Rol(Base):
    __tablename__ = 'roles'
    id_rol = Column(Integer, primary_key=True)
    nombre = Column(String(64))

class Profesor(Base):
    __tablename__ = 'profesores'
    id_profesor = Column(Integer, primary_key=True)
    username = Column(String(64), unique=True)
    nombre = Column(String(64))
    password = Column(String(255), nullable=False, default=Hash.argon2("Sampedro.1234"))
    password_temporal = Column(Boolean, nullable=False, default=True)
    nick = Column(String(64))
    color = Column(String(64))
    rol_codigo = Column(String(64), ForeignKey('roles.codigo'))


class Curso(Base):
    __tablename__ = 'cursos'
    id_curso = Column(Integer, primary_key=True)
    nombre = Column(String(64), index=True)

class Actividad(Base):
    __tablename__ = 'actividades'
    id_actividad = Column(Integer, primary_key=True)
    nombre = Column(String(64))

class Aula(Base):
    __tablename__ = 'aulas'
    id_aula = Column(Integer, primary_key=True)
    nombre = Column(String(64))

class Hora(Base):
    __tablename__ = 'horas'
    id_hora = Column(Integer, primary_key=True)
    tramo = Column(String(64))
    hora_inicio = Column(String(64))
    hora_fin = Column(String(64))

class Calendario(Base):
    __tablename__ = 'calendario'
    id = Column(Integer, primary_key=True, index=True, autoincrement=True)
    codigo_profesor = Column(Integer, ForeignKey('profesores.id_profesor'))
    codigo_profesor_sustituto = Column(Integer, ForeignKey('profesores.id_profesor'))
    codigo_asignatura = Column(Integer, ForeignKey('asignaturas.id_asignatura'))
    codigo_curso = Column(Integer, ForeignKey("cursos.id_curso"))
    codigo_clase = Column(Integer, ForeignKey("clases.id_claeses"))
    codigo_aula = Column(Integer, ForeignKey('aulas.id_aula'))
    fecha = Column(Date)
    dia_semana = Column(SQLAlchemyEnum(DiaSemanaEnum))
    hora = Column(Integer, ForeignKey("horas.id_hora"))
    ausencia = Column(Boolean, default=False)
