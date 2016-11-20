# Template for Django in python 3.4+ on Azure

## How to use it

Create directory for this project *myapp*

    $ mkdir myapp

Create the environment *env*

    $ cd myapp
    $ python -m venv env

On linux if you don't have the packet install it

    $ apt-get install python3.4-venv

Activate it

    $ env/Scripts/activate.bat # cmd
    $ env/Scripts/Activate.ps1 # powershell
    $ env/bin/activate         # bash

Install django on the virtualenv

    (env) $ python -m pip install django

Create the project from this template

    (env) $ django-admin startproject --template=https://github.com/SchroterQuentin/Azure-Django-Python3/archive/custom.zip --extension=config,txt myapp .

Install packet for dev

    (env) $ pip install -r myapp/requirements/dev.txt

Run the migrations and the server

    (env) $ python manage.py migrate
    (env) $ python manage.py runserver

## Add library

In your environment, install your library with pip then

    (env) $ pip freeze > myapp/requirements/common.txt

## Deploy

By default the settings use in deployment is prod.py, you can change that by set DJANGO_SETTINGS_MODULE environment variable to another settings file.
