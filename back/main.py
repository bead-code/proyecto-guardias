from fastapi import FastAPI
from starlette.middleware.cors import CORSMiddleware

from db.database import Base, engine, truncate_all_tables
from generador_horarios.conversor_xml_to_df import load_tables, load_calendario
from generador_horarios.generador_actividades import load_actividades_from_xml
from generador_horarios.generador_aulas import load_aulas_from_xml
from generador_horarios.generador_calendario import generate_calendario
from generador_horarios.generador_clases import load_clases_from_xml
from generador_horarios.generador_cursos import load_cursos_from_xml
from generador_horarios.generador_profesores import load_profesores_from_xml
from generador_horarios.generador_roles import generar_roles
from generador_horarios.generador_tramos_horarios import load_tramos_horarios_from_xml
from routers import login, profesor, rol, curso, actividad, calendario, clase, aula, tramo_horario, guardia, \
    grupo_guardia

app = FastAPI()
app.include_router(login.router)
app.include_router(profesor.router)
app.include_router(guardia.router)
app.include_router(grupo_guardia.router)
app.include_router(calendario.router)
app.include_router(rol.router)
app.include_router(curso.router)
app.include_router(clase.router)
app.include_router(actividad.router)
app.include_router(aula.router)
app.include_router(tramo_horario.router)
origins = [
    "http://localhost",
    "http://localhost:8000",
    "http://localhost:3000",
    "http://localhost:5173",
]

app.add_middleware(
    CORSMiddleware,
    allow_origins=origins,
    allow_credentials=True,
    allow_methods=["*"],
    allow_headers=["*"],
)


Base.metadata.create_all(bind=engine)

def init_data():
    generar_roles()
    load_profesores_from_xml(load_tables())
    load_aulas_from_xml(load_tables())
    load_cursos_from_xml(load_tables())
    load_actividades_from_xml(load_tables())
    load_tramos_horarios_from_xml(load_tables())
    load_clases_from_xml(load_tables())
    generate_calendario(load_calendario())


@app.on_event("startup")
def on_startup():
    truncate_all_tables()
    init_data()

