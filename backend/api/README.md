## How to run Apps REST API Project?


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
##### Note: Python version: min: v3.6 or up

- Run  project

```bash
# You can run with docker or docker compose
docker build  # build docker
docker run    # docker run
docker ps     # check docker container

------ Alternatives

# Install requirements
pip3 install -r requirements.txt

# Run project
uvicorn main:app --reload --workers 1 --host 0.0.0.0 --port 8000
```

- Unit Tests
```
# You can run test with pytest
python -m pytest
```



### Some Backend Screens

- API DOC
 ![API DOC](https://github.com/keremvatandas/apps_challenge/blob/main/docs/images/apidoc1.png?raw=true)


 - API REDOC
 ![API REDOC](https://github.com/keremvatandas/apps_challenge/blob/main/docs/images/apidoc2.png?raw=true)

