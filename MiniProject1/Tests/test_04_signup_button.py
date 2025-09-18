# Test Classes contains test scripts and calling actions
# Importing pytest modules to use in test cases
import pytest
# Importing login page to use methods in it.
from Pages.login_page import LoginPage
# Importing Exceptions to use when error raises
from selenium.common import NoSuchElementException


# To use setup fixture from conftest.py
@pytest.mark.usefixtures("setup")
class TestSignupButton:

    #test_signup_button() checks the visibility and clickability of Sign-Up button.
    def test_signup_button(self):

        # This line creates an instance of the LoginPage class, and passes the WebDriver instance (self.driver) to it.
        login_page = LoginPage(self.driver)
        signup_button=login_page.find_element(*login_page.SIGNUP_BUTTON)

        # is_displayed()checks the visibility
        assert signup_button.is_displayed(),"SignUp button is not visible"
        # is_enabled() checks whether its clickable or not
        assert signup_button.is_enabled(), "SignUp button is not clickable"
        login_page.click_signup()
        print("Navigated to Signup page")


    # test_invalid_signup_button() checks the visibility and clickability of Invalid Sign-Up button.
    # This negative test passes since it handles using Exception Handling
    @pytest.mark.negative
    def test_invalid_signup_button(self):

        # This line creates an instance of the LoginPage class, and passes the WebDriver instance (self.driver) to it.
        login_page = LoginPage(self.driver)

        # Uses exception handling to access the Invalid Signup Button
        try:
            signup_button = login_page.find_element(*login_page.INVALID_SIGNUP_BUTTON)

            # If the button exists, it should NOT be visible or enabled
            # is_displayed()checks the visibility
            assert not  signup_button.is_displayed(), "SignUp button is visible"
            # is_enabled() checks whether its clickable or not
            assert not signup_button.is_enabled(), "SignUp button is clickable"

        # Element not found is expected, so test passes
        except NoSuchElementException:
            print("NoSuchElementException:Invalid Signup button not found")
