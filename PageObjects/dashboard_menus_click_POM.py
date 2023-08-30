from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from Test_locators.test_locators import AdminPage_Locators, Dashboardpage_Locators
from Test_utilities.customLogger import logGen
from time import sleep

class DashboardPage_ClickMenus_Actions:

    def __init__(self, driver):
        self.admin_loc_obj = AdminPage_Locators()  # created an object for locator class
        self.dashboardpage_loc_obj = Dashboardpage_Locators()
        self.logs_obj = logGen.logger()
        self.driver = driver
        self.wait = WebDriverWait(self.driver, 10)

    def pim_click(self):
        """
        Click on PIM Menu
        :return:
        """
        pim_menu_we = self.wait.until(EC.element_to_be_clickable((By.XPATH,self.dashboardpage_loc_obj.pim_loc_menu_xpath)))
        pim_menu_we.click()
        self.logs_obj.info("PIM Menu Clicked")
        sleep(2)

    def leave_click(self):
        """
        Click on LEAVE Menu
        :return:
        """
        leave_menu_we = self.wait.until(EC.element_to_be_clickable((By.XPATH,self.dashboardpage_loc_obj.leave_loc_menu_xpath)))
        leave_menu_we.click()
        self.logs_obj.info("Leave Menu Clicked")
        sleep(2)

    def time_click(self):
        """
        Click on Time Menu
        :return:
        """
        time_menu_we = self.wait.until(EC.element_to_be_clickable((By.XPATH,self.dashboardpage_loc_obj.time_loc_menu_xpath)))
        time_menu_we.click()
        self.logs_obj.info("Time Menu Clicked")
        sleep(2)

    def recruitment_click(self):
        """
        Click on Recruitment Menu
        :return:
        """
        recruitment_menu_we = self.wait.until(EC.element_to_be_clickable((By.XPATH,self.dashboardpage_loc_obj.recruitment_loc_menu_xpath)))
        recruitment_menu_we.click()
        self.logs_obj.info("Recruitment Menu Clicked")
        sleep(2)

    def myinfo_click(self):
        """
        Click on My Info Menu
        :return:
        """
        myinfo_we = self.wait.until(EC.element_to_be_clickable((By.XPATH,self.dashboardpage_loc_obj.myinfo_loc_menu_xpath)))
        myinfo_we.click()
        self.logs_obj.info("My Info Menu Clicked")
        sleep(2)

    def performance_click(self):
        """
        Click on Performance Menu
        :return:
        """
        performance_menu_we = self.wait.until(EC.element_to_be_clickable((By.XPATH,self.dashboardpage_loc_obj.performance_loc_menu_xpath)))
        performance_menu_we.click()
        self.logs_obj.info("Performance Menu Clicked")
        sleep(2)

    def dashboard_click(self):
        """
        Click on Dashboard Menu
        :return:
        """
        dashboard_menu_we = self.wait.until(EC.element_to_be_clickable((By.XPATH,self.dashboardpage_loc_obj.dashboard_loc_menus_xpath)))
        dashboard_menu_we.click()
        self.logs_obj.info("Leave Menu Clicked")
        sleep(2)

    def directory_click(self):
        """
        Click on Directory Menu
        :return:
        """
        directory_menu_we = self.wait.until(EC.element_to_be_clickable((By.XPATH,self.dashboardpage_loc_obj.directory_loc_menu_xpath)))
        directory_menu_we.click()
        self.logs_obj.info("Directory Menu Clicked")
        sleep(2)

    def maintenance_click(self):
        """
        Click on Maintenance Menu
        :return:
        """
        maintenance_menu_we = self.wait.until(EC.element_to_be_clickable((By.XPATH,self.dashboardpage_loc_obj.maintenance_loc_menu_xpath)))
        maintenance_menu_we.click()
        self.logs_obj.info("Maintenance Menu Clicked")
        sleep(2)

    def claim_click(self):
        """
        Click on CLAIM Menu
        :return:
        """
        claim_menu_we = self.wait.until(EC.element_to_be_clickable((By.XPATH,self.dashboardpage_loc_obj.claim_loc_menu_xpath)))
        claim_menu_we.click()
        self.logs_obj.info("Claim Menu Clicked")
        sleep(2)

    def buzz_click(self):
        """
        Click on BUZZ Menu
        :return:
        """
        buzz_menu_we = self.wait.until(EC.element_to_be_clickable((By.XPATH, self.dashboardpage_loc_obj.buzz_loc_menu_xpath)))
        buzz_menu_we.click()
        self.logs_obj.info("Buzz Menu Clicked")
        sleep(2)
