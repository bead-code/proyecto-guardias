from datetime import date
from typing import Optional

from pydantic import BaseModel, Field
from sqlalchemy import Date

from db.models import DiaSemanaEnum

# LOGIN
class Token(BaseModel):
    access_token: str
    token_type: str

class LoginData(BaseModel):
    username: str
    password: str

# ROLES
class RolDb(BaseModel):
    id_rol: int
    nombre: str

class RolDTO(BaseModel):
    nombre:str


# PROFESORES
class ProfesorDB(BaseModel):
    id_profesor: int
    username: str
    nombre: str
    password: str
    password_temporal: bool
    nick: str
    color: str
    rol: RolDTO

    class Config:
        from_atributes = True


class ProfesorDTO(BaseModel):
    username: str
    nombre: str
    nick: str
    color: str
    rol: RolDTO
    class Config:
        from_atributes = True


class ProfesorCalendario(BaseModel):
    nombre: str

class ProfesorAuth(BaseModel):
    username: str
    nombre: str
    rol: RolDTO

    class Config:
        from_atributes = True

# CURSOS
class CursoDb(BaseModel):
    id_curso: int
    nombre: str

class CursoDTO(BaseModel):
    nombre: str

class CursoCalendario(BaseModel):
    nombre: str

# ASIGNATURAS
class AsignaturaDb(BaseModel):
    codigo: str
    nombre: str

class AsignaturaDTO(BaseModel):
    nombre: str

class AsignaturaCalendario(BaseModel):
    nombre: str


# AULAS
class AulaDb(BaseModel):
    codigo: str
    nombre: str
    codigo_ciclo: str

class AulaDTO(BaseModel):
    nombre: str

# CLASES
class ClaseDb(BaseModel):
    id_clase: int
    nombre: str

class ClaseDTO(BaseModel):
    nombre: str

#CalendarioS
class CalendarioDb(BaseModel):
    id: int = Field(...,description="Id de la hora de la clase" )
    codigo_profesor: int = Field(..., description="Id del profesor titular")
    codigo_profesor_sustituto: Optional[int] = Field(None, description="Id del profesor sustituto")
    codigo_actividad: int = Field(..., description="Id de la actividad")
    codigo_curso: int = Field(..., description="Id del curso")
    codigo_aula: int = Field(..., description="Id del aula")
    codigo_clase: int = Field(..., description="Id del clase")
    fecha: date = Field(..., description="Fecha del calendario")
    dia_semana: DiaSemanaEnum = Field(..., description="Día de la semana")
    hora: int = Field(..., description="Hora del día")
    ausencia: bool = Field(False, description="Indica si hay ausencia del profesor")

    class Config:
        from_attributes = True

class CalendarioDTO(BaseModel):
    profesor: ProfesorCalendario
    profesor_sustituto: ProfesorCalendario
    asignatura: AsignaturaCalendario
    curso: CursoCalendario
    clase: ClaseCalendario
    aula: AulaDto
    fecha: Date
    dia_semana: DiaDTO
    hora: str
    aucencia: bool

    class Config:
        from_attributes = True

