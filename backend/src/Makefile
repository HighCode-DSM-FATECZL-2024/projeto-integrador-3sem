VENV_PATH := .venv/bin/activate
PYTHON := python3

.PHONY: help venv run

help:
	@echo " Available Commands:"
	@echo " venv         - Creates and activates the virtual environment and installs dependencies"
	@echo " run          - Starts the FastAPI application"

venv:
	@echo " Checking for virtual environment..."
	@if [ ! -d .venv ]; then \
		echo " Creating virtual environment..."; \
		$(PYTHON) -m venv .venv > /dev/null; \
	fi
	@echo " Installing dependencies..."
	@.venv/bin/pip install --upgrade pip > /dev/null
	@.venv/bin/pip install -r requirements.txt > /dev/null
	@echo " Virtual environment ready!"

run:
	@echo "\n\n > Running FastAPI application..."
	@echo " Running in http://localhost:8000"
	@PYTHONPATH=. .venv/bin/uvicorn app.app:app --reload --log-level error --no-access-log