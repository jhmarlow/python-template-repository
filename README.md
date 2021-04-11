# Python Template Repository
![example workflow](https://github.com/jhmarlow/google-cloud-platform-project/actions/workflows/main.yml/badge.svg)
![example workflow](https://img.shields.io/github/issues/jhmarlow/google-cloud-platform-project)
![example workflow](https://img.shields.io/github/forks/jhmarlow/google-cloud-platform-project)
![example workflow](https://img.shields.io/github/stars/jhmarlow/google-cloud-platform-project)
![example workflow](https://img.shields.io/github/license/jhmarlow/google-cloud-platform-project)
![example workflow](https://img.shields.io/twitter/url?style=social&url=https%3A%2F%2Ftwitter.com%2FJacobMarlow19)

Setup a template repository to be used in future python projects.

# TODO:
- Integrate tests with CI
- Setup versioning

# Badges
Badges created using shield.io
https://shields.io

# Setup
To setup:

`pip install -e .`

With test external package dependencies:

`pip install -e '.[test]'`

# Testing
Run tests:
`./ci/run_tests.sh`
## Unit testing
Using pytest
## Flake8
Using flake8
## Pylint
Fail under 8

Runs with flake8 plugin.

# Continuous Integration (CI)
Uses GitHub actions.

# Documentation
Uses Sphinx and GitHub pages.
https://jhmarlow.github.io

# Versioning 
Uses versioneer.
https://github.com/python-versioneer/python-versioneer

# Package Management 
Setuptools
https://setuptools.readthedocs.io/en/latest/userguide/quickstart.html
