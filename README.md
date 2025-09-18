               ** Automation Testing of EdTech Platform Web Application(GUVI Website)**
		
This project automates the testing of the GUVI Web Application (https://www.guvi.in) by simulating real user actions and validating critical UI functionalities. It ensures the reliability of key components through both positive and negative test scenarios along with cross browser validation.

Test script is written using Selenium with Python and Pytest along with the Page Object Model framework(POM)and also follows OOPS principles.The test data is externalized (CSV) using Data Driven framework, and common configurations are handled in config.py. Data Driven framework is followed to test the invalid login credentilas in GUVI website.It includes 10 detailed test cases  like verifying page behavior, accessibility of critical elements, navigation flows, and login and logout functionalities.



**Project Architecture :**

**MiniProject1/**
│
├── **Data/**
│   ├── __init__.py
│   ├── invalid_login_data.csv
│
├── **Pages/**
│   ├── __init__.py
│   ├── base_page.py
│   ├── login_page.py
│   ├── home_page.py
│
├── **Tests/**
│   ├── __init__.py
│   ├── conftest.py
│   ├── test_01_url.py
│   ├── test_02_title.py
│   ├── test_03_login_button.py
│   ├── test_04_signup_button.py
│   ├── test_05_signin.py
│   ├── test_06_valid_login.py
│   ├── test_07_invalid_login.py
│   ├── test_08_menu_icons.py
│   ├── test_09_dobby_assistant.py
│   ├── test_10_logout.py
│
├── **Utils/**
│   ├── __init__.py
│   ├── config.py
│
├── requirements.txt
├── README.md



**Tools & Technologies:**
*     Selenium WebDriver
*     Python 
*     Pytest
*     OOPS
*     Page Object Model (POM)
*     Data Driven Framework
*     Test Data(CSV file)
*     Explicit Waits
*     Exception Handling
*     Pytest HTML Reports



**Test Suite :**

Test Case 1: Check whether the URL https://www.guvi.in is valid or not.

	* Positive case: Properly opens chrome and navigates to GUVI
	* Negative case: Open Chrome but doesn’t navigate to GUVI

Test Case 2: Verify whether the title of the webpage is correct.

	* Positive case: Exactly matches the title “GUVI | Learn to code in your native language”
	* Negative case: Doesn’t match the given title and displays an error message.

Test Case 3:Login button visibility and clickability

	* Positive case: Assert login button is visible and interactable.Clicking login button navigates to https://www.guvi.in/sign-in/
	* Negative case: Assert invalid login button is visible and interactable. Excepts NoSuchElementException if invalid login button is not found.

Test Case 4: SignUp button visibility and clickability

	* Positive case: Assert signup button is visible and interactable.Clicking signup button navigates to https://www.guvi.in/register/
	* Negative case: Assert invalid signup button is visible and interactable. Excepts NoSuchElementException if invalid signup button is not found.

Test Case 5:  Navigation to the Sign-In page via the Sign-Up button.

	* Positive case: Clicking signup button navigates to https://www.guvi.in/register/.Checks the redirected url matches the sign-in page.
	* Negative case: Navigation to the Sign-In page and asserts Invalid Signin URL matches with current URL.

Test Case 6: Login functionality with valid credentials.

	* Enters valid email and password and clicks login button
	* Enters the dashboard/profile page
	* Check the dashboard url https://www.guvi.in/courses/?current_tab=myCourses

Test Case 7: Login functionality with invalid credentials.

	* Enters invalid email and password and clicks login button follows Data Driven Framework with multiple set of invalid data in CSV file.
	* Displays error message as “Incorrect Email or Password” or "Hey, Did you forgot your password? Try again".

Test Case 8: Check menu items like “Courses”, “LIVE Classes”, and “Practice” are displayed.

	* Positive case: Checks  “Courses”, “LIVE Classes”, and “Practice” are visible and interactable.If menu items are not  found, exceptions are raised.
	* Negative case: Checks invalid menu are visible and interactable. Excepts NoSuchElementException if invalid menu items are not found.

Test Case 9: Dobby Guvi Assistant is present on the page.

	* Positive case: Checks  Dobby Guvi Assistant is visible and interactable.
  * Negative case: Using pytest.raise() checks Dobby Assistant is invisible. This test fail since it doesn't raise NoSuchElementException.
 
Test Case 10: Logout functionality

	* Positive case: Enters valid data,navigates to dashboard page and under the profile menu clicks Sign out.It re-enters the login page again.
	* Negative case: Tests logout functionality without login. This throws TimeoutException error.
	

**Instructions:**

1.Ensure Selenium,Python and any Browser(Chrome,Firefox,Edge) installed in your system. 

2.To create a virtual environment,

	>python -m venv venv
 
	>source venv/bin/activate(macOS)
 
	>venv\scripts\activate(Windows)

3.To install the specific version,

	>pip install -r requirements.txt

4.To execute all the test files,

	>pytest -v -s Tests/

	>pytest pytest -v -s Tests/test_01_url.py(for any specific file)

	>pytest pytest -v -s Tests/test_01_url.py::test_valid_url(for specific method in a test file)


**To Generate HTML Report:**

To install pytest–html package

	>pip install pytest–html

To execute all the test files and generate html report,

	>pytest -v -s Tests/   --html=reports.html    --self-contained-html

To execute single file and generate html report,

	>pytest -v -s Tests/test_01_url.py   --html=case01_report.html   --self-contained-html
 

**** Screen Recording**:https://drive.google.com/file/d/1V3tgJLu52qcqj4u9NA8JtuYrhDyrUb0v/view?usp=sharing



