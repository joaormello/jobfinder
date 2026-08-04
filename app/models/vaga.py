from sqlalchemy import Column, Integer, String, DateTime 
from datetime import datetime

from app.database.base import Base 

class Vaga(Base):
    __tablename__ = "vagas"

    id = Column(Integer, primary_key=True, index=True)
    titulo = Column(String, nullable = False)
    empresa = Column(String)
    localizacao = Column(String)
    tipo_contrato = Column(String)
    nivel = Column(String)
    salario = Column(String)
    link = Column(String, unique = True)
    data_coleta = Column(DateTime, default=datetime.utcnow)
    