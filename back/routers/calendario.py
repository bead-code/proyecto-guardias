import logging
import os
from io import BytesIO

from fastapi import APIRouter, UploadFile, File, Depends
from starlette import status


from dao import dao_calendario
from db.database import Session, get_db
from db.schemas import CalendarioDTO
from generador_horarios.conversor_xml_to_df import load_calendario_from_file

router = APIRouter(
    prefix="/calendario",
    tags=["calendario"],
)

@router.get("/{id}", response_model=CalendarioDTO, status_code=status.HTTP_200_OK)
def get_calendario_by_id(id: int, db: Session = Depends(get_db)):
    logging.info(f"Request recibida...")
    return dao_calendario.get_calendario_by_id(id, db)
