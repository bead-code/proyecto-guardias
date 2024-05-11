from pydantic import BaseModel

class ProfesorDb(BaseModel):
    id: str
    password: str
    nick: str
    color: str
