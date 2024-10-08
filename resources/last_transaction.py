from flask_restful import Resource, reqparse
from models.transaction import TransactionModel
from datetime import datetime


class LastTransaction(Resource):
    parser = reqparse.RequestParser()

    def get(self):
        try:
            last = TransactionModel.query.order_by(TransactionModel._id.desc()).first()
        except Exception as e:
            return {"success": False, "message": str(e)}, 500
        return last.json(), 200

    def delete(self):
        try:
            last = TransactionModel.query.order_by(TransactionModel._id.desc()).first()
            last.delete_from_db()
        except Exception as e:
            return {"success": False, "message": str(e)}, 500
        return {"success": True}, 202
