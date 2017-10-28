from selenium.webdriver.common.by import By

class Invoice():

    def __init__(self, driver):
        self.driver = driver

    def click_proceed_to_issuing(self):
        proceed_to_issuing = self.driver.find_element(By.XPATH, "//form[@id='application-review-form']/div[3]/a/span[2]/span/span")
        proceed_to_issuing.click()

    def click_save_and_exit(self):
        save_and_exit = self.driver.find_element(By.CSS_SELECTOR, "span.text-button-ds > span")
        save_and_exit.click()