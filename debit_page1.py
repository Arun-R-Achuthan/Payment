from flask import Flask
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
from random import random
from random import randint
from flask.ext.qrcode import QRcode
from flask_qr import QR


app = Flask(__name__)
app.config['SQLALCHEMY_DATABASE_URI'] = 'postgresql://postgres:a1c1h2u3t5h8an@localhost/debit_system'
db = SQLAlchemy(app)
QRcode(app)

import random
r = random.randint(1000,9999)
now = datetime.now()
stat= 'Not_Approved'
user1='student'
user2='client'
app.secret_key='super secret key'
login_manager = LoginManager()
login_manager.init_app(app)

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






class Client(db.Model):
	__tablename__ = "client"
	client_name=db.Column(db.String(50), nullable=False)
	client_no=db.Column(db.Integer, autoincrement=True, primary_key=True)
	password = db.Column(db.String(20),nullable=False)
	owner=db.Column(db.String(20), nullable=False)
	email_id = db.Column(db.String(30), nullable=False)
	reg_date=db.Column(db.String(30), nullable=False)
	status=db.Column(db.String(30), nullable=False)
	mobile_no=db.Column(db.String(15), nullable=False)

	def __init__(self,client_name,password,owner,email_id,reg_date,status,mobile_no):
		self.client_name = client_name
		self.password = password
		self.owner=owner
		self.email_id=email_id
		self.reg_date=reg_date
		self.status=status
		self.mobile_no=mobile_no
		
		
	def __repr__(self):
		return '<Clintname %r>' % self.client_name
		return '<Pass %r>' % self.password
		return '<Own %r>' % self.owner
		return '<email_id %r>' % self.email_id
		return '<regdate %r>' % self.reg_date
		return '<Status %r>' % self.status
		return '<Mobile %r>' % self.mobile_no

	def is_authenticated(self):
		return True
 
	def is_active(self):
		return True
 
	def is_anonymous(self):
		return False
 
	def get_id(self):
		return unicode(self.id)




class Logman(db.Model):
	__tablename__ = "login"
	email_id=db.Column(db.String(50), nullable=False,primary_key=True)
	usertype=db.Column(db.String(20), nullable=False)
	password=db.Column(db.String(20), nullable=False)

	def __init__(self,email_id,usertype,password):
		self.email_id =email_id
		self.usertype=usertype
		self.password=password
		
		
		
	def __repr__(self):
		return '<Email_id %r>' % self.email_id
		return '<Usertype %r>' % self.usertype
		return '<Password %r>' % self.password
		

	def is_authenticated(self):
		return True
 
	def is_active(self):
		return True
 
	def is_anonymous(self):
		return False
 
	def get_id(self):
		return unicode(self.id)




@app.route("/AGstudent_registration.html")
def student1():
	return render_template('AGstudent_registration.html', my_string="Wheeeee!", my_list=[0,1,2,3,4,5])

@app.route("/AGlogin.html")
def AGlogin():
	return render_template('AGlogin.html', my_string="Wheeeee!", my_list=[0,1,2,3,4,5])

@app.route("/AGclient_registration.html")
def client1():
	return render_template('AGclient_registration.html', my_string="Wheeeeel!", my_list=[0,1,2,3,4,5,6])

@app.route("/lock.html")
def logman():
	return render_template('lock.html', my_string="Wheeeeel!", my_list=[0,1,2,3,4,5,6])

@app.route("/AGForgot.html")
def Forgoten():
	return render_template('AGForgot.html', my_string="Wheeeeel!", my_list=[0,1,2,3,4,5,6])

@app.route("/QR")
def template_test():
    return render_template('Ascan_qr.html', my_string="Wheeeee!", my_list=[0,1,2,3,4,5])





@app.route('/student_reg', methods=['POST'])
def student_reg():
	user = User(request.form['admno'],request.form['name'],request.form['semester'],request.form['branch'],request.form['gender']
			   ,request.form['password'],r,request.form['email'],stat,now,request.form['cardtype'])
	if user.password== request.form['Repass']:
		db.session.add(user) 
		db.session.commit()
		log1 = Logman(request.form['email'],user1,request.form['password'])
		db.session.add(log1)
		db.session.commit() 
		return render_template('/AGlogin.html')
	else:
		return('Passwords dont match')


@app.route('/client_reg', methods=['POST'])
def client_reg():
	client = Client(request.form['name'],request.form['password'],request.form['owner_name'],request.form['email'],now
			   ,stat,request.form['mobile'])
	if client.password== request.form['Repass']:
		db.session.add(client) 
		db.session.commit()
		log2 = Logman(request.form['email'],user2,request.form['password'])
		db.session.add(log2)
		db.session.commit() 
		return render_template('/AGlogin.html')
	else:
		return('Passwords dont match')


@app.route('/log_man', methods=['POST'])
def log_man(): 
    email = request.form['email']
    password = request.form['password']
    result = db.engine.execute("select * from login where email_id = '" + email + "' and password= '" + password + "'") 
    names = []
    if result.rowcount > 0 :
        session[email]=email
        return render_template('/AGlock.html')
    else :
        return "false"    

@app.route("/neqQR.html")
def login1():
    email = request.args['email']
    result = db.engine.execute("select * from student where email = '" + email + "'")

    for row in result:
       sno = row["cardnumber"]
    return render_template('neqQR.html', sno = sno, my_list=[0,1,2,3,4,5])



if __name__ == '__main__':
	app.run(debug=True)

		











