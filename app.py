from flask import *
from database_python import *
from password_hashing import prep_database

app = Flask(__name__)

@app.route("/")
def index():
    
    return render_template("index.html")

@app.route("/signup")
def signup():
    return render_template("signup.html")

@app.route("/login")
def login():
    return render_template("login.html")

@app.route("/logged_in", methods=["POST"])
def logged_in():

    username = request.form.get("username")
    password = request.form.get("password")


    return render_template("index.html")


@app.route("/signed_up", methods=["POST"])
def signed_up():
    username = request.form.get("new_username")
    password = request.form.get("new_password")

    prep_database(username, password.encode(), "NONE")

    return render_template("index.html")

if __name__ == "__main__":
    app.run(debug=True)