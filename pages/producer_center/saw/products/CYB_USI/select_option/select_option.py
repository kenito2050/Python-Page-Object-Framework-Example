from selenium.webdriver.common.by import By

class Select_Option():

    def __init__(self, driver):
        self.driver = driver

    def select_premium(self):
        select_option = self.driver.find_element(By.NAME, "rate_id")
        select_option.click()

    def click_accept_rate_and_continue(self):
        accept_rate_and_continue = self.driver.find_element(By.XPATH,"//form[@id='application-review-form']/div[5]/a/span[2]/span/span")
        accept_rate_and_continue.click()