from flask import Flask
from user import *

app = Flask(__name__)


@app.route("/")
def home():
    martin = User("Martin")
    return martin.toString()