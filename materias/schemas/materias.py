from pydantic import BaseModel, Field
    
class Materias_output(BaseModel):
    nombre: str
    duracion: int
    
class Materias_create(BaseModel):
    nombre: str = Field(min_length=1, max_length=100)
    duracion: int = Field(ge=1, le=12)

class Materias(Materias_create):
    id: int
    
    class Config:
        from_atributes = True