from flask_restful import Resource, reqparse
from models.transaction import TransactionModel
from datetime import datetime


class LastTransaction(Resource):
    parser = reqparse.RequestParser()

    def get(self):
        return TransactionModel.query.order_by(TransactionModel._id.desc()).first().json()