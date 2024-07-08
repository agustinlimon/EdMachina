from fastapi import FastAPI
from db import create_tables

from carreras.controller.carreras_controller import router_carreras
from materias.controller.materias_controller import router_materias
from personas.controller.personas_controller import router_personas

#* Creacion de la aplicacion
app = FastAPI()
app.include_router(router_carreras)
app.include_router(router_materias)
app.include_router(router_personas)

#* Creacion de las tablas en la base de datos
create_tables()

@app.get("/")
def home():
    return "EdMachina Homepage"