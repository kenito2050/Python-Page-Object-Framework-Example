from selenium.webdriver.common.by import By
from selenium.webdriver.support.wait import WebDriverWait

class active_policies():

    def __init__(self, driver):
        self.driver = driver

    def Page_Elements(self):

        return self

    def enter_policy_name(self, _policy_number):
        search_field = self.driver.find_element(By.ID, "search")
        search_field.click()
        search_field.send_keys(_policy_number)

    def click_search_button(self):
        search_field = self.driver.find_element(By.ID, "search-btn")
        search_field.click()

    def click_policy_link(self, _policy_number):
        policy_link = self.driver.find_element(By.LINK_TEXT, _policy_number)
        policy_link.click()