class LoginPage_Locators:
    def __init__(self):
        pass
    username_loc_name = "username"
    password_loc_name = "password"
    login_loc_btn_xpath = '//button[@type="submit"]'
    dashboard_page = "//h6[text()='Dashboard']"
    invalid_loc_text_xpath = "//p[text()='Invalid credentials']"
    forgotpwd_loc_link_xpth = '//p[@class="oxd-text oxd-text--p orangehrm-login-forgot-header"]'

class Resetpwd_Locators:
    username_loc_txt_name = "username"
    resetpwd_loc_btn_xpath = '//button[@type="submit"]'
    resetmsg_loc_title_xpath = '//h6[@class="oxd-text oxd-text--h6 orangehrm-forgot-password-title"]'

class Dashboardpage_Locators:
    # dashboard_loc_menus_xpath ="(//*[contains(@class,'oxd-main-menu')])[5]//following::li"
    # adminmenus_loc_menu_xpath = '(//nav[@role="navigation"])[2]'
    # adminmenus_loc_menu_xpath = "(//*[contains(@role,'navigation')])[2]//following::li"
    titleorangehrm_loc_txt_xpath = "//title[text()='OrangeHRM']"
    dashboard_loc_menus_xpath = "//ul[@class='oxd-main-menu']//li"
    adminmenus_loc_menu_xpath = "//nav[@class ='oxd-topbar-body-nav']//li"
    pim_loc_menu_xpath = '//a[@href="/web/index.php/pim/viewPimModule"]'
    leave_loc_menu_xpath ='//a[@href="/web/index.php/leave/viewLeaveModule"]'
    time_loc_menu_xpath = '//a[@href="/web/index.php/time/viewTimeModule"]'
    recruitment_loc_menu_xpath = '//a[@href="/web/index.php/recruitment/viewRecruitmentModule"]'
    myinfo_loc_menu_xpath = '//a[@href="/web/index.php/pim/viewMyDetails"]'
    performance_loc_menu_xpath = '//a[@href = "/web/index.php/performance/viewPerformanceModule"]'
    dashboard_loc_menu_xpath = '//a[@href="/web/index.php/dashboard/index"]'
    directory_loc_menu_xpath = '//a[@href="/web/index.php/directory/viewDirectory"]'
    maintenance_loc_menu_xpath = '//a[@href="/web/index.php/maintenance/viewMaintenanceModule"]'
    claim_loc_menu_xpath = '//a[@href="/web/index.php/claim/viewClaimModule"]'
    buzz_loc_menu_xpath = '//a[@href="/web/index.php/buzz/viewBuzz"]'

class AdminPage_Locators:
    admin_loc_xpath = '//a[@href="/web/index.php/admin/viewAdminModule"]'
    # User management menu and submenu locators
    # user_mgmt_loc_dd_xpath = '//li[@class="--active oxd-topbar-body-nav-tab --parent --visited"]'
    user_mgmt_loc_dd_xpath = "//span[text()='User Management ']"

    # Job menu and sub-menu locators
    job_loc_dd_xpath = "//span[text()='Job ']"
    job_menus_loc_xpath = '//ul[@class="oxd-dropdown-menu"]//li'
    job_titles_loc_xpath = "//a[text()='Job Titles']"
    paygrade_loc_xpath = "//a[text()='Pay Grades']"
    empstatus_loc_xpath = "//a[text()='Employment Status']"
    job_categories_loc_xpath = "//a[text()='Job Categories']"
    workshifts_loc_xpath = "//a[text()='Work Shifts']"

    # Organization menu and sub-menu locators
    organization_loc_xpath = "//span[text()='Organization ']"
    organization_menus_loc_xpath = '//ul[@class="oxd-dropdown-menu"]//li'
    generalinfo_loc_xpath = "//a[text()='General Information']"
    locations_loc_xpath = "//a[text()='Locations']"
    structure_loc_xpath = "//a[text()='Structure']"

    # Qualification menu and sub-menu locators
    qualification_loc_xpath = "//span[text()='Qualifications ']"
    qualification_menus_loc_xpath = '//ul[@class="oxd-dropdown-menu"]//li'
    skills_loc_xpath = "//a[text()='Skills']"
    education_loc_xpath = "//a[text()='Education']"
    licenses_loc_xpath = "//a[text()='Licenses']"
    languages_loc_xpath = "//a[text()='Languages']"
    memberships_loc_xpath = "//a[text()='Memberships']"

    nationalities_loc_xpath = "//a[text()='Nationalities']"
    corporatebranding_loc_xpath = "//a[text()='Corporate Branding']"

    # Configuration menu and sub-menu locators
    configuration_loc_xpath = "//span[text()='Configuration ']"
    configuration_menus_loc_xpath = '//ul[@class="oxd-dropdown-menu"]//li'
    emailconfig_loc_xpath = "//a[text()='Email Configuration']"
    emailsub_loc_xpath = "//a[text()='Email Subscriptions']"
    localization_loc_xpath = "//a[text()='Localization']"
    languagepackages_loc_xpath = "//a[text()='Language Packages']"
    modules_loc_xpath = "//a[text()='Modules']"
    socialmedia_loc_xpath = "//a[text()='Social Media Authentication']"
    register_loc_xpath = "//a[text()='Register OAuth Client']"
    ldap_loc_xpath = "//a[text()='LDAP Configuration']"


    users_loc_dd_xpath = '//a[@role="menuitem"]'
    username_loc_textbox_xpath ='(//input[@class="oxd-input oxd-input--active"])[2]'
    userrole_loc_dropdown_xpath = "(//i[@class='oxd-icon bi-caret-down-fill oxd-select-text--arrow'])[1]"
    employeename_loc_textbox_xpath = '//input[@placeholder="Type for hints..."]'
    status_loc_dropdown_xpath = "(//i[@class='oxd-icon bi-caret-down-fill oxd-select-text--arrow'])[2]"
    add_user_loc_xpath = '//button[@type="button" and @class="oxd-button oxd-button--medium oxd-button--secondary"]'
    # dashboard_page = "//h6[text()='Dashboard']"

