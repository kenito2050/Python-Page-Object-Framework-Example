from selenium.webdriver.common.by import By

class ClientSearch():

    def __init__(self, driver):
        self.driver = driver

    def input_bogus_client_data(self, postal_code):

        client_name = self.driver.find_element(By.ID, "name")
        client_name.send_keys("IPSO FACTO QUID PRO QUO")

        zip_code = self.driver.find_element(By.ID, "zip")
        zip_code.send_keys(postal_code)

        submit_button = self.driver.find_element(By.CSS_SELECTOR, "span.text-button-ds > span")
        submit_button.click()

    def manually_input_new_client(self):
        radio_button_manually_enter_location = self.driver.find_element(By.ID, "insured-na")
        radio_button_manually_enter_location.click()

    def enter_new_client_name_address(self, company_name_string, address_value, city, state):
        client_name = self.driver.find_element(By.ID, "name")
        client_name.clear()
        client_name.send_keys(company_name_string)

        street_address = self.driver.find_element(By.ID, "address-1-physical")
        street_address.send_keys(address_value)

        city_physical = self.driver.find_element(By.ID, "city-physical")
        city_physical.send_keys(city)

        state_physical = self.driver.find_element(By.ID, "state-physical")
        state_physical.send_keys(state)

        # Copy from Physical Address to Billing Address
        link_copy_from_physical_address_to_billing_address = self.driver.find_element(By.ID, "copy-physical")
        link_copy_from_physical_address_to_billing_address.click()

        next_button = self.driver.find_element(By.XPATH, "(//button[@type='button'])[3]")
        next_button.click()