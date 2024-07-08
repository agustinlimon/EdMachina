from fastapi import APIRouter, Query, status
from fastapi_pagination import Page, paginate, add_pagination

from db import db_dependency
from personas.schemas.personas import *
from personas.service.personas_service import *

router_personas = APIRouter(
    tags=['Personas'],
    prefix='/personas' 
)

@router_personas.get(
    '/buscar', 
    summary="Buscar personas", 
    description="Buscar todas las personas", 
    response_model=Page[Personas_output], 
    status_code=status.HTTP_200_OK
)
async def buscar_personas(
    db: db_dependency,
    nombre: str = Query(None, description="Nombre de la persona a buscar"),
    apellido: str = Query(None, description="Apellido de la persona a buscar"),
    dni: int = Query(None, description="DNI de la persona a buscar")
):
    personas = ver_personas(
        db, 
        nombre, 
        apellido, 
        dni
    )
    return paginate(personas)

    
@router_personas.post(
    '/crear', 
    summary="Crear persona", 
    description="Dar de alta una persona", 
    response_model=Personas_output, 
    status_code=status.HTTP_201_CREATED
)
async def nueva_persona(
    db: db_dependency, 
    persona: Personas_create
):
    return crear_persona(db, persona)


@router_personas.put(
    '/{leg_persona}',
    summary="Editar persona", 
    description="Editar los datos personales de una persona",
    response_model=Personas_output, 
    status_code=status.HTTP_200_OK
) 
async def modificar_persona(
    db: db_dependency, 
    leg_persona: int, 
    persona: Personas_create
):
    return editar_persona(db, leg_persona, persona)


@router_personas.delete(
    '/{leg_persona}',
    summary="Eliminar persona",
    description="Dar de baja una persona", 
    response_model=Personas_output, 
    status_code=status.HTTP_200_OK
)
async def eliminar_persona(
    db: db_dependency, 
    leg_persona: int
): 
    return borrar_persona(db, leg_persona)


add_pagination(router_personas)