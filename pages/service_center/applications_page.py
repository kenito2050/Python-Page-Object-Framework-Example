from selenium.webdriver.common.by import By

class ApplicationsPage():

    def __init__(self, driver):
        self.driver = driver

    def enter_application_id(self, application_id):
        search_field = self.driver.find_element(By.ID, "search")
        search_field.click()
        search_field.send_keys(application_id)

    def click_search_button(self,):
        search_field = self.driver.find_element(By.ID, "search-btn")
        search_field.click()

    # THIS METHOD IS NOT WORKING - Ken; 1-3-17
    def click_application_id_link(self, application_id):
        application_id_link = self.driver.find_element(By.ID, application_id)
        application_id_link.click()