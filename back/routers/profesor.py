from fastapi import APIRouter, Depends
from db.database import get_db
from dao import profesor_dao
from schemas.profesor import Profesor
router = APIRouter(
    prefix="/profesor",
    tags=["profesor"]
)


# Obtener un profesor especifico

@router.get("/{nombre}", response_model= Profesor)
async def get_profesor(nombre: str, Session = Depends(get_db)):
    return profesor_dao.get_profesor(Session, nombre)
