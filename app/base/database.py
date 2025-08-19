from sqlalchemy import create_engine
from sqlalchemy.ext.declarative import declarative_base
from sqlalchemy.orm import sessionmaker

DATABASE_URL = "sqlite:///./nombres.db"

# motor de base de datos
engine = create_engine( DATABASE_URL,connect_args={"check_same_thread": False})

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