import unittest
from tests.home.login_test import LoginTest
from tests.courses.register_courses_csv_data import RegisterCoursesCSVDataTest

# Get all test from test classes
tc1 = unittest.TestLoader().loadTestsFromTestCase(LoginTest)
tc2 = unittest.TestLoader().loadTestsFromTestCase(RegisterCoursesCSVDataTest)

# Create a test suite combining all test cases
smoke_test = unittest.TestSuite([tc1, tc2])
unittest.TextTestRunner(verbosity=2).run(smoke_test)
