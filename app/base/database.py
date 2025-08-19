from sqlalchemy import create_engine
from sqlalchemy.ext.declarative import declarative_base
from sqlalchemy.orm import sessionmaker
from dotenv import load_dotenv
import os

load_dotenv()

DATABASE_URL = os.getenv("DATABASE_EXTERNAL_URL")

# motor de base de datos
engine = create_engine(DATABASE_URL)

# sesion para interactuar con la base
SessionLocal = sessionmaker(autocommit=False, autoflush=False, bind=engine)

# base para definir los modelos de tablas
Base = declarative_base()

def get_db():
    db = SessionLocal()
    try:
        yield db
    finally:
        db.close()