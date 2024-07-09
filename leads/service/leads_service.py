from datetime import datetime
from fastapi import HTTPException

from db import db_dependency
from leads.models.leads import Leads
from carreras.models.carreras import Carreras
from materias.models.materias import Materias
from personas.models.personas import Personas
from leads.schemas.leads import Leads_create, Leads_output

def ver_leads(db: db_dependency, id_lead: int):
    query = db.query(Leads)

    if id_lead:
        query = query.filter(Leads.id == id_lead)

    leads = query.all() 
    leads_filtradas = []

    for lead in leads:
        persona = db.query(Personas).filter(Personas.legajo == lead.leg_persona).first()
        materia = db.query(Materias).filter(Materias.id == lead.id_materia).first()
        carrera = db.query(Carreras).filter(Carreras.id == lead.id_carrera).first()

        lead = Leads_output(
            nombre=persona.nombre,
            apellido=persona.apellido,
            legajo=persona.legajo,
            dni=persona.dni,
            email=persona.email,
            direccion=persona.direccion,
            telefono=persona.telefono,
            nombre_materia=materia.nombre,
            duracion_materia=materia.duracion,
            nombre_carrera=carrera.nombre,
            anio=lead.anio,
            cantidad_veces=lead.cantidad_veces
        )
        leads_filtradas.append(lead)
    return sorted(leads_filtradas, key=lambda x: x.nombre)


def crear_lead(db: db_dependency, lead: Leads_create):
    validar_datos(db, lead)

    leads = db.query(Leads).filter(
        (Leads.leg_persona == lead.leg_persona) & 
        (Leads.id_materia == lead.id_materia) & 
        (Leads.id_carrera == lead.id_carrera)
    ).all()


    db_lead = Leads(
        leg_persona=lead.leg_persona,
        id_materia=lead.id_materia,
        id_carrera=lead.id_carrera,
        anio=datetime.now().year,
        cantidad_veces=len(leads) + 1
    )
    db.add(db_lead)
    db.commit()
    db.refresh(db_lead)

    return "El lead se ha creado exitosamente, numero de identificacion: " + str(db_lead.id)

#* Validar que los datos ingresados para la creacion del lead existan en la base de datos
def validar_datos(db: db_dependency, lead: Leads_create):
    if not db.query(Personas).filter(Personas.legajo == lead.leg_persona).first():
        raise HTTPException(status_code=404, detail="La persona no existe")
    if not db.query(Materias).filter(Materias.id == lead.id_materia).first():
        raise HTTPException(status_code=404, detail="La materia no existe")
    if not db.query(Carreras).filter(Carreras.id == lead.id_carrera).first():
        raise HTTPException(status_code=404, detail="La carrera no existe")


def borrar_lead(db: db_dependency, id_lead: int):
    lead_existente = db.query(Leads).filter(Leads.id == id_lead).first()
    if not lead_existente:
        raise HTTPException(status_code=404, detail="El lead no existe")

    db.delete(lead_existente)
    db.commit()
    return "Lead eliminado exitosamente"