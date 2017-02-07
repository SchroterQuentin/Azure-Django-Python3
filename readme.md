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
    $ source env/bin/activate  # bash

Install django on the virtualenv

    (env) $ python -m pip install django

Create the project from this template

    (env) $ django-admin startproject --template=https://github.com/SchroterQuentin/Azure-DjangoTemplate/archive/master.zip --extension=config myapp .

Run the migrations and the server

    (env) $ python manage.py migrate
    (env) $ python manage.py runserver

## How to deploy on Azure

First add the host/domain names that this Django site can serve to ALLOWED_HOST in the settings file.

### With git local deployment

Put yourself in the directory where there is the web.config file

    $ git init
    $ git add .
    $ git commit -m "first commit"

Add the remote git and push

    $ git remote add azure https://*user*@*appname*.scm.azurewebsites.net:443
    $ git push azure master

You will now see the stack of deployment after that your site is ready

### With github deployment

Put yourself in the directory where there is the web.config file

    $ git init
    $ git add .
    $ git commit -m "first commit"
    $ git push origin master

If it's the first time wait the necessary time for the server to create the environment and install the requirements.  
Now your site is ready


## Add library

Activate your environment, install your library with pip then

    (env) $ pip freeze > requirements.txt

# Custom template with debug-toolbar and some settings

Change the branch from master to custom on this repo to see the README. The main change is the URL of the repo when you create the django project.

    $ django-admin startproject --template=https://github.com/SchroterQuentin/Azure-Django-Python3/archive/custom.zip --extension=config myapp .

And the requirements you must install after create the project
