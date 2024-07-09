from pydantic import BaseModel, Field
    
class Carreras_output(BaseModel):
    nombre: str
    
class Carreras_create(BaseModel):
    nombre: str = Field(min_length=1, max_length=100)

class Carreras(Carreras_create):
    id: int
    
    class Config:
        from_atributes = True