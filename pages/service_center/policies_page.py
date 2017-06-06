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

    def click_all_link (self):
        all_link = self.driver.find_element(By.LINK_TEXT, "All")
        all_link.click()

    def click_policy_link(self, _policy_number):
        policy_link = self.driver.find_element(By.LINK_TEXT, _policy_number)
        policy_link.click()

    def click_policy_link_test(self):
        policy_link = self.driver.find_element(By.PARTIAL_LINK_TEXT, "TEST")
        policy_link.click()