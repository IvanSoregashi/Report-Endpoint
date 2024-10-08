"""
BaseTest

This class should be the parent class to each non-unit test.
It allows for instantiation of the database dynamically,
and makes sure that it is a new, blank database each time.
"""

from unittest import TestCase
from app import app, db


class BaseTest(TestCase):
    @classmethod
    def setUpClass(cls):
        app.config['DEBUG'] = False
        app.config['SQLALCHEMY_DATABASE_URI'] = "sqlite:///"

    def setUp(self):
        with app.app_context():
            db.create_all()

        self.app = app.test_client
        self.app_context = app.app_context

    def tearDown(self):
        with app.app_context():
            db.session.remove()
            db.drop_all()
