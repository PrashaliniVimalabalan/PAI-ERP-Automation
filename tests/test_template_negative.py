from utils.driver_setup import get_driver
from pages.login_page import LoginPage
from pages.template_page import TemplatePage
import time

def test_empty_name():

    driver = get_driver()

    login_page = LoginPage(driver)
    template_page = TemplatePage(driver)

    login_page.open_url()

    login_page.login(
        "ADMIN001",
        "Admin@123"
    )

    template_page.open_template_page()

    template_page.fill_template_details(
        name="",
        address="Jaffna",
        role="Software Engineer",
        joining_date="01/01/2024",
        ending_date="01/01/2025",
        department="IT",
        manager="Nishothman",
        manager_email="nishothmans.pineappleai@gmail.com"
    )

    template_page.click_preview()

    print("Empty Name Validation Tested")

    driver.quit()

def test_invalid_manager_email():

    driver = get_driver()

    login_page = LoginPage(driver)
    template_page = TemplatePage(driver)

    login_page.open_url()

    login_page.login(
        "ADMIN001",
        "Admin@123"
    )

    template_page.open_template_page()

    template_page.fill_template_details(
        name="Affath",
        address="Jaffna",
        role="Software Engineer",
        joining_date="01/01/2024",
        ending_date="01/01/2025",
        department="IT",
        manager="Nishothman",
        manager_email="abc123"
    )

    template_page.click_preview()

    print("Invalid Email Validation Tested")

    driver.quit()

