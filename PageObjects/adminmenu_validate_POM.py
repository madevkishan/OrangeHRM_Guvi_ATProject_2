from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.common.action_chains import ActionChains
from Test_locators.test_locators import AdminPage_Locators,Dashboardpage_Locators
from Test_utilities.customLogger import logGen
from time import sleep
class AdminPage_Menu_Actions:

    def __init__(self, driver):
        self.admin_loc_obj = AdminPage_Locators()  # created an object for locator class
        self.dashboardpage_loc_obj = Dashboardpage_Locators()
        self.logs_obj = logGen.logger()
        self.driver = driver
        self.wait = WebDriverWait(self.driver,20)
        self.action_obj = ActionChains(self.driver)

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

    # Validating the sub-menus
    def user_management(self,driver):
        """
        Click on USER MANAGEMENT Menu
        :return:
        """
        user_mgmt_we = self.wait.until(EC.element_to_be_clickable((By.XPATH,self.admin_loc_obj.user_mgmt_loc_dd_xpath)))
        print(f'{user_mgmt_we.text} is displayed')
        user_mgmt_we.click()
        sleep(2)
        users_we = self.driver.find_element(By.XPATH, self.admin_loc_obj.users_loc_dd_xpath)
        self.logs_obj.info(f'{users_we.text} is displayed')
        self.action_obj.move_to_element(users_we).click(users_we).perform()
        sleep(2)

    def job_menus(self,driver):
        """
        Click on JOB Menu and identify the sub-menus available and displayed
        :return:
        """

        job_we = self.wait.until(EC.element_to_be_clickable((By.XPATH, self.admin_loc_obj.job_loc_dd_xpath)))
        job_we.click()
        sleep(2)

        job_menus_we = self.driver.find_elements(By.XPATH,self.admin_loc_obj.job_menus_loc_xpath)
        self.logs_obj.info("Job sub-menus are:")
        for i in range(len(job_menus_we)):
            job_menus_title = job_menus_we[i]
            if job_menus_title.is_displayed:
                print(f'{job_menus_title.text} is displayed')
                self.logs_obj.info(f'{job_menus_title.text} is displayed')

    def job_titles(self,driver):
        """
        Clicking on Job Titles sub-menu
        :return:
        """

        job_titles_we = self.wait.until(EC.element_to_be_clickable((By.XPATH,self.admin_loc_obj.job_titles_loc_xpath)))
        print(f'{job_titles_we.text} is clicked')
        job_titles_we.click()
        sleep(1)

    def paygrade(self):
        """
        Clicking on Paygrade sub-Menu
        :return:
        """
        job_we = self.wait.until(EC.element_to_be_clickable((By.XPATH, self.admin_loc_obj.job_loc_dd_xpath)))
        job_we.click()
        sleep(2)

        paygrades_we = self.wait.until(EC.element_to_be_clickable((By.XPATH,self.admin_loc_obj.paygrade_loc_xpath)))
        paygrades_we.click()
        sleep(2)

    def employment_status(self):
        """
        Clicking on Employment Status sub-Menu
        :return:
        """
        job_we = self.wait.until(EC.element_to_be_clickable((By.XPATH, self.admin_loc_obj.job_loc_dd_xpath)))
        job_we.click()
        sleep(2)

        emp_status_we = self.wait.until(EC.element_to_be_clickable((By.XPATH, self.admin_loc_obj.empstatus_loc_xpath)))
        emp_status_we.click()
        sleep(2)

    def job_categories(self):
        """
        Clicking on Job Categories sub-Menu
        :return:
        """
        job_we = self.wait.until(EC.element_to_be_clickable((By.XPATH, self.admin_loc_obj.job_loc_dd_xpath)))
        job_we.click()
        sleep(2)

        job_categories_we = self.wait.until(EC.element_to_be_clickable((By.XPATH, self.admin_loc_obj.job_categories_loc_xpath)))
        job_categories_we.click()
        sleep(2)

    def work_shifts(self):
        """
        Clicking on Workshifts sub-Menu
        :return:
        """
        job_we = self.wait.until(EC.element_to_be_clickable((By.XPATH, self.admin_loc_obj.job_loc_dd_xpath)))
        job_we.click()
        sleep(2)

        workshifts_we = self.wait.until(EC.element_to_be_clickable((By.XPATH, self.admin_loc_obj.workshifts_loc_xpath)))
        workshifts_we.click()
        sleep(2)

    def organization_menus(self,driver):
        """
        Click on Organization Menu and identify the sub-menus available
        :return:
        """
        org_we = self.wait.until(EC.element_to_be_clickable((By.XPATH, self.admin_loc_obj.organization_loc_xpath)))
        org_we.click()
        sleep(2)

        org_menus_we = self.driver.find_elements(By.XPATH,self.admin_loc_obj.organization_menus_loc_xpath)

        self.logs_obj.info("Organization sub-menus are:")
        for i in range(len(org_menus_we)):
            org_menus_title = org_menus_we[i]
            if org_menus_title.is_displayed:
                print(f'{org_menus_title.text} is displayed')
                self.logs_obj.info(f'{org_menus_title.text} is displayed')

    def general_information(self,driver):
        """
            Clicking on General Information sub-menu
        :return:
        """
        org_we = self.wait.until(EC.element_to_be_clickable((By.XPATH, self.admin_loc_obj.organization_loc_xpath)))
        org_we.click()
        sleep(2)

        geninfo_we = self.wait.until(EC.element_to_be_clickable((By.XPATH, self.admin_loc_obj.generalinfo_loc_xpath)))
        geninfo_we.click()
        sleep(2)
    def locations(self,driver):
        """
        Clicking on Locatons sub-Menu
        :return:
        """
        org_we = self.wait.until(EC.element_to_be_clickable((By.XPATH, self.admin_loc_obj.organization_loc_xpath)))
        org_we.click()
        sleep(2)

        locations_we = self.wait.until(EC.element_to_be_clickable((By.XPATH, self.admin_loc_obj.locations_loc_xpath)))
        locations_we.click()
        sleep(2)

    def structure_1(self,drtver):
        """
        Clicking on Structure sub-Menu
        :return:
        """
        org_we = self.wait.until(EC.element_to_be_clickable((By.XPATH, self.admin_loc_obj.organization_loc_xpath)))
        org_we.click()
        sleep(2)

        structure_we= self.wait.until(EC.element_to_be_clickable((By.XPATH, self.admin_loc_obj.structure_loc_xpath)))
        structure_we.click()
        sleep(2)


    def qualifications_menu(self,driver):
        """
        Clicking on Qualifications Menu
        :return:
        """
        qualification_we = self.wait.until(EC.element_to_be_clickable((By.XPATH,self.admin_loc_obj.qualification_loc_xpath)))
        qualification_we.click()

        qualifications_menu_we = self.driver.find_elements(By.XPATH,self.admin_loc_obj.qualification_menus_loc_xpath)

        self.logs_obj.info("Qualification sub-menus are:")
        for i in range(len(qualifications_menu_we)):
            qualification = qualification_we[i]
            if qualification.is_displayed():
                print(f'{qualification.text} is displayed')
                self.logs_obj.info(f'{qualification.text} is displayed')


    def skills(self, driver):
        """
        Clicking on Skills sub-Menu
        :return:
        """
        skills_we = self.wait.until(EC.element_to_be_clickable((By.XPATH,self.admin_loc_obj.skills_loc_xpath)))
        self.logs_obj.info(f'{skills_we.text} is clicked')
        skills_we.click()

    def education(self,driver):
        """
        Clicking on Education sub-Menu
        :return:
        """
        qualification_we = self.wait.until(EC.element_to_be_clickable((By.XPATH,self.admin_loc_obj.qualification_loc_xpath)))
        qualification_we.click()

        education_we = self.wait.until(EC.element_to_be_clickable((By.XPATH,self.admin_loc_obj.education_loc_xpath)))
        self.logs_obj.info(f'{education_we.text} is clicked')
        education_we.click()

    def licenses(self,driver):
        """
        Clicking on Licenses sub-Menu
        :return:
        """
        qualification_we = self.wait.until(EC.element_to_be_clickable((By.XPATH,self.admin_loc_obj.qualification_loc_xpath)))
        qualification_we.click()

        licenses_we = self.wait.until(EC.element_to_be_clickable((By.XPATH,self.admin_loc_obj.licenses_loc_xpath)))
        self.logs_obj.info(f'{licenses_we.text} is clicked')
        licenses_we.click()

    def languages(self,driver):
        """
        Clicking on Languages sub-Menu
        :return:
        """
        qualification_we = self.wait.until(EC.element_to_be_clickable((By.XPATH,self.admin_loc_obj.qualification_loc_xpath)))
        qualification_we.click()

        languages_we = self.wait.until(EC.element_to_be_clickable((By.XPATH,self.admin_loc_obj.languages_loc_xpath)))
        self.logs_obj.info(f'{languages_we.text} is clicked')
        languages_we.click()

    def membership(self,driver):
        """
        Clicking on Membership sub-Menu
        :return:
        """
        qualification_we = self.wait.until(EC.element_to_be_clickable((By.XPATH,self.admin_loc_obj.qualification_loc_xpath)))
        qualification_we.click()

        memberships_we = self.wait.until(EC.element_to_be_clickable((By.XPATH,self.admin_loc_obj.memberships_loc_xpath)))
        self.logs_obj.info(f'{memberships_we.text} is clicked')
        memberships_we.click()

    def nationalities(self,driver):
        """
        Clicking on Nationalities sub-Menu
        :return:
        """

        nationalities_we = self.wait.until(EC.element_to_be_clickable((By.XPATH,self.admin_loc_obj.nationalities_loc_xpath)))
        self.logs_obj.info(f'{nationalities_we.text} is clicked')
        nationalities_we.click()

    def corporate_branding(self,driver):
        """
        Clicking on Corporate Branding sub-Menu
        :return:
        """
        corporatebranding_we = self.wait.until(EC.element_to_be_clickable((By.XPATH, self.admin_loc_obj.corporatebranding_loc_xpath)))
        self.logs_obj.info(f'{corporatebranding_we.text} is clicked')
        corporatebranding_we.click()

    def configuration(self, driver):
        """
        Clicking on Configuration Menu
        :return:
        """
        # configuration_loc_xpath = self.admin_loc_obj.configuration_loc_xpath
        # print(f"Trying to locate element with XPath: {configuration_loc_xpath}")

        configuration_we = self.wait.until(EC.element_to_be_clickable((By.XPATH,self.admin_loc_obj.configuration_loc_xpath)))
        # self.logs_obj.info(f'{configuration_we.text} is clicked')
        configuration_we.click()

    def configuration_menus(self, driver):
        """
        Displaying submenus available in configuration menu
        :return:
        """
        configuration_we = self.wait.until(EC.element_to_be_clickable((By.XPATH,self.admin_loc_obj.configuration_loc_xpath)))
        configuration_we.click()

        config_menus_we = self.driver.find_elements(By.XPATH,self.admin_loc_obj.configuration_menus_loc_xpath)

        self.logs_obj.info("Configuration sub-menus are:")
        for i in range(len(config_menus_we)):
            config_menu = config_menus_we[i]
            if config_menu.is_displayed():
                print(f'{config_menu.text} is displayed')
                self.logs_obj.info(f'{config_menu.text} is displayed')

    def email_config(self,driver):
        """
        Clicking on Email configuration submenu
        :return:
        """
        configuration_we = self.wait.until(EC.element_to_be_clickable((By.XPATH, self.admin_loc_obj.configuration_loc_xpath)))
        configuration_we.click()

        email_config_we = self.wait.until(EC.element_to_be_clickable((By.XPATH,self.admin_loc_obj.emailconfig_loc_xpath)))
        # self.logs_obj.info(f'{email_config_we.text} is displayed')
        email_config_we.click()

    def email_subscription(self,driver):
        """
        Clicking on Email Subscription submenu
        :return:
        """
        configuration_we = self.wait.until(EC.element_to_be_clickable((By.XPATH, self.admin_loc_obj.configuration_loc_xpath)))
        configuration_we.click()

        email_subscription_we = self.wait.until(EC.element_to_be_clickable((By.XPATH,self.admin_loc_obj.emailsub_loc_xpath)))
        # self.logs_obj.info(f'{email_subscription_we.text} is displayed')
        email_subscription_we.click()

    def localization(self,driver):
        """
        Clicking on Localization submenu
        :return:
        """
        configuration_we = self.wait.until(EC.element_to_be_clickable((By.XPATH, self.admin_loc_obj.configuration_loc_xpath)))
        configuration_we.click()

        localization_we = self.wait.until(EC.element_to_be_clickable((By.XPATH,self.admin_loc_obj.localization_loc_xpath)))
        self.logs_obj.info(f'{localization_we.text} is displayed')
        localization_we.click()

    def language_packages(self,driver):
        """
        Clicking on Language Packages submenu
        :return:
        """
        configuration_we = self.wait.until(EC.element_to_be_clickable((By.XPATH, self.admin_loc_obj.configuration_loc_xpath)))
        configuration_we.click()

        lang_packages_we = self.wait.until(EC.element_to_be_clickable((By.XPATH,self.admin_loc_obj.languagepackages_loc_xpath)))
        self.logs_obj.info(f'{lang_packages_we.text} is displayed')
        lang_packages_we.click()

    def modules(self,driver):
        """
        Clicking on Modules submenu
        :return:
        """
        configuration_we = self.wait.until(EC.element_to_be_clickable((By.XPATH, self.admin_loc_obj.configuration_loc_xpath)))
        configuration_we.click()

        modules_we = self.wait.until(EC.element_to_be_clickable((By.XPATH,self.admin_loc_obj.modules_loc_xpath)))
        self.logs_obj.info(f'{modules_we.text} is displayed')
        modules_we.click()

    def socialmedia_auth(self,driver):
        """
        Clicking on Email Subscription submenu
        :return:
        """
        configuration_we = self.wait.until(EC.element_to_be_clickable((By.XPATH, self.admin_loc_obj.configuration_loc_xpath)))
        configuration_we.click()

        socialmedia_auth_we = self.wait.until(EC.element_to_be_clickable((By.XPATH,self.admin_loc_obj.socialmedia_loc_xpath)))
        self.logs_obj.info(f'{socialmedia_auth_we.text} is displayed')
        socialmedia_auth_we.click()

    def register_client(self,driver):
        """
        Clicking on Register OAuth Client submenu
        :return:
        """
        configuration_we = self.wait.until(EC.element_to_be_clickable((By.XPATH, self.admin_loc_obj.configuration_loc_xpath)))
        configuration_we.click()

        register_we = self.wait.until(EC.element_to_be_clickable((By.XPATH,self.admin_loc_obj.register_loc_xpath)))
        self.logs_obj.info(f'{register_we.text} is displayed')
        register_we.click()

    def ldap_config(self,driver):
        """
        Clicking on LDAP Configuration submenu
        :return:
        """
        configuration_we = self.wait.until(EC.element_to_be_clickable((By.XPATH, self.admin_loc_obj.configuration_loc_xpath)))
        configuration_we.click()

        ldap_we = self.wait.until(EC.element_to_be_clickable((By.XPATH,self.admin_loc_obj.ldap_loc_xpath)))
        self.logs_obj.info(f'{ldap_we.text} is displayed')
        ldap_we.click()
