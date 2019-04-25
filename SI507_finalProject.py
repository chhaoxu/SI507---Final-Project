import os
from SI507project_tools import *
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

import requests
from lxml import etree

'''app = Flask(__name__)
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

class User(db.Model):
    __tablename__ = 'users'
    username = Column(String(32), index=True, nullable=False)
    id = db.Column(Integer, primary_key=True)

    password = db.Column(db.String(32), doc='password', nullable=False)
    comments = db.relationship('Comment', backref='users', cascade='all', lazy='dynamic')


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
    username = db.Column(db.String(32), db.ForeignKey('users.id'))
class Type(db.Model):
    __tablename__= "types"
    id = db.Column(db.Integer(),primary_key=True)
    name = db.Column(db.String(64))
    books = db.relationship('Book', backref='Type')
    def __repr__(self):
        return self.name
'''
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


@app.route("/",methods=["GET","POST"])
def add_book():
    true_form = TrueForm()
    if true_form.validate_on_submit():
        type_name = true_form.type.data
        book_name = true_form.book.data
        book_content = true_form.comment.data
        type_query = Type.query.filter_by(name=type_name).first()
        if type_query:
            book_query = Book.query.filter_by(name=book_name).first()
            if book_query:
                new_content = Comment(bookId=book_query.id, content=book_content)
                db.session.add(new_content)
                db.session.commit()


            else:
                try:
                    new_book = Book(name=book_name, type_id=Type.query.filter_by(name=type_name).first().id)
                    db.session.add(new_book)
                    db.session.commit()
                    new_content = Comment(bookId=new_book.id, content=book_content)
                    db.session.add(new_content)
                    db.session.commit()
                except Exception as e:
                    flash("There is an error when add book!")
                    db.session.rollback()
        else:
            try:
                new_type = Type(name=type_name)
                db.session.add(new_type)
                db.session.commit()
                new_book = Book(name=book_name, type_id=new_type.id)
                db.session.add(new_book)
                db.session.commit()
                new_content = Comment(bookId=new_book.id, content=book_content)
                db.session.add(new_content)
                db.session.commit()
            except Exception as e:
                flash("1ERROR!")
                db.session.rollback()
    else:
        if request.method == "POST":
            flash("ERROR!")
    all_types = Type.query.all()
    return render_template("book_manage.html", all_types=all_types, form=true_form)



def spider():


    html = etree.HTML(requests.get("https://thegreatestbooks.org/").content)
    book_name = html.xpath('//div[@class="col"]/h4/a[1]/text()')
    name = html.xpath('//div[@class="col"]/h4/a[2]/text()')
    return book_name, name


book_list, name_list = spider()


@app.route('/bookRecommendation')
def hello_world():
    return render_template('bookRecommendation.html', book_list=book_list, name_list=name_list)


@app.route("/myBook",methods=["GET","POST"])
def my_book():

    all_types = Type.query.all()
    return render_template("myBook.html", all_types=all_types)



@app.route("/delete_type/<type_id>",methods=["GET","POST"])
def delete_type(type_id):
    type = Type.query.get(type_id)
    try:
        db.session.delete(type)
        db.session.commit()
    except Exception as e:
        flash(" ")
        db.session.rollback()
    return render_template('success.html')

@app.route("/delete_book/<book_id>",methods=["GET","POST"])
def delete_book(book_id):
    book = Book.query.get(book_id)
    try:

        db.session.delete(book)
        db.session.commit()
    except Exception as e:
        db.session.rollback()
        return render_template('fail.html')
    return render_template('success.html')

@app.route("/delete_comment/<comment_id>",methods=["GET","POST"])
def delete_comment(comment_id):
    comment = Comment.query.get(comment_id)
    try:
        db.session.delete(comment)
        db.session.commit()
    except Exception as e:
        flash(" ")
        db.session.rollback()
    return render_template('success.html')




if __name__ == '__main__':
    db.drop_all()
    db.create_all()
    make_type()
    app.run(debug=True)