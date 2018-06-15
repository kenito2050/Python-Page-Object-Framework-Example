from selenium.webdriver.common.by import By

class Insured_Information():

    def __init__(self, driver):
        self.driver = driver

    def PageElements(self):
        self.occupied_beds = self.driver.find_element(By.ID, "occupied_beds")

        self.next_button = self.driver.find_element(By.NAME, "submit")

        self.return_to_Admin = self.driver.find_element(By.LINK_TEXT, "Return to Admin Interface")

        return self

    def enter_number_occupied_beds(self, total_occupied_beds):
        Insured_Information.PageElements(self).occupied_beds.send_keys(total_occupied_beds)

    def click_next(self):
        Insured_Information.PageElements(self).next_button.click()

    def click_return_to_Admin_Interface(self):
        Insured_Information.PageElements(self).return_to_Admin.click()


