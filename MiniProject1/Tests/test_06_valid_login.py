# Test Classes contains test scripts and calling actions
# Importing pytest modules
import pytest
# Importing Class LoginPage from login_page under Pages folder
from Pages.login_page import LoginPage
# Importing WebDriverWait is used to explicitly wait for elements to appear, disappear,clickable
from selenium.webdriver.support.ui import WebDriverWait
# Importing expected_conditions like url contains,presence of element,visibility of element
from selenium.webdriver.support import expected_conditions as EC
# To reuse data from Utils folder like valid credentials
from Utils.config import valid_email,valid_password


# To use setup fixture from conftest.py
@pytest.mark.usefixtures("setup")
class TestValidLogin:

    # test_valid_login() enters valid data and moves into dashboard page
    def test_valid_login(self):

        # This line creates an instance of the LoginPage class, and passes the WebDriver instance (self.driver) to it.
        login_page = LoginPage(self.driver)
        # login_page object calls login() from login_page.py and enters username and password
        login_page.login(valid_email,valid_password)

        # Checks url of the dashboard page after login
        expected_url = "https://www.guvi.in/courses/?current_tab=myCourses"
        WebDriverWait(self.driver, 10).until(EC.url_contains(expected_url))

        # Assert the final URL
        assert expected_url in login_page.get_current_url()
        print("Logged in:", login_page.get_current_url())
