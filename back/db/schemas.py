from datetime import date
from typing import Optional

from pydantic import BaseModel, Field
from sqlalchemy import Date

from db.models import DiaSemanaEnum, HoraEnum

# LOGIN
class Token(BaseModel):
    access_token: str
    token_type: str

class LoginData(BaseModel):
    codigo: str
    password: str

class TokenData(BaseModel):
    codigo: str


# ROLES
class RolDb(BaseModel):
    codigo: str

class RolDto(BaseModel):
    codigo: str
    class Config:
        orm_mode = True


# PROFESORES
class ProfesorDTO(BaseModel):
    codigo: str
    nick: str
    color: str
    rol_codigo: str
    class Config:
        orm_mode = True

class ProfesorDb(BaseModel):
    codigo: str
    password: str
    nick: str
    color: str
    rol_codigo: str

    class Config:
        orm_mode = True

class ProfesorHorario(BaseModel):
    codigo: str

class ProfesorAuth(BaseModel):
    codigo: str
    nombre: str
    rol_codigo: str

    class Config:
        orm_mode = True

# ASIGNATURAS
class AsignaturaDb(BaseModel):
    codigo: str
    nombre: str

class AsignaturaDto(BaseModel):
    nombre: str

class AsignaturaHorario(BaseModel):
    nombre: str


# CICLOS
class CicloDb(BaseModel):
    codigo: str
    nombre: str

class CicloDto(BaseModel):
    nombre: str

# AULAS
class AulaDb(BaseModel):
    codigo: str
    nombre: str
    codigo_ciclo: str

class AulaDto(BaseModel):
    nombre: str

#HORARIOS
class HorarioDb(BaseModel):
    codigo_profesor: str = Field(..., max_length=64, description="Código del profesor titular")
    codigo_profesor_sustituto: Optional[str] = Field(None, max_length=64, description="Código del profesor sustituto")
    codigo_asignatura: str = Field(..., max_length=64, description="Código de la asignatura")
    codigo_aula: str = Field(..., max_length=64, description="Código del aula")
    fecha: date = Field(..., description="Fecha del horario")
    dia_semana: DiaSemanaEnum = Field(..., description="Día de la semana")
    hora: HoraEnum = Field(..., description="Hora del día")
    ausencia: bool = Field(False, description="Indica si hay ausencia del profesor")

    class Config:
        arbitrary_types_allowed = True
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
        arbitrary_types_allowed = True





