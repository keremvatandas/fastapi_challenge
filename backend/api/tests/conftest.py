from typing import Any, Generator

import pytest

from core.config import TEST_SQLALCHEMY_DATABASE_URI
from core.db import Base, get_db
from core.auth import Auth

from fastapi import FastAPI
from fastapi.testclient import TestClient

from models import app, screenshot, user
from resources.init_data import read_and_prepare_data

from routes.app import router as app_router
from routes.auth import router as auth_router
from routes.webp import router as webp_router

from sqlalchemy import create_engine
from sqlalchemy.orm import sessionmaker

auth = Auth()


def start_application():
    app = FastAPI()
    app.include_router(auth_router)
    app.include_router(app_router)
    app.include_router(webp_router)
    return app


engine = create_engine(
    TEST_SQLALCHEMY_DATABASE_URI,
    encoding="utf-8",
    echo=True,
    connect_args={"check_same_thread": False},
)
SessionTesting = sessionmaker(autocommit=False, autoflush=False, bind=engine)


def create_test_user():
    with SessionTesting() as sess:
        sess.add(
            user.User(
                username="test",
                password="$2b$12$Zj4fqnVqwh1S4VTqOc2ePe816S7cVYTyjGSEODidheojXo44q8cN2",
            )
        )
        sess.commit()


def create_app_and_ss():
    apps, ss = read_and_prepare_data()
    with SessionTesting() as session:
        session.bulk_save_objects(apps)
        session.bulk_save_objects(ss)
        session.commit()


def prepare_db() -> None:
    create_test_user()
    create_app_and_ss()


@pytest.fixture(scope="function")
def app() -> Generator[FastAPI, Any, None]:
    """
    Create a fresh database on each test case.
    """
    Base.metadata.create_all(engine)  # Create the tables.
    prepare_db()
    _app = start_application()
    yield _app
    Base.metadata.drop_all(engine)


@pytest.fixture(scope="function")
def db_session(app: FastAPI) -> Generator[SessionTesting, Any, None]:
    connection = engine.connect()
    transaction = connection.begin()
    session = SessionTesting(bind=connection)
    yield session
    session.close()
    connection.close()


@pytest.fixture(scope="function")
def client(
    app: FastAPI, db_session: SessionTesting
) -> Generator[TestClient, Any, None]:
    """
    Create a new FastAPI TestClient that uses the `db_session` fixture to override
    the `get_db` dependency that is injected into routes.
    """

    def _get_test_db():
        try:
            yield db_session
        finally:
            pass

    app.dependency_overrides[get_db] = _get_test_db
    with TestClient(app) as client:
        yield client


@pytest.fixture(scope="function")
def access_token() -> str:
    return auth.encode_token("test")


@pytest.fixture(scope="function")
def refresh_token() -> str:
    return auth.encode_refresh_token("test")
