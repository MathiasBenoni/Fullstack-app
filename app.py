from flask import *
from database_python import *
from password_hashing import prep_database

app = Flask(__name__)
app.secret_key = "NOPE"

@app.route("/")
def index():
    
    return render_template("index.html")

@app.route("/signup")
def signup():
    return render_template("signup.html")

@app.route("/login")
def login():
    return render_template("login.html")

from password_hashing import prep_database, test_password

@app.route("/logged_in", methods=["POST"])
def logged_in():
    username = request.form.get("username")
    password = request.form.get("password")
    password = password.encode()

    if test_password(username, password):
        result = database("SELECT privileges FROM users WHERE username = %s", (username,))
        session["username"] = username
        session["privileges"] = result[0][0]
        return redirect(url_for("index"))
    else:
        return render_template("login.html", error="Incorrect password")


@app.route("/signed_up", methods=["POST"])
def signed_up():
    username = request.form.get("new_username")
    password = request.form.get("new_password")

    prep_database(username, password.encode(), "NONE")

    return render_template("index.html")

@app.route("/logout")
def logout():
    session.clear()
    return redirect(url_for("index"))



if __name__ == "__main__":
    app.run(debug=True)
