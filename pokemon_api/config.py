import os
from decouple import config


class Config(object): 
    FLASK_ENV = config('FLASK_ENV')
    SECRET_KEY = config('SECRET_KEY')
    SQLALCHEMY_DATABASE_URI = config('DATABASE_URI')
    SQLALCHEMY_TRACK_MODIFICATIONS = False