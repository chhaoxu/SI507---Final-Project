import os
from flask import Flask, render_template, session, redirect, url_for, request,flash
from flask_sqlalchemy import SQLAlchemy
from sqlalchemy import create_engine, Column, Integer, String, Float, Boolean, DECIMAL, Enum, Date, DateTime, Time, Text
from flask_wtf import FlaskForm
from wtforms import StringField,SubmitField
from wtforms.validators import DataRequired

from wtforms import Form
from wtforms.fields import simple,core,html5
from wtforms import validators
from wtforms import widgets
app = Flask(__name__)
app.debug = True
app.use_reloader = True
app.config['SECRET_KEY'] = 'hard to guess string for app security adgsdfsadfdflsdfsj'
app.config['SQLALCHEMY_DATABASE_URI'] = 'sqlite:///./sample_books.sqlite'
app.config['SQLALCHEMY_COMMIT_ON_TEARDOWN'] = True
app.config['SQLALCHEMY_TRACK_MODIFICATIONS'] = False
# Set up Flask debug stuff
db = SQLAlchemy(app) # For database use
session = db.session # to make queries easy


book_type=db.Table('book_type',
    db.Column('book_id',db.Integer(),db.ForeignKey('books.id')),
    db.Column('type_id',db.Integer(),db.ForeignKey('types.id')))

class User(db.Model):
    __tablename__ = 'users'
    username = Column(String(32), index=True, nullable=False)
    id = db.Column(Integer, primary_key=True)

    password = db.Column(db.String(32), doc='password', nullable=False)
    comments = db.relationship('Comment', backref='users', cascade='all', lazy='dynamic')
    #isAdmin = db.Column(db.Boolean, doc='isadmin', default=False)
    #gender = db.Column(db.String(32), doc='gender', nullable=False)
    #comments = db.Column(db.String(32), db.ForeignKey('comments.id'), nullable=True)
    #comments = db.relationship('Comment', backref='User', cascade='all', lazy='dynamic')

class Book(db.Model):
    __tablename__ = 'books'

    id = db.Column(db.Integer, primary_key=True)
    name = db.Column(db.String(64))
    description = db.Column(db.Text, doc='book description', default='no description!', nullable=True)
    rating = db.Column(db.Float, doc='book rating', default=0)
    comments = db.relationship('Comment', backref='Book')

    types = db.relationship('Type', secondary=book_type, backref=db.backref('book',lazy='dynamic'),lazy='dynamic')
    type_id = db.Column(db.Integer, db.ForeignKey("types.id"))

class Comment(db.Model):

    __tablename__ = 'comments'

    id = db.Column(db.Integer, primary_key=True)
    #username = db.Column(db.String(32), db.ForeignKey('users.id'), nullable=True)
    bookId = db.Column(db.Integer, db.ForeignKey('books.id'), nullable=False)
    content = db.Column(db.Text, nullable=False, doc='content')
    rating = db.Column(db.SmallInteger, nullable=True)
    username = db.Column(db.String(32), db.ForeignKey('users.id'))

class Type(db.Model):
    __tablename__= "types"
    id = db.Column(db.Integer(),primary_key=True)
    name = db.Column(db.String(64))
    books = db.relationship('Book', backref='Type')
    def __repr__(self):
        return self.name


class LoginForm(Form):
    name = simple.StringField(
        label='username',
        validators=[
            validators.DataRequired(message='Username can not be empty!'),
            validators.Length(min=3,max=15,message='The name must be longer than%(min)d and be less than%(max)d')
        ],
        widget= widgets.TextInput(),
        render_kw= {'class':'form-control'}
    )

    pwd = simple.PasswordField(
        label= 'password',
        validators=[
            validators.DataRequired(message='The password can not be empty！'),
            validators.Length(min=6,message='The lenth must be longer than%(min)d'),
        ],
        widget= widgets.PasswordInput(),
        render_kw={'class':'form-control'}

    )

class RegisterForm(Form):
    name = simple.StringField(
        label='username',
        validators=[
            validators.DataRequired()
        ],
        widget=widgets.TextInput(),
        render_kw={'class':'form-control'},
        default='chhaoxu'
    )

    pwd = simple.PasswordField(
        label='password',
        validators = [
            validators.DataRequired()
        ],
        widget=widgets.PasswordInput(),
        render_kw={'class':'form-control'}
    )


    pwd_confirm =simple.PasswordField(
        label='password confirmation',
        validators = [
            validators.DataRequired(message='password can not be empty！'),
            validators.EqualTo('pwd','not equal!')
        ],
        widget = widgets.PasswordInput(),
        render_kw= {'class':'form-control'}
    )

class TrueForm(FlaskForm):
    type = StringField("Type",validators=[DataRequired()])
    book = StringField("Book",validators=[DataRequired()])
    comment = StringField("Comment", validators=[DataRequired()])
    submit = SubmitField("ADD")

def make_type():
    type1 = Type(name="Pets")
    db.session.add(type1)
    db.session.commit()
    book1 = Book(name="<<How to play with cats?>>", type_id=type1.id)
    db.session.add(book1)
    db.session.commit()
    comment1 = Comment(content="very good!", bookId=book1.id)
    db.session.add(comment1)
    db.session.commit()
    user1 = User(username='chhaoxu', password = '12345678')
    db.session.add(user1)
    db.session.commit()
from functools import wraps
def loginFirst(func):
    @wraps(func)
    def wrapper(*args, ** kwargs):
         return func(*args, ** kwargs)
    return wrapper

class Rating(object):
    unit_name = "rating"
    def __init__(self, value):
        self.value = value

    def __str__(self):
        if(self.value >= 9):
            return str(self.value) + ' high scores'
        if(self.value < 6):
            return str(self.value) + ' low scores'

if __name__ == '__main__':
    db.drop_all()
    db.create_all()
    make_type()
    app.run(debug=True)