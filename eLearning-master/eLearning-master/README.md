# Introduction
E-Learning, a scalable web application developed in Python (Django), was crafted with the aim of delivering an enriching user experience.
<img src="https://github.com/Bcoolie/eLearning/blob/master/users/static_in_users/static_files/img/home-sample.png" width="720" height="400">
# Installation
If you're utilizing virtualenv, adhere to these instructions to download and execute the e-learning application within this directory:

    $ git clone https://github.com/misbah999u/Projects/eLearning.git
    $ cd eLearning
    $ python -m pip install -U PySide
    $ py -m pip install numpy 
    $ pip install --user virtualenv
    $ python -m virtualenv venv
    $ -cd venv
    $ cd Scripts
    $ .\activate
    $ python -m venv env
    $ virtualenv venv
    $ source ./venv/bin/activate
    $ pip install -r requirements
    $ python manage.py migrate
    $ python manage.py runserver

* Initial data supports 3 types of users for testing purposes:
    * User (username=user, password=letmein123)
    * Professor (username=professor, password=letmein123)
    * Admin (username=admin, password=letmein123)
    * Visit http://127.0.0.1:8000/

# Compatibility
* Python 2.7
* Django 1.9
* SQLite, PostgreSQL, MySQL

# Notes
* This project uses third-party library tinymce (https://www.tinymce.com/) with own licence
    * Licence is located in static_files/js/tinymce
* If you wish to use contact/registration features you will need to add settings_sensitive file in source
*	You can find template for settings sensitive in source directory
*	For more information visit (https://docs.djangoproject.com/ja/1.9/topics/email/)
*	This project is no longer maintained, and should only serve as a learning example
