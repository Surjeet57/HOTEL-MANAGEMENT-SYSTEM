from logging import fatal
from flask import Flask, render_template 
from flask_sqlalchemy import SQLAlchemy
from datetime import datetime



app = Flask(__name__)



@app.route("/hsm")
def hsm():
    return render_template ("hsm.html")

@app.route("/about")
def about():
    return  "about.html"

@app.route("/account")
def account():
    return "account.html"

@app.route("/booking")
def booking():
    return "booking.html" 

@app.route("/catering")
def catering():
    return "catering.html"

@app.route("/contact")
def contact():
    return "contact.html"    

@app.route("/directory")
def directory():
    return "directory.html"       

@app.route("/event")
def event():
    return "event.html"    

@app.route("/forget")
def forget():
    return "forget.html"

@app.route("/gallery")
def gallery():
    return "gallery.html"

@app.route("/GAMEBOOK")
def GAMEBOOK():
    return "GAMEBOOK.html" 

@app.route("/gservice")
def gservice():
    return "gservice.html"  

@app.route("/guest")
def guest():
    return "guest.html"
           
@app.route("/guestroom")
def guestroom():
    return "guestroom.html"   

@app.route("/login")
def login():
    return "login.html"

@app.route("/login1")
def login1():
    return "login1.html"    

@app.route("/manager")
def manager():
    return "manager.html"

@app.route("/manager1")
def manager1():
    return "manager1.html"

@app.route("/meetinghall")
def meetinghall():
    return "meetinghall.html"

@app.route("/new")
def new():
    return "new.html"

@app.route("/partyhal")
def partyhal():
    return "partyhal.html"

@app.route("/pool")
def pool():
    return "pool.html"

@app.route("/reception")
def reception():
    return "reception.html"  

@app.route("/renew")
def renew():
    return "renew.html"   

@app.route("/room")
def room():
    return "room.html"

@app.route('/rservice')
def rservice():
    return "rservice.html"      

@app.route('/staff')
def staff():
    return "staff.html"

@app.route('/trans')
def trans():
    return "trans.html" 

@app.route("/TRY")
def TRY():
    return "TRY.html"

@app.route("/VISIT")
def VISIT():
    return "VISIT.html" 

@app.route("/wedding_hall")
def wedding_hall():
    return "wedding_hall.html"

    

if __name__ == "__main__":
    app.run(debug=True , port=8000)    