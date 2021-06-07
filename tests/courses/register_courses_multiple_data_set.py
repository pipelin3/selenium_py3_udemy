from pages.courses.register_courses_page import RegisterCoursesPage
from utilities.test_status import TestStatus
import unittest
import pytest
from ddt import ddt, data, unpack


@pytest.mark.usefixtures("one_time_set_up", "set_up")
@ddt()
class RegisterMultipleCoursesTest(unittest.TestCase):

    @pytest.fixture(autouse=True)
    def class_setup(self, one_time_set_up):
        self.cp = RegisterCoursesPage(self.driver)
        self.ts = TestStatus(self.driver)

    @pytest.mark.run(order=1)
    @data(("JavaScript for beginners", "6548 9856 1254 1236", "1023", "123"),
          ("Learn Python 3 from scratch", "6548 9856 1254 1239", "1024", "321"))
    @unpack
    def test_invalid_enrollment(self, course_name, cc_num, cc_exp, cc_cvv):
        self.cp.enter_course_name(course_name)
        self.cp.select_course_to_enroll(course_name)
        self.cp.enroll_course(cc_num, cc_exp, cc_cvv)
        result = self.cp.verify_enroll_failed()
        self.ts.mark_final("test_invalid_enrollment", result, "Enrollment fail verification")
        self.driver.find_element_by_link_text("ALL COURSES").click()
