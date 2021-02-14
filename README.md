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

## Link to the models
In this repository we have added the smaller models to test, however the larger models are uploaded to a google drive since the file is too large to be put on github. The link to all the random forest models is  here - https://drive.google.com/drive/folders/1yq6sXaYbL57noe6vibt3_U4DmV72bHPh?usp=sharing
- Unzip the files to the models/ directory and test them using the "Random_Forest Testing all models" notebook.
 
