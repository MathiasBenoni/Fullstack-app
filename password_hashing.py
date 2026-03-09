import bcrypt
from database_python import *

pw = b'GeekPassword'
s = bcrypt.gensalt()
h = bcrypt.hashpw(pw, s)
entered_pw = b'GeekPassword'

if bcrypt.checkpw(entered_pw, h):
    print("Password match!")
else:
    print("Incorrect password.")

def hash_password(password):
    salt = bcrypt.gensalt()
    hashed_password = bcrypt.hashpw(password, salt)
    return hashed_password

def prep_database(user, password, privileges):
    hashed_password = hash_password(password)
    insert_database(user, hashed_password, privileges)

prep_database("test", b"123", "NONE")