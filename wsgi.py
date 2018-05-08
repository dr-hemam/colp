import os, sys
sys.path.append(os.path.abspath(os.path.join(os.path.dirname(__file__), '..')))

from colp import app
SECRET_KEY= 'never-guess'
DEBUG = True
DB_USER_NAME ='hassanemam'
DB_PASSWORD =''
DB_NAME = 'colp'
DB_HOST = os.getenv('IP', '0.0.0.0')
DB_URI ="mysql+pymysql://%s:%s@%s/%s" %(DB_USER_NAME, DB_PASSWORD, DB_HOST, DB_NAME)
SQLALCHEMY_DATABASE_URI = DB_URI
SQLALCHEMY_TRACK_MODIFICATIONS = True

if __name__ == "__main__":
	app.run(ssl_context='adhoc')
