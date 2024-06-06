from datetime import date, time
from typing import Optional, List
from pydantic import BaseModel, Field

# LOGIN
class Token(BaseModel):
    access_token: str
    token_type: str

class LoginData(BaseModel):
    username: str
    password: str

# ROLES
class RolCreate(BaseModel):
    nombre: str

class RolUpdate(BaseModel):
    nombre: str

class RolDTO(BaseModel):
    id_rol: int
    nombre: str

# PROFESORES
class ProfesorCreate(BaseModel):
    username: str
    nombre: str
    id_rol: int

class ProfesorUpdate(BaseModel):
    nombre: Optional[str] = None
    color: Optional[str] = None
    id_rol: Optional[int] = None

class ProfesorDTO(BaseModel):
    id_profesor: int
    username: Optional[str]
    nombre: Optional[str]
    color: Optional[str]
    rol: Optional[RolDTO]
    class Config:
        from_attributes = True

class ProfesorCalendario(BaseModel):
    nombre: str

class ProfesorAuth(BaseModel):
    username: str
    nombre: str
    rol: RolDTO

    class Config:
        from_attributes = True

# CURSOS
class CursoCreate(BaseModel):
    nombre: str

class CursoUpdate(BaseModel):
    nombre: str

class CursoDTO(BaseModel):
    id_curso: int
    nombre: str

class CursoCalendario(BaseModel):
    nombre: str

# ACTIVIDAD
class ActividadCreate(BaseModel):
    nombre: str

class ActividadUpdate(BaseModel):
    nombre: str

class ActividadDTO(BaseModel):
    id_actividad: int
    nombre: str

class ActividadCalendario(BaseModel):
    nombre: str

# AULAS
class AulaCreate(BaseModel):
    nombre: str

class AulaUpdate(BaseModel):
    nombre: str

class AulaDTO(BaseModel):
    id_aula: int
    nombre: str

class AulaCalendario(BaseModel):
    nombre: str

# CLASES
class ClaseCreate(BaseModel):
    nombre: str

class ClaseUpdate(BaseModel):
    nombre: str

class ClaseDTO(BaseModel):
    id_clase: int
    nombre: str

class ClaseCalendario(BaseModel):
    nombre: str

# TRAMO HORARIO
class TramoHorarioCreate(BaseModel):
    nombre: str
    hora_inicio: time
    hora_fin: time

    class Config:
        arbitrary_types_allowed = True

class TramoHorarioUpdate(BaseModel):
    nombre: str
    hora_inicio: time
    hora_fin: time

    class Config:
        arbitrary_types_allowed = True

class TramoHorarioDTO(BaseModel):
    id_tramo_horario: int
    nombre: str
    hora_inicio: time
    hora_fin: time

    class Config:
        arbitrary_types_allowed = True
        from_attributes = True

class TramoHorarioCalendario(BaseModel):
    nombre: str
    hora_inicio: time
    hora_fin: time

    class Config:
        arbitrary_types_allowed = True
        from_attributes = True

#CALENDARIO
class CalendarioCreate(BaseModel):
    id_profesor: int = Field(..., description="Id del profesor titular")
    id_profesor_sustituto: Optional[int] = Field(None, description="Id del profesor sustituto")
    id_actividad: int = Field(..., description="Id de la actividad")
    id_curso: int = Field(..., description="Id del curso")
    id_aula: int = Field(..., description="Id del aula")
    id_clase: int = Field(..., description="Id del clase")
    fecha: date = Field(..., description="Fecha del calendario")
    dia_semana: int = Field(..., description="Día de la semana")
    id_tramo_horario: int = Field(..., description="Hora del día")
    ausencia: bool = Field(False, description="Indica si hay ausencia del profesor")

    class Config:
        from_attributes = True

class CalendarioDTO(BaseModel):
    profesor: ProfesorDTO
    profesor_sustituto: ProfesorDTO
    actividad: ActividadDTO
    curso: CursoDTO
    clase: ClaseDTO
    aula: AulaDTO
    fecha: date
    dia: int
    tramo_horario: TramoHorarioDTO
    ausencia: bool

    class Config:
        from_attributes = True
