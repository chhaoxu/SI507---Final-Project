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

    
def spider():


    html = etree.HTML(requests.get("https://thegreatestbooks.org/").content)
    book_name = html.xpath('//div[@class="col"]/h4/a[1]/text()')
    name = html.xpath('//div[@class="col"]/h4/a[2]/text()')
    return book_name, name


book_list, name_list = spider()


@app.route('/bookRecommendation')
def hello_world():
    return render_template('bookRecommendation.html', book_list=book_list, name_list=name_list)

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
