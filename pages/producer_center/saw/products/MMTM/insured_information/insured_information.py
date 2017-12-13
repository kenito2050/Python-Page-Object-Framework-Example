from selenium.webdriver.common.by import By

class Insured_Information():
    def __init__(self, driver):
        self.driver = driver

    def PageElements(self):
        self.next_button = self.driver.find_element(By.NAME, "submit")

        self.return_to_Admin = self.driver.find_element(By.LINK_TEXT, "Return to Admin Interface")

        # Total Annual Revenues
        self.total_annual_revenues = self.driver.find_element(By.ID, "annual_revenue_current_year")

        return self

    def create_quote_01(self, annual_gross_sales):
        Insured_Information.PageElements(self).total_annual_revenues.send_keys(annual_gross_sales)

        return self

    def click_next(self):
        Insured_Information.PageElements(self).next_button.click()

    def click_return_to_Admin_Interface(self):
        Insured_Information.PageElements(self).return_to_Admin.click()