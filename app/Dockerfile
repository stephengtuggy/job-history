FROM python:3.12.4-slim-bookworm

ENV PYTHONDONTWRITEBYTECODE 1
ENV PYTHONUNBUFFERED 1

WORKDIR /usr/src/app

RUN apt-get -y update
RUN apt-get -y upgrade

RUN mkdir -p /usr/src/app
COPY ./requirements.txt /usr/src/app
RUN python -m pip install --upgrade -r ./requirements.txt

COPY . /usr/src/app

RUN chmod u+x docker-entrypoint.sh
RUN chmod u+x manage.py

HEALTHCHECK CMD curl --fail http://localhost:8000 || exit 1

ENTRYPOINT [ "./docker-entrypoint.sh" ]
