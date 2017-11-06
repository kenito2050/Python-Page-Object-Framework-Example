from selenium.webdriver.common.by import By

class Insured_Information():

    def __init__(self, driver):
        self.driver = driver

    def enter_location_count(self, number_locations):
        location_count = self.driver.find_element(By.ID, "location_count")
        location_count.send_keys(number_locations)

    def click_next(self):
        next_button = self.driver.find_element(By.NAME, "submit")
        next_button.click()


