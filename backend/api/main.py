from fastapi import FastAPI
from fastapi.middleware.cors import CORSMiddleware
from fastapi.openapi.utils import get_openapi
from fastapi.staticfiles import StaticFiles
from starlette.middleware.sessions import SessionMiddleware

from core.config import API_VERSION, DEBUG, PROJECT_NAME, SECRET_KEY
from core.constants import STATIC_FILES_PATH
from core.db import Base, Session, engine
from models import app, screenshot, user
from resources.init_data import read_and_prepare_data
from routes.app import router as app_router
from routes.auth import router as auth_router
from routes.webp import router as webp_router
from routes.docs import router as doc_router


def start_app() -> FastAPI:
    Base.metadata.create_all(engine)
    create_dummy_data()
    app = FastAPI(title=PROJECT_NAME, debug=DEBUG, version=API_VERSION)
    app.openapi = custom_openapi
    app.mount(STATIC_FILES_PATH, StaticFiles(directory="static"), name="static")
    app.add_middleware(SessionMiddleware, secret_key=SECRET_KEY)
    app.add_middleware(
        CORSMiddleware,
        allow_origins=["*"],
        allow_credentials=True,
        allow_methods=["*"],
        allow_headers=["*"],
    )

    include_router(app)
    return app


def create_dummy_data():
    import os
    from pathlib import Path

    path = f"{os.getcwd()}/.created"
    if not os.path.exists(path):
        tmp_user = user.User(username="appz", password="`123456&*")
        apps, ss = read_and_prepare_data()
        with Session() as session:
            session.bulk_save_objects(apps)
            session.bulk_save_objects(ss)
            session.add(tmp_user)
            session.commit()
        Path(path).touch()


def custom_openapi():
    if app.openapi_schema:
        return app.openapi_schema
    openapi_schema = get_openapi(
        title="Apps Interview API Docs",
        version="0.1",
        description="Interview Question",
        routes=app.routes,
    )
    openapi_schema["info"]["x-logo"] = {
        "url": "https://fastapi.tiangolo.com/img/logo-margin/logo-teal.png"
    }
    app.openapi_schema = openapi_schema
    return app.openapi_schema


def include_router(app: FastAPI) -> FastAPI:
    app.include_router(app_router)
    app.include_router(auth_router)
    app.include_router(webp_router)
    app.include_router(doc_router)


app = start_app()
