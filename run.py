import os
from flask import Flask, render_template


app = Flask(__name__)

@app.route("/")
def index():
    return render_template("index.html")

@app.route("/all")
def all():
    return render_template("all.html")

@app.route("/addrecipe")
def addrecipe():
    return render_template("addrecipe.html")

@app.route("/contact")
def contact():
    return render_template("contact.html")


if __name__ == "__main__":
    app.run(
        host=os.environ.get("IP", "0.0.0.0"),
        port=int(os.environ.get("PORT", "5000")),
        debug=True) ##Update to False before submitting##
