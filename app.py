from flask import Flask, render_template, request, redirect, url_for
app = Flask(__name__)
@app.route("/")
def home():
    return "Hello World"
if __name__ == '__main__':
    app.run(host='0.0.0.0', port=75, debug=True)