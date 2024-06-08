import logging
from io import BytesIO
from typing import List

from fastapi import APIRouter, UploadFile, File, Depends, HTTPException
from starlette import status


from dao import dao_calendario
from db.database import Session, get_db
from db.schemas import CalendarioDTO, ProfesorDTO
from generador_horarios.generador_tablas import generate_tables_from_files
from security.oauth2 import get_current_profesor, check_roles_and_id, check_roles

router = APIRouter(
    prefix="/calendario",
    tags=["calendario"],
)


@router.get(
    "/{id}",
    summary="Devuelve un calendario de la base de datos",
    description="Esta llamada devuelve un calendario en base a su id",
    response_model=CalendarioDTO,
    status_code=status.HTTP_200_OK
)
def get_calendario_by_id(
        id: int,
        current_user: ProfesorDTO = Depends(get_current_profesor),
        db: Session = Depends(get_db)
):
    check_roles(current_user)
    logging.info(f"Request recibida...")
    return dao_calendario.get_calendario_by_id(id, db)

@router.get(
    "/{profesor_id}",
    summary="Devuelve el calendario de un profesor",
    description="Esta llamada devuelve el calendario de un profesor en base a su id",
    response_model=List[CalendarioDTO],
    status_code=status.HTTP_200_OK
)
async def get_calendario_by_id_profesor(
        profesor_id: int,
        current_user: ProfesorDTO = Depends(get_current_profesor),
        db: Session = Depends(get_db)
):
    check_roles_and_id(profesor_id, current_user)
    logging.info(f"Request recibida...")
    return dao_calendario.get_calendario_by_id_profesor(profesor_id, db)

@router.get(
    "/hora_actual/{profesor_id}",
    summary="Devuelve el calendario de un profesor en base a la hora actual",
    description="Esta llamada devuelve el calendario de un profesor en base a la hora actual",
    response_model=List[CalendarioDTO],
    status_code=status.HTTP_200_OK
)
async def get_calendario_actual_by_id_profesor(
        profesor_id: int,
        current_user: ProfesorDTO = Depends(get_current_profesor),
        db: Session = Depends(get_db)
):
    check_roles_and_id(profesor_id, current_user)
    logging.info(f"Request recibida...")
    return dao_calendario.get_actual_calendario_by_id_profesor(profesor_id, db)

@router.post(
    "/generar_calendario/",
    summary="Genera el calendario para el año actual",
    description="Esta llamada genera el calendario para el año actual",
    status_code=status.HTTP_200_OK
)
async def upload_tables(
        tablas: UploadFile = File(...),
        calenario: UploadFile = File(...),
        current_user: ProfesorDTO = Depends(get_current_profesor)
):
    if current_user.rol != "admin":
        raise HTTPException(status_code=403, detail="No tienes permisos para realizar esta acción")
    tablas_byte = await tablas.read()
    horarios_byte = await calenario.read()
    generate_tables_from_files(BytesIO(tablas_byte), BytesIO(horarios_byte))
    return {"message": "Horarios generados correctamente"}


