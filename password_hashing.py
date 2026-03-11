import bcrypt
from database_python import *

def hash_password(password):
    salt = bcrypt.gensalt()
    hashed_password = bcrypt.hashpw(password, salt)
    return hashed_password

def prep_database(user, password, privileges):
    hashed_password = hash_password(password)
    insert_user_database(user, hashed_password, privileges)

def test_password(username, password):
    result = database("SELECT password FROM users WHERE username = %s", (username,))
    
    if not result:
        return False
    
    stored_hash = result[0][0].encode()
    return bcrypt.checkpw(password, stored_hash)