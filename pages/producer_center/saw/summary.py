from selenium.webdriver.common.by import By

class Summary():

    def __init__(self, driver):
        self.driver = driver

    def Page_Elements(self):

        # Generate Quote
        self.generate_quote = self.driver.find_element(By.CSS_SELECTOR,
                                                  "#submit-blockui > span.button-mid > span.text-button-ds > span")
        # Save and Exit
        self.save_and_exit = self.driver.find_element(By.CSS_SELECTOR, "span.text-button-ds > span")

        # Submit for Review
        self.submit_for_review = self.driver.find_element(By.LINK_TEXT, "Submit for Review")

        return self

    def click_generate_quote(self):
        Summary.Page_Elements(self).generate_quote.click()
