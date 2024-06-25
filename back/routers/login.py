"""
API Router para gestionar la autenticación y obtención de tokens de acceso.

Este módulo define las rutas y funciones para manejar la autenticación de profesores y la obtención de tokens de acceso.

Rutas
-----

* **POST /login**: Autentica a un profesor y devuelve un token de acceso.

Dependencias
------------

* **get_db**: Dependencia para obtener la sesión de la base de datos.

Dependencias Inyectadas
-----------------------

* **db**: La sesión de la base de datos (Session).

"""
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
    """
    Autentica a un profesor y devuelve un token de acceso.

    :param request: Formulario de solicitud de OAuth2 con nombre de usuario y contraseña.
    :type request: OAuth2PasswordRequestForm
    :param db: La sesión de la base de datos.
    :type db: Session
    :returns: Un token de acceso.
    :rtype: Token
    :raises HTTPException: Si las credenciales son inválidas.
    """
    profesor = dao_profesor.get_profesor_by_username(request.username, db)
    if not profesor:
        raise HTTPException(status_code=status.HTTP_404_NOT_FOUND, detail="Invalid credentials")

    if not Hash.verify(request.password, profesor.password):
        raise HTTPException(status_code=status.HTTP_404_NOT_FOUND, detail="Invalid credentials")

    rol = dao_rol.get_rol_by_id(profesor.id_rol, db)
    access_token = oauth2.create_access_token(data={'sub': profesor.id_profesor, 'rol': rol.nombre})
    return {
        "access_token": access_token,
        "token_type": "Bearer"
    }



