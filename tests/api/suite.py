import unittest, sys, os
sys.path.append(os.path.abspath(os.path.curdir))
from tests.api.testcases.test_reqres_api import TestReqResApi

#Load test cases from the test class
api_tests = unittest.TestLoader().loadTestsFromTestCase(TestReqResApi)

#Add test cases to the test suite
api_suite = unittest.TestSuite([api_tests])

#Execute the test suite
if __name__ == '__main__':
    unittest.TextTestRunner(verbosity=2).run(api_suite)