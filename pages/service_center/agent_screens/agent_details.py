from selenium.webdriver.common.by import By

class Agent_Details():

    def __init__(self, driver):
        self.driver = driver

    def Page_Elements(self):

        return self

    def define_submit_new_application_as_agent(self):

        self.submit_new_application_as_agent_link = self.driver.find_element_by_link_text("Submit New Application as Agent")

        return self

    def click_submit_new_application_as_agent(self):

        Agent_Details.define_submit_new_application_as_agent(self).submit_new_application_as_agent_link.click()