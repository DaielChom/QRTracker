# Libraries
import os

# Class
class Config(object):
    SECRET_KEY = ''

# Developer class - Developer config
class DevelopmentConfig(Config):
    DEBUG = True

    SQLALCHEMY_DATABASE_URI = 'postgresql://postgres:1234@localhost/qrtracker'
    SQLALCHEMY_TRACK_MODIFICATIONS = False
