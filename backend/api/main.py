from fastapi import FastAPI
from fastapi.middleware.cors import CORSMiddleware
from core.config import API_VERSION, DEBUG, PROJECT_NAME, SECRET_KEY


def start_app() -> FastAPI:
    app = FastAPI(title=PROJECT_NAME, debug=DEBUG, version=API_VERSION)
    app.add_middleware(
        CORSMiddleware,
        allow_origins=['localhost', 'http://localhost'],
        allow_credentials=True,
        allow_methods=["*"],
        allow_headers=["*"],
    )
    return app

app = start_app()
