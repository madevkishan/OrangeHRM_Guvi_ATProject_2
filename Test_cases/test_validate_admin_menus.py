from selenium.webdriver.support.ui import WebDriverWait
from PageObjects.login_page_POM import LoginPage_Actions
from PageObjects.adminmenu_validate_POM import AdminPage_Menu_Actions
from Test_utilities.customLogger import logGen
from time import sleep
class TestAdminMenu:
    def test_validate_admin_menus(self, setup_browser):  # Pass the 'setup_browser' fixture as an argument
        """
        Testcase for Valid Login - Positive Testcase
        :return:
        """
        self.driver = setup_browser
        logs_obj = logGen.logger()
        LoginPage_Actions_obj = LoginPage_Actions(driver=setup_browser)  # Create an instance of orangehrm_LoginPageActions class
        admin_obj = AdminPage_Menu_Actions(driver=setup_browser)
        logs_obj.info("Starting the Test")
        LoginPage_Actions_obj.login_to_orangehrm_valid()  # Call the method on the instance
        sleep(2)

        admin_obj.click_admin_menu(self.driver)
        sleep(3)

        # OrangeGRM title page verification
        title_verify = 'OrangeHRM'
        title_name = LoginPage_Actions_obj.title_of_page()
        if title_verify == title_name:
            print(f'{title_verify} title is verified in Admin Page')
            logs_obj.info("ORANGEHRM title is verified in Admin Page")

        admin_obj.admin_menu_validate()
