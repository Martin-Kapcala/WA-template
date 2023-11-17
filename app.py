from io import BytesIO #Metody potřebné pro práci se soubory
from flask import Flask, render_template, redirect, url_for, request, send_file
from flask_sqlalchemy import SQLAlchemy #Metody potřebné pro práci s databází
from user import *

app = Flask(__name__)

app.config['SQLALCHEMY_DATABASE_URI'] = 'sqlite:///db.sqlite3'
app.config['SQLALCHEMY_TRACK_MODIFICATIONS'] = False
db = SQLAlchemy(app)


#Hrátky s uživateli - vytvoření testovacích instancí objektu Uzivatel    
martin = User("Martin", None)
pepa = User("Pepa", "pepa@mail.cz")
ela = User("Ela", "ela@mail.cz")

#Pole uživatelů
users = [martin, pepa, ela]

#Načtení hlavní stránky
@app.route("/", methods = ["GET", "POST"])
def home():

    if request.method == 'POST':
        file = request.files['file']
        upload = Upload(filename=file.filename, data=file.read())
        db.session.add(upload)
        db.session.commit()
        return f'Uploaded: {file.filename}'
    
    return render_template("upload.html")

 
@app.route('/download/<upload_id>')
def download(upload_id):
    upload = Upload.query.filter_by(id=upload_id).first()
    return send_file(BytesIO(upload.data), 
                     download_name=upload.filename, as_attachment=True)

@app.route("/contact", methods = ["GET"])
def contact():
    resultNick = request.args.get("nick")

    return render_template("index.html", uzivatel = users[0], uzivatelNick = resultNick)

#Vypsání podrobných inforamcí uživatele na základě nicku
@app.route("/contact/<nick>")
def detail_contact(nick):
    for user in users:
       
        if user.get_nick() == nick:
            return render_template("detail.html", user = user)
            break
    
    return render_template("404.html", user = nick)
           
    

if __name__ == '__main__':
   app.run(debug = True)