class PimPage_EmployeeList_Locators:
    # pim_loc_menu_xpath = '//a[@href="/web/index.php/pim/viewPimModule"]'
    empname_loc_textbox_xpath = '(//input[@placeholder="Type for hints..."])[1]'
    search_loc_btn_xpath = '//button[@type="submit"]'
    edit_loc_btn_xpath = '//button[@class="oxd-icon-button oxd-table-cell-action-space"][2]'
    # delete_loc_btn_xpath = '(//button[@type="button"])[5]'
    delete_loc_btn_xpath = '//button[@class ="oxd-icon-button oxd-table-cell-action-space"][1]'
    alert_loc_yesbtn_xpath = '//button[@class ="oxd-button oxd-button--medium oxd-button--label-danger orangehrm-button-margin"]'

class PimAddEmployee_Locators:
    addemp_loc_tab_xpath = "//a[text()='Add Employee']"
    fname_loc_text_xpath = "//input[@name='firstName']"
    midname_loc_text_xpath = "//input[@name='middleName']"
    lastname_loc_text_xpath = "//input[@name='lastName']"
    empid_loc_text_xpath = '(//input[@class="oxd-input oxd-input--active"])[2]'
    save_loc_btn_xpath = '//button[@type="submit"]'

class MyinfoPage_Locators:
    # Personal Field Locators
    firstname_loc_text_name = 'firstName'
    middlename_loc_text_name = 'middleName'
    lastname_loc_text_name = 'lastName'
    nickname_loc_text_xpath = '//*[@class="oxd-input oxd-input--active"]//following::input[4]'
    empid_loc_text_xpath = '//*[@class="oxd-input oxd-input--active"]//following::input[5]'
    otherid_loc_text_xpath = '//*[@class="oxd-input oxd-input--active"]//following::input[6]'
    driverlicense_loc_text_xpath ='//*[@class="oxd-input oxd-input--active"]//following::input[7]'
    liceexpiry_loc_cal_xpath ='(//input[@placeholder="yyyy-mm-dd"])[1]'
    ssnnum_loc_text_xpath = '//*[@class="oxd-input oxd-input--active"]//following::input[9]'
    sinnum_loc_text_xpath = '//*[@class="oxd-input oxd-input--active"]//following::input[10]'
    nationality_loc_ddown_xpath ='//*[@class="oxd-select-text-input"]//following::div[1]'
    nationality_loc_selectcountry_xpath = '(//div[@role="listbox"]//child::div)[3]'
    marital_loc_ddown_xpath = '//*[@class="oxd-icon bi-caret-down-fill oxd-select-text--arrow"]//following::div[8]'
    marital_loc_select_xpath = '(//div[@role="listbox"]//child::div)[4]'
    # dob_loc_cal_xpath = '//*[@class="oxd-input oxd-input--active"]//following::input[11]'
    dob_loc_cal_xpath = '(//input[@ placeholder="yyyy-mm-dd"])[2]'
    # gender_loc_xpath = '//input[@value="2"]' # This locator doesnt work,ElementInterceptedException
    gender_loc_xpath = '(//span[@class="oxd-radio-input oxd-radio-input--active --label-right oxd-radio-input"])[2]'
    # military_loc_xpath = '//input[@fdprocessedid="n89495"]' #This xpath failed,NosuchElement exception
    # military_loc_xpath = '//*[@class="oxd-input oxd-input--active"]//following::input[14]'
    military_loc_text_xpath = "(//input[@class='oxd-input oxd-input--active'])[10]"
    smoker_loc_radio_xpath ='//i[@class="oxd-icon bi-check oxd-checkbox-input-icon"]'
    save_personal_btn_loc_xpath ='//button[@type="submit"]'

    # Custom Field Locators
    blood_loc_ddown_xpath = '(//div[@class="oxd-select-text--after"])[3]'
    blood_loc_selecttype_xpath = "(//div[@role='listbox']//child::div)[3]"
    savecustom_loc_btn_xpath = '(//button[@type="submit"])[2]'

    #Attachments
    attachadd_loc_btn_xpath = '(//button[@type="button"])[3]'
    browse_loc_btn_xpath = '//div[@class="oxd-file-button"]'
    attachsave_loc_btn_xpath = '(//button[@type="submit"])[3]'