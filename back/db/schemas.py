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
