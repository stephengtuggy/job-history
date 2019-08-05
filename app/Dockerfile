FROM python:3.7-buster

WORKDIR /usr/src/app

RUN apt-get -y update
# Netcat is used by tcp-port-wait.sh
RUN apt-get -y install netcat postgresql-client
RUN apt-get -y dist-upgrade

COPY ./requirements.txt /usr/src/app
RUN pip install -r ./requirements.txt

COPY . /usr/src/app

RUN chmod u+x docker-entrypoint.sh
RUN chmod u+x tcp-port-wait.sh
RUN chmod u+x manage.py

ENTRYPOINT [ "./docker-entrypoint.sh" ]
