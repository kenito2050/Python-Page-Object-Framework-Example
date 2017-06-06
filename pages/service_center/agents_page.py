from xml.etree import ElementTree as ET
from selenium.webdriver.common.by import By

class AgentsPage():

    def __init__(self, driver):
        self.driver = driver

    def Page_Elements(self):

        self.search_field = self.driver.find_element(By.ID, "search")

        self.search_button = self.driver.find_element(By.ID, "search-btn")

        self.show_wholesaler_contacts = self.driver.find_element(By.LINK_TEXT, "Show Wholesaler Contacts")

        #self.agent_link = self.driver.find_element_by_link_text(agent)

        return self

    def search_for_agent(self, agent):

        AgentsPage.Page_Elements(self).search_field.send_keys(agent)
        AgentsPage.Page_Elements(self).search_button.click()
        AgentsPage.Page_Elements(self).show_wholesaler_contacts.click()
        self.agent_link = self.driver.find_element_by_link_text(agent)
        self.agent_link.click()


    def define_submit_new_application_as_agent(self):

        self.submit_new_application_as_agent_link = self.driver.find_element_by_link_text("Submit New Application as Agent")

        return self

    def click_submit_new_application_as_agent(self):

        AgentsPage.define_submit_new_application_as_agent(self).submit_new_application_as_agent_link.click()

    def search_for_agent_old(self, agent):

        # # Access XML to retrieve the agent to search for
        # tree = ET.parse('Agents.xml')
        # root = tree.getroot()
        #
        # agent = (root[0][0].text)

        # Declare & fill in Search Field
        search_field = self.driver.find_element(By.ID, "search")
        search_field.send_keys(agent)

        # Declare & click Search Button
        search_button = self.driver.find_element(By.ID, "search-btn")
        search_button.click()

        # Click Show Wholesaler Contacts link
        show_wholesaler_contacts = self.driver.find_element(By.LINK_TEXT, "Show Wholesaler Contacts")
        show_wholesaler_contacts.click()

        # Declare & click on agent link (agent name is variable)
        agent_link = self.driver.find_element_by_link_text(agent)
        agent_link.click()

        # On Agent Details screen, Declare the "Submit New Application as Agent" & click this link
        submit_new_application_as_agent_link = self.driver.find_element_by_link_text("Submit New Application as Agent")
        submit_new_application_as_agent_link.click()