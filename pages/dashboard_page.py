from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait, Select
from selenium.webdriver.support import expected_conditions as ec
import time


class DashboardPage:

    def __init__(self, driver):

        self.driver = driver

        # Logout
        self.logout_button = (
            By.XPATH,
            '//*[@id="root"]/div/div[1]/nav/a[7]/span'
        )

        # Attendance View All
        self.view_all_attendance = (
            By.XPATH,
            '//*[@id="root"]/div/div[2]/div/div/div[2]/section/div[1]/button'
        )

        # Employee Filter
        self.employee_filter = (
            By.XPATH,
            '//*[@id="root"]/div/div[2]/div/div/div[2]/div[1]/div[1]/div[1]/button/span'
        )

        # Employee Checkbox
        self.employee_checkbox = (
            By.XPATH,
            '//*[@id="root"]/div/div[2]/div/div/div[3]/div/div[3]/button[1]/span[3]/span[1]'
        )

        # Add Button
        self.add_button = (
            By.XPATH,
            '//*[@id="root"]/div/div[2]/div/div/div[3]/div/button'
        )

        # Status Dropdown
        self.status_dropdown = (
            By.XPATH,
            '//*[@id="root"]/div/div[2]/div/div/div[2]/div[1]/div[1]/div[1]/select'
        )

        # From Date
        self.from_date = (
            By.XPATH,
            '//*[@id="root"]/div/div[2]/div/div/div[2]/div[1]/div[1]/div[2]/div[1]/input'
        )

        # To Date
        self.to_date = (
            By.XPATH,
            '//*[@id="root"]/div/div[2]/div/div/div[2]/div[1]/div[1]/div[2]/div[2]/input'
        )

        # Apply Filter
        self.apply_filter = (
            By.XPATH,
            '//*[@id="root"]/div/div[2]/div/div/div[2]/div[1]/div[1]/div[2]/div[3]/button[1]'
        )

        # Clear Filter
        self.clear_filter = (
            By.XPATH,
            '//*[@id="root"]/div/div[2]/div/div/div[2]/div[1]/div[1]/div[2]/div[3]/button[2]'
        )

    def is_dashboard_displayed(self):

        WebDriverWait(self.driver, 20).until(
            lambda d: "dashboard" in d.current_url
        )

        return "dashboard" in self.driver.current_url

    def open_attendance_page(self):

        attendance = WebDriverWait(self.driver, 20).until(
            ec.element_to_be_clickable(
                self.view_all_attendance
            )
        )

        self.driver.execute_script(
            "arguments[0].click();",
            attendance
        )

        time.sleep(3)

    def select_employee_filter(self):

        employee = WebDriverWait(self.driver, 20).until(
            ec.element_to_be_clickable(
                self.employee_filter
            )
        )

        employee.click()

        time.sleep(2)

        checkbox = WebDriverWait(self.driver, 20).until(
            ec.element_to_be_clickable(
                self.employee_checkbox
            )
        )

        checkbox.click()

        time.sleep(1)

        add = WebDriverWait(self.driver, 20).until(
            ec.element_to_be_clickable(
                self.add_button
            )
        )

        add.click()

        time.sleep(2)

    def select_status(self, status):

        dropdown = Select(
            WebDriverWait(self.driver, 20).until(
                ec.presence_of_element_located(
                    self.status_dropdown
                )
            )
        )

        dropdown.select_by_visible_text(status)

        time.sleep(2)

    def enter_dates(self, from_date, to_date):

        from_field = WebDriverWait(self.driver, 20).until(
            ec.element_to_be_clickable(
                self.from_date
            )
        )

        from_field.clear()
        from_field.send_keys(from_date)

        to_field = WebDriverWait(self.driver, 20).until(
            ec.element_to_be_clickable(
                self.to_date
            )
        )

        to_field.clear()
        to_field.send_keys(to_date)

        time.sleep(2)

    def click_apply_filter(self):

        apply_btn = WebDriverWait(self.driver, 20).until(
            ec.element_to_be_clickable(
                self.apply_filter
            )
        )

        apply_btn.click()

        time.sleep(3)

    def click_clear_filter(self):

        clear_btn = WebDriverWait(self.driver, 20).until(
            ec.element_to_be_clickable(
                self.clear_filter
            )
        )

        clear_btn.click()

        time.sleep(2)

    def click_logout(self):

        logout = WebDriverWait(self.driver, 20).until(
            ec.element_to_be_clickable(
                self.logout_button
            )
        )

        self.driver.execute_script(
            "arguments[0].click();",
            logout
        )

        WebDriverWait(self.driver, 20).until(
            lambda d: "login" in d.current_url
        )