from fastapi import FastAPI
from fastapi.middleware.cors import CORSMiddleware
from starlette.middleware.sessions import SessionMiddleware

from core.config import API_VERSION, DEBUG, PROJECT_NAME, SECRET_KEY
from core.db import Base, Session, engine
from models import app, screenshot
from resources.init_data import read_and_prepare_data


def start_app() -> FastAPI:
    Base.metadata.create_all(engine)
    create_dummy_data()
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


def create_dummy_data():
    import os
    from pathlib import Path

    path = f"{os.getcwd()}/.created"
    if not os.path.exists(path):
        apps, ss = read_and_prepare_data()
        with Session() as session:
            session.bulk_save_objects(apps)
            session.bulk_save_objects(ss)
            session.commit()
        Path(path).touch()


app = start_app()
