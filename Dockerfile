# Simple Dockerfile to run a specified script.

FROM python:3.11

RUN pip install poetry

COPY pyproject.toml poetry.lock /app/
COPY retriever /app/retriever
WORKDIR /app/

RUN poetry install --no-root

CMD [ "poetry", "run", "python", "retriever/retrieve.py" ]
