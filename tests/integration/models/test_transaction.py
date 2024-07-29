from tests.base_test import BaseTest
from models.transaction import TransactionModel
from datetime import datetime


class TransactionTest(BaseTest):
    def test_crud(self):
        with self.app_context():
            date_time = datetime.now()

            transaction = TransactionModel(
                date_time,
                "TEST_TYPE",
                "TEST_ACCOUNT",
                "TEST_CURRENCY",
                999.999,
                "TEST_CATEGORY",
                "TEST_COMMENT")

            self.assertIsNone(TransactionModel.find_by_date(date_time), "Found transaction by date, should not have.")

            transaction.save_to_db()

            self.assertIsNotNone(TransactionModel.find_by_date(date_time), "Not found transaction by date, should have.")

            transaction.delete_from_db()

            self.assertIsNone(TransactionModel.find_by_date(date_time), "Found transaction by date, should not have.")
