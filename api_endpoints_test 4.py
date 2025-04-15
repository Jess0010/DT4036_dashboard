import unittest
from app import app


class TestApiEndpoints(unittest.TestCase):
    def setUp(self):
        self.app = app.test_client()
        self.app.testing = True

    def test_low_stock_levels(self):
        response = self.app.get("api/low_stock_levels")
        self.assertEqual(response.status_code, 200)

        self.assertTrue(response.is_json)

        self.assertTrue("products" in response.json)
        self.assertTrue("quantities" in response.json)


        self.assertIsInstance(response.json["products"], list)

        self.assertTrue(all(isinstance(x, int) for x in response.json["quantities"]))


if __name__ == "__main__":
    unittest.main()
