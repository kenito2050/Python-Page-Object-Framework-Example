from selenium.webdriver.common.by import By

class Insured_Information():

    def __init__(self, driver):
        self.driver = driver

    def PageElements(self):

        self.next_button = self.driver.find_element(By.NAME, "submit")

        self.return_to_Admin = self.driver.find_element(By.LINK_TEXT, "Return to Admin Interface")

        # Projected Revenues for Next Year’s Fiscal Year:
        self.project_revenue_next_year = self.driver.find_element(By.ID, "projected_revenue_next_year")

        return self

    def enter_projected_revenue(self, revenue):
        Insured_Information.PageElements(self).project_revenue_next_year.clear()
        Insured_Information.PageElements(self).project_revenue_next_year.send_keys(revenue)

        return self

    def click_next(self):
        Insured_Information.PageElements(self).next_button.click()

    def click_return_to_Admin_Interface(self):
        Insured_Information.PageElements(self).return_to_Admin.click()


