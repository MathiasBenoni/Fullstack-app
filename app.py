from flask import *
from database import *

app = Flask(__name__)

@app.route("/")
def index():
    
    return render_template("index.html")

@app.route("/submit", methods=["POST"])
def test():
    
    username = request.form.get("username")
    password = request.form.get("password")
    print(username, password)
    return f"Welcome, {username}!"

if __name__ == "__main__":
    app.run(debug=True)