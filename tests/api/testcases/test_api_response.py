"""
Test Case: To verify api's response is as expected.

    Author: Sachin Chaudhary
    Created on: 29th Dec 2021
    Last Modified on: 29th Dec 2021
"""

import unittest
from utils.api_utils import ApiUtils


class TestApi(unittest.TestCase):
    """Test class to test api endpoints"""

    def setUp(self):
        self.api = ApiUtils()

    def test_response_schema(self):
        """Test the response schema is as expected."""
        response = self.api.call_endpoint()

        validate_result = self.api.validate_response_schema(response)
        self.assertTrue(validate_result)


if __name__ == '__main__':
    unittest.main()
