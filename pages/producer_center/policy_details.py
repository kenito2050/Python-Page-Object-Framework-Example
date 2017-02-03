from selenium.webdriver.common.by import By

class Policy_Details():

    def __init__(self, driver):
        self.driver = driver

    def retrieve_store_policy_number(self, policy_number):
        policy_number = self.driver.find_element(By.ID, "policy-link").getText()