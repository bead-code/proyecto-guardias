import os
import shutil

from fastapi import APIRouter, UploadFile, File
from starlette import status
from starlette.exceptions import HTTPException

router = APIRouter(
    prefix="/horario",
    tags=["horario"],
)

BASE_DIR = os.path.dirname(os.path.abspath(__file__))
UPLOAD_DIR = os.path.join(BASE_DIR, "..", "generador_horarios", "xml")


@router.post("/upload_xml/", status_code=status.HTTP_201_CREATED)
async def create_upload_file(file: UploadFile = File(...)):
    file_path = os.path.join(UPLOAD_DIR, file.filename)
    os.makedirs(UPLOAD_DIR, exist_ok=True)

    try:
        with open(file_path, "wb") as buffer:
            shutil.copyfileobj(file.file, buffer)
    except Exception as e:
        raise HTTPException(status_code=500, detail=f"Error saving file: {str(e)}")

    return {"filename": file.filename, "file_path": file_path}
