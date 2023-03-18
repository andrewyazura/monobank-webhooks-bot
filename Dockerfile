# syntax=docker/dockerfile:1

FROM python:3.11-slim-bullseye AS requirements-stage

WORKDIR /tmp

RUN pip install poetry

COPY pyproject.toml poetry.lock ./
RUN poetry export -f requirements.txt --output requirements.txt --without-hashes

FROM python:3.11-slim-bullseye

WORKDIR /code

COPY --from=requirements-stage /tmp/requirements.txt /code/requirements.txt
RUN pip install --no-cache-dir --upgrade -r /code/requirements.txt

CMD ["uvicorn", "monobank_webhooks_bot.main:app", "--proxy-headers", "--host", "0.0.0.0", "--port", "80"]

COPY ./monobank_webhooks_bot /code/monobank_webhooks_bot
