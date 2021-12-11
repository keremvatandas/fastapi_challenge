from core.config import API_PREFIX
from core.db import Session, get_db
from fastapi import APIRouter, Depends
from fastapi.encoders import jsonable_encoder
from fastapi.responses import JSONResponse
from models.app import App

router = APIRouter(prefix=API_PREFIX)


@router.get("/get_apps")
async def get_apps(db: Session = Depends(get_db)) -> JSONResponse:
    result = db.query(App).all()
    apps = jsonable_encoder(result)
    return JSONResponse(apps)
