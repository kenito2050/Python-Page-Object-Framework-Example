from selenium.webdriver.common.by import By

class Insured_Information():

    def __init__(self, driver):
        self.driver = driver

    def PageElements(self):
        self.physician_count = self.driver.find_element(By.ID, "physician_count")

        self.next_button = self.driver.find_element(By.NAME, "submit")

        return self

    def enter_physician_count(self, revenue):
        Insured_Information.PageElements(self).physician_count.send_keys(revenue)

    def click_next(self):
        Insured_Information.PageElements(self).next_button.click()


