from flask import render_template, request, redirect, url_for
from dgroup import app, db
from dgroup .models import Feedback


@app.route("/")
def home():
    return render_template("index.html")


# Made the request form should get the data and render the success page.
# - Create a JS popup to give the feedback that the informations was received.
@app.route('/submit', methods=['POST'])
def submit():
    if request.method == 'POST':
        fback = Feedback(
            client = request.form["client"],
            rating = request.form["rating"],
            comments = request.form["comments"]
        )
        db.session.add(fback)
        db.session.commit()
        return render_template("success.html")
    return render_template("index.html")