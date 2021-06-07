from base.base_page import BasePage


class NavigationPage(BasePage):

    def __init__(self, driver):
        super().__init__(driver)
        self.driver = driver

    # Locators
    _logo = ".navbar-logo"
    _home = "HOME"
    _all_courses = "ALL COURSES"
    _support = "SUPPORT"
    _my_courses = "MY COURSES"
    _user_settings_icon = "dropdownMenu1"

    def navigate_to_logo(self):
        self.element_click(locator=self._logo, locator_type='css')

    def navigate_to_home(self):
        self.element_click(locator=self._home, locator_type='link')

    def navigate_to_all_courses(self):
        self.element_click(locator=self._all_courses, locator_type='link')

    def navigate_to_support(self):
        self.element_click(locator=self._support, locator_type='link')

    def navigate_to_my_courses(self):
        self.element_click(locator=self._my_courses, locator_type='link')

    def navigate_to_user_settings(self):
        self.element_click(locator=self._user_settings_icon)
