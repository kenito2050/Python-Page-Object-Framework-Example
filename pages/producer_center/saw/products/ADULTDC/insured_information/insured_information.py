from selenium.webdriver.common.by import By

class Insured_Information():

    def __init__(self, driver):
        self.driver = driver

    def PageElements(self):
        self.daily_participants = self.driver.find_element(By.ID, "adc_daily_participants")

        self.next_button = self.driver.find_element(By.NAME, "submit")

        self.return_to_Admin = self.driver.find_element(By.LINK_TEXT, "Return to Admin Interface")

        return self

    def enter_number_daily_participants(self, number_of_daily_participants):
        Insured_Information.PageElements(self).daily_participants.send_keys(number_of_daily_participants)

    def click_next(self):
        Insured_Information.PageElements(self).next_button.click()

    def click_return_to_Admin_Interface(self):
        Insured_Information.PageElements(self).return_to_Admin.click()



