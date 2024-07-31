from unittest import TestCase
from datetime import datetime

from models.transaction import TransactionModel


class TestModel(TestCase):
    def test_transaction_create(self):
        date_time = datetime.now()

        transaction = TransactionModel(
            date_time,
            "TEST_TYPE",
            "TEST_ACCOUNT",
            "TEST_CURRENCY",
            999.999,
            "TEST_CATEGORY",
            "TEST_COMMENT")

        self.assertEqual(transaction.type, "TEST_TYPE",
                         "The 'type' after creation does not equal the constructor argument")
        self.assertEqual(transaction.account, "TEST_ACCOUNT",
                         "The 'account' after creation does not equal the constructor argument")
        self.assertEqual(transaction.currency, "TEST_CURRENCY",
                         "The 'currency' after creation does not equal the constructor argument")
        self.assertEqual(transaction.amount, 999.999,
                         "The 'amount' after creation does not equal the constructor argument")
        self.assertEqual(transaction.category, "TEST_CATEGORY",
                         "The 'category' after creation does not equal the constructor argument")
        self.assertEqual(transaction.comment, "TEST_COMMENT",
                         "The 'comment' after creation does not equal the constructor argument")

    def test_transaction_json(self):
        date_time = datetime.now()

        transaction = TransactionModel(
            date_time,
            "TEST_TYPE",
            "TEST_ACCOUNT",
            "TEST_CURRENCY",
            999.999,
            "TEST_CATEGORY",
            "TEST_COMMENT")

        expected = {
            'date_time': str(date_time),
            'type': 'TEST_TYPE',
            'account': 'TEST_ACCOUNT',
            'currency': 'TEST_CURRENCY',
            'amount': 999.999,
            'category': 'TEST_CATEGORY',
            'comment': 'TEST_COMMENT'
        }

        self.assertEqual(transaction.json(), expected,
                         f"The JSON export item is incorrect.\nReceived {transaction.json()}, Expected {expected}")
