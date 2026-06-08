# Makefile

install:
	pip install -r requirements.txt

run:
	python app.py

test:
	pytest tests/

format:
	black .

lint:
	flake8 .