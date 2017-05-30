from flask import Flask, render_template
app = Flask(__name__)


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