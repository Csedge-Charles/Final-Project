from flask import Flask, render_template, request, redirect, url_for
from tinydb import TinyDB, Query
import random

url_list = ['a', 'b', 'c', 'd', 'e', 'f', 'g', 'h', 'i', 'j', 'k', 'l', 'm', 'n', 'o', 'p', 'q', 'r', 's', 't', 'u', 'v', 'w', 'x', 'y', 'z', '1', '2', '3', '4', '5', '6', '7', '8', '9', '0']





db = TinyDB("./db.json")
personal = Query()

import func



def getEmail():
    EmailList = []
    for i in db.all():
        EmailList.append(i['email'])
    return EmailList

def findPass(email):
    for i in db.all():
        if i['email'] == email:
            return str(i['password'])
        
def findKey(email):
    for i in db.all():
        if i['email'] == email:
            return str(i['key'])
        
def findActivity(key):
    for i in db.all():
        if i['key'] == key:
            return str(i['activity'])

app = Flask(__name__)

@app.route('/', methods=['POST', 'GET'])

def success():
    if request.method == 'POST':
        global email
        if request.form['submit'] == 'Create account':
            return redirect('/create-account', code=302)
        if request.form['email'] in getEmail():
            email = request.form['email']
            return redirect('/password', code=302)
        return render_template('email.html', reject='Email does not exist', email=request.form['email'])
    return render_template('email.html', reject='')

@app.route("/create-account", methods=['POST', 'GET'])
def create():
    if request.method == 'POST':
        global email
        global password
        global key
        global activity
        global updater
        
        updater = ""
        activity = updater
        email = request.form['email']
        password = request.form['password']
        if email not in getEmail():
            key = f'{random.choice(url_list)}{random.choice(url_list)}{random.choice(url_list)}{random.choice(url_list)}{random.choice(url_list)}{random.choice(url_list)}{random.choice(url_list)}{random.choice(url_list)}{random.choice(url_list)}{random.choice(url_list)}{random.choice(url_list)}{random.choice(url_list)}{random.choice(url_list)}{random.choice(url_list)}{random.choice(url_list)}{random.choice(url_list)}{random.choice(url_list)}{random.choice(url_list)}{random.choice(url_list)}{random.choice(url_list)}{random.choice(url_list)}{random.choice(url_list)}{random.choice(url_list)}{random.choice(url_list)}{random.choice(url_list)}{random.choice(url_list)}{random.choice(url_list)}{random.choice(url_list)}{random.choice(url_list)}{random.choice(url_list)}{random.choice(url_list)}{random.choice(url_list)}{random.choice(url_list)}{random.choice(url_list)}{random.choice(url_list)}'
            db.insert({'email': email, 'password':password, 'key': key, "activity": activity})
            return redirect('/', code=302)
        else:
            if email in getEmail():
                print(getEmail())
                return render_template('create.html', wrong='username is already used', email=email, password=password)
    return render_template('create.html', wrong='')




        
    

@app.route('/password', methods=['POST', 'GET'])

def password():
    global inputs
    if request.method == 'POST':
        password = request.form['password']
        if request.form['password'] == findPass(email):
            inputs = []
            key = findKey(email)
            return redirect(url_for('home', key=key), code=302)
        else:
            return render_template('password.html', wrong='Password incorrect', reset=request.form['password'])
    return render_template('password.html', wrong='')

@app.route("/home/<key>", methods=['POST', 'GET'])



def home(key):
    global updater
    inputs = findActivity(key).split()
    if request.method == "POST":
        updater = findActivity(key)
        schedule = request.form['submit']
        updater += f" {schedule}"
        db.update({"activity": updater}, personal.email == email)
        inputs.append(schedule)
        return render_template("index.html", user=inputs)
    return render_template("index.html", user=inputs)
if __name__ == '__main__':
    app.run(host='0.0.0.0', port=75, debug=True)