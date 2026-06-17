from utils.driver_setup import get_driver
from pages.login_page import LoginPage
from pages.employee_page import EmployeePage
from pages.add_employee_page import AddEmployeePage
import time


def test_empty_employee_name():

    driver = get_driver()

    login_page = LoginPage(driver)
    employee_page = EmployeePage(driver)
    add_employee_page = AddEmployeePage(driver)

    # Login
    login_page.open_url()
    login_page.login(
        "ADMIN001",
        "Admin@123"
    )

    # Open Employee Page
    employee_page.open_employee_page()

    # Click New Employee
    employee_page.click_new_employee()

    # Empty Name
    add_employee_page.fill_personal_information(
        "",
        "Female",
        "11-04-2001",
        "+94 0779458933",
        "Colombo",
        "test@gmail.com",
        "Test@123",
        "testuser"
    )

    add_employee_page.click_create_button()

    time.sleep(3)

    print("Empty Employee Name Validation Tested")

    driver.quit()

def test_invalid_personal_email():
    driver = get_driver()

    login_page = LoginPage(driver)
    employee_page = EmployeePage(driver)
    add_employee_page = AddEmployeePage(driver)

    login_page.open_url()
    login_page.login("ADMIN001", "Admin@123")

    employee_page.open_employee_page()
    employee_page.click_new_employee()

    add_employee_page.fill_personal_information(
        "Test User",
        "Female",
        "11-04-2001",
        "+94 0779458933",
        "Colombo",
        "invalidemail",
        "Test@123",
        "testuser"
    )

    add_employee_page.click_create_button()

    print("Invalid Email Validation Tested")

    driver.quit()



def test_empty_personal_email():
    driver = get_driver()

    login_page = LoginPage(driver)
    employee_page = EmployeePage(driver)
    add_employee_page = AddEmployeePage(driver)

    login_page.open_url()
    login_page.login("ADMIN001", "Admin@123")

    employee_page.open_employee_page()
    employee_page.click_new_employee()

    add_employee_page.fill_personal_information(
        "Test User",
        "Female",
        "11-04-2001",
        "+94 0779458933",
        "Colombo",
        "",
        "Test@123",
        "testuser"
    )

    add_employee_page.click_create_button()

    print("Empty Personal Email Validation Tested")

    driver.quit()

def test_invalid_phone_number():
    driver = get_driver()

    login_page = LoginPage(driver)
    employee_page = EmployeePage(driver)
    add_employee_page = AddEmployeePage(driver)

    login_page.open_url()
    login_page.login("ADMIN001", "Admin@123")

    employee_page.open_employee_page()
    employee_page.click_new_employee()

    add_employee_page.fill_personal_information(
        "Test User",
        "Female",
        "11-04-2001",
        "123",
        "Colombo",
        "test@gmail.com",
        "Test@123",
        "testuser"
    )

    add_employee_page.click_create_button()

    print("Invalid Phone Validation Tested")

    driver.quit()



def test_empty_phone_number():
    driver = get_driver()

    login_page = LoginPage(driver)
    employee_page = EmployeePage(driver)
    add_employee_page = AddEmployeePage(driver)

    login_page.open_url()
    login_page.login("ADMIN001", "Admin@123")

    employee_page.open_employee_page()
    employee_page.click_new_employee()

    add_employee_page.fill_personal_information(
        "Test User",
        "Female",
        "11-04-2001",
        "",
        "Colombo",
        "test@gmail.com",
        "Test@123",
        "testuser"
    )

    add_employee_page.click_create_button()

    print("Empty Phone Validation Tested")

    driver.quit()


def test_weak_password():
    driver = get_driver()

    login_page = LoginPage(driver)
    employee_page = EmployeePage(driver)
    add_employee_page = AddEmployeePage(driver)

    login_page.open_url()
    login_page.login("ADMIN001", "Admin@123")

    employee_page.open_employee_page()
    employee_page.click_new_employee()

    add_employee_page.fill_personal_information(
        "Test User",
        "Female",
        "11-04-2001",
        "+94 0779458933",
        "Colombo",
        "test@gmail.com",
        "123",
        "testuser"
    )

    add_employee_page.click_create_button()

    print("Weak Password Validation Tested")

    driver.quit()
