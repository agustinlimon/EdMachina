from sqlalchemy import Column, Integer, String
from db import Base

class Carreras(Base):
    __tablename__='carreras'
    
    id = Column(Integer, primary_key=True, index=True)
    nombre = Column(String, unique=True)