from typing import List

from fastapi import APIRouter, Depends
from sqlalchemy.orm import Session
from starlette import status

from dao import dao_curso
from db.database import get_db
from db.schemas import CursoDTO, CursoCreate, CursoUpdate, ProfesorDTO
import logging

from security.oauth2 import get_current_profesor

logging.basicConfig(level=logging.INFO)

router = APIRouter(
    prefix="/curso",
    tags=["curso"],
)

@router.get("/{id}", response_model=CursoDTO, status_code=status.HTTP_200_OK)
async def get_curso(id: int, current_user: ProfesorDTO = Depends(get_current_profesor), db:Session = Depends(get_db)):
    logging.info(f"Request recibida....")
    return dao_curso.get_curso_by_id(id, db)

@router.get("/nombre/{nombre}", response_model=CursoDTO, status_code=status.HTTP_200_OK)
async def get_curso_by_name(nombre: str, current_user: ProfesorDTO = Depends(get_current_profesor), db:Session = Depends(get_db)):
    logging.info(f"Request recibida....")
    return dao_curso.get_curso_by_nombre(nombre, db)

@router.get("/", response_model=List[CursoDTO], status_code=status.HTTP_200_OK)
async def get_cursos(current_user: ProfesorDTO = Depends(get_current_profesor), db:Session = Depends(get_db)):
    logging.info(f"Request recibida....")
    return dao_curso.get_cursos(db)

@router.post("/", response_model=CursoDTO, status_code=status.HTTP_201_CREATED)
async def create_curso(request: CursoCreate, current_user: ProfesorDTO = Depends(get_current_profesor), db:Session = Depends(get_db)):
    logging.info(f"Request recibida: {request}")
    return dao_curso.create_curso(request, db)

@router.put("/{id}", response_model=CursoDTO, status_code=status.HTTP_200_OK)
async def update_curso(id: int, request: CursoUpdate, current_user: ProfesorDTO = Depends(get_current_profesor), db: Session = Depends(get_db)):
    logging.info(f"Request recibida....")
    return dao_curso.update_curso(id, request, db)

@router.delete("/{id}", status_code=status.HTTP_204_NO_CONTENT)
async def delete_curso(id: int, current_user: ProfesorDTO = Depends(get_current_profesor),  db:Session = Depends(get_db)):
    logging.info(f"Request recibida....")
    return dao_curso.delete_curso(id, db)


