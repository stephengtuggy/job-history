FROM dhi.io/python:3.14.3-debian13-dev

ENV PYTHONDONTWRITEBYTECODE 1
ENV PYTHONUNBUFFERED 1

WORKDIR /usr/local/src/app

RUN python -m pip install --upgrade --upgrade-strategy eager pip

RUN mkdir -p /usr/local/src/app
COPY ./requirements.txt /usr/local/src/app
RUN python -m pip install --require-hashes -r ./requirements.txt

COPY . /usr/local/src/app

RUN chmod u+x docker-entrypoint.sh
RUN chmod u+x manage.py

HEALTHCHECK CMD curl --fail http://localhost:8000 || exit 1

ENTRYPOINT [ "./docker-entrypoint.sh" ]
