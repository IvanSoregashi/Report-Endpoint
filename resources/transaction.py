from flask_restful import Resource, reqparse
from models.transaction import TransactionModel


class Transaction(Resource):
    parser = reqparse.RequestParser()
    parser.add_argument('date_time', type=str, required=True, help="This field cannot be blank.")
    parser.add_argument('type', type=str, required=True, help="This field cannot be blank.")
    parser.add_argument('account', type=str, required=True, help="This field cannot be blank.")
    parser.add_argument('currency', type=str, required=True, help="This field cannot be blank.")
    parser.add_argument('amount', type=float, required=True, help="This field cannot be blank.")
    parser.add_argument('category', type=str, required=True, help="This field cannot be blank.")
    parser.add_argument('comment', type=str, required=False, help="This field can be blank.")

    def post(self):
        data = Transaction.parser.parse_args()

        transaction = TransactionModel(
            date_time=data['date_time'],
            type=data['type'],
            account=data['account'],
            currency=data['currency'],
            amount=data['amount'],
            category=data['category'],
            comment=data.get('comment', 'transaction by API')
        )

        try:
            transaction.save_to_db()
        except:
            return {"message": "An error occurred inserting the transaction."}, 500

        return {"message": "Transaction created successfully."}, 201


