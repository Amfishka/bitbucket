DB_HOST="localhost"
DB_NAME="dbname"
DB_USER="myuser"
DB_PASS="mypassword"

class Config(object):
    SECRET_KEY = 'devkey'
    SQLALCHEMY_DATABASE_URI = f"postgresql://{DB_USER}:{DB_PASS}@{DB_HOST}/{DB_NAME}"
    SQLALCHEMY_TRACK_MODIFICATIONS = False