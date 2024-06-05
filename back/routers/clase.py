from typing import List

from fastapi import APIRouter, Depends
from starlette import status

from dao import dao_clase
from db.database import Session, get_db
from db.schemas import ClaseDTO, ClaseCreate, ClaseUpdate, ProfesorDTO
import logging

from security.oauth2 import get_current_profesor

router = APIRouter(
    prefix="/clase",
    tags=["clase"],
)


@router.get("/{id}", response_model=ClaseDTO, status_code=status.HTTP_200_OK)
def get_clase_by_id(id: int, current_user: ProfesorDTO = Depends(get_current_profesor), db: Session = Depends(get_db)):
    logging.info(f"Request recibida...")
    return dao_clase.get_clase_by_id(id, db)


@router.get("/nombre/{nombre}", response_model=ClaseDTO, status_code=status.HTTP_200_OK)
def get_clase_by_nombre(nombre: str, current_user: ProfesorDTO = Depends(get_current_profesor), db: Session = Depends(get_db)):
    logging.info(f"Request recibida...")
    return dao_clase.get_clase_by_nombre(nombre, db)


@router.get("/", response_model=List[ClaseDTO], status_code=status.HTTP_200_OK)
def get_clases(current_user: ProfesorDTO = Depends(get_current_profesor), db: Session = Depends(get_db)):
    logging.info(f"Request recibida...")
    return dao_clase.get_clases(db)


@router.post("/", response_model=ClaseDTO, status_code=status.HTTP_200_OK)
def create_clase(request: ClaseCreate, current_user: ProfesorDTO = Depends(get_current_profesor), db: Session = Depends(get_db)):
    logging.info(f"Request recibida...")
    return dao_clase.create_clase(request, db)


@router.put("/{id}", response_model=ClaseDTO, status_code=status.HTTP_200_OK)
def update_clase(id: int, request: ClaseUpdate, current_user: ProfesorDTO = Depends(get_current_profesor), db: Session = Depends(get_db)):
    logging.info(f"Request recibida...")
    return dao_clase.update_clase(id, request, db)


@router.delete("/{id}", status_code=status.HTTP_204_NO_CONTENT)
def delete_clase(id: int, current_user: ProfesorDTO = Depends(get_current_profesor), db: Session = Depends(get_db)):
    logging.info(f"Request recibida...")
    return dao_clase.delete_clase(id, db)
