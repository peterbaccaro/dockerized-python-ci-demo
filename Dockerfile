# STAGE 1: Build
FROM python:3.13-slim AS build

WORKDIR /opt/calculator

COPY poetry.lock ./
COPY pyproject.toml ./

RUN python -m pip install --upgrade pip && \
    python -m pip install poetry && \
    poetry install --only main

COPY app ./app

# STAGE 2: Tests
FROM build AS test

COPY tests ./tests

RUN poetry install --only test && \
    poetry run pytest . > test_results.txt

#STAGE 3: Production Image
FROM python:3.13-slim

WORKDIR /opt/calculator

COPY --from=build /opt/calculator/app ./app

# CMD["python", "main.py"]
