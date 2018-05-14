from selenium.webdriver.common.by import By
from selenium.webdriver.common.keys import Keys
import time

class App_Details_sub_agent():
    def __init__(self, driver):
        self.driver = driver

    def Page_Elements(self):

        # Create Date field
        self.create_date_field = self.driver.find_element_by_name("ts_create")

        # Submit Button
        self.submit_button = self.driver.find_element_by_css_selector("#ts-created-form > p > span.data > input[type=\"submit\"]")

        # Sub-Agent Link -- Not the Dynamic Link
        self.sub_agent_link = self.driver.find_element(By.LINK_TEXT, "Sub-Agent")

        return self

    def update_create_date(self, ad_hoc_Date):

         #   App_Details.Page_Elements(self).create_date_field.click();
         App_Details_sub_agent.Page_Elements(self).create_date_field.clear()
         App_Details_sub_agent.Page_Elements(self).create_date_field.send_keys(ad_hoc_Date)
         App_Details_sub_agent.Page_Elements(self).create_date_field.send_keys(Keys.TAB)

    time.sleep(2)

    def click_update_button(self):
        App_Details_sub_agent.Page_Elements(self).submit_button.click()

    def click_sub_agent_text_link(self):
        App_Details_sub_agent.Page_Elements(self).sub_agent_link.click()

    def click_agent_link(self, _agent):
        agent_link = self.driver.find_element(By.LINK_TEXT, _agent)
        agent_link.click()