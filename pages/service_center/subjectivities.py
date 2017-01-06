from selenium.webdriver.common.by import By

class Subjectivities():

    def __init__(self, driver):
        self.driver = driver

    # This code is working - Ken 1-4-17
    def change_open_subjectivities_to_received(self):
        radio_button_01 = self.driver.find_element_by_css_selector('[id*="1_subj_received_"]')
        radio_button_01.click()

        radio_button_02 = self.driver.find_element_by_css_selector('[id*="2_subj_received_"]')
        radio_button_02.click()

        radio_button_03 = self.driver.find_element_by_css_selector('[id*="3_subj_received_"]')
        radio_button_03.click()

        radio_button_04 = self.driver.find_element_by_css_selector('[id*="4_subj_received_"]')
        radio_button_04.click()

        radio_button_05 = self.driver.find_element_by_css_selector('[id*="5_subj_received_"]')
        radio_button_05.click()

        radio_button_06 = self.driver.find_element_by_css_selector('[id*="6_subj_received_"]')
        radio_button_06.click()

        radio_button_07 = self.driver.find_element_by_css_selector('[id*="7_subj_received_"]')
        radio_button_07.click()

        #signed_application_subjectivity_received_radio_button = self.driver.find_element_by_css_selector('[id*="4_subj_received_"]')
        #signed_application_subjectivity_received_radio_button.click()

        #cloud_storage_provider_confirmation_radio_button = self.driver.find_element_by_css_selector('[id*="6_subj_received_"]')
        #cloud_storage_provider_confirmation_radio_button.click()

    def select_yes_to_subjectivities_met(self):
        subjectivities_met_drop_down = self.driver.find_element(By.ID, "subjectivities_met")
        subjectivities_met_drop_down.send_keys("Yes, all subjectivities have been met.")

    def click_submit(self):
        submit_button = self.driver.find_element(By.XPATH, "//form[@id='main-form']/div[3]/a/span[2]/span/span")
        submit_button.click()

    def click_agent_link(self):
        agent_link = self.driver.find_element(By.LINK_TEXT, "Agent")
        agent_link.click()