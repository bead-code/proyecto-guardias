from fastapi import FastAPI
from starlette.middleware.cors import CORSMiddleware

from db.database import Base, engine, truncate_all_tables
from generador_horarios.conversor_xml_to_df import load_tables_from_path, load_calendario_from_path
from generador_horarios.generador_actividades import load_actividades_from_xml
from generador_horarios.generador_aulas import load_aulas_from_xml
from generador_horarios.generador_calendario import load_calendario
from generador_horarios.generador_clases import load_clases_from_xml
from generador_horarios.generador_cursos import load_cursos_from_xml
from generador_horarios.generador_profesores import load_profesores_from_xml
from generador_horarios.generador_roles import generar_roles
from generador_horarios.generador_tramos_horarios import load_tramos_horarios_from_xml
from routers import authentication, profesor, rol, curso, actividad, calendario, clase, aula, tramo_horario

app = FastAPI()
app.include_router(profesor.router)
app.include_router(rol.router)
app.include_router(curso.router)
app.include_router(clase.router)
app.include_router(actividad.router)
app.include_router(aula.router)
app.include_router(tramo_horario.router)
app.include_router(authentication.router)
app.include_router(calendario.router)
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
    load_profesores_from_xml(load_tables_from_path())
    load_aulas_from_xml(load_tables_from_path())
    load_cursos_from_xml(load_tables_from_path())
    load_actividades_from_xml(load_tables_from_path())
    load_tramos_horarios_from_xml(load_tables_from_path())
    load_clases_from_xml(load_tables_from_path())
    load_calendario(load_calendario_from_path())


@app.on_event("startup")
def on_startup():
    truncate_all_tables()
    init_data()

