import os
from decouple import config


class Config(object): 
    FLASK_ENV = config('FLASK_ENV')
    SECRET_KEY = config('SECRET_KEY')
    DB_USER = config('DB_USER')
    DB_PASSWORD = config('DB_PASSWORD')
    SQLALCHEMY_DATABASE_URI = f'postgresql://{DB_USER}:{DB_PASSWORD}@localhost:5432/pokemon_db'
    SQLALCHEMY_TRACK_MODIFICATIONS = False