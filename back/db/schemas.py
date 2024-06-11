from datetime import date, time
from typing import Optional, Annotated

from pydantic import BaseModel, Field, StringConstraints

Color = Annotated[str, StringConstraints(pattern=r'^#(?:[0-9a-fA-F]{3}){1,2}$')]

# LOGIN
class Token(BaseModel):
    """
    Modelo para representar un token de acceso.

    :param access_token: El token de acceso.
    :type access_token: str
    :param token_type: El tipo de token.
    :type token_type: str
    """
    access_token: str
    token_type: str

class LoginData(BaseModel):
    """
    Modelo para representar los datos de inicio de sesión.

    :param username: El nombre de usuario.
    :type username: str
    :param password: La contraseña.
    :type password: str
    """
    username: str
    password: str

# ROLES
class RolCreate(BaseModel):
    """
    Modelo para crear un nuevo rol.

    :param nombre: El nombre del rol.
    :type nombre: str
    """
    nombre: str

class RolUpdate(BaseModel):
    """
    Modelo para actualizar un rol existente.

    :param nombre: El nombre del rol.
    :type nombre: str
    """
    nombre: str

class RolDTO(BaseModel):
    """
    Modelo de transferencia de datos para un rol.

    :param id_rol: El ID del rol.
    :type id_rol: int
    :param nombre: El nombre del rol.
    :type nombre: str
    """
    id_rol: int
    nombre: str

# PROFESORES
class ProfesorCreate(BaseModel):
    """
    Modelo para crear un nuevo profesor.

    :param username: El nombre de usuario del profesor.
    :type username: str
    :param nombre: El nombre del profesor.
    :type nombre: str
    :param id_rol: El ID del rol asociado al profesor.
    :type id_rol: int
    """
    username: str
    nombre: str
    id_rol: int

class ProfesorUpdate(BaseModel):
    """
    Modelo para actualizar un profesor existente.

    :param nombre: El nombre del profesor.
    :type nombre: Optional[str]
    :param color: El color asociado al profesor.
    :type color: Optional[Color]
    :param id_rol: El ID del rol asociado al profesor.
    :type id_rol: Optional[int]
    """
    nombre: Optional[str] = None
    color: Optional[Color] = None
    id_rol: Optional[int] = None

class ProfesorDTO(BaseModel):
    """
    Modelo de transferencia de datos para un profesor.

    :param id_profesor: El ID del profesor.
    :type id_profesor: int
    :param username: El nombre de usuario del profesor.
    :type username: Optional[str]
    :param nombre: El nombre del profesor.
    :type nombre: Optional[str]
    :param color: El color asociado al profesor.
    :type color: Optional[Color]
    :param rol: El rol asociado al profesor.
    :type rol: Optional[RolDTO]
    """
    id_profesor: int
    username: Optional[str]
    nombre: Optional[str]
    color: Optional[Color]
    rol: Optional[RolDTO]

    class Config:
        from_attributes = True

class ProfesorAuth(BaseModel):
    """
    Modelo para representar los datos de autenticación de un profesor.

    :param username: El nombre de usuario del profesor.
    :type username: str
    :param nombre: El nombre del profesor.
    :type nombre: str
    :param rol: El rol asociado al profesor.
    :type rol: RolDTO
    """
    username: str
    nombre: str
    rol: RolDTO

    class Config:
        from_attributes = True

# CURSOS
class CursoCreate(BaseModel):
    """
    Modelo para crear un nuevo curso.

    :param nombre: El nombre del curso.
    :type nombre: str
    """
    nombre: str

class CursoUpdate(BaseModel):
    """
    Modelo para actualizar un curso existente.

    :param nombre: El nombre del curso.
    :type nombre: str
    """
    nombre: str

class CursoDTO(BaseModel):
    """
    Modelo de transferencia de datos para un curso.

    :param id_curso: El ID del curso.
    :type id_curso: int
    :param nombre: El nombre del curso.
    :type nombre: str
    """
    id_curso: int
    nombre: str

# ACTIVIDAD
class ActividadCreate(BaseModel):
    """
    Modelo para crear una nueva actividad.

    :param nombre: El nombre de la actividad.
    :type nombre: str
    """
    nombre: str

class ActividadUpdate(BaseModel):
    """
    Modelo para actualizar una actividad existente.

    :param nombre: El nombre de la actividad.
    :type nombre: str
    """
    nombre: str

class ActividadDTO(BaseModel):
    """
    Modelo de transferencia de datos para una actividad.

    :param id_actividad: El ID de la actividad.
    :type id_actividad: int
    :param nombre: El nombre de la actividad.
    :type nombre: str
    """
    id_actividad: int
    nombre: str

class ActividadCalendario(BaseModel):
    """
    Modelo para representar una actividad en el calendario.

    :param nombre: El nombre de la actividad.
    :type nombre: str
    """
    nombre: str

# AULAS
class AulaCreate(BaseModel):
    """
    Modelo para crear un nuevo aula.

    :param nombre: El nombre del aula.
    :type nombre: str
    """
    nombre: str

class AulaUpdate(BaseModel):
    """
    Modelo para actualizar un aula existente.

    :param nombre: El nombre del aula.
    :type nombre: str
    """
    nombre: str

