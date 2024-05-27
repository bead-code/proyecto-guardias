from typing import List

from fastapi import APIRouter, Depends
from starlette import status

from dao import dao_actividad
from db.database import get_db, Session
from db.schemas import ActividadCreate, ActividadDTO, ActividadUpdate
import logging

router = APIRouter(
    prefix="/actividad",
    tags=["actividad"],
)

@router.get("/{id}", response_model=ActividadDTO, status_code=status.HTTP_200_OK)
async def get_asignatura_by_codigo(id: int, db: Session = Depends(get_db)):
    logging.info(f"Request recibida...")
    return dao_actividad.get_actividad_by_id(id, db)

@router.get("/{nombre}", response_model=ActividadDTO, status_code=status.HTTP_200_OK)
async def get_asignatura_by_codigo(nombre: str, db: Session = Depends(get_db)):
    logging.info(f"Request recibida...")
    return dao_actividad.get_actividad_by_nombre(nombre, db)

@router.get("/", response_model=List[ActividadDTO], status_code=status.HTTP_200_OK)
async def get_actividades(db: Session = Depends(get_db)):
    logging.info(f"Request recibida...")
    return dao_actividad.get_actividades(db)

@router.post("/", response_model=ActividadDTO, status_code=status.HTTP_201_CREATED)
async def create_actividad(request: ActividadCreate, db: Session = Depends(get_db)):
    logging.info(f"Request recibida: {request}")
    return dao_actividad.create_actividad(request, db)

@router.put("/{id}", response_model=ActividadDTO, status_code=status.HTTP_200_OK)
async def update_actividad(id: int, request: ActividadUpdate, db: Session = Depends(get_db)):
    logging.info(f"Request recibida...")
    return dao_actividad.update_actividad(id, request, db)

@router.delete("/{id}", status_code=status.HTTP_204_NO_CONTENT)
async def delete_actividad(id: int, db: Session = Depends(get_db)):
    logging.info(f"Request recibida...")
    return dao_actividad.delete_actividad(id, db)

