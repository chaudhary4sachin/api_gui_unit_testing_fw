import unittest
from testcases.test_homepage import TestHomepage

#Load test cases from the test class
gui_tests = unittest.TestLoader().loadTestsFromTestCase(TestHomepage)

#Add test cases to the test suite
gui_suite = unittest.TestSuite([gui_tests])

#Execute the test suite
if __name__ == '__main__':
    unittest.TextTestRunner(verbosity=2).run(gui_suite)