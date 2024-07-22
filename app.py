from flask import Flask, request, render_template
from flask_sqlalchemy import SQLAlchemy
from datetime import datetime

app = Flask(__name__)
app.config["SQLALCHEMY_DATABASE_URI"] = "sqlite:///transactions.sqlite3"
app.config["SQLALCHEMY_TRACK_MODIFICATIONS"] = False

db = SQLAlchemy(app)


class Transaction(db.Model):
    _id = db.Column("id", db.Integer, primary_key=True)
    date_time = db.Column(db.DateTime)
    type = db.Column(db.String(20))
    account = db.Column(db.String(20))
    currency = db.Column(db.String(3))
    amount = db.Column(db.Integer)
    category = db.Column(db.String(50))
    comment = db.Column(db.String(100))

    def __init__(self, date_time, type, account, currency, amount, category, comment):
        self.date_time = datetime.now()
        #to be continued


@app.route("/home")
def home():
    return "<h1>Hello!</h1> Main Page!"


@app.route("/input", methods=["POST", "GET"])
def input_form():
    if request.method == "GET":
        return render_template("input.html")
    if request.method == "POST":
        type = request.form["type"]
        account = request.form["account"]
        currency = request.form["currency"]
        amount = request.form["amount"]
        category = request.form["category"]
        return f"<h4>Transaction received</h4>{type, account, currency, amount, category}"


if __name__ == "__main__":
    app.run()
