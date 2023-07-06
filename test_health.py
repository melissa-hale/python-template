import unittest
from main import app


class HealthCheckTestCase(unittest.TestCase):
    def setUp(self):
        self.app = app.test_client()

    def test_health_check(self):
        response = self.app.get('/thisapi/v1/health')
        data = response.get_json()
        expected = {"message": "All systems go."}
        self.assertEqual(response.status_code, 200)
        self.assertEqual(data, expected)


if __name__ == '__main__':
    unittest.main()