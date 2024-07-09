from sqlalchemy import Column, BigInteger, Integer, String
from db import Base

class Personas(Base):
    __tablename__='personas'
    
    legajo = Column(Integer, primary_key=True, index=True)
    nombre = Column(String)
    apellido = Column(String)
    dni = Column(Integer, unique=True)
    email = Column(String)
    direccion = Column(String)
    telefono = Column(BigInteger)