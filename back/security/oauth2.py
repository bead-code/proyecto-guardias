import logging
from datetime import datetime, timedelta, UTC

import jwt
from fastapi import HTTPException, Security, Depends
from fastapi.security import OAuth2PasswordBearer
from starlette import status

from db.database import Session, get_db
from db.models import Profesor
from db.schemas import ProfesorDTO

oauth2_scheme = OAuth2PasswordBearer(tokenUrl='login')

SECRET_KEY = '77407c7339a6c00544e51af1101c4abb4aea2a31157ca5f7dfd87da02a628107'
ALGORITHM = 'HS256'
ACCESS_TOKEN_EXPIRE_MINUTES = 180
MINIMUM_ADMIN_ROLE = 3


def create_access_token(data: dict):
    to_encode = data.copy()
    expire = datetime.now(UTC) + timedelta(minutes=ACCESS_TOKEN_EXPIRE_MINUTES)
    to_encode.update({"exp": expire})
    encoded_jwt = jwt.encode(to_encode, SECRET_KEY, algorithm=ALGORITHM)
    return encoded_jwt


def verify_access_token(token: str):
    try:
        payload = jwt.decode(token, SECRET_KEY, algorithms=[ALGORITHM])
        return payload
    except jwt.ExpiredSignatureError:
        raise HTTPException(status_code=401, detail="Token expirado")
    except jwt.InvalidTokenError:
        raise HTTPException(status_code=401, detail="El token es inválido")


def get_current_profesor(token: str = Security(oauth2_scheme), db: Session = Depends(get_db)):
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
    if current_profesor.rol.id_rol > MINIMUM_ADMIN_ROLE:
        raise HTTPException(
            status_code=status.HTTP_403_FORBIDDEN,
            detail="No tienes permisos para realizar esta acción"
        )
    return current_profesor

