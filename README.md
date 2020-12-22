# Learning to draw

A project to learn a machine to draw with `Google Quick, Draw` Dataset.

## Setup and development

Install `poetry`, and `python 3.7+`. Then from the root directory run. (Poetry is a dependency/environment manager similar to pipenv). It helps you to keep the project python seperate from the rest of your the system.

    poetry install

This will install all project dependencies. Add new dependencies by running.
   
    poetry add <insert name of dependency>

This will add a new entry to the `pyproject.toml` file. To start jupyter notebook you have two options. Either activate the virtualenvironment that poetry has created or execute trough poetry directly.

    poetry shell
    jupyter lab
    # or
    jupyter notebook

Alternative:

    poetry run jupyter lab
    # or
    poetry run jupyter notebook


Checkout poetry documentation on: https://python-poetry.org/
