from utils.driver_setup import get_driver
from pages.login_page import LoginPage
from pages.template_page import TemplatePage
import time


def test_template_page():

    driver = get_driver()

    login_page = LoginPage(driver)
    template_page = TemplatePage(driver)

    # ==================================
    # LOGIN
    # ==================================

    login_page.open_url()

    login_page.login(
        "ADMIN001",
        "Admin@123"
    )

    # ==================================
    # OPEN TEMPLATE PAGE
    # ==================================

    template_page.open_template_page()

    # ==================================
    # OFFER LETTER
    # ==================================

    print("Testing Offer Letter...")

    template_page.fill_template_details(
        name="Affath",
        address="Jaffna",
        role="Software Engineer",
        joining_date="01/01/2024",
        ending_date="01/01/2025",
        department="IT",
        manager="Nishothman",
        manager_email="nishothmans.pineappleai@gmail.com"
    )

    template_page.click_preview()

    time.sleep(3)

    print("Offer Letter Completed")

    # ==================================
    # SERVICE LETTER
    # ==================================

    print("Testing Service Letter...")

    template_page.open_service_letter()

    template_page.fill_service_letter()

    template_page.click_add_achievement()

    template_page.click_service_preview()

    time.sleep(3)

    template_page.click_service_download()

    print("Service Letter Completed")

    # ==================================
    # FINISH
    # ==================================

    print("Template Module Tested Successfully")

    time.sleep(5)

    driver.quit()