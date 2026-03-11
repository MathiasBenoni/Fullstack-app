from os import error

from flask import *
from database_python import *
from password_hashing import prep_database
from google.oauth2 import id_token
from google.auth.transport import requests as grequests


app = Flask(__name__)
app.secret_key = "NOPE"

@app.route("/")
def index():
    
    return render_template("index.html")

@app.route("/google_login", methods=["POST"])
def google_login():
    token = request.json.get("token")
    try:
        idinfo = id_token.verify_oauth2_token(
            token,
            grequests.Request(),
            "303838859659-1aa84a95l3jibim48c7c918q5aq573cj.apps.googleusercontent.com"
        )
        session["username"] = idinfo["email"]
        session["privileges"] = "NONE"
        return jsonify({"success": True})
    except Exception as e:
        return jsonify({"success": False, "error": str(e)})


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

@app.route("/submit", methods=["POST"])
def submit():

    username = session.get("username")
    date = request.form.get("date")
    if not date:
        return render_template("index.html")
    else:
        print(date)
        print(username)

        insert_choaching_database(username, date)

        return redirect(url_for("index"))
        


if __name__ == "__main__":
    app.run(debug=True)
