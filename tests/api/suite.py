import unittest
from testcases.test_api_response import TestApi

#Load test cases from the test class
api_tests = unittest.TestLoader().loadTestsFromTestCase(TestApi)

#Add test cases to the test suite
api_suite = unittest.TestSuite([api_tests])

#Execute the test suite
if __name__ == '__main__':
    unittest.TextTestRunner(verbosity=2).run(api_suite)