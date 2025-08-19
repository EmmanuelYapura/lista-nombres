from fastapi import APIRouter, Depends, HTTPException, Request, Form
from fastapi.responses import RedirectResponse
from sqlalchemy.orm import Session
from app.base.database import get_db
#from app.schemas.nombre_schema import NombreSchema
from app.base.models.nombre_model import NombreModel
from app.repositories.repository import get_nombres, create_nombre, delete_nombre
from fastapi.templating import Jinja2Templates

router = APIRouter()

templates = Jinja2Templates(directory="app/templates")

@router.get("/")
def index(request: Request, db: Session = Depends(get_db)):
    nombres = get_nombres(db)
    return templates.TemplateResponse("home.html", {"request": request, "nombres": nombres})

@router.get("/nombre")
def mostrar_nombres(db: Session = Depends(get_db)):
    nombres = get_nombres(db)
    return nombres

@router.get("/nombre/{id}/delete")
def eliminar_nombre(id: int, db: Session = Depends(get_db)):
    tarea_eliminada = delete_nombre(db, id)
    if not tarea_eliminada:
        raise HTTPException(status_code=404, detail="Tarea no encontrada para eliminar")
    return RedirectResponse(url="/", status_code=303)

@router.post("/nombre")
def crear_nombre(nombre: str = Form(...), db: Session = Depends(get_db)):
    nuevo_nombre = NombreModel(nombre=nombre)
    create_nombre(db, nuevo_nombre)
    return RedirectResponse(url="/", status_code=303)
