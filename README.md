# Student Information System Backend
A backend for Secondary Schools Student Profile and results system.


###Introduction
This project is to demonstrate how one can create an API backend using python and Django.
It is a school project in which student's data are recorded through the django Admin and 
They can be viewed by students by either the frontend or phone app.

###Getting it local
To download the project, run

`git clone https://github.com/herfingerscancode/StudentInformationSystemBackend.git`

then navigate to the project folder 

`cd StudentInformationSystemBackend`

###VirtualEnv Setup
For better results, it is advised to create a virtual environment for this project. 
To create a virtual env run

`python -m venv venv`

in the root of the project

To activate it run

`source venv/bin/activate` for linux

`cd venv/Scripts` then `activate` for windows

###Requirements
The project uses django basic requirements and django rest framework
All requirements are found in the requrements.txt file.

To install all requirements, run

`pip install -r requirements.txt`

(make sure your virtual env is activated)

###Setting up the Project
You can setup the database by initially running 

`python manage.py makemigrations` (Assuming migrations files are not included with the commit)

then

`python manage.py migrate`

You can then create the admin credentials for the django admin
run 

`python manage.py createsuperuser`


###Running the project
The project server can be run by simply running 

`python manage.py runserver`

The project server will, by default run on port 8000.
To change the port simply include it in the command

`python manage.py runserver 6000` 
Changes the running port to 6000


###Deployment
The deployment of the project depends on where you want to deploy it.
In our case we are going to deploy it in Heroku
