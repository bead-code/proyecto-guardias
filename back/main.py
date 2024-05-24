from datetime import datetime

from fastapi import FastAPI
from starlette.middleware.cors import CORSMiddleware

from db.database import Base, engine, Session
from db.models import Rol, Profesor, Aula, Actividad, Curso, Horario
from generador_horarios.generador_actividades import load_actividades_from_xml
from generador_horarios.generador_aulas import load_aulas_from_xml
from generador_horarios.generador_profesores import load_profesores_from_xml
from generador_horarios.generador_cursos import load_cursos_from_xml
from routers import authentication, profesor, rol, ciclo, actividad, horario
from security.hash import Hash

app = FastAPI()
app.include_router(profesor.router)
app.include_router(rol.router)
app.include_router(ciclo.router)
app.include_router(actividad.router)
app.include_router(authentication.router)
app.include_router(horario.router)
origins = [
    "http://localhost",
    "http://localhost:8000",
    "http://localhost:3000",
]

app.add_middleware(
    CORSMiddleware,
    allow_origins=origins,
    allow_credentials=True,
    allow_methods=["*"],
    allow_headers=["*"],
)


Base.metadata.create_all(bind=engine)

def init_data(db: Session):
        load_profesores_from_xml()
        load_aulas_from_xml()
        load_cursos_from_xml()
        load_asignaturas_from_xml()


@app.on_event("startup")
def on_startup():
    db = Session()
    try:
        init_data(db)
    finally:
        db.close()
