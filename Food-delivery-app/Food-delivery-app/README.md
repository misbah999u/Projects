# food-delivery-app

## Project setup
```
npm install
```

### Compiles and hot-reloads for development
```
npm run serve
```

### Compiles and minifies for production
```
npm run build
```

### Run your tests
```
npm run test
```

### Lints and fixes files
```
npm run lint
```

### Customize configuration
See [Configuration Reference](https://cli.vuejs.org/config/).

Install Python: Ensure that Python is installed on your system. You can download it from the official website: https://www.python.org/downloads/.

Install Django: After installing Python, install Django using pip, the Python package manager. Run the following command in your terminal or command prompt:

Copy code
pip install django
Create a Virtual Environment: It is recommended to create a virtual environment for your project. To create a virtual environment, run the following command in your terminal or command prompt:
bash
Copy code
python -m venv myenv
Replace myenv with the name of your virtual environment.

Activate the Virtual Environment: Activate the virtual environment by running the following command:
bash
Copy code
source myenv/bin/activate  # On Windows, use `myenv\Scripts\activate`
Install Dependencies: Install the required dependencies for the project by running the following command in your terminal or command prompt:
bash
Copy code
pip install -r requirements.txt
Run Migrations: Apply any pending migrations to the database by running the following command:
bash
Copy code
python manage.py migrate
Run the Development Server: Start the development server by running the following command:
bash
Copy code
python manage.py runserver
Access the Project: Open your web browser and navigate to http://127.0.0.1:8000/ to access the project.