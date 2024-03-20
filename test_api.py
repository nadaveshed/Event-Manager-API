import unittest
import requests


class TestAPI(unittest.TestCase):
    base_url = 'http://localhost:5000'

    def setUp(self):
        self.auth = ('user', 'password')

    def test_schedule_event(self):
        data = {
            "name": "Test Event",
            "location": "Test Location",
            "date": "2024-03-21T10:00:00",
            "participants": 100
        }
        response = requests.post(f'{self.base_url}/schedule', json=data, auth=self.auth)
        self.assertEqual(response.status_code, 200)

    def test_get_all_events(self):
        response = requests.get(f'{self.base_url}/events', auth=self.auth)
        self.assertEqual(response.status_code, 200)
        self.assertIsInstance(response.json(), list)


if __name__ == '__main__':
    unittest.main()
