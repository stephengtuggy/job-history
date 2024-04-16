FROM python:3.11-bookworm

ENV PYTHONDONTWRITEBYTECODE 1
ENV PYTHONUNBUFFERED 1

WORKDIR /usr/src/app

RUN apt-get -y update
RUN apt-get -y upgrade
# Netcat is used by tcp-port-wait.sh
RUN apt-get -y install netcat-traditional postgresql-client libgdal-dev

RUN python -m pip install --upgrade --upgrade-strategy eager pip

RUN mkdir -p /usr/src/app
COPY ./requirements.txt /usr/src/app
RUN python -m pip install --upgrade -r ./requirements.txt

COPY . /usr/src/app

RUN chmod u+x docker-entrypoint.sh
RUN chmod u+x tcp-port-wait.sh
RUN chmod u+x manage.py

ENTRYPOINT [ "./docker-entrypoint.sh" ]
