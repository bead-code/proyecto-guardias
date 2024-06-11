"""
Módulo de seguridad y autenticación.

Este módulo proporciona funciones para la creación y verificación de tokens de acceso,
así como para la gestión de la autenticación y autorización de los profesores.

Funciones
---------

* **create_access_token**: Crea un token de acceso JWT.
* **verify_access_token**: Verifica la validez de un token de acceso JWT.
* **get_current_profesor**: Obtiene el profesor actual a partir del token de acceso.
* **check_admin_role**: Verifica si el profesor actual tiene un rol de administrador.

Variables
---------

* **oauth2_scheme**: Esquema de seguridad OAuth2PasswordBearer.
* **SECRET_KEY**: Clave secreta para firmar los tokens JWT.
* **ALGORITHM**: Algoritmo utilizado para firmar los tokens JWT.
* **ACCESS_TOKEN_EXPIRE_MINUTES**: Tiempo de expiración del token de acceso en minutos.
* **MINIMUM_ADMIN_ROLE**: Rol mínimo requerido para considerarse administrador.
"""

import logging
from datetime import datetime, timedelta, UTC

import jwt
from fastapi import HTTPException, Security, Depends
from fastapi.security import OAuth2PasswordBearer
from starlette import status

from db.database import Session, get_db
from db.models import Profesor
from db.schemas import ProfesorDTO

# Configuración de OAuth2
oauth2_scheme = OAuth2PasswordBearer(tokenUrl='login')

# Clave secreta y algoritmo para JWT
SECRET_KEY = '77407c7339a6c00544e51af1101c4abb4aea2a31157ca5f7dfd87da02a628107'
ALGORITHM = 'HS256'
ACCESS_TOKEN_EXPIRE_MINUTES = 180
MINIMUM_ADMIN_ROLE = 3

def create_access_token(data: dict):
    """
    Crea un token de acceso JWT.

    :param data: Los datos a codificar en el token.
    :type data: dict
    :returns: El token de acceso JWT.
    :rtype: str
    """
    to_encode = data.copy()
    expire = datetime.now(UTC) + timedelta(minutes=ACCESS_TOKEN_EXPIRE_MINUTES)
    to_encode.update({"exp": expire})
    encoded_jwt = jwt.encode(to_encode, SECRET_KEY, algorithm=ALGORITHM)
    return encoded_jwt

def verify_access_token(token: str):
    """
    Verifica la validez de un token de acceso JWT.

    :param token: El token de acceso JWT.
    :type token: str
    :returns: Los datos decodificados del token.
    :rtype: dict
    :raises HTTPException: Si el token es inválido o ha expirado.
    """
    try:
        payload = jwt.decode(token, SECRET_KEY, algorithms=[ALGORITHM])
        return payload
    except jwt.ExpiredSignatureError:
        raise HTTPException(status_code=401, detail="Token expirado")
    except jwt.InvalidTokenError:
        raise HTTPException(status_code=401, detail="El token es inválido")

def get_current_profesor(token: str = Security(oauth2_scheme), db: Session = Depends(get_db)):
    """
    Obtiene el profesor actual a partir del token de acceso.

    :param token: El token de acceso JWT.
    :type token: str
    :param db: La sesión de la base de datos.
    :type db: Session
    :returns: El profesor actual.
    :rtype: Profesor
    :raises HTTPException: Si el token es inválido o el profesor no existe.
    """
    payload = verify_access_token(token)
    id_profesor = payload.get("sub")
    if id_profesor is None:
        raise HTTPException(status_code=401, detail="Token inválido")
    profesor = db.query(Profesor).filter(Profesor.id_profesor == id_profesor).first()
    if profesor is None:
        logging.error(f"Profesor not found with codigo {id_profesor}")
        raise HTTPException(status_code=401, detail="Token inválido")
    return profesor

def check_admin_role(current_profesor: ProfesorDTO = Depends(get_current_profesor)):
    """
    Verifica si el profesor actual tiene un rol de administrador.

    :param current_profesor: El profesor actual.
    :type current_profesor: ProfesorDTO
    :returns: El profesor actual si tiene un rol de administrador.
    :rtype: ProfesorDTO
    :raises HTTPException: Si el profesor no tiene permisos de administrador.
    """
    if current_profesor.rol.id_rol > MINIMUM_ADMIN_ROLE:
        raise HTTPException(
            status_code=status.HTTP_403_FORBIDDEN,
            detail="No tienes permisos para realizar esta acción"
        )
    return current_profesor


