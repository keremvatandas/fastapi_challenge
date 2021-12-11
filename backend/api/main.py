from fastapi import FastAPI
from fastapi.middleware.cors import CORSMiddleware
from starlette.middleware.sessions import SessionMiddleware

from core.config import API_VERSION, DEBUG, PROJECT_NAME, SECRET_KEY
from core.db import Base, engine
from models import app, screenshot


def start_app() -> FastAPI:
    Base.metadata.create_all(engine)
    app = FastAPI(title=PROJECT_NAME, debug=DEBUG, version=API_VERSION)
    app.add_middleware(SessionMiddleware, secret_key=SECRET_KEY)
    app.add_middleware(
        CORSMiddleware,
        allow_origins=["localhost", "http://localhost"],
        allow_credentials=True,
        allow_methods=["*"],
        allow_headers=["*"],
    )
    return app


app = start_app()
