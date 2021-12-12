import os
import configparser

# Project BaseDIR
config_file_path = os.path.abspath(os.path.join("..", os.getcwd()))
config = configparser.ConfigParser()
config.read(f"{config_file_path}/config.ini")

# DATABASE Settings
DEBUG: bool = (
    True if config["DATABASE"].get("DEBUG", False) in ["True", "true"] else False
)
SQLALCHEMY_DATABASE_URI: str = config["DATABASE"].get("SQLALCHEMY_DATABASE_URI", None)
TEST_SQLALCHEMY_DATABASE_URI: str = config["DATABASE"].get(
    "TEST_SQLALCHEMY_DATABASE_URI", None
)
ENCODING: str = config["DATABASE"].get("ENCODING", "utf-8")


# FASTAPI Settings
SECRET_KEY: str = config["FASTAPI"].get("SECRET_KEY", "secret_key!")
PROJECT_NAME: str = config["FASTAPI"].get("PROJECT_NAME", "APPS Interview Project")
API_PREFIX: str = config["FASTAPI"].get("API_PREFIX", "/api")
API_VERSION: str = config["FASTAPI"].get("API_VERSION", "v0.1")
API_ALGORITHM: str = config["FASTAPI"].get("API_ALGORITHM", "HS256")
