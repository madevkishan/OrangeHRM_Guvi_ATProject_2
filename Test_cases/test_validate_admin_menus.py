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
        # User Management Menu
        admin_obj.user_management(self.driver)
        sleep(2)

        # Job Menu
        admin_obj.job_menus(self.driver)
        sleep(2)

        admin_obj.job_titles(self.driver)
        sleep(2)

        admin_obj.paygrade()
        sleep(2)

        admin_obj.employment_status()
        sleep(2)

        admin_obj.job_categories()
        sleep(2)

        admin_obj.work_shifts()
        sleep(2)

        # Oranization Menu
        admin_obj.organization_menus(self.driver)
        sleep(1)

        admin_obj.general_information(self.driver)
        sleep(1)

        admin_obj.locations(self.driver)
        sleep(1)

        admin_obj.structure_1(self.driver)
        sleep(1)

        # Qualification Menu
        admin_obj.qualifications_menu(self.driver)
        sleep(2)

        admin_obj.skills(self.driver)
        sleep(2)

        admin_obj.education(self.driver)
        sleep(2)

        admin_obj.licenses(self.driver)
        sleep(2)

        admin_obj.languages(self.driver)
        sleep(3)

        admin_obj.membership(self.driver)
        sleep(3)

        # Nationalities Menu
        admin_obj.nationalities(self.driver)
        sleep(2)

        # Corporate Banking Menu
        admin_obj.corporate_branding(self.driver)
        sleep(2)

        # Configuration Menu
        admin_obj.configuration(self.driver)
        sleep(2)

        admin_obj.configuration_menus(self.driver)
        sleep(2)
        #
        admin_obj.email_config(self.driver)
        sleep(2)

        admin_obj.email_subscription(self.driver)
        sleep(2)

        admin_obj.localization(self.driver)
        sleep(2)

        admin_obj.language_packages(self.driver)
        sleep(2)

        admin_obj.modules(self.driver)
        sleep(2)

        admin_obj.socialmedia_auth(self.driver)
        sleep(2)

        admin_obj.register_client(self.driver)
        sleep(2)

        admin_obj.ldap_config(self.driver)
        sleep(2)
