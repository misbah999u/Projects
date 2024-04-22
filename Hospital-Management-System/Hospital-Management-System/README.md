# Hospital-Management-System
It is a web application for Hospital Management in which administrative staffs of hospital can manage the patient information, assign them medicines,diagnostics etc.
and can also generate the bill for patient when patient wish to discharge.

### Requirements

1. Flask

### How To use:
1. Clone the project
2. Install flask in the directory where cloned. Using command "pip install flask" in cmd.
3. Then run the following commands in cmd to run the project
  (i).   set Flask_APP= flaskr
  (ii).  set Flask_ENV= development
  (iii). flask run
4. Visit url "http://127.0.0.1:5000/auth/login" to see the webpage running.
5. Default Username and Password for the authentication is admin and password respectively.

Here are the steps to run this project:

Make sure you have Python installed on your system. You can download it from the official website.
Create a new directory for your project and navigate to it in your terminal or command prompt.
Create a new file in this directory called app.py and paste the code provided in the context into this file.
Create a new file in the same directory called schema.sql and add the SQL commands to create the necessary tables for the application.
Create a new file in the same directory called requirements.txt and add the following dependencies:
Copy code
Flask==2.0.1
click==8.0.1
Install the dependencies by running pip install -r requirements.txt in your terminal or command prompt.
Create a new file in the same directory called config.py and add the following code to configure the database connection:
Copy code
import os

basedir = os.path.abspath(os.path.dirname(__file__))

DATABASE = os.path.join(basedir, 'app.db')
Modify the app.py file to import the config module and use the DATABASE variable to configure the database connection.
Run the application by executing python app.py in your terminal or command prompt.
Initialize the database by executing flask init-db in your terminal or command prompt.
That's it! You should now be able to run the application and interact with the database.



