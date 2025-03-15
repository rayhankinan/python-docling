install:
	poetry install

build:
	poetry build

run:
	poetry run streamlit run ./src/app.py