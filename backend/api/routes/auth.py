from core.auth import Auth
from core.config import API_PREFIX
from core.constants import LOGIN_URL, REFRESH_TOKEN_URL, SIGNUP_URL, SUCCESS_CREATED_MSG
from core.db import Session, get_db
from fastapi import APIRouter, Depends, Security, status
from fastapi.encoders import jsonable_encoder
from fastapi.responses import JSONResponse
from fastapi.security import HTTPAuthorizationCredentials, HTTPBearer
from models.user import User
from sqlalchemy.exc import SQLAlchemyError
from starlette.requests import Request

from routes.exceptions import (
    INVALID_KEYWORD,
    INVALID_PASSWORD,
    INVALID_USERNAME,
    MISSING_PARAMS,
)

router = APIRouter(prefix=API_PREFIX)


security = HTTPBearer()
auth = Auth()


@router.post(SIGNUP_URL)
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


@router.post(LOGIN_URL)
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


@router.get(REFRESH_TOKEN_URL)
async def refresh_token(
    credentials: HTTPAuthorizationCredentials = Security(security),
) -> JSONResponse:
    refresh_token = credentials.credentials
    new_token = auth.refresh_token(refresh_token)
    return {"access_token": new_token}
