from fastapi import HTTPException

from db import db_dependency
from carreras.models.carreras import Carreras
from carreras.schemas.carreras import Carreras_create, Carreras_output

def ver_carreras(db: db_dependency, nombre: str):
    query = db.query(Carreras)

    if nombre:
        query = query.filter(Carreras.nombre.ilike(f"%{nombre}%"))

    carreras = query.all()
    carreras_filtradas = []
    
    for car in carreras:
        car = Carreras_output(
            nombre=car.nombre, 
        )
        carreras_filtradas.append(car)
    return sorted(carreras_filtradas, key=lambda x: x.nombre, reverse=True)


def crear_carrera(db: db_dependency, carrera: Carreras_create):
    carrera_existente = db.query(Carreras).filter(Carreras.nombre.ilike(carrera.nombre)).first()
    if carrera_existente:
        raise HTTPException(status_code=400, detail="Ya existe una carrera con el nombre indicado")
    
    db_carrera = Carreras(nombre=carrera.nombre)
    db.add(db_carrera)
    db.commit()
    db.refresh(db_carrera)
    return Carreras_output(nombre=db_carrera.nombre)


def editar_carrera(db: db_dependency, id_carrera: int, carrera: Carreras_create):
    carrera_existente = db.query(Carreras).filter(Carreras.id == id_carrera).first()
    if not carrera_existente:
        raise HTTPException(status_code=404, detail="La carrera no existe")
    
    if db.query(Carreras).filter(Carreras.nombre.ilike(carrera.nombre)).where(
        Carreras.id != carrera_existente.id).first():
            raise HTTPException(status_code=400, detail="Ya existe una carrera con el nombre indicado")

    carrera_existente.nombre = carrera.nombre
    db.commit()
    db.refresh(carrera_existente)
    return carrera_existente  


def borrar_carrera(db: db_dependency, id_carrera: int):
    carrera_existente = db.query(Carreras).filter(Carreras.id == id_carrera).first()
    if not carrera_existente:
        raise HTTPException(status_code=404, detail="La carrera no existe")

    db.delete(carrera_existente)
    db.commit()
    return carrera_existente