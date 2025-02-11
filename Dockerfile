# Simple Dockerfile to run a specified script.

FROM python:3.11

RUN pip install poetry

COPY sa-records-retriever-main/pyproject.toml sa-records-retriever-main/poetry.lock /app/
COPY sa-records-retriever-main/retriever /app/retriever
WORKDIR /app/

RUN poetry install

CMD [ "poetry", "run", "python", "retriever/deduplicate.py" ]
