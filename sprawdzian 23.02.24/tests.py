import unittest
import json
from app import app

class TestApp(unittest.TestCase):
    def setUp(self):
        self.app = app.test_client()

    def test_get_users(self):
        response = self.app.get('/users')
        self.assertEqual(response.status_code, 200)

    def test_create_user(self):
        user_data = {
            "firstName": "A",
            "lastName": "K",
            "birthYear": 2000,
            "group": "user"
        }
        response = self.app.post('/users', json=user_data)
        self.assertEqual(response.status_code, 201)

    def test_get_user_by_id(self):
        response = self.app.get('/users/1')
        self.assertEqual(response.status_code, 200)

    def test_update_user(self):
        user_data = {
            "firstName": "A",
            "lastName": "K",
            "birthYear": 2000,
            "group": "user"
        }
        response = self.app.patch('/users/1', json=user_data)
        self.assertEqual(response.status_code, 200)

    def test_delete_user(self):
        response = self.app.delete('/users/1')
        self.assertEqual(response.status_code, 200)

if __name__ == '__main__':
    unittest.main()
