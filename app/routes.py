from app import app
from flask import render_template, request
from flask_login import login_user, logout_user, login_required, current_user
from app.forms import SignUpForm, LoginForm

@app.route("/")
def index():
    return render_template('index.html')


@app.route("/signup", methods=["GET", "POST"])
def signup():
    form = SignUpForm()
   
    return render_template('signup.html', form=form)

@app.route("/login")
def login():
    form = LoginForm()
    if request.method=="POST":
        if form.validate():
            pass
    return render_template('/login.html', form=form)

@app.route("/logout")
def logout():
    logout_user()
    flash('You are logged out!')
    return render_template('logout.html', logout=logout)

@app.route("/contact", methods=["GET", "POST"])
def add_contact():
    form = AddForm()
    return render_template('/contact.html', form=form)



    

