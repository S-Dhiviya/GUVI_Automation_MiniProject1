# Automation Testing of EdTech Platform Web Application
# BASE PAGE FOR GUVI PORTAL
# Page classes represents the webpage.
# Importing WebDriverWait is used to explicitly wait for elements to appear, disappear,clickable
# Explicit wait is used to wait for specific condition to occur before proceeding to next.
from selenium.webdriver.support.ui import WebDriverWait
# Importing expected_conditions like url contains,presence of element,visibility of element
from selenium.webdriver.support import expected_conditions as EC
#Importing exceptions to raise when error occurs
from selenium.common.exceptions import TimeoutException,ElementNotInteractableException


# BasePage class contains methods to click,find,enter text in the element and get the URL,title of page
class BasePage:


    # Constructor method used to interact with Selenium Webdriver. Driver is passed from 'setup' code
    def __init__(self, driver):
        self.driver = driver


    # Finding the element using the locator with timeout of 5 seconds using explicit wait
    def find_element(self, locator, timeout=10):
        # Explicit wait until the element is located else raises TimeOutException
        try:
            return WebDriverWait(self.driver, timeout).until(EC.visibility_of_element_located(locator))
        except TimeoutException:
            print(f"Timeout: Element with locator {locator} not found")


    # Find and Click the element using the locator with timeout of 10 seconds using explicit wait
    def click_element(self, locator, timeout=10):
        # This uses find_element method to locate the element and then clicks it.
        try:
            element = self.find_element(locator, timeout)
            element.click()
        except ElementNotInteractableException:
            print(f" Element with locator {locator} is not interactable")


    # Find and Enter the text using the locator with timeout of 10 seconds using explicit wait
    def enter_text(self, locator, text, timeout=10):
        # This uses find_element method to locate the element and then types the given text.
        element = self.find_element(locator, timeout)
        # Clears the element before typing the text
        element.clear()
        element.send_keys(text)


    # get_current_url returns the current page URL
    def get_current_url(self):
        try:
            return self.driver.current_url
        except Exception as e:
            print(f"Failed to get current URL of the page:{e}")


    # get_title returns the page title
    def get_title(self):
        try:
            return self.driver.title
        except Exception as e:
            print(f"Failed to get current title of the page:{e}")