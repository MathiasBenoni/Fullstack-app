from flask import *
from database_python import *
from password_hashing import prep_database
from google.oauth2 import id_token
from google.auth.transport import requests as grequests


app = Flask(__name__)
app.secret_key = "NOPE"

@app.route("/")
def index():
    
    test = database("SELECT id, username, privileges FROM users;")
    


    return render_template("index.html", test=test)

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
    email = request.form.get("email")
    password = request.form.get("password")
    password = password.encode()

    if test_password(email, password):
        result = database("SELECT privileges FROM users WHERE username = %s", (email,))
        session["username"] = email
        session["privileges"] = result[0][0]
        return redirect(url_for("index"))
    else:
        return render_template("login.html", error="Incorrect password")


@app.route("/signed_up", methods=["POST"])
def signed_up():
    username = request.form.get("new_email")
    password = request.form.get("new_password")

    prep_database(username, password.encode(), "NONE")

    return render_template("index.html")

@app.route("/logout")
def logout():
    session.clear()
    return redirect(url_for("index"))

@app.route("/submit", methods=["POST"])
def submit():

    email = session.get("username")
    date = request.form.get("date")
    if not date:
        return render_template("index.html")
    else:
        print(date)
        print(email)

        insert_choaching_database(email, date)

        return redirect(url_for("index"))
        
@app.route("/approve")
def send_to_approve():
    rows = database("SELECT username, date FROM coaching")
    return render_template("approve.html", rows=rows)

@app.route("/approved", methods=["POST"])
def approved():
    email = request.form.get("email")
    date = request.form.get("date")
    
    database("DELETE FROM coaching WHERE username = %s AND date = %s", (email, date))
    return render_template("index.html")

@app.route("/manage_people")
def manage():
    rows = database("SELECT username, privileges FROM users")



    return render_template("manage_people.html", rows=rows)



@app.route("/update_privileges", methods=["POST"])
def update_privileges():
    username = request.form.get("username")
    privileges = request.form.get("privileges")

    database(
        "UPDATE users SET privileges = %s WHERE username = %s",
        (privileges, username)
    )

    return redirect(url_for("manage"))


if __name__ == "__main__":
    app.run(debug=True)
