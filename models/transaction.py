from db import db

class TransactionModel(db.Model):
    __tablename__ = 'transactions'

    _id = db.Column("id", db.Integer, primary_key=True)

    date_time = db.Column(db.DateTime)
    type = db.Column(db.String(20))
    account = db.Column(db.String(20))
    currency = db.Column(db.String(3))
    amount = db.Column(db.Float(precision=2))
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

    @classmethod
    def find_by_date(cls, date):
        return cls.query.filter_by(date_time=date).first()

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
