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
        self.date_time = date_time
        self.type = type
        self.account = account
        self.currency = currency
        self.amount = amount
        self.category = category
        self.comment = comment
        # TODO: validation



@app.route("/home")
def home():
    return render_template("home.html", values=Transaction.query.all())


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
        print(datetime.now())
        tr = Transaction(datetime.now(), type, account, currency, int(amount), category, "Created by web form")
        db.session.add(tr)
        db.session.commit()
        return render_template("home.html", values=Transaction.query.all())

@app.route("/transaction")
def transaction():
    pass

if __name__ == "__main__":
    with app.app_context():
        db.create_all()
    app.run()

