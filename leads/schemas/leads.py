from pydantic import BaseModel, Field
    
class Leads_output(BaseModel):
    nombre: str
    apellido: str
    legajo: int
    dni: int
    email: str
    direccion: str
    telefono: int
    nombre_materia: str
    duracion_materia: int
    nombre_carrera: str
    anio: int
    cantidad_veces: int
    
class Leads_create(BaseModel):
    leg_persona: int = Field(ge=0)
    id_materia: int = Field(ge=0)
    id_carrera: int = Field(ge=0)

class Personas(Leads_create):
    id: int
    anio: int
    cantidad_veces: int
    
    class Config:
        from_atributes = True