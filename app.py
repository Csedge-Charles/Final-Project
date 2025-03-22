from flask import Flask, render_template, request, redirect, url_for
from tinydb import TinyDB, Query




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

print(findPass('charlesshao@gmail.com'))

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
        global username
        global email
        global password
        username = request.form['username']
        email = request.form['email']
        password = request.form['password']
        db.insert({'email': email, 'password':password})
        print(password)
        if func.checker(email):
            print("yes")
            return redirect('/', code=302)
        else:
            print("no")
            return render_template('create.html', wrong='Invalid email address', email=email, password=password, username=username)
    return render_template('create.html', wrong='')




        
    

@app.route('/password', methods=['POST', 'GET'])

def password():
    if request.method == 'POST':
        password = request.form['password']
        print(password)
        if request.form['password'] == findPass(email):
            global username
            username = 'Admin'
            return redirect('/home', code=302)
        else:
            return render_template('password.html', wrong='Password incorrect', reset=request.form['password'])
    return render_template('password.html', wrong='')

@app.route("/home", methods=['POST', 'GET'])

def home():
    if request.method == "POST":
        schedule = request.form['submit']
        print(schedule)
    return render_template("index.html")
if __name__ == '__main__':
    app.run(host='0.0.0.0', port=75, debug=True)