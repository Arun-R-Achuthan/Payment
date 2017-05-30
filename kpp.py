from flask import Flask, render_template
from flask import render_template
from flask import request
from flask.ext.sqlalchemy import SQLAlchemy
from flask import redirect
from flask import flash
from flask import redirect
from flask import url_for
from flask.ext.login import LoginManager,login_user
from flask.ext.bcrypt import Bcrypt,check_password_hash
from flask import session
from datetime import datetime
from flask_qr import QR
from random import random
from flask.ext.qrcode import QRcode

app = Flask(__name__)
app.config['SQLALCHEMY_DATABASE_URI'] = 'postgresql://postgres:a1c1h2u3t5h8an@localhost/debit_system'
db = SQLAlchemy(app)
QRcode(app)

class User(db.Model):
    __tablename__ = "student"
    admissionnumber=db.Column(db.String(10), nullable=False)
    cardnumber=db.Column(db.Integer, autoincrement=True, primary_key=True)
    name=db.Column(db.String(30), nullable=False)
    semester=db.Column(db.String(10), nullable=False)
    branch=db.Column(db.String(25), nullable=False)
    gender=db.Column(db.String(10), nullable=False)
    password = db.Column(db.String(30),nullable=True)
    pin=db.Column(db.String(20), nullable=False)
    email = db.Column(db.String(30), nullable=False)
    status=db.Column(db.String(30), nullable=False)
    regdate=db.Column(db.String(30), nullable=False)
    balance=db.Column(db.BigInteger, nullable=False)

    def __init__(self,admissionnumber,name,semester,branch,gender,password,pin,email,status,regdate,balance):
        self.admissionnumber = admissionnumber
        self.name = name
        self.semester = semester
        self.branch=branch
        self.gender=gender
        self.password=password
        self.pin=pin
        self.email=email
        self.status=status
        self.regdate=regdate
        self.balance=balance
        
        
    def __repr__(self):
        return '<Admissionnumber %r>' % self.admissionnumber
        return '<Name %r>' % self.name
        return '<Semester %r>' % self.semester
        return '<Branch %r>' % self.branch
        return '<Gender %r>' % self.gender
        return '<Pass %r>' % self.password 
        return '<Pin %r>' % self.pin
        return '<Email %r>' % self.email
        return '<Status %r>' % self.status
        return '<Regdate %r>' % self.regdate
        return '<Bal %r>' % self.balance

    def is_authenticated(self):
        return True
 
    def is_active(self):
        return True
 
    def is_anonymous(self):
        return False
 
    def get_id(self):
        return unicode(self.id)


@app.route("/neqQR.html")
def login1():
    email = request.args['email']
    result = db.engine.execute("select * from student where email = '" + email + "'")

    for row in result:
       sno = row["cardnumber"]
    return render_template('neqQR.html', sno = sno, my_list=[0,1,2,3,4,5])




if __name__ == '__main__':
    app.run(debug=True)