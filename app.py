from flask import *
from database_python import *
from password_hashing import prep_database

app = Flask(__name__)

@app.route("/")
def index():
    
    return render_template("index.html")

@app.route("/logged_in", methods=["POST"])
def test():

    username = request.form.get("username")
    password = request.form.get("password")

    prep_database(username, password.encode(), "NONE")

    return f"Welcome, {username}!"

if __name__ == "__main__":
    app.run(debug=True)