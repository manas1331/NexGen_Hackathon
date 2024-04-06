from flask import Flask, render_template, redirect, request, session, url_for
from pymongo import MongoClient
import re
import os
import threading
app = Flask(__name__)

client = MongoClient("mongodb://localhost:27017/")
db = client['userdb']
users = db['users']

@app.route('/register', methods=['POST'])
def register():
    username = request.form['username']
    email=request.form['email']
    password = request.form['password']
    
    user = {'username': username, 'password':password, 'email': email}
    users.insert_one(user)
    return redirect(url_for('hello_world'))
    
def login():
    if request.method == 'POST':
        username = request.form['username']
        password = request.form['password']

        account = users.find_one({'username': username})
        if account:
            
            if account['password'] == password:
                session['loggedin'] = True
                session['id'] = str(account['_id'])
                session['username'] = account['username']
                print("Session ", session)
                return redirect(url_for('hello'))

        print('Invalid user credentials')
        return redirect(url_for('hello2'))
    else:
        return render_template('Login.html')
@app.route("/Login.html")
def hello_world(name=None):
    return render_template("Login.html")

"""@app.route("/")
def hello(name=None):
    return render_template("index.html")"""

@app.route("/")
def hello2(name=None):
    return render_template("index1.html")

@app.route("/subjects.html")
def hello3(name=None):
    return render_template("subjects.html")

@app.route("/courses.html")
def hello4(name=None):
    return render_template("courses.html")

@app.route("/teachers.html")
def hello5(name=None):
    return render_template("teachers.html")

@app.route("/teacher_deepu.html")
def hello6(name=None):
    return render_template("teacher_deepu.html")

@app.route("/teacher_luke.html")
def hello7(name=None):
    return render_template("teacher_luke.html")

@app.route("/teacher_rama.html")
def hello8(name=None):
    return render_template("teacher_rama.html")

@app.route("/teacher_sham.html")
def hello9(name=None):
    return render_template("teacher_sham.html")

@app.route("/teacher_john.html")
def hello10(name=None):
    return render_template("teacher_john.html")

@app.route("/teacher_lakshmi.html")
def hello11(name=None):
    return render_template("teacher_lakshmi.html")

@app.route("/Quiz/quiz.html")
def hello12(name=None):
    return render_template("quiz.html")

@app.route("/profile.html")
def hello13(name=None):
    return render_template("profile.html")

@app.route("/playlist.html")
def hello14(name=None):
    return render_template("playlist.html")

@app.route("/update.html")
def hello15(name=None):
    return render_template("update.html")

if __name__ == '__main__':
    app.run(debug = True)

