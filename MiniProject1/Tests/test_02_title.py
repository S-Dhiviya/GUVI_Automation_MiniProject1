# Test Classes contains test scripts and calling actions
# Importing pytest modules to use in test cases
import pytest
# Importing base page to use methods in it.
from Pages.base_page import BasePage


# To use setup fixture from conftest.py
@pytest.mark.usefixtures("setup")
class TestTitle:

    # test_webpage_title() checks the webpage title
    # Raises exception if it doesn't match
    def test_webpage_title(self):
        # This line creates an instance of the BasePage class, and passes the WebDriver instance (self.driver) to it.
        base_page = BasePage(self.driver)
        expected_value="GUVI | Learn to code in your native language"

        # Checks the matches of expected value using get_title() from Basepage
        assert base_page.get_title()== expected_value, "Title is incorrect"
        print("Title of the webpage is:GUVI | Learn to code in your native language")


    # test_negative_title() fails since the expected value doesn't match the title exists
    @pytest.mark.negative
    def test_negative_title(self):
        # This line creates an instance of the BasePage class, and passes the WebDriver instance (self.driver) to it.
        base_page = BasePage(self.driver)
        expected_value = "GUVI | Learn to code in your native"

        # Checks the matches of expected value using get_title() from Basepage
        assert base_page.get_title() == expected_value, "Title is incorrect"




