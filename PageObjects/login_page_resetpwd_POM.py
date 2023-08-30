import logging
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from selenium.common.exceptions import *
from selenium.webdriver.common.by import By
from Test_data import credentials_valid, credentials_invalid
from Test_locators.test_locators import LoginPage_Locators,Resetpwd_Locators
from time import sleep
class LoginPage_Resetpwd_Actions:

    def __init__(self, driver):   # Accept the WebDriver instance as an argument
        self.login_loc_obj = LoginPage_Locators()   # created an object for locator class
        self.reset_loc_obj = Resetpwd_Locators()
        self.driver = driver   # Use the WebDriver instance passed from the fixture
        self.wait = WebDriverWait(self.driver, 10)

    def enter_username_valid_login(self):
        """
        Find the webelement for username ,clear the text field and send the username
        :return:
        """
        # username_we = self.driver.find_element(By.NAME, self.login_loc_obj.username_loc_name)
        username_we = self.wait.until(EC.element_to_be_clickable((By.NAME, self.login_loc_obj.username_loc_name)))
        username_we.clear()
        username_we.send_keys(credentials_valid.username)
        logging.info("Username entered")

    def enter_password_valid_login(self):
        """
        find the webelement for password ,clear the text field and send the password
        :return:
        """
        password_we = self.wait.until(EC.element_to_be_clickable((By.NAME, self.login_loc_obj.password_loc_name)))
        password_we.clear()
        password_we.send_keys(credentials_valid.password)
        logging.info("password entered")

    def enter_username_invalid_login(self):
        """
        .032
        find the webelement for username ,clear the text field and send Invalid username
        :return:
        """
        username_we = self.wait.until(EC.element_to_be_clickable((By.NAME, self.login_loc_obj.username_loc_name)))
        username_we.clear()
        username_we.send_keys(credentials_invalid.username)
        logging.info("Username entered")

    def enter_password_invalid_login(self):
        """
        find the webelement for password ,clear the text field and send Invalid password
        :return:
        """
        password_we = self.wait.until(EC.element_to_be_clickable((By.NAME, self.login_loc_obj.password_loc_name)))
        password_we.clear()
        password_we.send_keys(credentials_invalid.password)
        logging.info("password entered")

    def click_login(self):
        login_button_we = self.wait.until(EC.element_to_be_clickable((By.XPATH, self.login_loc_obj.login_loc_btn_xpath)))
        login_button_we.click()
        logging.info("Login button clicked")

    def login_to_orangehrm_valid(self):
        self.enter_username_valid_login()
        self.enter_password_valid_login()
        self.click_login()
        # self.driver.implicitly_wait(5)

    def login_to_orangehrm_invalid(self):
        self.enter_username_invalid_login()
        self.enter_password_invalid_login()
        self.click_login()
        # self.driver.implicitly_wait(5)

    def title_of_page(self):
        title_name = self.driver.title
        # self.driver
        logging.info("Returning title of webpage", title_name)
        return title_name

    def dashboard_verify(self):
        try:
            dashboard_verify_we = self.wait.until(EC.element_to_be_clickable((By.XPATH,self.login_loc_obj.dashboard_page)))
            dashboard_text = dashboard_verify_we.text
            print(dashboard_text)
            return dashboard_text
        except NoSuchElementException:
            print("Element not found as failed to login")

    def capture_invalidcredentials(self):
        capture_invalid_we = self.wait.until(EC.element_to_be_clickable((By.XPATH, self.login_loc_obj.invalid_loc_text_xpath)))
        capture_invalid_text = capture_invalid_we.text
        return capture_invalid_text

    def forgot_password(self):
        forgot_pwd_we = self.wait.until(EC.element_to_be_clickable((By.XPATH,self.login_loc_obj.forgotpwd_loc_link_xpth)))
        forgot_pwd_we.click()
        logging.info("Clicked on 'Forgot Password' Link")

    def reset_password(self):
        username_txt_we = self.wait.until(EC.element_to_be_clickable((By.NAME, self.reset_loc_obj.username_loc_txt_name)))
        username_txt_we.clear()
        username_txt_we.send_keys('admin')

        username_btn_we = self.wait.until(EC.element_to_be_clickable((By.XPATH, self.reset_loc_obj.resetpwd_loc_btn_xpath)))
        username_btn_we.click()
        sleep(3)

    def reset_validation(self):
        resetpwd_title_check_we = self.wait.until(EC.element_to_be_clickable((By.XPATH, self.reset_loc_obj.resetmsg_loc_title_xpath)))
        reset_txt_validation = resetpwd_title_check_we.text
        return reset_txt_validation