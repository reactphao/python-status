.PHONY: help setup run clean

help:
	@echo "Targets:"
	@echo "  make setup  - create venv and install deps"
	@echo "  make run    - run the demo script"
	@echo "  make clean  - remove venv and caches"

setup:
	python3 -m venv .venv
	. .venv/bin/activate && pip install -r requirements.txt

run:
	python3 backend/day1.py

clean:
	rm -rf .venv __pycache__
