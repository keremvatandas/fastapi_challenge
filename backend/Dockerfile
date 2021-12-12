from python:3.9

WORKDIR /backend/api/

COPY . /backend

ENV PYTHONDONTWRITEBYTECODE 1
ENV PYTHONBUFFERED 1

# install python dependencies
RUN pip install --upgrade pip
RUN pip install -r requirements.txt
