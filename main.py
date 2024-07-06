from fastapi import FastAPI
from db import create_tables

from carreras.controller.carreras_controller import router_carreras

#* Creacion de la aplicacion
app = FastAPI()
app.include_router(router_carreras)

#* Creacion de las tablas en la base de datos
create_tables()

@app.get("/")
def home():
    return "EdMachina Homepage"