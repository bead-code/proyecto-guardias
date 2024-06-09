from fastapi import APIRouter, Depends, HTTPException
from fastapi.security import OAuth2PasswordRequestForm
from starlette import status

from dao import dao_profesor, dao_rol
from db.database import Session, get_db
from db.schemas import Token
from security import oauth2
from security.hash import Hash

router = APIRouter(
    prefix="/login",
    tags=["login"],
)

@router.post(
    "",
    summary="Obtener token de acceso",
    description="Esta llamada devuelve un token de acceso en base a las credenciales del profesor",
    response_description="Token de acceso",
    response_model=Token,
    status_code=status.HTTP_200_OK)
def get_token(
        request: OAuth2PasswordRequestForm = Depends(),
        db: Session = Depends(get_db)
):
    profesor = dao_profesor.get_profesor_by_username(request.username, db)
    rol = dao_rol.get_rol_by_id(profesor.id_rol, db)
    if not profesor:
        raise HTTPException(status_code=status.HTTP_404_NOT_FOUND, detail="Invalid credentials")
    if not Hash.verify(request.password, profesor.password):
        raise HTTPException(status_code=status.HTTP_404_NOT_FOUND, detail="Invalid credentials")
    access_token = oauth2.create_access_token(data={'sub': profesor.id_profesor, 'rol': rol.nombre})
    return{
        "access_token": access_token,
        "token_type": "Bearer"
    }

