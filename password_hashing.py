import bcrypt
from database_python import *

def hash_password(password):
    salt = bcrypt.gensalt()
    hashed_password = bcrypt.hashpw(password, salt)
    return hashed_password

def prep_database(user, password, privileges):
    hashed_password = hash_password(password)
    insert_database(user, hashed_password, privileges)

def test_password(user, password):
    pass