from selenium.webdriver.common.by import By
from selenium.common.exceptions import NoSuchElementException
from selenium.webdriver.support.ui import Select
import time

class Account_Creation():

    def __init__(self, driver):
        self.driver = driver

    def Page_Elements(self):

        # Did you receive a custom registration code
        self.custom_registration_code_yes = self.driver.find_element(By.ID, "custom_registration_code-yes")

        self.custom_registration_code_no = self.driver.find_element(By.ID, "custom_registration_code-no")

        # First Name
        self.first_name_field = self.driver.find_element(By.ID, "first-name")

        # Last Name
        self.last_name_field = self.driver.find_element(By.ID, "last-name")

        # Email Address Field
        self.email_address_field = self.driver.find_element(By.ID, "email")

        # Company
        self.company_field = self.driver.find_element(By.ID, "company")

        # Title
        self.title_field = self.driver.find_element(By.ID, "title")

        # Address 1 Field
        self.address_1_field = self.driver.find_element(By.ID, "address_1")

        # Address 2 Field
        self.address_2_field = self.driver.find_element(By.ID, "address_2")

        # City Field
        self.city_field = self.driver.find_element(By.ID, "city")

        # State Field
        self.state_field = self.driver.find_element(By.ID, "state")

        # zip code Field
        self.postal_code_field = self.driver.find_element(By.ID, "zip")

        # Phone
        self.phone_field = self.driver.find_element(By.ID, "phone")

        # Send Button
        self.send_button = self.driver.find_element(By.ID, "submit-btn")

        return self

    def click_custom_registration_code_no(self):
        Account_Creation.Page_Elements(self).custom_registration_code_no.click()

    def click_custom_registration_code_yes(self):
        Account_Creation.Page_Elements(self).custom_registration_code_yes.click()

    def select_retail_agency_type(self):

        # Select Retail from Agency Type Drop Down
        self.agency_type_field = self.driver.find_element(By.ID, "agency_type")
        self.agency_type_field.send_keys("Retail")
        time.sleep(2)

    def select_wholesale_agency_type(self):
        # Select Wholesale from Agency Type Drop Down
        self.agency_type_field = self.driver.find_element(By.ID, "agency_type")
        self.agency_type_field.send_keys("Wholesale")
        time.sleep(2)

    def input_registration_code(self, registration_code):
        # Registration Code
        self.registration_code = self.driver.find_element(By.ID, "reg_code")
        self.registration_code.send_keys(registration_code)

    def fill_in_first_last_name_email_address_city_zip_phone(self, first_name, last_name, email_address, address_value, city, formatted_postal_code, phone):
        Account_Creation.Page_Elements(self).first_name_field.send_keys(first_name)
        Account_Creation.Page_Elements(self).last_name_field.send_keys(last_name)
        Account_Creation.Page_Elements(self).email_address_field.send_keys(email_address)
        Account_Creation.Page_Elements(self).address_1_field.send_keys(address_value)
        Account_Creation.Page_Elements(self).city_field.send_keys(city)
        Account_Creation.Page_Elements(self).postal_code_field.send_keys(formatted_postal_code)
        Account_Creation.Page_Elements(self).phone_field.send_keys(phone)

    def input_title(self, title):
        Account_Creation.Page_Elements(self).title_field.send_keys(title)

    def select_state(self, state):
        # Select State Value based on value stored in state variable
        select = Select(self.driver.find_element_by_id('state'))
        select.select_by_value(state)

    def input_company_name_EXCEL(self, company_name_excel):
        Account_Creation.Page_Elements(self).company_field.send_keys(company_name_excel)
        # Click on Address 2 Field (Preferred Wholesaler Drop Down Should Display if Retail was Selected)
        Account_Creation.Page_Elements(self).address_2_field.click()

    def input_company_name_FAKER(self, company_name_faker):
        Account_Creation.Page_Elements(self).company_field.send_keys(company_name_faker)
        # Click on Address 2 Field (Preferred Wholesaler Drop Down Should Display if Retail was Selected)
        Account_Creation.Page_Elements(self).address_2_field.click()

    def select_preferred_wholesaler(self, preferred_wholesaler):
        # Preferred Wholesaler ONLY displays if
        # 1 - Retail Agency Selected
        # 2 - Company
        # Preferred Wholesaler
        self.preferred_wholesaler_field = self.driver.find_element(By.ID, "p_wholesaler")
        self.preferred_wholesaler_field.send_keys(preferred_wholesaler)

    def click_send_button(self):
        Account_Creation.Page_Elements(self).send_button.click()