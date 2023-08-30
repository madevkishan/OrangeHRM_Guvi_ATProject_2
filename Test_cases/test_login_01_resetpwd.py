from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.common.by import By
from PageObjects.login_page_POM import LoginPage_Actions
from PageObjects.login_page_resetpwd_POM import LoginPage_Resetpwd_Actions
from Test_utilities.customLogger import logGen


class TestLoginPage:
    def test_login_page_resetpwd(self, setup_browser):  # Pass the 'setup_browser' fixture as an argument
        """
        Testcase for invalid login - Negative testcase
        :return:
        """
        self.driver = setup_browser
        logs_obj = logGen.logger()
        LoginPage_Actions_obj = LoginPage_Actions(driver=setup_browser)  # Create an instance of orangehrm_LoginPageActions class
        resetpwd_obj = LoginPage_Resetpwd_Actions(driver=setup_browser)
        logs_obj.info("Starting the Test")
        LoginPage_Actions_obj.login_to_orangehrm_invalid()  # Call the method on the instance

        capture_invalid_text = LoginPage_Actions_obj.capture_invalidcredentials()
        invalid_text_check = 'Invalid credentials'

        if invalid_text_check == capture_invalid_text:
            print("**** Login Unsuccessfull because of Invalid Credentials")
            logs_obj.info("Login Failed because of Invalid credentials")

        resetpwd_obj.forgot_password()
        resetpwd_obj.reset_password()
        reset_validation_text = resetpwd_obj.reset_validation()

        # validating whether 'Reset Password' is successfull
        reset_text_check = 'Reset Password link sent successfully'

        if reset_validation_text == reset_text_check:
            print("**** Reset of Password is successfull")
            logs_obj.info("Reset of Password is successfull")

