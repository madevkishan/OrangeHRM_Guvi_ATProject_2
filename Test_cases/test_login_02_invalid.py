from selenium.webdriver.support.ui import WebDriverWait
# import Test_locators.test_locators
from selenium.webdriver.common.by import By
from PageObjects.login_page_POM import LoginPage_Actions
from Test_utilities.customLogger import logGen


class TestLoginPage:
    def test_login_page_invalid(self, setup_browser):  # Pass the 'setup_browser' fixture as an argument
        """
        Testcase for invalid login - Negative testcase
        :return:
        """
        self.driver = setup_browser
        logs_obj = logGen.logger()
        LoginPage_Actions_obj = LoginPage_Actions(driver=setup_browser)  # Create an instance of orangehrm_LoginPageActions class

        logs_obj.info("Starting the Test")
        LoginPage_Actions_obj.login_to_orangehrm_invalid()  # Call the method on the instance

        capture_invalid_text = LoginPage_Actions_obj.capture_invalidcredentials()
        invalid_text_check = 'Invalid credentials'

        if invalid_text_check == capture_invalid_text:
            print("**** Login Unsuccessfull because of Invalid Credentials")
            logs_obj.info("Login Failed because of Invalid credentials")
            self.driver.save_screenshot("../Screenshots/Login_Failed_InvalidCredentials.png")
            logs_obj.info("Screenshot captured for failed testcase")

