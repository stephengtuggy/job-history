FROM python:3.12.4-alpine3.20

ENV PYTHONDONTWRITEBYTECODE 1
ENV PYTHONUNBUFFERED 1

WORKDIR /usr/src/app

RUN python -m pip install pdm

RUN mkdir -p /usr/src/app
COPY ./pdm.lock ./pyproject.toml /usr/src/app/
RUN pdm install

COPY . /usr/src/app

RUN chmod u+x docker-entrypoint.sh
RUN chmod u+x manage.py

HEALTHCHECK CMD curl --fail http://localhost:8000 || exit 1

ENTRYPOINT [ "./docker-entrypoint.sh" ]
