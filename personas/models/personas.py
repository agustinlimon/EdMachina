from sqlalchemy import Column, Integer, String
from db import Base

class Personas(Base):
    __tablename__='personas'
    
    id = Column(Integer, primary_key=True, index=True)
    nombre = Column(String)
    apellido = Column(String)
    legajo = Column(Integer, unique=True)
    email = Column(String)
    direccion = Column(String)
    telefono = Column(Integer)