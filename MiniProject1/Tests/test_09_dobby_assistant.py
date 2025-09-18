# Test Classes contains test scripts and calling actions
# Importing pytest modules
import pytest
# Importing Class HomePage from home_page under Pages folder
from Pages.home_page import HomePage
# Importing Exceptions to use when error raises
from selenium.common.exceptions import NoSuchElementException


# To use setup fixture from conftest.py
@pytest.mark.usefixtures("setup")
class TestDobby:

    # test_dobby_assistant() validates that the Dobby Guvi Assistant is present on the page.
    def test_dobby_assistant(self):

        try:
            # This line creates an instance of the LoginPage class, and passes the WebDriver instance (self.driver) to it.
            home_page = HomePage(self.driver)

            # Checks whether dobby assistant is displayed on the page
            dobby_chatbot=home_page.dobby_assistant()
            assert dobby_chatbot.is_displayed(),"Dobby Assistant is not displayed"
            print("Dobby Assistant is present on the page")

        except NoSuchElementException:
            print("Dobby Assistant is not visible on the page")


    # test_invisibility_of_dobby_assistant() validates that the Dobby Guvi Assistant is invisible on the page.
    # This test fails because Dobby Assistant is always present on the page once loaded
    @pytest.mark.negative
    def test_invisibility_of_dobby_assistant(self):

      with pytest.raises(NoSuchElementException):
        # This line creates an instance of the LoginPage class, and passes the WebDriver instance (self.driver) to it.
            home_page = HomePage(self.driver)

            # Checks whether dobby assistant is displayed on the page
            dobby_chatbot = home_page.dobby_assistant()
            assert dobby_chatbot.is_displayed(), "Dobby Assistant is not displayed"
            print("Dobby Assistant is visible on the page")





        