from selenium.webdriver.common.by import By
from selenium.webdriver.support.wait import WebDriverWait

class BallPark_PAF():

    def __init__(self, driver):
        self.driver = driver

    def switch_windows(self):
        # Switch Windows
        WebDriverWait(self.driver, 10).until(lambda d: len(d.window_handles) == 2)

        # switch windows
        self.driver.switch_to.window(self.driver.window_handles[1])

        # wait to make sure the new window is loaded
        WebDriverWait(self.driver, 10).until(lambda d: d.title != "")

        self.driver.maximize_window()

    def select_contract_class(self, contract_class):
        select_contract_class = self.driver.find_element(By.ID, "coverage_category__contract_class_name")
        select_contract_class.send_keys(contract_class)

    def start_ballpark_enter_faker_company_name_valid_zip(self, company_name_string, postal_code):
        name_of_Insured_field = self.driver.find_element(By.ID, "name")
        name_of_Insured_field.clear()
        name_of_Insured_field.send_keys(company_name_string)

        zip_code = self.driver.find_element(By.ID, "zip")
        zip_code.send_keys(postal_code)

    def click_ballpark_button(self):
        ballpark_button = self.driver.find_element(By.CSS_SELECTOR, "span.text-button-ds > span")
        ballpark_button.click()

    def select_product(self):
        # Ballpark Product Identifiers

        # TODO: Move these identifiers into a separate class

        # NGP Cyber Liability - product - list - item - 74
        cb_NGP = self.driver.find_element(By.ID, "product-list-item-74")

        # US Pro Cyber Liability  - product-list-item-105
        cb_NGP_USPRO = self.driver.find_element(By.ID, "product-list-item-105")

        # PrivaSafe Cyber Liability  - product-list-item-82
        cb_NGP_USI = self.driver.find_element(By.ID, "product-list-item-82")

        # Swett IIABCal Cyber Liability - product-list-item-83
        cb_NGP_SWETT = self.driver.find_element(By.ID, "product-list-item-83")

        cb_NGP.click()

    def enter_revenue(self):
        revenue_field = self.driver.find_element(By.ID, "annual_revenue_current_year")
        revenue_field.send_keys("280,000")

