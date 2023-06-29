from app import db, login
from datetime import datetime
from werkzeug.security import generate_password_hash, check_password_hash
from flask_login import UserMixin




class User(db.Model,UserMixin):
    __tablename__='user'
    id = db.Column(db.Integer,primary_key=True)
    first_name = db.Column(db.String(25),nullable=False)
    last_name = db.Column(db.String(25),nullable=False)
    email = db.Column(db.String(75))
    username = db.Column(db.String(75),nullable=False,unique=True)
    password = db.Column(db.String(255),nullable=False)
    date_created = db.Column(db.DateTime,nullable=False,default=datetime.utcnow)
    contacts = db.relationship('Contact',backref='user')

    def __init__(self,**kwargs):
        super().__init__(**kwargs)
        self.password = generate_password_hash(kwargs['password'])
       

    def __repr__(self):
        return f'<User {self.id}|{self.username}>'
    
    def check_password(self,password_guess):
        return check_password_hash(self.password, password_guess)
    
class Contact(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    first_name = db.Column(db.String(25), nullable=False)
    last_name = db.Column(db.String(25), nullable=False)
    phone = db.Column(db.Numeric(10), nullable=False, unique=True)
    address = db.Column(db.String(50), nullable=True)
    date_created = db.Column(db.DateTime, nullable=False, default=datetime.utcnow)
    user_id = db.Column(db.Integer, db.ForeignKey('user.id'))

    def __init__(self, **kwargs):
        super().__init__(**kwargs)
        db.session.add(self)
        db.session.commit()


    def __repr__(self):
        return f"<Contact {self.id}|{self.last_name} {self.first_name}>"
    
@login.user_loader
def get_user(user_id):
    return db.session.get(User,user_id)