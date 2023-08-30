from selenium.webdriver.support.ui import WebDriverWait
from PageObjects.login_page_POM import LoginPage_Actions
from PageObjects.dashboard_menu_validate_POM import DashboardPage_Menu_Actions
from PageObjects.dashboard_menus_click_POM import DashboardPage_ClickMenus_Actions
from Test_utilities.customLogger import logGen
from time import sleep
class TestDashboardMenu:
    def test_validate_dashboard_menus(self, setup_browser):  # Pass the 'setup_browser' fixture as an argument
        """
        Testcase to validate Dashboard menus
        :return:
        """
        self.driver = setup_browser
        logs_obj = logGen.logger()
        LoginPage_Actions_obj = LoginPage_Actions(driver=setup_browser)  # Create an instance of orangehrm_LoginPageActions class
        dashboard_obj = DashboardPage_Menu_Actions(driver=setup_browser)
        dashboard_click_obj = DashboardPage_ClickMenus_Actions(driver=setup_browser)
        logs_obj.info("Starting the Test")
        LoginPage_Actions_obj.login_to_orangehrm_valid()  # Call the method on the instance
        sleep(4)
        dashboard_obj.dashboard_menu_validate()
        sleep(2)

        dashboard_click_obj.pim_click()
        sleep(2)

        dashboard_click_obj.leave_click()
        sleep(2)

        dashboard_click_obj.time_click()
        sleep(2)

        dashboard_click_obj.recruitment_click()
        sleep(2)

        dashboard_click_obj.myinfo_click()
        sleep(2)

        dashboard_click_obj.performance_click()
        sleep(2)

        dashboard_click_obj.dashboard_click()
        sleep(2)

        dashboard_click_obj.directory_click()
        sleep(2)

        dashboard_click_obj.maintenance_click()
        sleep(2)
        self.driver.back()

        dashboard_click_obj.claim_click()
        sleep(2)

        dashboard_click_obj.buzz_click()
        sleep(2)