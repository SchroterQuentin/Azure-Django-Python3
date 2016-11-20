# Template for Django in python 3.4+ on Azure

## How to use it

Create directory for this project *myapp*

    $ mkdir myapp

Create the environment *env*

    $ python -m venv env

On linux 

    $ apt-get install python3.4-venv

Activate it

    $ env/Scripts/activate.bat 
    $ env/Scripts/Activate.ps1
    $ env/bin/activate

Install django on the virtualenv

    $ python -m pip install django

Create the project from this template

    $ django-admin startproject --template=https://github.com/SchroterQuentin/Azure-DjangoTemplate/archive/master.zip --extension=config myapp

Run the migrations and the server

    $ python manage.py migrate
    $ python manage.py runserver

## How to deploy on Azure

