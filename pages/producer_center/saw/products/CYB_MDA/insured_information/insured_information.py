from selenium.webdriver.common.by import By

class Insured_Information():

    def __init__(self, driver):
        self.driver = driver

    def enter_staff_count(self, staff_count):
        broker_count = self.driver.find_element(By.ID, "ngp_sbdia_brokers_advisors_covered")
        broker_count.send_keys(staff_count)

    def click_next(self):
        next_button = self.driver.find_element(By.NAME, "submit")
        next_button.click()


