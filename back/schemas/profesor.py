from pydantic import BaseModel
from schemas.rol import Rol


class Profesor(BaseModel):
    nick: str
    color: str
    rol: Rol

