
# A very simple Flask Hello World app for you to get started with...

from flask import Flask, render_template, request, url_for, redirect
from flask_sqlalchemy import SQLAlchemy

app = Flask(__name__)
app.config["DEBUG"] = True

SQLALCHEMY_DATABASE_URI = "mysql+mysqlconnector://{username}:{password}@{hostname}/{databasename}".format(
    username="joaopaulomcc",
    password="123zxc456asd",
    hostname="joaopaulomcc.mysql.pythonanywhere-services.com",
    databasename="joaopaulomcc$comments",
)

app.config["SQLALCHEMY_DATABASE_URI"] = SQLALCHEMY_DATABASE_URI
app.config["SQLALCHEMY_POOL_RECYCLE"] = 299
app.config["SQLALCHEMY_TRACK_MODIFICATIONS"] = False

db = SQLAlchemy(app)

comments = []

@app.route('/', methods=("GET", "POST"))
def index():

    if request.method == "GET":
        return render_template("main_page.html", comments=comments)

    comments.append(request.form["contents"])

    return redirect(url_for("index"))
