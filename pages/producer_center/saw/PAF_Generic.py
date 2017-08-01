from selenium.webdriver.common.by import By

class PAF_Generic():

    def __init__(self, driver):
        self.driver = driver

    def PageElements(self):

        # self.next_button = self.driver.find_element(By.NAME, "submit")

        self.return_to_Admin = self.driver.find_element(By.LINK_TEXT, "Return to Admin Interface")

        return self

    # def click_next(self):
    #     PAF_Generic.PageElements(self).next_button.click()

    def click_return_to_Admin_Interface(self):
        PAF_Generic.PageElements(self).return_to_Admin.click()


