# Introduction
E-Learning, a scalable web application developed in Python (Django), was crafted with the aim of delivering an enriching user experience.

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
* Preliminary data indicates the presence of three user types designated for testing.
    * User (username=user, password=letmein123)
    * Professor (username=professor, password=letmein123)
    * Admin (username=admin, password=letmein123)
    * Visit http://127.0.0.1:8000/

# Compatibility
* Python 2.7
* Django 1.9
* SQLite, PostgreSQL, MySQL

# Notes
* The project utilizes the third-party library TinyMCE (https://www.tinymce.com/) under its own license.
  * The license can be found in static_files/js/tinymce.
* To enable contact/registration functionalities, it's necessary to include a settings_sensitive file in the source code.
* You'll discover a template for the settings_sensitive file in the source directory.
* Further details can be found at (https://docs.djangoproject.com/ja/1.9/topics/email/).
* Please note that this project is no longer actively maintained and should be utilized solely as a learning resource.
