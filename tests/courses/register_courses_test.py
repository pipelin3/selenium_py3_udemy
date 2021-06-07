from pages.courses.register_courses_page import RegisterCoursesPage
from utilities.test_status import TestStatus
import unittest
import pytest


@pytest.mark.usefixtures("one_time_set_up", "set_up")
class RegisterCoursesTest(unittest.TestCase):

    @pytest.fixture(autouse=True)
    def class_setup(self, one_time_set_up):
        self.cp = RegisterCoursesPage(self.driver)
        self.ts = TestStatus(self.driver)

    @pytest.mark.run(order=1)
    def test_invalid_enrollment(self):
        self.cp.enter_course_name("JavaScript")
        self.cp.select_course_to_enroll("JavaScript for beginners")
        self.cp.enroll_course("6548 9856 1254 1236", "1023", "123")
        result = self.cp.verify_enroll_failed()
        self.ts.mark_final("test_invalid_enrollment", result, "Enrollment fail verification")
