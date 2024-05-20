import os
import shutil

from fastapi import APIRouter, UploadFile, File
from starlette import status

router = APIRouter(
    prefix="/horario",
    tags=["horario"],
)

# Encuentra la ruta base del proyecto
BASE_DIR = os.path.dirname(os.path.abspath(__file__))

# Define la ruta donde se guardarán los archivos subidos relativa a la base del proyecto
UPLOAD_DIR = os.path.join(BASE_DIR, "..", "generador_horarios", "xml")

@router.post("/upload_xml/", status_code=status.HTTP_201_CREATED)
async def create_upload_file(file: UploadFile = File(...)):
    file_path = os.path.join(UPLOAD_DIR, file.filename)
    try:
        with open(file_path, "wb") as buffer:
            shutil.copyfileobj(file.file, buffer)
    except Exception as e:
        return {"error": str(e)}
    return {"filename": file.filename, "file_path": file_path}
