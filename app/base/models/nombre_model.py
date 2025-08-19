from sqlalchemy import Column, String, Integer
from app.base.database import Base

class NombreModel(Base):
    __tablename__ = "nombres"

    id = Column(Integer, primary_key=True)
    nombre = Column(String, unique=True, nullable=False)