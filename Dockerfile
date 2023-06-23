FROM python:3.11-alpine

WORKDIR /code

ENV PYTHONDONTWRITEBYTECODE 1
ENV PYTHONUNBUFFERED 1

RUN apk update \
    && apk add postgresql-dev python3-dev musl-dev gcc

COPY ./requirements.txt .
RUN python3 -m pip install -r requirements.txt

RUN python3 -m pip install --upgrade pip

COPY . /code/

