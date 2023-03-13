.PHONY: all test clean

coverage:  ## Run tests with coverage
	coverage erase
	coverage run -m pytest -ra
	coverage report -m

deps:  ## Install dependencies
	pip install black coverage flake8 mypy pylint pytest tox

lint:  ## Lint and static-check
	flake8 
	pylint .
	mypy .

push:  ## Push code with tags
	git push && git push --tags

test:  ## Run tests
	python3 -m pytest -s ./test

specific_test:  ## Run only one test
	python3 -m pytest -s ./test/test_2_create_asa_token.py