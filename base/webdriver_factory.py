from selenium import webdriver

class WebDriverFactory():

    def __init__(self, browser):

        self.browser = browser

    def get_web_driver_instance(self):

        base_url = "https://courses.letskodeit.com/"
        if self.browser == 'firefox':
            driver = webdriver.Firefox(executable_path="C:\\Users\\Pipe\\Documents\\Dark's\\To Study\\PythonWorkspace\\SeleniumWDFramework\\geckodriver.exe")
        
        if self.browser == 'chrome':
            driver = webdriver.Chrome(executable_path="C:\\Users\\Pipe\\Documents\\Dark's\\To Study\\PythonWorkspace\\SeleniumWDFramework\\chromedriver.exe")

        else:
            driver = webdriver.Firefox(executable_path="C:\\Users\\Pipe\\Documents\\Dark's\\To Study\\PythonWorkspace\\SeleniumWDFramework\\geckodriver.exe")
        
        driver.maximize_window()
        driver.implicitly_wait(3)
        driver.get(base_url)

        return driver
