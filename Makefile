SHELL:=/bin/bash

init:
	python3 -m venv env
	source env/bin/activate
	pip install -r requirements.txt
test:
	pytest

