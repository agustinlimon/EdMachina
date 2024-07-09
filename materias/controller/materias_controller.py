from fastapi import APIRouter, Query, status
from fastapi_pagination import Page, paginate, add_pagination

from db import db_dependency
from materias.schemas.materias import *
from materias.service.materias_service import *

router_materias = APIRouter(
    tags=['Materias'],
    prefix='/materias' 
)

@router_materias.get(
    '/buscar', 
    summary="Buscar materias", 
    description="Buscar todas las materias", 
    response_model=Page[Materias_output], 
    status_code=status.HTTP_200_OK
)
async def buscar_materias(
    db: db_dependency,
    nombre: str = Query(None, description="Nombre de la materia a buscar")
):
    materias = ver_materias(db, nombre)
    return paginate(materias)

    
@router_materias.post(
    '/crear', 
    summary="Crear materia", 
    description="Dar de alta una materia", 
    response_model=Materias_output, 
    status_code=status.HTTP_201_CREATED
)
async def nueva_materia(
    db: db_dependency, 
    materia: Materias_create
):
    return crear_materia(db, materia)


@router_materias.put(
    '/{id_materia}',
    summary="Editar materia", 
    description="Editar el nombre o la duracion de una materia",
    response_model=Materias_output, 
    status_code=status.HTTP_200_OK
) 
async def modificar_materia(
    db: db_dependency, 
    id_materia: int, 
    materia: Materias_create
):
    return editar_materia(db, id_materia, materia)


@router_materias.delete(
    '/{id_materia}',
    summary="Eliminar materia",
    description="Dar de baja una materia", 
    response_model=Materias_output, 
    status_code=status.HTTP_200_OK
)
async def eliminar_materia(
    db: db_dependency, 
    id_materia: int
): 
    return borrar_materia(db, id_materia)


add_pagination(router_materias)