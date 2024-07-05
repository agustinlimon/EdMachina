from sqlalchemy import Column, Integer, ForeignKey
from sqlalchemy.orm import relationship
from db import Base

from personas.models.personas import Personas
from materias.models.materias import Materias
from carreras.models.carreras import Carreras

class Leads(Base):
    __tablename__='leads'
    
    id = Column(Integer, primary_key=True, index=True)
    id_persona = Column(Integer, ForeignKey('personas.id', ondelete='CASCADE'))
    id_materia = Column(Integer, ForeignKey('materias.id', ondelete='CASCADE'))
    id_carrera = Column(Integer, ForeignKey('carreras.id', ondelete='CASCADE'))
    anio = Column(Integer)

    persona = relationship('Personas', backref='personas')
    materia = relationship('Materias', backref='materias')
    carrera = relationship('Carreras', backref='carreras')
