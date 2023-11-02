from flask import Flask, render_template, redirect, url_for, request
from user import *

app = Flask(__name__)

martin = User("Martin", None)
pepa = User("Pepa", "pepa@mail.cz")
ela = User("Ela", "ela@mail.cz")
users = [martin, pepa, ela]

@app.route("/")
def home():
    
    return redirect(url_for("contact"))

@app.route("/contact", methods = ["GET"])
def contact():
    return render_template("index.html", uzivatel = pepa)

@app.route("/contact/<nick>")
def detail_contact(nick):
    for user in users:
       
        if user.get_nick() == nick:
            return render_template("detail.html", user = user)
            break
    
    return render_template("404.html", user = nick)
           
    

if __name__ == '__main__':
   app.run(debug = True)