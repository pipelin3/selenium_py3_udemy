from selenium.webdriver.common.by import By
from traceback import print_stack
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as ec
from selenium.common.exceptions import NoSuchElementException, ElementNotVisibleException, ElementNotSelectableException
import logging
import utilities.custom_logger as cl
import time
import os


class SeleniumDriver():

    log = cl.custom_logger(logging.DEBUG)

    def __init__(self, driver):
        self.driver = driver

    def screen_shot(self, result_message):
        file_name = result_message + "." + str(round(time.time() * 1000)) + ".png"
        screenshot_directory = "..\\screenshots\\"
        relative_file_name = screenshot_directory + file_name
        current_directory = os.path.dirname(__file__)
        destination_file = os.path.join(current_directory, relative_file_name)
        destination_directory = os.path.join(current_directory, screenshot_directory)

        try:
            if not os.path.exists(destination_directory):
                os.makedirs(destination_directory)
            self.driver.save_screenshot(destination_file)
            self.log.info("Screenshot saved to directory: " + destination_file)
        except:
            self.log.error("### Exception Occurred")
            print_stack()

    def get_title(self):
        return self.driver.title

    def get_by_type(self, locator_type):
        locator_type == locator_type.lower()

        if locator_type == 'id':
            return By.ID
        elif locator_type == 'name':
            return By.NAME
        elif locator_type == 'xpath':
            return By.XPATH
        elif locator_type == 'css':
            return By.CSS_SELECTOR
        elif locator_type == 'class':
            return By.CLASS_NAME
        elif locator_type == 'link':
            return By.LINK_TEXT
        else:
            self.log.info("Locator type " + locator_type + " not correct/supported")
        return False

    def get_element(self, locator, locator_type='id'):
        element = None
        try:
            by_type = self.get_by_type(locator_type)
            element = self.driver.find_element(by_type, locator)
            self.log.info("Element found with locator: " + locator + " and locatorType: " + locator_type)
        except:
            self.log.info("Element not found with locator: " + locator + " and locatorType: " + locator_type)
        return element

    def get_element_list(self, locator, locator_type='id'):
        element = None
        try:
            by_type = self.get_by_type(locator_type)
            element = self.driver.find_elements(by_type, locator)
            self.log.info("Element list found with locator: " + locator + " and locatorType: " + locator_type)
        except:
            self.log.info("Element list not found with locator: " + locator + " and locatorType: " + locator_type)
        return element

    def element_click(self, locator='', locator_type='id', element=None):
        try:
            if locator:
                element = self.get_element(locator, locator_type)
            element.click()
            self.log.info("Clicked on element: " + locator + " and locator type: " + locator_type)
        except:
            self.log.info("Cannot click on the element with locator: " +
                          locator + " and locator type: " + locator_type)
            print_stack()

    def send_keys(self, data, locator='', locator_type='id', element=None):
        try:
            if locator:
                element = self.get_element(locator, locator_type)
            element.send_keys(data)
            self.log.info("Sent keys on element: " + locator + " and locator type: " + locator_type)
        except:
            self.log.info("Cannot send keys on the element with locator: " +
                          locator + " and locator type: " + locator_type)
            print_stack()

    def get_text(self, locator='', locator_type='id', element=None, info=''):
        try:
            if locator:
                self.log.debug("In locator condition")
                element = self.get_element(locator, locator_type)
            self.log.debug("Before finding text")
            text = element.text
            self.log.debug("After finding element, size is: " + str(len(text)))
            if len(text) == 0:
                text = element.get_attribute('innerText')
            if len(text) != 0:
                self.log.info("Getting text on element :: " + info)
                self.log.info("The text is :: '" + text + "'")
                text = text.strip()
        except:
            self.log.error("Failed to get text on element " + info)
            print_stack()
            text = None
        return text

    def is_element_present(self, locator='', locator_type='id', element=None):
        try:
            if locator:
                element = self.get_element(locator, locator_type)
            if element is not None:
                self.log.info("Element present with locator: " + locator + " locator_type " + locator_type)
                return True
            else:
                self.log.info("Element not present with locator: " + locator + " locator_type " + locator_type)
                return False
        except:
            self.log.info("Element not found")
            return False

    def is_element_displayed(self, locator='', locator_type='id', element=None):
        is_displayed = False
        try:
            if locator:
                element = self.get_element(locator, locator_type)
            if element is not None:
                is_displayed = element.is_displayed()
                self.log.info("Element is displayed with locator: " + locator + " locator_type " + locator_type)
                return is_displayed
            else:
                self.log.info("Element not displayed with locator: " + locator + " locator_type " + locator_type)
                return False
        except:
            self.log.info("Element not found")
            return False

    def element_presence_check(self, locator, byType):
        try:
            element_list = self.driver.find_elements(byType, locator)
            if len(element_list) > 0:
                self.log.info("Element found")
                return True
            else:
                self.log.info("Element not found")
                return False
        except:
            self.log.info("Element not found")
            return False

    def wait_for_element(self, locator, locator_type="id", timeout=10, poolFrequemcy=0.5):
        element = None
        try:
            self.log.info("Waiting for maximum :: " + str(timeout) + " :: seconds for element to be clickable")
            by_type = self.get_by_type(locator_type)
            wait = WebDriverWait(self.driver, 10, poll_frequency=1,
                                 ignored_exceptions=[NoSuchElementException,
                                                     ElementNotVisibleException, ElementNotSelectableException])
            element = wait.until(ec.element_to_be_clickable((by_type, "stopFilter_stops-0")))
            self.log.info("Element appeared on the web page")
        except:
            self.log.info("Element not appeared on the web page")
            print_stack()
        return element

    def web_scroll(self, direction='up'):
        if direction == 'up':
            self.driver.execute_script("window.scrollBy(0, -1000);")
        if direction == 'down':
            self.driver.execute_script("window.scrollBy(0, 1000);")

    def switch_to_frame(self, id='', name='', index=None, element=None):
        if id:
            self.driver.switch_to.frame(id)
        elif name:
            self.driver.switch_to.frame(name)
        elif index:
            self.driver.switch_to.frame(index)
        else:
            self.driver.switch_to.frame(element)

    def switch_to_default_content(self):
        self.driver.switch_to.default_content()

    def get_element_attribute_value(self, attribute, element=None, locator='', locator_type='id'):
        if locator:
            element = self.get_element(locator=locator, locator_type=locator_type)
        value = element.get_attribute(attribute)
        return value

    def is_enable(self, locator, locator_type='', info=''):
        element = self.get_element(locator, locator_type=locator_type)
        enabled = False
        try:
            attribute_value = self.get_element_attribute_value(element=element, attribute='disabled')
            if attribute_value is not None:
                enabled = element.is_enabled()
            else:
                value = self.get_element_attribute_value(element=element, attribute='class')
                self.log.info("Attribute value from Aplication Web UI --> :: " + value)
                enabled = not ("block" in value)
            if enabled:
                self.log.info("Element :: '" + info + "' is enabled")
            else:
                self.log.info("Element :: '" + info + "' is not enabled")
        except:
            self.log.error("Element :: '" + info + "' state could not be found")
        return enabled
