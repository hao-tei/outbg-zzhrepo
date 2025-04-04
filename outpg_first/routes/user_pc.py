from routes import app
from flask import render_template
@app.route("/")
@app.route("/index.html")
def home_page():
    return render_template("index.html", my_title="home")

@app.route("/login.html")
def login_page():
    return render_template("login.html", my_title="home")