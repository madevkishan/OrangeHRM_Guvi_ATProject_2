from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from Test_locators.test_locators import AdminPage_Locators,Dashboardpage_Locators
from Test_utilities.customLogger import logGen

class AdminPage_Menu_Actions:

    def __init__(self, driver):
        self.admin_loc_obj = AdminPage_Locators()  # created an object for locator class
        self.dashboardpage_loc_obj = Dashboardpage_Locators()
        self.logs_obj = logGen.logger()
        self.driver = driver
        self.wait = WebDriverWait(self.driver,10)

    def click_admin_menu(self, driver):
        """
        click on Admin menu item
        :return:
        """
        admin_we = self.wait.until(EC.element_to_be_clickable((By.XPATH,self.admin_loc_obj.admin_loc_xpath)))
        admin_we.click()

    def admin_menu_validate(self):
        """
        Validate whether you find all the menus displayed in Admin Menu
        :return:
        """
        # admin_menus_we = self.wait.until(EC.presence_of_all_elements_located(By.XPATH, self.dashboardpage_loc_obj.a)))
        admin_menu_we = self.driver.find_elements(By.XPATH,self.dashboardpage_loc_obj.adminmenus_loc_menu_xpath)
        print("Number of elements:", len(admin_menu_we))
        self.logs_obj.info("Menus under 'Admin':")
        # count = 0
        # if count < len(admin_menu_we):
        #     for i in admin_menu_we:
        #         if i.is_displayed():        #             print(f'{i.text} is displayed')
        #             self.logs_obj.info(f'{i.text} is displayed')
        #         else:
        #             break
        # count += 1

        for i in range(len(admin_menu_we)):
            item = admin_menu_we[i]
            if item.is_displayed():
                print(f'{item.text} is displayed')
                self.logs_obj.info(f'{item.text} is displayed')
