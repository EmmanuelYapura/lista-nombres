from sqlalchemy.orm import Session
from app.base.models.nombre_model import NombreModel


# pedir nombres
def get_nombres(db: Session):
    return db.query(NombreModel).all() 

# crear nombre
def create_nombre(db: Session, nuevo_nombre: NombreModel):
    new_nombre = NombreModel(nombre=nuevo_nombre.nombre)
    db.add(new_nombre)
    db.commit()
    db.refresh(new_nombre)
    return new_nombre

# borrar nombre
def delete_nombre(db: Session, id_nombre: int):
    db_nombre = db.query(NombreModel).filter(NombreModel.id == id_nombre).first()
    if db_nombre:
        db.delete(db_nombre)
        db.commit()
    return db_nombre
