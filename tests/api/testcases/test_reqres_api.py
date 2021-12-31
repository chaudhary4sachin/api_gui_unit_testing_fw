"""
Test Case: To verify api's response is as expected.

    Author: Sachin Chaudhary
    Created on: 29th Dec 2021
    Last Modified on: 31st Dec 2021
"""
import os
import unittest
from utils.reqres_api_utils import ReqResApiUtils


class TestReqResApi(unittest.TestCase):
    """Test class to test api endpoints"""

    @classmethod
    def setUpClass(cls):
        cls.expected_response_json = 'expected_file.json'
        cls.create_name = "Paul"
        cls.create_job = "Architect"
        cls.api = ReqResApiUtils()
        cls.list_users_response = cls.api.list_users()
        cls.create_user_response = cls.api.create_user(name=cls.create_name, job=cls.create_job)

    def test_list_users_response_schema(self):
        """Test the response schema is as expected."""
        validate_result = self.api.validate_list_users_response_schema(self.list_users_response)
        self.assertTrue(validate_result)

    def test_create_users_response_schema(self):
        """Test the response schema is as expected."""
        validate_result = self.api.validate_create_user_response_schema(self.create_user_response)
        self.assertTrue(validate_result)

    def test_new_created_user(self):
        user_present = self.api.verify_user_in_create_user(name=self.create_name, job=self.create_job,
                                                           response=self.create_user_response)
        self.assertTrue(user_present)

    def test_response_against_expected(self):
        """Test the response against the static expected file. This is useful when the response isn't dynamic and
        can be compared against a sample file."""
        files_match = self.api.compare_response_to_expected(response=self.list_users_response,
                                                            expected_file=self.expected_response_json)
        self.assertTrue(files_match)

    @classmethod
    def tearDownClass(cls):
        if os.path.isfile(cls.expected_response_json):
            os.remove(cls.expected_response_json)

if __name__ == '__main__':
    unittest.main()
