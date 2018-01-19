from selenium.webdriver.common.by import By

class Confirm_Order_Details():

    def __init__(self, driver):
        self.driver = driver

    def click_next(self):
        next_button = self.driver.find_element(By.CSS_SELECTOR, "#submit-blockui > span.button-mid > span.text-button-ds > span")

        #JS
        # scroll to element
        self.driver.execute_script("return arguments[0].scrollIntoView();", next_button)

        next_button.click()

    def click_save_and_exit(self):
        save_and_exit = self.driver.find_element(By.CSS_SELECTOR, "span.text-button-ds > span")
        save_and_exit.click()
