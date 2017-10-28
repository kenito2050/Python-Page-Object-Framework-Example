from selenium.webdriver.common.by import By

class Quote_Review():

    def __init__(self, driver):
        self.driver = driver

    def click_select_option(self):
        select_option = self.driver.find_element(By.XPATH, "//form[@id='application-review-form']/div[6]/a/span[2]/span/span")
        select_option.click()