from flask import *

app = Flask(__name__)

@app.route("/")
def index():

    return "True"


if __name__ == "__main__":
    app.run(debug=True)