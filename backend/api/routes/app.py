from core.auth import Auth
from core.config import API_PREFIX
from core.db import Session, get_db
from fastapi import APIRouter, Depends, Security
from fastapi.encoders import jsonable_encoder
from fastapi.responses import JSONResponse
from fastapi.security import HTTPAuthorizationCredentials, HTTPBearer
from models.app import App

from routes.exceptions import INVALID_TOKEN

router = APIRouter(prefix=API_PREFIX)

security = HTTPBearer()
auth = Auth()


@router.get("/get_apps")
async def get_apps(
    db: Session = Depends(get_db),
    credentials: HTTPAuthorizationCredentials = Security(security),
) -> JSONResponse:
    token = credentials.credentials
    if auth.decode_token(token):
        result = db.query(App).all()
        apps = jsonable_encoder(result)
        return JSONResponse(apps)
    raise INVALID_TOKEN
