# About

Data structures and Algorithms in Python

## Install

Prerequisites:

- Install pipenv
- For development

```bash
# Install dependencies
pipenv shell
pipevn install

# to run all tests
pytest -v

# to run a test file
pytest -q path_to_file

# to see the test coverage
pytest --cov src

# to see statements not covered by tests
pytest --cov=src --cov-report term-missing
```
