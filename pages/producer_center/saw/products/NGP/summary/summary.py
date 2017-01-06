from selenium.webdriver.common.by import By

class Summary():

    def __init__(self, driver):
        self.driver = driver

    def click_generate_quote(self):
        generate_quote = self.driver.find_element(By.CSS_SELECTOR, "#submit-blockui > span.button-mid > span.text-button-ds > span")
        generate_quote.click()

    def click_save_and_exit(self):
        save_and_exit = self.driver.find_element(By.CSS_SELECTOR, "span.text-button-ds > span")
        save_and_exit.click()

    def click_submit_for_review(self):
        submit_for_review = self.driver.find_element(By.LINK_TEXT, "Submit for Review")
        submit_for_review.click()
