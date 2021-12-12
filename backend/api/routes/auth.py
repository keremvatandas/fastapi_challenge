from fastapi import HTTPException, Security
from fastapi.security import HTTPAuthorizationCredentials, HTTPBearer
from sqlalchemy.exc import SQLAlchemyError
from core.auth import Auth
from models.user import User
from fastapi import APIRouter, Depends, status

from fastapi.responses import JSONResponse
from starlette.requests import Request
from core.constants import SUCCESS_CREATED_MSG
from routes.exceptions import (
    MISSING_PARAMS,
    INVALID_KEYWORD,
    INVALID_USERNAME,
    INVALID_PASSWORD,
)
from core.config import API_PREFIX
from core.db import Session, get_db
from fastapi import APIRouter, Depends
from fastapi.encoders import jsonable_encoder


router = APIRouter(prefix=API_PREFIX)


security = HTTPBearer()
auth = Auth()


@router.post("/signup")
async def signup(data: Request, db: Session = Depends(get_db)) -> JSONResponse:
    req_body = await data.json()
    try:
        req_body["password"] = auth.encode_password(req_body["password"])
        user = User(**req_body)
        db.add(user)
        db.commit()
    except TypeError:
        raise INVALID_KEYWORD
    except SQLAlchemyError:
        raise MISSING_PARAMS
    return JSONResponse(
        status_code=status.HTTP_201_CREATED, content=SUCCESS_CREATED_MSG
    )


@router.post("/login")
async def login(data: Request, db: Session = Depends(get_db)) -> JSONResponse:
    req_body = await data.json()
    user = db.query(User).filter(User.username == req_body.get("username")).first()

    if user is None:
        raise INVALID_USERNAME

    if not auth.verify_password(req_body.get("password"), user.password):
        raise INVALID_PASSWORD

    access_token = auth.encode_token(user.username)
    refresh_token = auth.encode_refresh_token(user.username)
    return {"access_token": access_token, "refresh_token": refresh_token}


@router.get("/refresh_token")
async def refresh_token(
    credentials: HTTPAuthorizationCredentials = Security(security),
) -> JSONResponse:
    refresh_token = credentials.credentials
    new_token = auth.refresh_token(refresh_token)
    return {"access_token": new_token}
