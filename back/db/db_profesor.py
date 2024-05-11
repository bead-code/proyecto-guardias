from sqlalchemy.orm import Session
from hash import Hash
from db.schemas import ProfesorDb


def create_profesor(db: Session, request: ProfesorDb):
    new_profesor = ProfesorDb(
        id=request.id,
        password=Hash.bcrypt(request.password),
        nick=request.nick,
        color=request.color,
    )
    db.add(new_profesor)
    db.commit()
    db.refresh(new_profesor)
    return new_profesor
