from fastapi import APIRouter, Query, status
from fastapi_pagination import Page, paginate, add_pagination

from db import db_dependency
from carreras.schemas.carreras import *
from carreras.service.carreras_service import *

router_carreras = APIRouter(
    tags=['Carreras'],
    prefix='/carreras' 
)

@router_carreras.get(
    '/buscar', 
    summary="Buscar carreras", 
    description="Buscar todas las carreras", 
    response_model=Page[Carreras_output], 
    status_code=status.HTTP_200_OK
)
async def buscar_carrreras(
    db: db_dependency,
    nombre: str = Query(None, description="Nombre de la carrera a buscar")
):
    carreras = ver_carreras(db, nombre)
    return paginate(carreras)

    
@router_carreras.post(
    '/crear', 
    summary="Crear carrera", 
    description="Dar de alta una carrera", 
    response_model=Carreras_output , 
    status_code=status.HTTP_201_CREATED
)
async def nueva_carrera(
    db: db_dependency, 
    carrera: Carreras_create
):
    return crear_carrera(db, carrera)


@router_carreras.put(
    '/{id_carrera}',
    summary="Editar carrera", 
    description="Editar el nombre de una carrera",
    response_model=Carreras_output, 
    status_code=status.HTTP_200_OK
) 
async def modificar_carrera(
    db: db_dependency, 
    id_carrera: int, 
    carrera: Carreras_create
):
    return editar_carrera(db, id_carrera, carrera)


@router_carreras.delete(
    '/{id_carrera}',
    summary="Eliminar carrera",
    description="Dar de baja una carrera", 
    response_model=Carreras_output, 
    status_code=status.HTTP_200_OK
)
async def eliminar_carrera(
    db: db_dependency, 
    id_carrera: int
): 
    return borrar_carrera(db, id_carrera)


add_pagination(router_carreras)