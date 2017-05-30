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

app = Flask(__name__)
app.config['SQLALCHEMY_DATABASE_URI'] = 'postgresql://postgres:a1c1h2u3t5h8an@localhost/trial'
db = SQLAlchemy(app)

login_manager = LoginManager()
login_manager.init_app(app)

 
class User(db.Model):
    __tablename__ = "login"
    password = db.Column(db.String(30),unique=True)
    name = db.Column(db.String(100),unique=True)
    email = db.Column(db.String(150), primary_key=True)

    def __init__(self, email,password,name):
        self.password = password
        self.name = name
        self.email = email


    def __repr__(self):
        return '<Pass %r>' % self.password
        return '<Name %r>' % self.name
        return '<E-mail %r>' % self.email

    def is_authenticated(self):
        return True
 
    def is_active(self):
        return True
 
    def is_anonymous(self):
        return False
 
    def get_id(self):
        return unicode(self.id)
  

@app.route("/logins.html")
def login1():
    return render_template('logins.html', my_string="Wheeeee!", my_list=[0,1,2,3,4,5])

@app.route("/regs.html")
def reg1():
    return render_template('regs.html', my_string="Wheeeee!", my_list=[0,1,2,3,4,5])

@app.route("/lock.html")
def lock():
    return render_template('lock.html', my_string="Wheeeee!", my_list=[0,1,2,3,4,5])

@app.route('/post_user', methods=['POST'])
def post_user():
    user = User(request.form['email'],request.form['password'],request.form['name'])
    db.session.add(user) 
    db.session.commit()
    return render_template('/logins.html')


@app.route('/login', methods=['POST'])
def login(): 
    user = User.query.filter_by(email=request.form['email']).first()
    if user.email == NULL:
        return render_template('/regs.html')
    else:
        session['logged_in'] = True
        return render_template('/lock.html')
        


if __name__ == '__main__':
    app.run(debug=True)