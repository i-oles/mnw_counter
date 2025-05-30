build:
	python3 -m venv venv && \
	venv/bin/pip install -r requirements.txt

run: build
	venv/bin/python -m project.main

test:
	python3 -m pytest tests

format:
	ruff check . --fix
	ruff format .