## How to run Apps Project?


- Edit config.ini file

```bash
cp api/config-sample.ini api/config.ini

# Exm: edit this lines
[DATABASE]
DEBUG=True
SQLALCHEMY_DATABASE_URI=sqlite:///./apps.db
TEST_SQLALCHEMY_DATABASE_URI=sqlite:///./apps_test.db
ENCODING=utf-8

[FASTAPI]
SECRET_KEY=secret!
PROJECT_NAME=APPS Interview Project
API_PREFIX=/api
API_VERSION=v0.1
API_ALGORITHM=HS256

```

-----

- Build and Run  project

```bash
# Built project
docker-compose build

# You can run this project with -d option  from the background
docker-compose up -d

# To follow docker container logs
docker-compose logs -f

```

Check docker container

```
# Example
(apps) ➜  apps_challenge git:(main) ✗ docker ps
CONTAINER ID   IMAGE                    COMMAND                  CREATED          STATUS          PORTS                    NAMES
0c01b5e0e548   apps_challenge_backend   "uvicorn main:app --…"   12 seconds ago   Up 10 seconds   0.0.0.0:8000->8000/tcp   apps_challenge_backend_1
```