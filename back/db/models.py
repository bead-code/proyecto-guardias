"""
Modelos de la base de datos.

Este módulo define los modelos de la base de datos y sus relaciones.

Modelos
-------

* **Rol**: Modelo que representa un rol en la base de datos.
* **Profesor**: Modelo que representa un profesor en la base de datos.
* **Curso**: Modelo que representa un curso en la base de datos.
* **Clase**: Modelo que representa una clase en la base de datos.
* **Actividad**: Modelo que representa una actividad en la base de datos.
* **Aula**: Modelo que representa un aula en la base de datos.
* **TramoHorario**: Modelo que representa un tramo horario en la base de datos.
* **Calendario**: Modelo que representa un calendario en la base de datos.
"""

import uuid
from sqlalchemy import Column, String, Integer, Date, Boolean, ForeignKey, Time
from sqlalchemy.orm import relationship
from db.database import Base
from security.hash import Hash


class Rol(Base):
    """
    Modelo que representa un rol en la base de datos.

    :param id_rol: ID del rol.
    :type id_rol: int
    :param nombre: Nombre del rol.
    :type nombre: str
    :param activo: Indica si el rol está activo.
    :type activo: bool
    """
    __tablename__ = 'roles'
    id_rol = Column(Integer, primary_key=True)
    nombre = Column(String(64))
    activo = Column(Boolean, default=True)
    profesores = relationship("Profesor", back_populates="rol")


class Profesor(Base):
    """
    Modelo que representa un profesor en la base de datos.

    :param id_profesor: ID del profesor.
    :type id_profesor: int
    :param username: Nombre de usuario del profesor.
    :type username: str
    :param password: Contraseña del profesor.
    :type password: str
    :param nombre: Nombre del profesor.
    :type nombre: str
    :param password_temporal: Indica si la contraseña es temporal.
    :type password_temporal: bool
    :param color: Color asociado al profesor.
    :type color: str
    :param id_rol: ID del rol asociado al profesor.
    :type id_rol: int
    :param activo: Indica si el profesor está activo.
    :type activo: bool
    """

    def generate_unique_username(self):
        """
        Genera un nombre de usuario único utilizando UUID.
        """
        return f"user_{uuid.uuid4().hex[:8]}"

    __tablename__ = 'profesores'
    id_profesor = Column(Integer, primary_key=True)
    username = Column(String(64), unique=True, default=generate_unique_username)
    password = Column(String(255), nullable=False, default=Hash.argon2("Sampedro.1234"))
    nombre = Column(String(64))
    password_temporal = Column(Boolean, nullable=False, default=True)
    color = Column(String(64), server_default="#FFFFFF")
    id_rol = Column(Integer, ForeignKey('roles.id_rol'), nullable=False)
    activo = Column(Boolean, default=True)
    rol = relationship("Rol", back_populates="profesores")
    calendario = relationship("Calendario", back_populates="profesor", foreign_keys="[Calendario.id_profesor]")
    calendario_sustituto = relationship("Calendario", back_populates="profesor_sustituto", foreign_keys="[Calendario.id_profesor_sustituto]")


class Curso(Base):
    """
    Modelo que representa un curso en la base de datos.

    :param id_curso: ID del curso.
    :type id_curso: int
    :param nombre: Nombre del curso.
    :type nombre: str
    :param activo: Indica si el curso está activo.
    :type activo: bool
    """
    __tablename__ = 'cursos'
    id_curso = Column(Integer, primary_key=True)
    nombre = Column(String(255))
    activo = Column(Boolean, default=True)
    calendario = relationship("Calendario", back_populates="curso")


class Clase(Base):
    """
    Modelo que representa una clase en la base de datos.

    :param id_clase: ID de la clase.
    :type id_clase: int
    :param nombre: Nombre de la clase.
    :type nombre: str
    :param activo: Indica si la clase está activa.
    :type activo: bool
    """
    __tablename__ = 'clases'
    id_clase = Column(Integer, primary_key=True)
    nombre = Column(String(64), index=True, unique=True)
    activo = Column(Boolean, default=True)
    calendario = relationship("Calendario", back_populates="clase")


