from fastapi import HTTPException

from db import db_dependency
from personas.models.personas import Personas
from personas.schemas.personas import Personas_output, Personas_create

def ver_personas(
        db: db_dependency, 
        nombre: str,
        apellido: str,
        dni: int
    ):
    query = db.query(Personas)

    if nombre:
        query = query.filter(Personas.nombre.ilike(f"%{nombre}%"))
    if apellido:
        query = query.filter(Personas.apellido.ilike(f"%{apellido}%"))
    if dni:
        query = query.filter(Personas.dni == dni)

    personas = query.all()
    personas_filtradas = []
    
    for per in personas:
        per = Personas_output(
            nombre=per.nombre,
            apellido=per.apellido,
            dni=per.dni
        )
        personas_filtradas.append(per)
    return sorted(personas_filtradas, key=lambda x: x.nombre)


def crear_persona(db: db_dependency, persona: Personas_create):
    persona_existente = db.query(Personas).filter(Personas.dni == persona.dni).first()
    if persona_existente:
        raise HTTPException(status_code=400, detail="Ya existe una persona con el DNI indicado")
    
    db_persona = Personas(
        nombre=persona.nombre,
        apellido=persona.apellido,
        dni=persona.dni,
        email=persona.email, 
        direccion=persona.direccion,
        telefono=persona.telefono
    )
    db.add(db_persona)
    db.commit()
    db.refresh(db_persona)

    return Personas_output(
        nombre=persona.nombre,
        apellido=persona.apellido,
        dni=persona.dni
    )


def editar_persona(db: db_dependency, leg_persona: int, persona: Personas_create):
    persona_existente = db.query(Personas).filter(Personas.legajo == leg_persona).first()
    if not persona_existente:
        raise HTTPException(status_code=404, detail="La persona no existe")
    
    if db.query(Personas).filter(Personas.dni == persona.dni).where(
        Personas.legajo != persona_existente.legajo).first():
            raise HTTPException(status_code=400, detail="Ya existe una persona con el DNI indicado")

    persona_existente.nombre = persona.nombre
    persona_existente.apellido = persona.apellido
    persona_existente.dni = persona.dni
    persona_existente.email = persona.email
    persona_existente.direccion = persona.direccion
    persona_existente.telefono = persona.telefono

    db.commit()
    db.refresh(persona_existente)
    return persona_existente  


def borrar_persona(db: db_dependency, leg_persona: int):
    persona_existente = db.query(Personas).filter(Personas.legajo == leg_persona).first()
    if not persona_existente:
        raise HTTPException(status_code=404, detail="La persona no existe")

    db.delete(persona_existente)
    db.commit()
    return persona_existente