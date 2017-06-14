from selenium.webdriver.common.by import By


class Details():
    def __init__(self, driver):
        self.driver = driver

    def Page_Elements(self):

        return self

    def click_agent_link(self, _agent):
        agent_link = self.driver.find_element(By.LINK_TEXT, _agent)
        agent_link.click()