from datetime import datetime

from fastapi import FastAPI
from starlette.middleware.cors import CORSMiddleware

from db.database import Base, engine, Session
from db.models import Rol, Profesor, Aula, Asignatura, Ciclo, Horario
from generador_horarios.generador_aulas import cargar_aula_from_xml
from generador_horarios.generador_profesores import cargar_profesor_from_xml
from routers import authentication, profesor, rol, ciclo, asignatura
from security.hash import Hash

app = FastAPI()
app.include_router(profesor.router)
app.include_router(rol.router)
app.include_router(ciclo.router)
app.include_router(asignatura.router)
app.include_router(authentication.router)
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


# SE INCIAN LOS DATOS CON DOS PERFILES POR DEFECTO
def init_data(db: Session):
    if not db.query(Rol).filter(Rol.codigo == 'admin').first():
        rol_admin = Rol(codigo='admin')
        rol_profesor = Rol(codigo='profesor')
        db.add(rol_admin)
        db.add(rol_profesor)
        db.commit()

    if not db.query(Profesor).filter(Profesor.codigo == 'admin').first():
        profesor_admin = Profesor(
            codigo='admin',
            password=Hash.argon2('adminpassword'),
            nick='adminnick',
            color='red',
            rol_codigo='admin'
        )
        db.add(profesor_admin)

    if not db.query(Profesor).filter(Profesor.codigo == 'profesormock').first():
        profesor_mock = Profesor(
            codigo='profesormock',
            password=Hash.argon2('mockpassword'),
            nick='mocknick',
            color='blue',
            rol_codigo='profesor'
        )
        db.add(profesor_mock)
        db.commit()

    if not db.query(Aula).filter(Aula.codigo == 'aula1').first():
        aula_mock = Aula(
            codigo='aula1',
            nombre='Aula número 1'
        )
        db.add(aula_mock)
        db.commit()

    if not db.query(Asignatura).filter(Asignatura.codigo == 'asignatura1').first():
        asignatura_mock = Asignatura(
            codigo='asignatura1',
            nombre="Asignatura número 1"
        )
        db.add(asignatura_mock)
        db.commit()
    if not db.query(Ciclo).filter(Ciclo.codigo == '2DAM').first():
        ciclo_mock = Ciclo(
            codigo='2DAM',
            nombre="Segundo de desarollo de aplicacones multimedia"
        )
        db.add(ciclo_mock)
        db.commit()
    if not db.query(Horario).filter(Horario.id == 1).first():
        horario_mock = Horario(
            codigo_profesor="admin",
            codigo_asignatura="asignatura1",
            codigo_aula="aula1",
            fecha=datetime.now(),
            dia_semana='LUNES',
            hora="1",
            ausencia=False
        )
        db.add(horario_mock)
        db.commit()

        cargar_profesor_from_xml()
        cargar_aula_from_xml()


# SE CREAN LOS PERFILES POR DEFECTO
@app.on_event("startup")
def on_startup():
    db = Session()
    try:
        init_data(db)
    finally:
        db.close()
