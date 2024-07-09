from typing import Annotated
from fastapi import Depends
from sqlalchemy import create_engine
from sqlalchemy.orm import sessionmaker, Session
from sqlalchemy.ext.declarative import declarative_base

#* Conexion a la base de datos
DATABASE_URL = "postgresql://postgres:admin@db:5432/EdMachina"
engine = create_engine(DATABASE_URL)
session_local = sessionmaker(bind=engine, autocommit=False, autoflush=False)
Base = declarative_base()


#* Creacion de tablas
def create_tables():
  Base.metadata.create_all(bind= engine)

#* Dependencia para obtener la session de la base de datos
def get_db():
  db = session_local()
  try: 
    yield db
    db.commit()
  finally:
    db.close()


#* Dependencia para obtener la session de la base de datos
db_dependency = Annotated[ Session, Depends(get_db) ]