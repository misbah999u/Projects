# Travellite
A travel agency Django app using [Materialize CSS framework]  

The database was MySQL.

Steps to run this project
pip install django
django-admin startproject travel_agency
cd travel_agency
python manage.py startapp travel
Define the database schema in travel/models.py
python manage.py migrate
Register models in travel/admin.py
Define the URLs in travel/urls.py
Define the views in travel/views.py
Create the HTML templates in travel/templates
python manage.py runserver


