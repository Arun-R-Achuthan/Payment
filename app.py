from flask import Flask
from flask import render_template
from flask import request
from flask.ext.sqlalchemy import SQLAlchemy
from flask import redirect

app = Flask(__name__)
app.config['SQLALCHEMY_DATABASE_URI'] = 'postgresql://postgres:a1c1h2u3t5h8an@localhost/main'
db = SQLAlchemy(app)

# Create our database model
class User(db.Model):
    __tablename__ = "users"
    username = db.Column(db.String(80), primary_key=True)
    email = db.Column(db.String(120), unique=True)

    def __init__(self, email,username):
        self.username=username
        self.email = email

    def __repr__(self):
        return '<E-mail %r>' % self.email
        return '<User %r>' % self.username

# Set "homepage" to index.html
@app.route('/abc.html')
def index():
    return render_template('/abc.html')

# Save e-mail to database and send to success page
@app.route('/post_user', methods=['POST'])
def post_user():
    user = User(request.form['username'],request.form['email'])
    db.session.add(user) 
    db.session.commit()
    return render_template('/login2.html')

if __name__ == '__main__':
    app.debug = True
    app.run()