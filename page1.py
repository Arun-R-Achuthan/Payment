
from flask import Flask, render_template
from flask_sqlalchemy import SQLAlchemy

app = Flask(__name__)
app.config['SQLALCHEMY_DATABASE_URI'] = 'postgresql://postgres:a1c1h2u3t5h8an@localhost/User'
db=SQLAlchemy(app)

class User(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    username = db.Column(db.String(80), unique=True)
    email = db.Column(db.String(120), unique=True)

def __init__(self, username, email):
        self.username = username
        self.email = email

    def __repr__(self):
        return '<User %r>' % self.username

@app.route("/login.html")
def login1():
    return render_template('login2.html', my_string="Wheeeee!", my_list=[0,1,2,3,4,5])

@app.route("/reg.html")
def reg1():
    return render_template('reg.html', my_string="Wheeeee!", my_list=[0,1,2,3,4,5])

@app.route("/forgot.html")
def forgot1():
    return render_template('Forgot.html', my_string="Wheeeee!", my_list=[0,1,2,3,4,5])

if __name__ == '__main__':
    app.run(debug=True)