from fastapi import HTTPException
from pydantic import BaseModel, Field, EmailStr, field_validator
import re
    
class Personas_output(BaseModel):
    nombre: str
    apellido: str
    dni: int
    
class Personas_create(BaseModel):
    nombre: str = Field(min_length=1, max_length=50)
    apellido: str = Field(min_length=1, max_length=50)
    dni: int = Field(ge=0, le=99999999)
    email: EmailStr 
    direccion: str = Field(min_length=1, max_length=70)
    telefono: int
    
    @field_validator('telefono')
    def validar_telefono(cls, v):
        telefono_str = str(v)
        if not re.match(r'^\d{10}$', telefono_str):
            raise HTTPException(status_code=400, detail="El telefono no es valido")
        return v

class Personas(Personas_create):
    legajo: int
    
    class Config:
        from_atributes = True