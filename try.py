from flask import Flask
from flask import render_template
from flask import request
from flask.ext.sqlalchemy import SQLAlchemy
from flask import redirect
from flask import flash
from flask import redirect
from flask import url_for

app = Flask(__name__)
app.config['SQLALCHEMY_DATABASE_URI'] = 'postgresql://postgres:a1c1h2u3t5h8an@localhost/trial'
db = SQLAlchemy(app)

# Create our database model
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

# Set "homepage" to index.html
@app.route('/reg.html')
def index():
    return render_template('/reg.html')

# Save e-mail to database and send to success page
@app.route('/post_user', methods=['POST'])
def post_user():
    user = User(request.form['email'],request.form['password'],request.form['name'])
    db.session.add(user) 
    db.session.commit()
    return render_template('/login2.html')

@app.route('/login', methods=['GET','POST'])
def login():
    error = None
    if request.method == 'POST':
        if request.form['email'] != 'achuthan@gmail.com' or request.form['password'] != 'pass':
            error = 'Invalid Credentials. Please try again.'
        else:
            error = 'True'
    return render_template('reg.html', error=error)


#:@app.route('/del_user', methods=['delete'])
#:def del_user():
  #:  user = User(request.form['asd'],request.form['arun'],request.form['arn@gmail'])
    #:db.session.delete(user) 
    #:db.session.commit()
    #:return render_template('/login2.html')

if __name__ == '__main__':
    app.debug = True
    app.run()