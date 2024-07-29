from unittest import TestCase
from app import app
from db import db


class BaseTest(TestCase):
    def setUp(self):
        app.testing = True
        self.app = app.test_client
        db.init_app(app)
