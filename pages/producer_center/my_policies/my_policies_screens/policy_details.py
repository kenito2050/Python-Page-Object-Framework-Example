from selenium.webdriver.common.by import By
from selenium.webdriver.support.wait import WebDriverWait

class policy_details():

    def __init__(self, driver):
        self.driver = driver

    def Page_Elements(self):

        return self

    def click_quote_now_link(self):
        quote_now_link = self.driver.find_element(By.LINK_TEXT, "Quote Now")
        quote_now_link.click()