from selenium.webdriver.common.by import By
import time

class Confirm_and_Issue():

    def __init__(self, driver):
        self.driver = driver

    def click_issue_policy(self):
        issue_policy = self.driver.find_element(By.XPATH, "//form[@id='application-review-form']/div[3]/a/span[2]/span/span")
        issue_policy.click()

    def click_save_and_exit(self):
        save_and_exit = self.driver.find_element(By.CSS_SELECTOR, "span.text-button-ds > span")
        save_and_exit.click()

    def click_return_to_Admin_Interface(self):
        #JS
        time.sleep(6)
        return_to_admin_interface = self.driver.find_element(By.LINK_TEXT, "Return to Admin Interface")
        return_to_admin_interface.click()

        #JS
        time.sleep(6)


    def input_signature(self):
        agent_signature_field = self.driver.find_element(By.ID, "agent_signature")
        agent_signature_field.send_keys("QA Test")

    def click_accept_terms_issue_policy(self):
        accept_terms_issue_policy_button = self.driver.find_element(By.CSS_SELECTOR, "#view-policy-details-modal > span.button-mid")
        accept_terms_issue_policy_button.click()

        issue_policy_button = self.driver.find_element(By.XPATH, "(//button[@type='button'])[3]")
        issue_policy_button.click()