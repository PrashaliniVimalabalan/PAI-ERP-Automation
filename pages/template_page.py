from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as ec
from selenium.webdriver.support.ui import Select
from datetime import datetime
import time


class TemplatePage:

    def __init__(self, driver):

        self.driver = driver

        # Template Menu
        self.template_menu = (
            By.XPATH,
            '//*[@id="root"]/div/div[1]/nav/a[5]/span'
        )

        # Name
        self.name_input = (
            By.XPATH,
            '//*[@id="root"]/div/div[2]/div/div/div[3]/div/form/div[1]/div[1]/input'
        )

        # Address
        self.address_input = (
            By.XPATH,
            '//*[@id="root"]/div/div[2]/div/div/div[3]/div/form/div[1]/div[2]/input'
        )

        # Date
        self.date_input = (
            By.XPATH,
            '//*[@id="root"]/div/div[2]/div/div/div[3]/div/form/div[1]/div[3]/div/input'
        )

        # Role
        self.role_dropdown = (
            By.XPATH,
            '//*[@id="root"]/div/div[2]/div/div/div[3]/div/form/div[1]/div[4]/div/select'
        )

        # Date of Joining
        self.joining_date_input = (
            By.XPATH,
            '//*[@id="root"]/div/div[2]/div/div/div[3]/div/form/div[1]/div[5]/div/input'
        )

        # Date of Ending
        self.ending_date_input = (
            By.XPATH,
            '//*[@id="root"]/div/div[2]/div/div/div[3]/div/form/div[1]/div[6]/div/input'
        )

        # Department
        self.department_input = (
            By.XPATH,
            '//*[@id="root"]/div/div[2]/div/div/div[3]/div/form/div[1]/div[7]/input'
        )

        # Reporting Manager
        self.reporting_manager_input = (
            By.XPATH,
            '//*[@id="root"]/div/div[2]/div/div/div[3]/div/form/div[1]/div[8]/input'
        )

        # Reporting Manager Email
        self.reporting_manager_email_input = (
            By.XPATH,
            '//*[@id="root"]/div/div[2]/div/div/div[3]/div/form/div[1]/div[9]/input'
        )

        # Preview Button
        self.preview_button = (
            By.XPATH,
            '//*[@id="root"]/div/div[2]/div/div/div[3]/div/form/div[2]/button[2]'
        )

        # =========================
        # SERVICE LETTER
        # =========================

        self.service_letter_tab = (
            By.XPATH,
            '//*[@id="root"]/div/div[2]/div/div/div[2]/button[2]'
        )

        self.service_name = (
            By.XPATH,
            '//*[@id="root"]/div/div[2]/div/div/div[3]/div/form/div[1]/div[1]/input'
        )

        self.service_designation = (
            By.XPATH,
            '//*[@id="root"]/div/div[2]/div/div/div[3]/div/form/div[1]/div[2]/div/select'
        )

        self.service_role = (
            By.XPATH,
            '//*[@id="root"]/div/div[2]/div/div/div[3]/div/form/div[1]/div[3]/div/select'
        )

        self.service_date = (
            By.XPATH,
            '//*[@id="root"]/div/div[2]/div/div/div[3]/div/form/div[1]/div[4]/div/input'
        )

        self.service_end_date = (
            By.XPATH,
            '//*[@id="root"]/div/div[2]/div/div/div[3]/div/form/div[1]/div[5]/div/input'
        )

        self.service_join_date = (
            By.XPATH,
            '//*[@id="root"]/div/div[2]/div/div/div[3]/div/form/div[1]/div[6]/div/input'
        )

        self.add_achievement = (
            By.XPATH,
            '//*[@id="root"]/div/div[2]/div/div/div[3]/div/form/button/span[2]'
        )

        self.service_preview = (
            By.XPATH,
            '//*[@id="root"]/div/div[2]/div/div/div[3]/div/form/div[3]/button[1]'
        )

        self.service_download = (
            By.XPATH,
            '/html/body/div[2]/div/div[2]/button'
        )

    # Open Template Page
    def open_template_page(self):

        template = WebDriverWait(self.driver, 20).until(
            ec.element_to_be_clickable(self.template_menu)
        )

        template.click()

        time.sleep(3)

    # Fill Form
    def fill_template_details(
            self,
            name,
            address,
            role,
            joining_date,
            ending_date,
            department,
            manager,
            manager_email
    ):

        WebDriverWait(self.driver, 20).until(
            ec.visibility_of_element_located(
                self.name_input
            )
        ).send_keys(name)

        self.driver.find_element(
            *self.address_input
        ).send_keys(address)

        today = datetime.now().strftime("%d/%m/%Y")

        self.driver.find_element(
            *self.date_input
        ).send_keys(today)

        Select(
            self.driver.find_element(
                *self.role_dropdown
            )
        ).select_by_visible_text(role)

        self.driver.find_element(
            *self.joining_date_input
        ).send_keys(joining_date)

        self.driver.find_element(
            *self.ending_date_input
        ).send_keys(ending_date)

        self.driver.find_element(
            *self.department_input
        ).send_keys(department)

        self.driver.find_element(
            *self.reporting_manager_input
        ).send_keys(manager)

        self.driver.find_element(
            *self.reporting_manager_email_input
        ).send_keys(manager_email)

        time.sleep(2)

    # Preview
    def click_preview(self):
        preview = WebDriverWait(self.driver, 20).until(
            ec.element_to_be_clickable(
                self.preview_button
            )
        )

        self.driver.execute_script(
            "arguments[0].scrollIntoView({block:'center'});",
            preview
        )

        time.sleep(2)

        self.driver.execute_script(
            "arguments[0].click();",
            preview
        )

        print("Preview clicked successfully")

        time.sleep(5)

    #Open service letter
    def open_service_letter(self):
        service = WebDriverWait(self.driver, 20).until(
            ec.element_to_be_clickable(
                self.service_letter_tab
            )
        )

        self.driver.execute_script(
            "arguments[0].click();",
            service
        )

        time.sleep(2)

    #fill service lette
    def fill_service_letter(self):
        today = datetime.now().strftime("%d/%m/%Y")

        # Name
        name = WebDriverWait(self.driver, 20).until(
            ec.visibility_of_element_located(
                self.service_name
            )
        )

        name.clear()
        name.send_keys("Affath")

        # Designation
        Select(
            self.driver.find_element(
                *self.service_designation
            )
        ).select_by_visible_text("QA Engineer")

        # Role
        Select(
            self.driver.find_element(
                *self.service_role
            )
        ).select_by_visible_text("Intern")

        # Current Date
        date_field = self.driver.find_element(
            *self.service_date
        )

        date_field.clear()
        date_field.send_keys(today)

        # End Date
        end_date = self.driver.find_element(
            *self.service_end_date
        )

        end_date.clear()
        end_date.send_keys("10/06/2026")

        # Join Date
        join_date = self.driver.find_element(
            *self.service_join_date
        )

        join_date.clear()
        join_date.send_keys("10/06/2025")

        # Scroll Down
        self.driver.execute_script(
            "window.scrollTo(0, document.body.scrollHeight);"
        )

        time.sleep(2)

    def click_add_achievement(self):
        achievement = WebDriverWait(self.driver, 20).until(
            ec.element_to_be_clickable(
                self.add_achievement
            )
        )

        self.driver.execute_script(
            "arguments[0].click();",
            achievement
        )

        time.sleep(2)


    #Preview
    def click_service_preview(self):
        preview = WebDriverWait(self.driver, 20).until(
            ec.presence_of_element_located(
                self.service_preview
            )
        )

        self.driver.execute_script(
            "arguments[0].scrollIntoView({block:'center'});",
            preview
        )

        time.sleep(2)

        self.driver.execute_script(
            "arguments[0].click();",
            preview
        )

        time.sleep(3)

    #Download

    def click_service_download(self):
        download = WebDriverWait(self.driver, 20).until(
            ec.presence_of_element_located(
                self.service_download
            )
        )

        self.driver.execute_script(
            "arguments[0].click();",
            download
        )

        time.sleep(3)