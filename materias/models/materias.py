from sqlalchemy import Column, Integer, String
from db import Base

class Materias(Base):
    __tablename__='materias'
    
    id = Column(Integer, primary_key=True, index=True)
    nombre = Column(String, unique=True)
    duracion = Column(Integer)