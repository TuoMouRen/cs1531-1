from flask import Flask, session, render_template, request, redirect, g, url_for
from server import app
import csv
from csv_fun import *
import os


app.secret_key = os.urandom(24)
@app.route('/', methods=['GET', 'POST'])
def index():
    error123 = None
    if request.method == 'POST':
        session.pop('user', None)
        if request.form['password'] == '123' and request.form['username'] == 'admin': 
                  #set password and username!!!!!!!!!!
            session['user'] = request.form['username']
            return redirect(url_for('login'))
        else:
             error123 = 'Invalid Username or Password. Please try again!'
    return render_template('index.html',error=error123)


@app.route('/loggedin')
def login():
    if g.user:
        return render_template('hello.html')
    return redirect(url_for('index'))

#check the session before actually run any request!!!
@app.before_request
def before_request():
    g.user = None
    if 'user' in session:
        g.user = session['user']

@app.route('/logout')
def dropsession():
    session.pop('user', None)
    return 'Log out successful!'

    
    
#################################################

    
@app.route("/All_courses",methods=["GET","POST"])
def all_courses():
   courses = print_from_csv("all_courses.csv")
   return render_template("all_courses.html",courses=courses)

@app.route("/All_surveys",methods=["GET","POST"])
def all_surveys():
   return render_template("all_surveys.html")

@app.route("/All_questions",methods=["GET","POST"])
def all_questions():
   return render_template("all_questions.html")
   
   
@app.route("/Add_course",methods=["GET","POST"])
def add_courses():
   if request.method =="GET":
      return render_template("add_course.html")
   else:
      course_name = request.form["course_name"]
      write_to_csv("all_courses.csv",[course_name])
      return redirect(url_for("all_courses"))

@app.route("/Add_survey",methods=["GET","POST"])
def add_surveys():
   return render_template("add_survey.html")

@app.route("/Add_question",methods=["GET","POST"])
def add_questions():
   return render_template("add_question.html")
   
   
   
   
   
   
   

