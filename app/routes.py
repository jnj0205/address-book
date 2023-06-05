from app import app
from flask import render_template, request, redirect, url_for, flash
from flask_login import login_user, logout_user, login_required, current_user
from app.forms import SignUpForm, LoginForm, AddForm


@app.route("/")
def index():
    return render_template('index.html')


@app.route("/signup", methods=["GET", "POST"])
def signup():
    form = SignUpForm()
    if form.validate_on_submit():
        print('yes!')
        first_name = form.first_name.data
        last_name = form.last_name.data
        first_name = form.first_name.data
        username = form.username.data
        email = form.email.data
        password = form.password.data
        flash(f"{username} has signed up!", "success")
        return redirect(url_for('index'))
    return render_template('signup.html', form=form)

@app.route("/login", methods=["GET", "POST"])
def login():
    form = LoginForm()
    if form.validate_on_submit():
        username = form.username.data
        password = form.password.data
        if user is not None and user.check_password(password):
            login_user(user)
            flash(f'{username} has successfully logged in', 'success')
            return redirect(url_for('index'))
        else:
            flash('Invalid username and/or password', 'danger')
            return redirect(url_for('login'))
    return render_template('/login.html', form=form)

@app.route("/logout")
def logout():
    logout_user()
    flash('You are logged out!')
    return render_template('logout.html', logout=logout)

@app.route('/contact', methods=["GET", "POST"])
def contact():
    form = AddForm()
    if request.method=="POST":
        if form.validate():
            pass
    return render_template('/contact.html', form=form)



    

