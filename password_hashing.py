import bcrypt
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
    print(hashed_password)
    print(password)

hash_password(b"Nice")
