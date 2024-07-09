from fastapi import HTTPException

from db import db_dependency
from materias.models.materias import Materias
from materias.schemas.materias import Materias_create, Materias_output

def ver_materias(db: db_dependency, nombre: str):
    query = db.query(Materias)

    if nombre:
        query = query.filter(Materias.nombre.ilike(f"%{nombre}%"))

    materias = query.all()
    materias_filtradas = []
    
    for mat in materias:
        mat = Materias_output(
            nombre=mat.nombre,
            duracion=mat.duracion 
        )
        materias_filtradas.append(mat)
    return sorted(materias_filtradas, key=lambda x: x.nombre)


def crear_materia(db: db_dependency, materia: Materias_create):
    materia_existente = db.query(Materias).filter(Materias.nombre.ilike(materia.nombre)).first()
    if materia_existente:
        raise HTTPException(status_code=400, detail="Ya existe una materia con el nombre indicado")
    
    db_materia = Materias(
        nombre=materia.nombre, 
        duracion=materia.duracion
    )
    db.add(db_materia)
    db.commit()
    db.refresh(db_materia)

    return Materias_output(
        nombre=db_materia.nombre, 
        duracion=db_materia.duracion
    )


def editar_materia(db: db_dependency, id_materia: int, materia: Materias_create):
    materia_existente = db.query(Materias).filter(Materias.id == id_materia).first()
    if not materia_existente:
        raise HTTPException(status_code=404, detail="La materia no existe")
    
    if db.query(Materias).filter(Materias.nombre.ilike(materia.nombre)).where(
        Materias.id != materia_existente.id).first():
            raise HTTPException(status_code=400, detail="Ya existe una materia con el nombre indicado")

    materia_existente.nombre = materia.nombre
    materia_existente.duracion = materia.duracion
    db.commit()
    db.refresh(materia_existente)
    return materia_existente  


def borrar_materia(db: db_dependency, id_materia: int):
    materia_existente = db.query(Materias).filter(Materias.id == id_materia).first()
    if not materia_existente:
        raise HTTPException(status_code=404, detail="La materia no existe")

    db.delete(materia_existente)
    db.commit()
    return materia_existente