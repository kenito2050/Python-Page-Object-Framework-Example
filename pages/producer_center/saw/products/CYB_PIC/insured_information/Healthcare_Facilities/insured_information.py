from selenium.webdriver.common.by import By

class Insured_Information_Healthcare_Facilities():

    def __init__(self, driver):
        self.driver = driver

    def PageElements(self):

        self.physician_count = self.driver.find_element(By.ID, "physician_count")

        self.annual_revenue = self.driver.find_element(By.ID, "annual_revenue_current_year")

        self.next_button = self.driver.find_element(By.NAME, "submit")

        self.return_to_Admin = self.driver.find_element(By.LINK_TEXT, "Return to Admin Interface")

        return self

    def enter_annual_revenue(self, revenue):
        Insured_Information_Healthcare_Facilities.PageElements(self).annual_revenue.send_keys(revenue)

    def click_next(self):
        Insured_Information_Healthcare_Facilities.PageElements(self).next_button.click()

    def click_return_to_Admin_Interface(self):
        Insured_Information_Healthcare_Facilities.PageElements(self).return_to_Admin.click()

    def enter_physician_count(self, doctor_count):
        Insured_Information_Healthcare_Facilities.PageElements(self).physician_count.send_keys(doctor_count)



