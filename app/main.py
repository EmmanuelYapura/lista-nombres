from fastapi import FastAPI
from app.base.database import Base, engine
from app.controllers.nombres_controllers import router
from fastapi.staticfiles import StaticFiles

app = FastAPI()
app.mount('/static', StaticFiles(directory='app/static'), 'static')
Base.metadata.create_all(engine)
app.include_router(router=router)