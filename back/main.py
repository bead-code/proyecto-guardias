from fastapi import FastAPI
from starlette.middleware.cors import CORSMiddleware
from db.database import Base, engine, truncate_all_tables
from generador_calendario.generador_tablas import generate_tables_from_path
from routers import login, profesor, rol, curso, actividad, calendario, clase, aula, tramo_horario, guardia, grupo_guardia

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


@app.on_event("startup")
def on_startup():
    generate_tables_from_path()

