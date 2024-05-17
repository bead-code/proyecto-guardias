from sqlalchemy import Column, String, Integer, Date, Enum as SQLAlchemyEnum, Boolean, ForeignKey
from sqlalchemy.orm import relationship
from enum import Enum as PyEnum


from db.database import Base


class DiaSemanaEnum(PyEnum):
    lunes = "1"
    martes = "2"
    miercoles = "3"
    jueves = "4"
    viernes = "5"

class HoraEnum(PyEnum):
    primera = "1"
    segunda = "2"
    tercera = "3"
    cuarta = "4"
    quinta = "5"
    sexta = "6"
    septima = "7"
    octava = "8"
    novena = "9"
    decima = "10"
    decimoprimera = "11"
    duodecima = "12"
    decimatercera = "13"
    decimocuarta  = "14"



class Rol(Base):
    __tablename__ = 'roles'
    codigo = Column(String(64), primary_key=True)

class Profesor(Base):
    __tablename__ = 'profesores'
    codigo = Column(String(64), primary_key=True, index=True)
    password = Column(String(255), nullable=False)
    nick = Column(String(64), nullable=False)
    color = Column(String(64), nullable=False)
    rol_codigo = Column(String(64), ForeignKey('roles.codigo'))


class Ciclo(Base):
    __tablename__ = 'ciclos'
    codigo = Column(String(64), primary_key=True, index=True)
    nombre = Column(String(64))

class Asignatura(Base):
    __tablename__ = 'asignaturas'
    codigo = Column(String(64), primary_key=True, index=True)
    nombre = Column(String(64))

class Aula(Base):
    __tablename__ = 'aulas'
    codigo = Column(String(64), primary_key=True)
    nombre = Column(String(64))

class Horario(Base):
    __tablename__ = 'horarios'
    id = Column(Integer, primary_key=True, index=True, autoincrement=True)
    codigo_profesor = Column(String(64), ForeignKey('profesores.codigo'))
    codigo_profesor_sustituto = Column(String(64), ForeignKey('profesores.codigo'))
    codigo_asignatura = Column(String(64), ForeignKey('asignaturas.codigo'))
    codigo_aula = Column(String(64), ForeignKey('aulas.codigo'))
    fecha = Column(Date)
    dia_semana = Column(SQLAlchemyEnum(DiaSemanaEnum))
    hora = Column(SQLAlchemyEnum(HoraEnum))
    ausencia = Column(Boolean, default=False)
