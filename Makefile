SHELL:=/bin/bash

init:
	pyenv install 3.9 -s
	pipenv install
	pipenv shell

test:
	nosetests tests

