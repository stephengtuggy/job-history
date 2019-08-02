FROM python:3.7-stretch

COPY . /usr/src/app
WORKDIR /usr/src/app

RUN sudo apt-get -y update
# Used by tcp-port-wait.sh
RUN sudo apt-get -y install netcat
RUN sudo apt-get -y dist-upgrade

RUN pip install -r ./requirements.txt

RUN chmod u+x docker-entrypoint.sh
RUN chmod u+x tcp-port-wait.sh
RUN chmod u+x manage.py

ENTRYPOINT [ "docker-entrypoint.sh" ]
