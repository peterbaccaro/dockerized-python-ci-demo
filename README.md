
poetry run isort .
poetry run black .
poetry run flake8 .


docker buildx build -t calculator .