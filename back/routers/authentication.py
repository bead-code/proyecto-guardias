from fastapi import APIRouter, Depends, HTTPException
from fastapi.security import OAuth2PasswordRequestForm
from starlette import status

from dao import dao_profesor
from db.database import Session, get_db
from security import oauth2
from security.hash import Hash

router = APIRouter(
    tags=["autentication"],
)

@router.post("/token")
def get_token(request: OAuth2PasswordRequestForm = Depends(), db: Session = Depends(get_db)):
    profesor = dao_profesor.get_profesor_by_codigo(request.username, db)
    if not profesor:
        raise HTTPException(status_code=status.HTTP_404_NOT_FOUND, detail="Invalid credentials")
    if not Hash.verify(request.password, profesor.password):
        raise HTTPException(status_code=status.HTTP_404_NOT_FOUND, detail="Invalid credentials")
    access_token = oauth2.create_access_token(data={'sub': profesor.codigo})
    return{
        "access_token": access_token,
        "token_type": "Bearer"
    }

