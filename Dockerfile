# STAGE 1: Build with tests
FROM python:3.11-slim AS build

WORKDIR /opt/calculator

COPY poetry.lock ./
COPY pyproject.toml ./

RUN python -m pip install --upgrade pip && \
    python -m pip install poetry && \
    poetry install

COPY app ./app
COPY tests ./tests

RUN poetry run pytest . > test_results.txt


#STAGE 2: Production image
FROM python:3.11-slim 

WORKDIR /opt/calculator

COPY --from=build /opt/calculator/app ./app
COPY --from=build /opt/calculator/test_results.txt ./

# CMD["python", "main.py"]
