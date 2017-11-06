from selenium.webdriver.common.by import By

class Insured_Information():

    def __init__(self, driver):
        self.driver = driver

    def enter_bed_count(self, number_beds):
        bed_count = self.driver.find_element(By.ID, "bed_count")
        bed_count.send_keys(number_beds)

    def enter_physician_count(self, doctor_count):
        physician_count = self.driver.find_element(By.ID, "physician_count")
        physician_count.send_keys(doctor_count)

    def click_next(self):
        next_button = self.driver.find_element(By.NAME, "submit")
        next_button.click()


