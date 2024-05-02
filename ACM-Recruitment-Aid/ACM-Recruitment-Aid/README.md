This is a Basic recruitment Python/Django based web application which aims to add , delete and update job posts. The project also  includes user registration, login and logout functionality. Where the User can add  their own Job Posts and view all available jobs in the database. As well as remove  or edit his/her own post.

## Installation
1. To Clone this  repository, open your terminal and type: `git clone https://github.com/misbah999u/Projects/ACM-Recruitment-Aid.git
2. First and Foremost , install the requirements  using pip:
$ `pip install -r requirements.txt`
3. Create the virtualenv using the following command:
$ python -m venv myenv
4. Activate your virtual environment by running in terminal :
- Windows: `.\myenv\Scripts\activate`
5. Make sure to apply all migrations  for Django app:
python manage.py makemigrations admin
python manage.py makemigrations auth
python manage.py makemigrations contenttypes
python manage.py makemigrations recruit
python manage.py makemigrations sessions
6. Apply database migrations:
python manage.py migrate
7. Create first superuser (admin profile), remember your credentials:
```
python manage.py createsuperuser
```
8. Run server on the localhost:
```
python manage.py runserver
```
9. . Now open an admin panel by visit URL `127.0.0.1:8000/en/admin/`.

You will see a login page, enter your username and password which you have created during creating super user.
