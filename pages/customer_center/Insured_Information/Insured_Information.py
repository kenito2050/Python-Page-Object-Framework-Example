from selenium.webdriver.common.by import By
from selenium.common.exceptions import NoSuchElementException

class Insured_Information():

    def __init__(self, driver):
        self.driver = driver

    def Page_Elements(self):

        # Name of Insured
        self.name_field = self.driver.find_element(By.ID, "name")

        # Address 1 Field
        self.address_1_field = self.driver.find_element(By.ID, "address-1")

        # Address 2 Field
        self.address_2_field = self.driver.find_element(By.ID, "address-2")

        # City Field
        self.city_field = self.driver.find_element(By.ID, "city")

        # State Field
        self.state_field = self.driver.find_element(By.ID, "state")

        # zip code Field
        self.postal_code_field = self.driver.find_element(By.ID, "zip")

        # Total Annual Revenue
        self.total_annual_revenue_field = self.driver.find_element(By.ID, "annual_revenue_current_year")

        # Continue Button
        self.continue_button = self.driver.find_element(By.CLASS_NAME, "text-button-ds")

        return self

    def fill_in_insured_information_fields(self, address_value, address_2, city, state, total_annual_revenue):

        Insured_Information.Page_Elements(self).address_1_field.send_keys(address_value)
        Insured_Information.Page_Elements(self).address_2_field.send_keys(address_2)
        Insured_Information.Page_Elements(self).city_field.send_keys(city)
        Insured_Information.Page_Elements(self).state_field.send_keys(state)
        Insured_Information.Page_Elements(self).total_annual_revenue_field.send_keys(total_annual_revenue)

    def fill_in_postal_code(self,postal_code):
        Insured_Information.Page_Elements(self).postal_code_field.send_keys(postal_code)

    def fill_in_formatted_postal_code(self, formatted_postal_code):
        Insured_Information.Page_Elements(self).postal_code_field.send_keys(formatted_postal_code)

    def click_continue_button(self):

        Insured_Information.Page_Elements(self).continue_button.click()