class Actividad(Base):
    """
    Modelo que representa una actividad en la base de datos.

    :param id_actividad: ID de la actividad.
    :type id_actividad: int
    :param nombre: Nombre de la actividad.
    :type nombre: str
    :param activo: Indica si la actividad está activa.
    :type activo: bool
    """
    __tablename__ = 'actividades'
    id_actividad = Column(Integer, primary_key=True)
    nombre = Column(String(255))
    activo = Column(Boolean, default=True)
    calendario = relationship("Calendario", back_populates="actividad")


class Aula(Base):
    """
    Modelo que representa un aula en la base de datos.

    :param id_aula: ID del aula.
    :type id_aula: int
    :param nombre: Nombre del aula.
    :type nombre: str
    :param activo: Indica si el aula está activa.
    :type activo: bool
    """
    __tablename__ = 'aulas'
    id_aula = Column(Integer, primary_key=True)
    nombre = Column(String(64), index=True, unique=True)
    activo = Column(Boolean, default=True)
    calendario = relationship("Calendario", back_populates="aula")


class TramoHorario(Base):
    """
    Modelo que representa un tramo horario en la base de datos.

    :param id_tramo_horario: ID del tramo horario.
    :type id_tramo_horario: int
    :param nombre: Nombre del tramo horario.
    :type nombre: str
    :param hora_inicio: Hora de inicio del tramo horario.
    :type hora_inicio: time
    :param hora_fin: Hora de fin del tramo horario.
    :type hora_fin: time
    :param activo: Indica si el tramo horario está activo.
    :type activo: bool
    """
    __tablename__ = 'tramos_horarios'
    id_tramo_horario = Column(Integer, primary_key=True)
    nombre = Column(String(64), index=True, unique=True)
    hora_inicio = Column(Time)
    hora_fin = Column(Time)
    activo = Column(Boolean, default=True)
    calendario = relationship("Calendario", back_populates="tramo_horario")


class Calendario(Base):
    """
    Modelo que representa un calendario en la base de datos.

    :param id_calendario: ID del calendario.
    :type id_calendario: int
    :param id_profesor: ID del profesor asociado al calendario.
    :type id_profesor: int
    :param id_profesor_sustituto: ID del profesor sustituto asociado al calendario.
    :type id_profesor_sustituto: int
    :param id_actividad: ID de la actividad asociada al calendario.
    :type id_actividad: int
    :param id_curso: ID del curso asociado al calendario.
    :type id_curso: int
    :param id_clase: ID de la clase asociada al calendario.
    :type id_clase: int
    :param id_aula: ID del aula asociada al calendario.
    :type id_aula: int
    :param fecha: Fecha del calendario.
    :type fecha: date
    :param dia: Día de la semana del calendario.
    :type dia: int
    :param id_tramo_horario: ID del tramo horario asociado al calendario.
    :type id_tramo_horario: int
    :param ausencia: Indica si hay ausencia en el calendario.
    :type ausencia: bool
    :param activo: Indica si el calendario está activo.
    :type activo: bool
    """
    __tablename__ = 'calendario'
    id_calendario = Column(Integer, primary_key=True, index=True, autoincrement=True)
    id_profesor = Column(Integer, ForeignKey('profesores.id_profesor'), nullable=False)
    id_profesor_sustituto = Column(Integer, ForeignKey('profesores.id_profesor'), nullable=True)
    id_actividad = Column(Integer, ForeignKey('actividades.id_actividad'), nullable=True)
    id_curso = Column(Integer, ForeignKey("cursos.id_curso"), nullable=True)
    id_clase = Column(Integer, ForeignKey("clases.id_clase"), nullable=True)
    id_aula = Column(Integer, ForeignKey('aulas.id_aula'), nullable=True)
    fecha = Column(Date, nullable=False)
    dia = Column(Integer, nullable=False)
    id_tramo_horario = Column(Integer, ForeignKey("tramos_horarios.id_tramo_horario"), nullable=False)
    ausencia = Column(Boolean, default=False)
    activo = Column(Boolean, default=True)
    profesor = relationship("Profesor", back_populates="calendario", foreign_keys=[id_profesor])
    profesor_sustituto = relationship("Profesor", back_populates="calendario_sustituto", foreign_keys=[id_profesor_sustituto])
    actividad = relationship("Actividad", back_populates="calendario")
    curso = relationship("Curso", back_populates="calendario")
    clase = relationship("Clase", back_populates="calendario")
    aula = relationship("Aula", back_populates="calendario")
    tramo_horario = relationship("TramoHorario", back_populates="calendario")

