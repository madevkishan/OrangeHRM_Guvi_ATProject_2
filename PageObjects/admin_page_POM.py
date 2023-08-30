from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from Test_locators.test_locators import AdminPage_Locators

class AdminPage_Actions:

    def __init__(self, driver):
        self.admin_loc_obj = AdminPage_Locators()  # created an object for locator class
        self.driver = driver
        self.wait = WebDriverWait(self.driver,10)

    def click_admin_menu(self, driver):
        """
        click on Admin menu item
        :return:
        """
        admin_we = self.wait.until(EC.element_to_be_clickable((By.XPATH,self.admin_loc_obj.admin_loc_xpath)))
        admin_we.click()

    def enter_username_admin(self):
        """
        Enter 'username' textbox in Admin Page
        :return:
        """
        username_we = self.wait.until(EC.element_to_be_clickable((By.XPATH, self.admin_loc_obj.username_loc_textbox_xpath)))
        username_we.clear()
        username_we.send_keys("Madhu")

    def enter_userrole_dropdown_1(self):
        """
        Selecting 'User Role' from the drop-down
        :return:
        """
        userrole_we = self.wait.until(EC.element_to_be_clickable((By.XPATH,self.admin_loc_obj.userrole_loc_dropdown_xpath)))
        userrole_we.click()

    def enter_employeename(self):
        """
        Entering 'Employee Name' in the Textbox
        :return:
        """
        employeename_we = self.wait.until(EC.element_to_be_clickable((By.XPATH,self.admin_loc_obj.employeename_loc_textbox_xpath)))
        employeename_we.send_keys("Madhumathi")

    def status_dropdown(self):
        """
        Selecting 'Status' from the dropdown menu
        :return:
        """
        status_we = self.wait.until(EC.element_to_be_clickable((By.XPATH,self.admin_loc_obj.status_loc_dropdown_xpath)))
        status_we.click()

    def click_add_button(self):
        """
        Click on ADD button
        :return:
        """
        add_we = self.wait.until(EC.element_to_be_clickable((By.XPATH,self.admin_loc_obj.add_user_loc_xpath)))
        add_we.click()