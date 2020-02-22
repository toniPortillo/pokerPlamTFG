# test.py
import sys
sys.path.append("../")
import app
from unittest import TestCase
from unittest.mock import patch, Mock

class TestBlog(TestCase):
    @patch('app.Add')
    def test_api_add_contact(self, MockApi):
        # ARRANGE
        api = MockApi()
        
        api.post.return_value = [
            {
                'message': 'SUCCESS'
            }
        ]
        # ACT
        response = api.post()
        
        # ASSERT
        self.assertIsNotNone(response)
        self.assertIsInstance(response[0], dict)

    @patch('app.Get_all')
    def test_api_get_all_contact(self, MockApi):
        # ARRANGE
        api = MockApi()

        # ACT
        api.get.return_value = [
            {
            "_id": {
                "$oid": "5e4a7c5437ca685c2c5ae0a0"
            },
            "contact": "gato",
            "name": "woody"
            }
        ]
        response = api.get()
        # ASSERT
        self.assertIsNotNone(response)
        self.assertIsInstance(response[0], dict)
        
        assert MockApi is app.Get_all
        assert MockApi.called
