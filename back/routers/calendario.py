import logging
from io import BytesIO


from fastapi import APIRouter, UploadFile, File, Depends
from starlette import status


from dao import dao_calendario
from db.database import Session, get_db, truncate_all_tables
from db.schemas import CalendarioDTO, ProfesorDTO

from generador_horarios.generador_tablas import generate_tables_from_files
from security.oauth2 import get_current_profesor

router = APIRouter(
    prefix="/calendario",
    tags=["calendario"],
)

@router.get("/{id}", response_model=CalendarioDTO, status_code=status.HTTP_200_OK)
def get_calendario_by_id(id: int, current_user: ProfesorDTO = Depends(get_current_profesor), db: Session = Depends(get_db)):
    logging.info(f"Request recibida...")
    return dao_calendario.get_calendario_by_id(id, db)

@router.post("/generar_horarios/", status_code=status.HTTP_200_OK)
async def upload_tables(tablas: UploadFile = File(...), calenario: UploadFile = File(...), current_user: ProfesorDTO = Depends(get_current_profesor)):
    tablas_byte = await tablas.read()
    horarios_byte = await calenario.read()
    generate_tables_from_files(BytesIO(tablas_byte), BytesIO(horarios_byte))
    return {"message": "Horarios generados correctamente"}


