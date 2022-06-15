from app import app
from flask import render_template


@app.route("/")
def hello():
    return render_template("index.html")


@app.route("/add/<int:first_number>/<int:second_number>")
def adding(first_number, second_number):
    res = first_number + second_number
    return render_template("result.html", variable=res)
