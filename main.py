from flask import Flask, render_template, request, redirect
from datetime import date


app = Flask(__name__)
current_date = date.today()
current_year = current_date.year


@app.route("/")
def home():
    return render_template("index.html", current_year=current_year)


@app.route("/about")
def about():
    return render_template("about.html", current_year=current_year)


@app.route("/courses.html")
def courses():
    return render_template("courses.html", current_year=current_year)


if __name__ == "__main__":
    app.run(debug=True)
