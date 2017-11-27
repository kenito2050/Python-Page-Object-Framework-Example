from selenium.webdriver.common.by import By

class Insured_Information():

    def __init__(self, driver):
        self.driver = driver

    def PageElements(self):

        self.next_button = self.driver.find_element(By.NAME, "submit")

        self.return_to_Admin = self.driver.find_element(By.LINK_TEXT, "Return to Admin Interface")

        # Number of locations
        self.total_number_of_locations = self.driver.find_element(By.ID, "lexr_tenant_total_number_of_locations")

        # Number of residential units
        self.total_number_of_residential_units = self.driver.find_element(By.ID,"lexr_tenant_total_number_of_residential_units")

        # Total Retail square footage
        self.total_retail_sq_ft = self.driver.find_element(By.ID, "lexr_tenant_total_commercial_square_footage_retail")

        # Total Office square footage
        self.total_office_sq_ft = self.driver.find_element(By.ID, "lexr_tenant_total_commercial_square_footage_office")

        # Total square footage
        self.total_industrial_sq_ft = self.driver.find_element(By.ID,"lexr_tenant_total_commercial_square_footage_industrial")

        return self

    def create_quote_01(self, number_locations, number_residential_units, retail_sq_ft, office_sq_ft, industrial_sq_ft):
        Insured_Information.PageElements(self).total_number_of_locations.clear()
        Insured_Information.PageElements(self).total_number_of_locations.send_keys(number_locations)

        Insured_Information.PageElements(self).total_number_of_residential_units.clear()
        Insured_Information.PageElements(self).total_number_of_residential_units.send_keys(number_residential_units)

        Insured_Information.PageElements(self).total_retail_sq_ft.clear()
        Insured_Information.PageElements(self).total_retail_sq_ft.send_keys(retail_sq_ft)

        Insured_Information.PageElements(self).total_office_sq_ft.clear()
        Insured_Information.PageElements(self).total_office_sq_ft.send_keys(office_sq_ft)

        Insured_Information.PageElements(self).total_industrial_sq_ft.clear()
        Insured_Information.PageElements(self).total_industrial_sq_ft.send_keys(industrial_sq_ft)

    def create_quote_02(self, number_locations, number_residential_units, retail_sq_ft, office_sq_ft, industrial_sq_ft):
        Insured_Information.PageElements(self).total_number_of_locations.clear()
        Insured_Information.PageElements(self).total_number_of_locations.send_keys(number_locations)

        Insured_Information.PageElements(self).total_number_of_residential_units.clear()
        Insured_Information.PageElements(self).total_number_of_residential_units.send_keys(number_residential_units)

        Insured_Information.PageElements(self).total_retail_sq_ft.clear()
        Insured_Information.PageElements(self).total_retail_sq_ft.send_keys(retail_sq_ft)

        Insured_Information.PageElements(self).total_office_sq_ft.clear()
        Insured_Information.PageElements(self).total_office_sq_ft.send_keys(office_sq_ft)

        Insured_Information.PageElements(self).total_industrial_sq_ft.clear()
        Insured_Information.PageElements(self).total_industrial_sq_ft.send_keys(industrial_sq_ft)

    def create_quote_trigger_DQ(self, number_locations, number_residential_units, retail_sq_ft, office_sq_ft,industrial_sq_ft):
        Insured_Information.PageElements(self).total_number_of_locations.clear()
        Insured_Information.PageElements(self).total_number_of_locations.send_keys(number_locations)

        Insured_Information.PageElements(self).total_number_of_residential_units.clear()
        Insured_Information.PageElements(self).total_number_of_residential_units.send_keys(number_residential_units)

        Insured_Information.PageElements(self).total_retail_sq_ft.clear()
        Insured_Information.PageElements(self).total_retail_sq_ft.send_keys(retail_sq_ft)

        Insured_Information.PageElements(self).total_office_sq_ft.clear()
        Insured_Information.PageElements(self).total_office_sq_ft.send_keys(office_sq_ft)

        Insured_Information.PageElements(self).total_industrial_sq_ft.clear()
        Insured_Information.PageElements(self).total_industrial_sq_ft.send_keys(industrial_sq_ft)

        return self

    def click_next(self):
        Insured_Information.PageElements(self).next_button.click()

    def click_return_to_Admin_Interface(self):
        Insured_Information.PageElements(self).return_to_Admin.click()