class AulaDTO(BaseModel):
    """
    Modelo de transferencia de datos para un aula.

    :param id_aula: El ID del aula.
    :type id_aula: int
    :param nombre: El nombre del aula.
    :type nombre: str
    """
    id_aula: int
    nombre: str

# CLASES
class ClaseCreate(BaseModel):
    """
    Modelo para crear una nueva clase.

    :param nombre: El nombre de la clase.
    :type nombre: str
    """
    nombre: str

class ClaseUpdate(BaseModel):
    """
    Modelo para actualizar una clase existente.

    :param nombre: El nombre de la clase.
    :type nombre: str
    """
    nombre: str

class ClaseDTO(BaseModel):
    """
    Modelo de transferencia de datos para una clase.

    :param id_clase: El ID de la clase.
    :type id_clase: int
    :param nombre: El nombre de la clase.
    :type nombre: str
    """
    id_clase: int
    nombre: str


# TRAMO HORARIO
class TramoHorarioCreate(BaseModel):
    """
    Modelo para crear un nuevo tramo horario.

    :param nombre: El nombre del tramo horario.
    :type nombre: str
    :param hora_inicio: La hora de inicio del tramo horario.
    :type hora_inicio: time
    :param hora_fin: La hora de fin del tramo horario.
    :type hora_fin: time
    """
    nombre: str
    hora_inicio: time
    hora_fin: time

    class Config:
        arbitrary_types_allowed = True

class TramoHorarioUpdate(BaseModel):
    """
    Modelo para actualizar un tramo horario existente.

    :param nombre: El nombre del tramo horario.
    :type nombre: str
    :param hora_inicio: La hora de inicio del tramo horario.
    :type hora_inicio: time
    :param hora_fin: La hora de fin del tramo horario.
    :type hora_fin: time
    """
    nombre: str
    hora_inicio: time
    hora_fin: time

    class Config:
        arbitrary_types_allowed = True

class TramoHorarioDTO(BaseModel):
    """
    Modelo de transferencia de datos para un tramo horario.

    :param id_tramo_horario: El ID del tramo horario.
    :type id_tramo_horario: int
    :param nombre: El nombre del tramo horario.
    :type nombre: str
    :param hora_inicio: La hora de inicio del tramo horario.
    :type hora_inicio: time
    :param hora_fin: La hora de fin del tramo horario.
    :type hora_fin: time
    """
    id_tramo_horario: int
    nombre: str
    hora_inicio: time
    hora_fin: time

    class Config:
        arbitrary_types_allowed = True
        from_attributes = True


#CALENDARIO
class CalendarioCreate(BaseModel):
    """
    Modelo para crear un nuevo registro en el calendario.

    :param id_profesor: ID del profesor titular.
    :type id_profesor: int
    :param id_profesor_sustituto: ID del profesor sustituto.
    :type id_profesor_sustituto: Optional[int]
    :param id_actividad: ID de la actividad.
    :type id_actividad: int
    :param id_curso: ID del curso.
    :type id_curso: int
    :param id_aula: ID del aula.
    :type id_aula: int
    :param id_clase: ID de la clase.
    :type id_clase: int
    :param fecha: Fecha del calendario.
    :type fecha: date
    :param dia_semana: Día de la semana.
    :type dia_semana: int
    :param id_tramo_horario: ID del tramo horario.
    :type id_tramo_horario: int
    :param ausencia: Indica si hay ausencia del profesor.
    :type ausencia: bool
    """
    id_profesor: int = Field(..., description="Id del profesor titular")
    id_profesor_sustituto: Optional[int] = Field(None, description="Id del profesor sustituto")
    id_actividad: int = Field(..., description="Id de la actividad")
    id_curso: int = Field(..., description="Id del curso")
    id_aula: int = Field(..., description="Id del aula")
    id_clase: int = Field(..., description="Id de la clase")
    fecha: date = Field(..., description="Fecha del calendario")
    dia_semana: int = Field(..., description="Día de la semana")
    id_tramo_horario: int = Field(..., description="Hora del día")
    ausencia: bool = Field(False, description="Indica si hay ausencia del profesor")

    class Config:
        from_attributes = True

class CalendarioDTO(BaseModel):
    """
    Modelo de transferencia de datos para un registro en el calendario.

    :param id_calendario: El ID del calendario.
    :type id_calendario: int
    :param profesor: El profesor asociado al calendario.
    :type profesor: ProfesorDTO
    :param profesor_sustituto: El profesor sustituto asociado al calendario.
    :type profesor_sustituto: ProfesorDTO
    :param actividad: La actividad asociada al calendario.
    :type actividad: ActividadDTO
    :param curso: El curso asociado al calendario.
    :type curso: CursoDTO
    :param clase: La clase asociada al calendario.
    :type clase: ClaseDTO
    :param aula: El aula asociada al calendario.
    :type aula: AulaDTO
    :param fecha: La fecha del calendario.
    :type fecha: date
    :param dia: El día de la semana del calendario.
    :type dia: int
    :param tramo_horario: El tramo horario asociado al calendario.
    :type tramo_horario: TramoHorarioDTO
    :param ausencia: Indica si hay ausencia en el calendario.
    :type ausencia: bool
    """
    id_calendario: int
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
