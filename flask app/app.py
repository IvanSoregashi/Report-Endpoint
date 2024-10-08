from flask import Flask, request, render_template, redirect, url_for
from flask_restful import Api
from datetime import datetime

from db import db
from models.transaction import TransactionModel
from resources.last_transaction import LastTransaction
from resources.transaction import Transaction

app = Flask(__name__)
app.config['DEBUG'] = True
app.config["SQLALCHEMY_DATABASE_URI"] = "sqlite:///transactions.sqlite3"
app.config["SQLALCHEMY_TRACK_MODIFICATIONS"] = False
app.config['PROPAGATE_EXCEPTIONS'] = True

api = Api(app)
db.init_app(app)


api.add_resource(Transaction, "/transaction")
api.add_resource(LastTransaction, "/last-transaction")


@app.route("/")
def home():
    return render_template("home.html", values=TransactionModel.query.all())


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
        transaction = TransactionModel(
            datetime.now(),
            type,
            account,
            currency,
            float(amount),
            category,
            "Created by web form")
        transaction.save_to_db()
        #return render_template("home.html", values=TransactionModel.query.all())
        return redirect(url_for("home"))

if __name__ == "__main__":
    with app.app_context():
        db.create_all()
    app.run()
    #app.run(host="0.0.0.0")
