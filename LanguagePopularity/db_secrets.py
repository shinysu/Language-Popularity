import os

DB_NAME = os.getenv("pyskills_db", 'popular_module')
USER_NAME = "root"
PASSWORD = os.getenv('db_password', "")
HOST = "localhost"
