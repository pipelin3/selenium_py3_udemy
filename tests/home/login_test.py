from pages.home.login_page import LoginPage
from utilities.test_status import TestStatus
import unittest
import pytest


@pytest.mark.usefixtures("one_time_set_up", "set_up")
class LoginTest(unittest.TestCase):

    @pytest.fixture(autouse=True)
    def class_setup(self, one_time_set_up):
        self.lp = LoginPage(self.driver)
        self.ts = TestStatus(self.driver)

    @pytest.mark.run(order=1)
    def test_invalid_login(self):
        self.lp.logout()
        self.lp.login("test@email2.com", "abcabcd")
        result = self.lp.verify_login_failed()
        assert result == True

    @pytest.mark.run(order=2)
    def test_valid_login(self):
        self.lp.login("test@email.com", "abcabc")
        result1 = self.lp.verify_login_title()
        self.ts.mark(result1, "Title verified")
        result2 = self.lp.verify_login_successful()
        self.ts.mark_final("test_valid_login", result2, "Login was successful")
