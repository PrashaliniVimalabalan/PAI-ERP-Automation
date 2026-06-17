from utils.driver_setup import get_driver
from pages.login_page import LoginPage
from pages.dashboard_page import DashboardPage
import time


def test_dashboard_attendance():

    driver = get_driver()

    login_page = LoginPage(driver)
    dashboard_page = DashboardPage(driver)

    login_page.open_url()

    login_page.login(
        "ADMIN001",
        "Admin@123"
    )

    dashboard_page.open_attendance_page()

    dashboard_page.select_employee_filter()

    dashboard_page.select_status(
        "Late"
    )

    dashboard_page.enter_dates(
        "01/06/2026",
        "15/06/2026"
    )

    dashboard_page.click_apply_filter()

    dashboard_page.click_clear_filter()

    print("Attendance Filter Tested Successfully")

    time.sleep(5)

    driver.quit()