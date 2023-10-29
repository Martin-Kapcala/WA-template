from flask import Flask
from user import *

app = Flask(__name__)


@app.route("/")
def home():
    martin = User("Pepa")
    return martin.toString()

if __name__ == '__main__':
   app.run(debug = True)