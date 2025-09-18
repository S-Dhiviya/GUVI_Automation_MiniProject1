# Importing By classes from selenium for locators
from selenium.webdriver.common.by import By
# To use the methods from base_page importing Class BasePage.
from Pages.base_page import BasePage
# Importing WebDriverWait is used to explicitly wait for elements to appear, disappear,clickable
from selenium.webdriver.support.ui import WebDriverWait
# Importing expected_conditions like url contains,presence of element,visibility of element
from selenium.webdriver.support import expected_conditions as EC



#HomePage inherits BasePage. LoginPage contains locators to be used in test cases.
class HomePage(BasePage):

    # LOCATORS - Uses find_element() from BasePage to locate these elements while doing interactions.
    # Courses, LiveClasses Button locator using XPATH
    COURSE_BUTTON = (By.XPATH, '//div[contains(@class,"basis-auto")]//child::a[1]')
    LIVECLASSES_BUTTON = (By.XPATH, '//p[@id="liveclasseslink"]')

    # Practice, Dobby assistant locator using XPATH
    PRACTICE_BUTTON = (By.XPATH, '//p[@id="practiceslink"]')
    DOBBY_ASSISTANT = (By.XPATH, '//div[@id="ym-auto-pop-up-container"]')

    # Invalid Courses, LiveClasses,Practice Button locator using XPATH
    INVALID_COURSE_BUTTON = (By.XPATH, '//div[contains(@class,"bas")]//child::a[1]')
    INVALID_LIVECLASSES_BUTTON = (By.XPATH, '//p[@id="liveclaslink"]')
    INVALID_PRACTICE_BUTTON = (By.XPATH, '//p[@id="practice"]')


    # Method to locate the dobby chatbot in the page
    def dobby_assistant(self):
        try:
            return WebDriverWait(self.driver, 15).until(EC.element_to_be_clickable(self.DOBBY_ASSISTANT))
        except Exception as e:
            print(f"Dobby Assistant is not found:{e}")


