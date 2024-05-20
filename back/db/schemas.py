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


class ProfesorHorario(BaseModel):
    nombre: str

class ProfesorAuth(BaseModel):
    username: str
    nombre: str
    rol: RolDTO

    class Config:
        from_atributes = True

# ASIGNATURAS
class AsignaturaDb(BaseModel):
    codigo: str
    nombre: str

class AsignaturaDto(BaseModel):
    nombre: str

class AsignaturaHorario(BaseModel):
    nombre: str


# CICLOS
class CursoDb(BaseModel):
    id_curso: int
    nombre: str

class CursoDto(BaseModel):
    nombre: str

# AULAS
class AulaDb(BaseModel):
    codigo: str
    nombre: str
    codigo_ciclo: str

class AulaDto(BaseModel):
    nombre: str

# CLASES
class ClaseDb(BaseModel):
    id_clase: int
    nombre: str

class ClaseDto(BaseModel):
    nombre: str

#HORARIOS
class HorarioDb(BaseModel):
    codigo_profesor: str = Field(..., max_length=64, description="Código del profesor titular")
    codigo_profesor_sustituto: Optional[str] = Field(None, max_length=64, description="Código del profesor sustituto")
    codigo_actividad: str = Field(..., max_length=64, description="Código de la actividad")
    codigo_aula: str = Field(..., max_length=64, description="Código del aula")
    fecha: date = Field(..., description="Fecha del horario")
    dia_semana: DiaSemanaEnum = Field(..., description="Día de la semana")
    hora: int = Field(..., description="Hora del día")
    ausencia: bool = Field(False, description="Indica si hay ausencia del profesor")

    class Config:
        from_attributes = True

class HorarioDTO(BaseModel):
    profesor: ProfesorHorario
    profesor_sustituto: ProfesorHorario
    asignatura: AsignaturaHorario
    aula: AulaDto
    fecha: Date
    dia_semana: str
    hora: str
    aucencia: bool

    class Config:
        from_attributes = True

