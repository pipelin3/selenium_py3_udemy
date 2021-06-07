import utilities.custom_logger as cl
import logging
from base.base_page import BasePage


class RegisterCoursesPage(BasePage):

    log = cl.custom_logger(logging.DEBUG)
    
    def __init__(self, driver):
        super().__init__(driver)
        self.driver = driver

    #locators
    _search_box = 'course'
    _course = "//div[contains(@class,'zen-course-title')]/h4[contains(text(),'{0}')]"
    _search_button = 'button.find-course.search-course'
    _enroll_button = '.btn-enroll'
    _cc_num_frame = "//iframe[@title='Secure card number input frame']"
    _cc_num = "//input[@aria-label='Credit or debit card number']"
    _cc_exp_frame = "//iframe[@title='Secure expiration date input frame']"
    _cc_exp = 'exp-date'
    _cc_cvv_frame = "//iframe[@title='Secure CVC input frame']"
    _cc_cvv = 'cvc'
    _submit_enroll = 'button.sp-buy'
    
    def enter_course_name(self, name):
        self.send_keys(name, locator=self._search_box, locator_type='name')
        self.element_click(self._search_button, 'css')

    def select_course_to_enroll(self, full_course_name):
        self.element_click(locator=self._course.format(full_course_name), locator_type='xpath')

    def click_on_enroll_button(self):
        self.element_click(self._enroll_button, locator_type='css')

    def enter_card_num(self, num):
        self.switch_to_frame(element=self.get_element(self._cc_num_frame, 'xpath'))
        self.send_keys(num, locator=self._cc_num, locator_type='xpath')
        self.switch_to_default_content()

    def enter_card_exp(self, exp):
        self.switch_to_frame(element=self.get_element(self._cc_exp_frame, 'xpath'))
        self.send_keys(exp, locator=self._cc_exp, locator_type='name')
        self.switch_to_default_content()

    def enter_card_cvv(self, cvv):
        self.switch_to_frame(element=self.get_element(self._cc_cvv_frame, 'xpath'))
        self.send_keys(cvv, locator=self._cc_cvv, locator_type='name')
        self.switch_to_default_content()

    def click_enroll_submit_button(self):
        self.element_click(self._submit_enroll, locator_type='css')

    def enter_credit_card_info(self, num, exp, cvv):
        self.enter_card_num(num)
        self.enter_card_exp(exp)
        self.enter_card_cvv(cvv)

    def enroll_course(self, num='', exp='', cvv=''):
        self.click_on_enroll_button()
        self.web_scroll(direction='down')
        self.enter_credit_card_info(num, exp, cvv)
        self.click_enroll_submit_button()

    def verify_enroll_failed(self):
        result = self.is_enable(locator=self._submit_enroll, locator_type='css', info="Enroll button")
        return not result
