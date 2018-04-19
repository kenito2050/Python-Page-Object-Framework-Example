from selenium.webdriver.common.by import By

class Insured_Information():

    def __init__(self, driver):
        self.driver = driver

    def enter_annual_revenue(self, revenue):
        annual_revenue = self.driver.find_element(By.ID, "annual_revenue_next_year")
        annual_revenue.send_keys(revenue)

    def click_next(self):
        next_button = self.driver.find_element(By.NAME, "submit")
        next_button.click()


