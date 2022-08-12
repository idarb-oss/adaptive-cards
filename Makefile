
SOURCE_FILES?=src

clean:
	rm -Rf htmlcov
	rm -f .coverage
	rm -f coverage.xml
	rm -f test-output.xml

format:
	poetry run black $(SOURCE_FILES)
	poetry run isort $(SOURCE_FILES)
	poetry run flake8 $(SOURCE_FILES)
	poetry run mypy $(SOURCE_FILES)

py-38:
	rm -Rf .venv
	poetry env use 3.8
	poetry install --with dev

py-39:
	rm -Rf .venv
	poetry env use 3.9
	poetry install --with dev

py-310:
	rm -Rf .venv
	poetry env use 3.10
	poetry install --with dev

test:
	poetry run pytest -rxXs --cov src --cov-report xml --cov-report=html

test-no-cov:
	poetry run pytest -rxXs --no-cov

lint:
	poetry run black --check --diff $(SOURCE_FILES)
	poetry run mypy $(SOURCE_FILES)
	poetry run isort --check --diff $(SOURCE_FILES)
	poetry run flake8 $(SOURCE_FILES)

pre-commit:
	poetry run pre-commit run --all-files

publish:
	python -m poetry publish --build
