from sqlalchemy import Column, Integer, String
from sqlalchemy.ext.declarative import declarative_base

Base = declarative_base()

class Strumento(Base):
    __tablename__ = 'strumenti'
    id = Column(Integer, primary_key=True, index=True)
    nome = Column(String, nullable=False)
    laboratorio = Column(String, nullable=False)