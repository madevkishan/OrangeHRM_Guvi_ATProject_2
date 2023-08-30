from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from Test_locators.test_locators import AdminPage_Locators,Dashboardpage_Locators
from Test_utilities.customLogger import logGen

class DashboardPage_Menu_Actions:

    def __init__(self, driver):
        self.admin_loc_obj = AdminPage_Locators()  # created an object for locator class
        self.dashboardpage_loc_obj = Dashboardpage_Locators()
        self.logs_obj = logGen.logger()
        self.driver = driver
        self.wait = WebDriverWait(self.driver, 10)

    def dashboard_menu_validate(self):
        """
        Validate whether you find all the menus displayed on the Dashboard
        :return:
        """
        dashboard_menu_we = self.driver.find_elements(By.XPATH,self.dashboardpage_loc_obj.dashboard_loc_menus_xpath)
        print("Number of elements:", len(dashboard_menu_we))
        self.logs_obj.info("Menus present on 'Dashboard Page':")

        for i in range(12):  # Loop through upto Dashboard items
            menu_item = dashboard_menu_we[i]
            if menu_item.is_displayed():
                print(f'{menu_item.text} is displayed')
                self.logs_obj.info(f'{menu_item.text} is displayed')





