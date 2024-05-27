import os


from fastapi import APIRouter, UploadFile, File
from starlette import status


from dao import dao_calendario

router = APIRouter(
    prefix="/horario",
    tags=["horario"],
)

BASE_DIR = os.path.dirname(os.path.abspath(__file__))
UPLOAD_DIR = os.path.join(BASE_DIR, "..", "generador_horarios", "xml")


@router.post("/upload_xml/", status_code=status.HTTP_201_CREATED)
async def upload_file(file: UploadFile = File(...)):

    dao_calendario.create_calendario()

    return {"filename": file.filename, "file_path": file_path}
