from pages.courses.register_courses_page import RegisterCoursesPage
from utilities.test_status import TestStatus
import unittest
import pytest
from ddt import ddt, data, unpack
from utilities.read_data import get_csv_data
from pages.home.navigation_page import NavigationPage


@pytest.mark.usefixtures("one_time_set_up", "set_up")
@ddt()
class RegisterCoursesCSVDataTest(unittest.TestCase):

    @pytest.fixture(autouse=True)
    def object_setup(self, one_time_set_up):
        self.cp = RegisterCoursesPage(self.driver)
        self.ts = TestStatus(self.driver)
        self.nav = NavigationPage(self.driver)

    def setUp(self):
        self.nav.navigate_to_all_courses()

    @pytest.mark.run(order=1)
    @data(*get_csv_data("test_data.csv"))
    @unpack
    def test_invalid_enrollment(self, course_name, cc_num, cc_exp, cc_cvv):
        self.cp.enter_course_name(course_name)
        self.cp.select_course_to_enroll(course_name)
        self.cp.enroll_course(cc_num, cc_exp, cc_cvv)
        result = self.cp.verify_enroll_failed()
        self.ts.mark_final("test_invalid_enrollment", result, "Enrollment fail verification")
