from flask import Flask, request, render_template
from flask_sqlalchemy import SQLAlchemy
from flask_restful import Api
from datetime import datetime

app = Flask(__name__)
app.config['DEBUG'] = True
app.config["SQLALCHEMY_DATABASE_URI"] = "sqlite:///transactions.sqlite3"
app.config["SQLALCHEMY_TRACK_MODIFICATIONS"] = False
app.config['PROPAGATE_EXCEPTIONS'] = True

db = SQLAlchemy(app)
api = Api(app)


class TransactionModel(db.Model):
    __tablename__ = 'transactions'

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
        # add validation

    def json(self):
        return {
             'date_time': self.date_time,
             'type': self.type,
             'account': self.account,
             'currency': self.currency,
             'amount': self.amount,
             'category': self.category,
             'comment': self.comment,
        }

    def save_to_db(self):
        db.session.add(self)
        db.session.commit()

    def delete_from_db(self):
        db.session.delete(self)
        db.session.commit()

    '''@classmethod
    def find_by_name(cls, name):
        return cls.query.filter_by(name=name).first()'''


#api.add_resource(TransactionModel, "/transaction")


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
        tr = TransactionModel(datetime.now(), type, account, currency, int(amount), category, "Created by web form")
        db.session.add(tr)
        db.session.commit()
        return render_template("home.html", values=TransactionModel.query.all())


if __name__ == "__main__":


    if app.config['DEBUG']:
        @app.before_request
        def create_tables():
            with app.app_context():
                db.create_all()
    app.run()
