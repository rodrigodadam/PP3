from flask import render_template
from dgroup import app, db
from dgroup .models import Feedback


@app.route("/")
def home():
    return render_template("index.html")