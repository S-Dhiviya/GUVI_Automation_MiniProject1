# Test Classes contains test scripts and calling actions
# Importing pytest modules
import pytest
# Importing Class HomePage from home_page under Pages folder
from Pages.home_page import HomePage
# Importing Exceptions to use when error raises
from selenium.common.exceptions import NoSuchElementException


# To use setup fixture from conftest.py
@pytest.mark.usefixtures("setup")
class TestIcons:

    # test_menu_items() checks items like “Courses”, “LIVE Classes”, and “Practice” are displayed.
    def test_menu_items(self):

        # This line creates an instance of the LoginPage class, and passes the WebDriver instance (self.driver) to it.
        home_page = HomePage(self.driver)
        try:
            courses_button=home_page.find_element(*home_page.COURSE_BUTTON)
            liveclass_button=home_page.find_element(*home_page.LIVECLASSES_BUTTON)
            practice_button=home_page.find_element(*home_page.PRACTICE_BUTTON)

        except NoSuchElementException:
            print("There are no such menu items in homepage")

        # Assertions for Courses button to check visibility and accessibility
        assert courses_button.is_displayed(), "Courses button is not visible"
        assert courses_button.is_enabled(), "Courses button is not clickable"

        # Assertions for Live Classes button
        assert liveclass_button.is_displayed(), "Live Classes button is not visible"
        assert liveclass_button.is_enabled(), "Live Classes button is not clickable"

        # Assertions for Practice button
        assert practice_button.is_displayed(), "Practice button is not visible"
        assert practice_button.is_enabled(), "Practice button is not clickable"


    # test_invalid_menu_items() checks invalid items like “Courses”, “LIVE Classes”, and “Practice” are displayed.
    # This negative test passes by excepting NoSuchElementException
    @pytest.mark.negative
    def test_invalid_menu_items(self):

        # This line creates an instance of the LoginPage class, and passes the WebDriver instance (self.driver) to it.
        home_page = HomePage(self.driver)
        try:
            courses_button = home_page.find_element(*home_page.INVALID_COURSE_BUTTON)
            liveclass_button = home_page.find_element(*home_page.INVALID_LIVECLASSES_BUTTON)
            practice_button = home_page.find_element(*home_page.INVALID_PRACTICE_BUTTON)

            # Assertions to check visibility of menu items
            assert not courses_button.is_displayed(), "Courses button is visible"
            assert not liveclass_button.is_displayed(), "Live Classes button is visible"
            assert not practice_button.is_displayed(), "Practice button is visible"

        except NoSuchElementException:
            print("NoSuchElementException:Invalid Menu items not found in home page")

