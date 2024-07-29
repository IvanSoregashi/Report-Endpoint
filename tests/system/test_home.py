from tests.base_test import BaseTest


class TestHome(BaseTest):
    def test_home(self):
        with self.app() as client:
            with self.app_context():
                response = client.get("/")
                self.assertEqual(response.status_code, 200)
