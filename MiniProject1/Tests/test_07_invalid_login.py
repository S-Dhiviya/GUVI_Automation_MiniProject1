# Test Classes contains test scripts and calling actions
# Importing pytest modules to use in test cases
import pytest
# Importing CSV and OS for utilizing CSV file[CSV File is stored under Data folder]
import csv
import os
# Importing login page to use methods in it.
from Pages.login_page import LoginPage


# get_login_data() locates the CSV file and reads the data
def get_login_data():
    login_data = []
    # Get the directory of the current script
    current_dir = os.path.dirname(__file__)
    # Construct the correct path to the CSV file
    data_file = os.path.join(current_dir, '../Data', 'invalid_login_data.csv')


    # Read the CSV file
    with open(data_file, newline='') as file:
        reader = csv.DictReader(file)
        for row in reader:
            # Ensure each row is treated as a dictionary
            username = row['username']
            password = row['password']
            login_data.append((username, password))
    return login_data


# To use setup fixture from conftest.py
@pytest.mark.usefixtures("setup")
class TestInvalidLogin:

    # test_invalid_login() enters invalid data and gets error message
    # This test fails since it cannot enter dashboard page
    @pytest.mark.parametrize("username,password",get_login_data())
    def test_invalid_login(self,username,password):

        # This line creates an instance of the LoginPage class, and passes the WebDriver instance (self.driver) to it.
        login_page = LoginPage(self.driver)
        # login_page object calls login() from login_page.py and enters username and password
        login_page.login(username,password)

        # Checks url of the page after login
        expected_url = "https://www.guvi.in/courses/?current_tab=myCourses"

        # Assert the final URL with invalid credentials
        error_msg = login_page.login_error_message()
        assert expected_url in login_page.get_current_url(),print(error_msg)



        
