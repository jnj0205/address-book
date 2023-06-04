from app import app
from flask import render_template
from flask_login import login_user, logout_user, login_required, current_user
from app.forms import SignUpForm, LoginForm

@app.route("/")
def index():
    return render_template('index.html')


@app.route("/signup")
def signup():
    form = SignUpForm()
    return render_template('/signup.html', form=form)

@app.route("/login")
def login():
    form = LoginForm
    return render_template('/login.html', form=form)

@app.route("/logout")
def logout():
    return render_template('/logout.html', logout=logout)



    

