# Python coding challenge - Pokemon API 
This api is created using the Flask python framework and other libraries like SQLAlchemy and Marshmallow. The reason why I used Flask it is a very lightweight framework and it works really well with small projects like this
***
# How to setup the project
These are the steps to set it up assuming you have python3 installed and also postgreSQL all setup. Clone the repository and open the terminal in the root folder of the project(using a venv is recomended).
During the steps we will use a database user <your_db_user> (default is postgres)
- STEP 1: $ ```pip install -r requirements.txt```
- STEP 2: $``` psql -U  <your_db_user>```
then type the password for your user. Now u should be inside psql
- STEP 3: $ ```CREATE DATABASE pokemon_db;```
then press CTRL+C to go back to the root directory terminal
-STEP 4 : Add a .env file in the root directory with this information:
```
FLASK_ENV = 'development'
SECRET_KEY = '4t-rHCKLuiq1k0Svv2O7PQ'
DB_USER = '<your_db_user>'
DB_PASSWORD = '<your_db_password>'
```
Please replace db user and db password according to your postgreSQL setup

- STEP 5: $ ```cd ./pokemon_api```
- STEP 6: $```python app.py run```

Now the server is hopefully successfully all that is left is to go the the homepage of the web server http://localhost:5000 and follow the instruction of how the api works using a software like Postman which is used for testing the API.
***
***Thank you for the opportunity. I hope you like my project*** 