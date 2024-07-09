from fastapi import APIRouter, Query, status
from fastapi_pagination import Page, paginate, add_pagination

from db import db_dependency
from leads.schemas.leads import *
from leads.service.leads_service import *

router_leads = APIRouter(
    tags=['Leads'],
    prefix='/leads' 
)

@router_leads.get(
    '/buscar', 
    summary="Consultar leads", 
    description="Consultar todos los leads de las personas", 
    response_model=Page[Leads_output], 
    status_code=status.HTTP_200_OK
)
async def buscar_leads(
    db: db_dependency,
    id_lead: int = Query(None, description="Identificador del lead a buscar")
):
    personas = ver_leads(db, id_lead)
    return paginate(personas)

    
@router_leads.post(
    '/crear', 
    summary="Crear lead", 
    description="Dar de alta un lead", 
    status_code=status.HTTP_201_CREATED
)
async def nuevo_lead(
    db: db_dependency, 
    lead: Leads_create
):
    return crear_lead(db, lead)


@router_leads.delete(
    '/{id_lead}',
    summary="Eliminar lead",
    description="Dar de baja una lead", 
    status_code=status.HTTP_200_OK
)
async def eliminar_lead(
    db: db_dependency, 
    id_lead: int
): 
    return borrar_lead(db, id_lead)


add_pagination(router_leads)