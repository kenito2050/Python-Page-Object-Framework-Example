from selenium.webdriver.common.by import By

class PoliciesPage():

    def __init__(self, driver):
        self.driver = driver

    def enter_policy_name(self, _policy_number):
        search_field = self.driver.find_element(By.ID, "search")
        search_field.click()
        search_field.send_keys(_policy_number)

    def click_search_button(self):
        search_field = self.driver.find_element(By.ID, "search-btn")
        search_field.click()