# Learning to draw

A project to learn a machine to draw with `Google Quick, Draw` Dataset.

## Setup and development

Install `poetry`, and `python 3.7+` for best experience. Then from the root directory run. (Poetry is a dependency/environment manager similar to pipenv). It helps you to keep the project python seperate from the rest of your the system, and helps you to install all requirements with ease. It also eliminates the problem of users running different versions.

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

## Steps to run the model
- Ensure to have the 'cloud.npz' dataset
- Ensure to have the dependencies installed using poetry as mentioned above
    1) Linear regression: Run the notebook entitled "LinearRegression.ipynb".
    2) Random forest regression: <br />
     - To train a model from scratch and test it, run the "Random_Forest Training and Testing.ipynb" notebook <br />
     - To load all existing trained models and to test them, run the "Random_Forest Testing all models.ipynb" notebook. (Check the link below to download all models of random forest)

## Link to the models
In this repository we have added the smaller models to test, however the larger models are uploaded to a google drive since the file is too large to be put on github. The link to all the random forest models is  here - https://drive.google.com/drive/folders/1yq6sXaYbL57noe6vibt3_U4DmV72bHPh?usp=sharing
- Unzip the files to the 'models/\ directory and test them using the 'Random_Forest Testing all models' notebook.
 
