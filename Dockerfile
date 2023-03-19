# syntax=docker/dockerfile:1

FROM python:3.11-slim-bullseye AS requirements-stage

WORKDIR /tmp

RUN pip install poetry

COPY pyproject.toml poetry.lock ./
RUN poetry export --output requirements.txt --with=prod

FROM python:3.11-slim-bullseye

WORKDIR /code

COPY --from=requirements-stage /tmp/requirements.txt /code/requirements.txt
RUN pip install --no-cache-dir --upgrade -r /code/requirements.txt

CMD [ \
    "gunicorn", \
    "--bind", "0.0.0.0:80", \
    "--workers", "4", \
    "--worker-class", "uvicorn.workers.UvicornH11Worker", \
    "monobank_webhooks_bot.main:app"\
    ]

COPY ./monobank_webhooks_bot /code/monobank_webhooks_bot
