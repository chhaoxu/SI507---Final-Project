import os
from flask import Flask, render_template, session, redirect, url_for, request,flash
from flask_sqlalchemy import SQLAlchemy
from sqlalchemy import create_engine, Column, Integer, String, Float, Boolean, DECIMAL, Enum, Date, DateTime, Time, Text


app = Flask(__name__)
app.debug = True
app.use_reloader = True
app.config['SECRET_KEY'] = 'hard to guess string for app security adgsdfsadfdflsdfsj'
app.config['SQLALCHEMY_DATABASE_URI'] = 'sqlite:///./sample_books.db'
app.config['SQLALCHEMY_COMMIT_ON_TEARDOWN'] = True
app.config['SQLALCHEMY_TRACK_MODIFICATIONS'] = False

db = SQLAlchemy(app)
session = db.session

book_type=db.Table('book_type',
    db.Column('book_id',db.Integer(),db.ForeignKey('books.id')),
    db.Column('type_id',db.Integer(),db.ForeignKey('types.id')))

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
    bookId = db.Column(db.Integer, db.ForeignKey('books.id'), nullable=False)
    content = db.Column(db.Text, nullable=False, doc='content')
    rating = db.Column(db.SmallInteger, nullable=True)


class Type(db.Model):
    __tablename__= "types"
    id = db.Column(db.Integer(),primary_key=True)
    name = db.Column(db.String(64))
    books = db.relationship('Book', backref='Type')
    def __repr__(self):
        return self.name

class Rating(object):
    unit_name = "rating"
    def __init__(self, value):
        self.value = value

    def __str__(self):
        if(self.value >= 9):
            return str(self.value) + ' high scores'
        if(self.value < 6):
            return str(self.value) + ' low scores'

