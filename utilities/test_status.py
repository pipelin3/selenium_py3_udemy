
from base.selenium_driver import SeleniumDriver
from traceback import print_stack

class TestStatus(SeleniumDriver):

    def __init__(self, driver):

        super(TestStatus, self).__init__(driver)
        self.result_list = []

    def set_result(self, result, result_message):
        try:
            if result is not None:
                if result:
                    self.result_list.append("PASS")
                    self.log.info("### VERIFICATION SUCCESSFUL :: " + result_message)
                else:
                    self.result_list.append("FAIL")
                    self.log.error("### VERIFICATION FAIL :: " + result_message)
                    self.screen_shot(result_message)
            else:
                self.result_list.append("FAIL")
                self.log.error("### VERIFICATION FAIL :: " + result_message)
                self.screen_shot(result_message)
        except:
            self.result_list.append("FAIL")
            self.log.error("### Exception occured!!")
            self.screen_shot(result_message)
            print_stack()

    def mark(self, result, result_message):
        self.set_result(result, result_message)

    def mark_final(self, test_name, result, result_message):
        self.set_result(result, result_message)

        if "FAIL" in self.result_list:
            self.log.error(test_name + " ### TEST FAILED !!")
            self.result_list.clear()
            assert True == False
        else:
            self.log.info(test_name + " ### TEST SUCCESSFUL !!")
            self.result_list.clear()
            assert True == True
