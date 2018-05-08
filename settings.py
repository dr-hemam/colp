import os

SECRET_KEY= 'never-guess'
SECURITY_PASSWORD_SALT = 'hard-to-guess'
DEBUG = True
DB_USER_NAME ='hemam'
DB_PASSWORD ='Hassan@81'
DB_NAME = 'colp'
DB_HOST = 'localhost'
DB_URI ="mysql+pymysql://%s:%s@%s/%s" %(DB_USER_NAME, DB_PASSWORD, DB_HOST, DB_NAME)
SQLALCHEMY_DATABASE_URI = DB_URI
SQLALCHEMY_TRACK_MODIFICATIONS = True



# mail accounts
MAIL_DEFAULT_SENDER = 'eng.hassanemam@gmail.com'

