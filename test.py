import bcrypt
pw = b'GeekPassword'
s = bcrypt.gensalt()
h = bcrypt.hashpw(pw, s) # Hash password
entered_pw = b'GeekPassword'

if bcrypt.checkpw(entered_pw, h):
    print(entered_pw)
    print(h)
    print(bcrypt.hashpw(entered_pw, h))
    print("Password match!")
else:
    print("Incorrect password.")