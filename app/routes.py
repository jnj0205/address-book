from app import app, db
from flask import render_template, redirect, url_for, flash
from flask_login import login_user, logout_user, login_required, current_user
from app.forms import SignUpForm, LoginForm, ContactForm, EditForm
from app.models import Contact, User


@app.route("/")
def index():
    return render_template('index.html')



@app.route('/signup',methods=['GET','Post'])
def signup():
    form = SignUpForm()
    if form.validate_on_submit():
        first_name = form.first_name.data
        last_name = form.last_name.data
        username = form.username.data
        email = form.email.data
        password = form.password.data
        print(first_name)
        user_check = db.session.execute(db.select(User).where((User.username==username)|(User.email==email))).scalars().all()
        if user_check:
            flash('A user with that username and/or email already exists', 'danger')
            return redirect(url_for('signup'))
        new_user = User(first_name=first_name, last_name=last_name, username=username, email=email, password=password)
        print(new_user)
        db.session.add(new_user)
        db.session.commit()
        flash(f"{username} has signed up into secret book!", 'success')
        return redirect(url_for('index'))
    return render_template('signup.html', form=form)

@app.route("/login", methods=["GET", "POST"])
def login():
    form = LoginForm()
    if form.validate_on_submit():
        username = form.username.data
        password = form.password.data
        print(username, password)
        user = db.session.execute(db.select(User).where(User.username==username)).scalars().one_or_none()
        if user is not None and user.check_password(password):
            login_user(user)
            flash(f'{username} has successfully logged in', 'success')
            return redirect(url_for('index'))
        else:
            flash('Invalid username and/or password', 'danger')
            return redirect(url_for('login'))
    return render_template('/login.html', form=form)

@app.route('/addcontact', methods=["GET", "POST"])
@login_required
def addcontact():
    form = ContactForm()
    if form.validate_on_submit():
        first_name = form.first_name.data
        last_name = form.last_name.data
        phone = form.phone.data
        address = form.address.data
        email = form.email.data
        print(first_name, last_name, phone, *address)
        try:
            print(float(phone))
        except:
            flash('Numbers only!')
            return redirect(url_for('index'))
        new_contact = Contact(first_name=first_name,last_name=last_name,phone=phone,address=address, email=email)
        db.session.add(new_contact)
        db.session.commit()
        flash(f'{first_name} {last_name} has been added to your little secret book','danger-subtle')
        return redirect(url_for('index'))
    return render_template('contact.html',form=form)


@app.route('/logout')
@login_required
def logout():
    logout_user()
    flash('You are logged out.', 'primary')
    return redirect(url_for('index'))

@app.route('/viewcontacts',methods=['GET','Post'])

@login_required
def viewcontacts():
    contacts = db.session.execute(db.select(Contact).where(Contact.user==current_user.id)).scalars().all()
    return render_template('viewcontacts.html',contacts=contacts)


@app.route('/deletecontact',methods=['GET','Post'])
@login_required
def deletecontact():
    flash('Contact deleted')
    return redirect(url_for('index'))

@app.route('/search',methods=['GET','Post'])
@login_required
def search():
    return render_template('search.html')