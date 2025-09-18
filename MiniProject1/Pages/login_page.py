# Importing By classes from selenium for locators
from selenium.webdriver.common.by import By
# Importing Exceptions to use when error raises
from selenium.common.exceptions import NoSuchElementException
# To use the methods from base_page importing Class BasePage.
# from folder_name.file_name import Class_name
from Pages.base_page import BasePage


# LoginPage inherits BasePage. LoginPage contains locators and methods to interact with locators.
class LoginPage(BasePage):


    # LOCATORS - Uses find_element() from BasePage to locate these elements while doing interactions.
    # Login,Signup Button locator using XPATH
    LOGIN_ICON = (By.XPATH, '//a[@id="login-btn"]')
    SIGNUP_BUTTON = (By.XPATH, '//a[text()="Sign up"]')

    # Email and password box,login button locator using XPATH
    USERNAME_INPUT = (By.XPATH, '//input[@id="email"]')
    PASSWORD_INPUT = (By.XPATH, '//input[@id="password"]')
    LOGIN_BUTTON = (By.XPATH, '//a[@id="login-btn"]')

    # Dropdown and Logout button locator using XPATH
    DROPDOWN=(By.XPATH,'//div[contains(@class,"dropdown")]')
    LOGOUT_BUTTON = (By.XPATH, '//li[@id="dropdown_contents"]//child::div')

    # Error message locator using XPATH
    ERROR_MESSAGE = (By.XPATH, '//div[@class="invalid-feedback"]')
    EMAIL_ERROR_MESSAGE=(By.XPATH,'//input[@id="email"]/following::div[1]')

    # Invalid login, signup locator for negative test case
    INVALID_LOGIN_BUTTON = (By.XPATH, '//a[@id="loginnbtn"]')
    INVALID_SIGNUP_BUTTON = (By.XPATH, '//a[text()="sign"]')


    # METHODS TO INTERACT WITH THE ELEMENTS
    # click_signup() is used to navigate to sign up page
    def click_signup(self):
        self.click_element(self.SIGNUP_BUTTON)


    # click_login() is used to navigate to login page
    def click_login(self):
        self.click_element(self.LOGIN_ICON)


    # login() is used to find username and password and enter the valid data and to click login button
    def login(self, username, password):

        # Clicks the login icon after locating the self.LOGIN_ICON
        self.click_element(self.LOGIN_ICON)

        # self.USERNAME_INPUT,self.PASSWORD_INPUT are locators. username,password are the text to be entered
        # After entering valid clicks login to navigate to courses page
        self.enter_text(self.USERNAME_INPUT, username)
        self.enter_text(self.PASSWORD_INPUT, password)
        self.click_element(self.LOGIN_BUTTON)


    # logout() is used to click the profile dropdown and clicks logout. After logout it navigates to login page
    def logout(self):
        self.click_element(self.DROPDOWN)
        self.click_element(self.LOGOUT_BUTTON)
        self.find_element(self.LOGIN_BUTTON)


    # login_error_message() is used to return the error message if there are invalid credentials
    def login_error_message(self):
        try:
            error_element = self.find_element(self.ERROR_MESSAGE)
            return error_element.text
        except NoSuchElementException:
            return







