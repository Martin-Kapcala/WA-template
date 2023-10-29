from flask import Flask, render_template
from user import *

app = Flask(__name__)


@app.route("/")
def home():
    martin = User("Pepa")
    return martin.toString()

@app.route("/contact")
def contact():
    martin = User("Pepa")
    return render_template("index.html", user = martin)


if __name__ == '__main__':
   app.run(debug = True)