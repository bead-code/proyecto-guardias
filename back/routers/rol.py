from fastapi import APIRouter, Depends
from sqlalchemy.orm import Session
from dao import dao_rol
from db.database import get_db
from db.schemas import RolDb, RolDto

router = APIRouter(
    prefix="/rol",
    tags=["rol"]
)


@router.post('/', response_model=RolDb)
async def create_rol(request: RolDb, db: Session = Depends(get_db)):
    return dao_rol.create_rol(request, db)


@router.get('/', response_model=RolDto)
async def get_roll_by_codigo(codigo: str, db: Session = Depends(get_db)):
    return dao_rol.get_rol_by_codigo(codigo, db)