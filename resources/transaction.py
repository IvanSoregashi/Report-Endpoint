from flask_restful import Resource, reqparse

class Transaction(Resource):
    parser = reqparse.RequestParser()
    parser.add_argument()