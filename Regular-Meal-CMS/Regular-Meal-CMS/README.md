Regular Meal CMS contains only professional and reliable software technologies like Python Django, Django REST framework and JWT social authentication. Now you can forget about specifically and expensive website templates and hard to fix SQL errors! Furthermore, Regular Meal CMS provide localization and internationalization features.

# Easy restaurant management setup
1. Clone the GitHub repo in a separate folder:
```
git clone https://github.com/misbah999u/Projects/Regular-Meals-CMS.git
```
2. Go to the main directory of the project:
```
cd Regular-Meals-CMS
```
3. Install dependencies:
```
pip install -r requirements.txt
```
4. Create database migrations for each app:
```
python manage.py makemigrations menu
python manage.py makemigrations delivery
python manage.py makemigrations client
python manage.py makemigrations subscription
python manage.py makemigrations
```
5. Apply database migrations:
```
python manage.py migrate
```
6. Create first superuser (admin profile), remember your credentials:
```
python manage.py createsuperuser
```
7. Run server on the localhost:
```
python manage.py runserver
```
8. Now open an admin panel by visit URL `127.0.0.1:8000/en/admin/`.
9. Enter your superuser credentials and press "Log in" button.
10. ### Congratulations, you've done with the CMS setup!
*Now you can create new dishes and menus, categories, delivery regimes and subscription types.*

