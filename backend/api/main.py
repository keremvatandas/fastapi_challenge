from fastapi import FastAPI
from fastapi.middleware.cors import CORSMiddleware

def start_app() -> FastAPI:
    app = FastAPI(title="Apps Interview", debug=True, version="v0.1")
    app.add_middleware(
        CORSMiddleware,
        allow_origins=['localhost', 'http://localhost'],
        allow_credentials=True,
        allow_methods=["*"],
        allow_headers=["*"],
    )
    return app

app = start_app()
