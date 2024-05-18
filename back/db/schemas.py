from datetime import date
from typing import Optional

from pydantic import BaseModel, Field
from sqlalchemy import Date

from db.models import DiaSemanaEnum, HoraEnum

# ROLES
class RolDb(BaseModel):
    codigo: str

class RolDto(BaseModel):
    codigo: str
    class Config:
        orm_mode = True
