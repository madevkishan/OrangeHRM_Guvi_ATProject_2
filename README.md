# OrangeHRM Guvi Project 2

Testscases dealing with requirement:
===================================

1. test_login_01_resetpwd.py = Forgot Password link validation on login Page

2. test_validate_admin_menus.py = Header Validation on Admin Page

3. test_validate_dashboard_menus.py = Main Menu Validation on Admin Page

PageObjects = For each Page,A CLASS has been created which contains the functions/tasks to be performed on that page 

Locators = To perform action on the webelements,we need to locate the webelements and they are defined in a separate class file,so it would be easy to maintain the code

Logs = As automation is a quick operation,it will be difficult for us to see what's opening,so its better to log our operations for better understanding 

Screenshots = Its a good practice to capture the screenshot of failed testcases.

Test data = It contains the common data which are to be used all over the testcases.

Test cases = Each testcase contains only the logic.

Reports = Tetscases Reports can be found in OrangeHRM_Guvi_ATProject_2/Reports/reports.html

Though it's not recommended to use implicit wait or sleep, I have used it show the navigation of each page
Please check automation.log also

