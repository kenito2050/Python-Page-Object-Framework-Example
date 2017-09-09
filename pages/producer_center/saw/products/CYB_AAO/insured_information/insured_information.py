from selenium.webdriver.common.by import By

class Insured_Information():

    def __init__(self, driver):
        self.driver = driver

    def PageElements(self):
        self.fte_physician_count = self.driver.find_element(By.ID, "fte_physician_count")

        self.non_fte_physician_count = self.driver.find_element(By.ID, "non_fte_physician_count")

        self.next_button = self.driver.find_element(By.NAME, "submit")

        self.return_to_Admin = self.driver.find_element(By.LINK_TEXT, "Return to Admin Interface")

        return self

    def click_next(self):
        Insured_Information.PageElements(self).next_button.click()

    def click_return_to_Admin_Interface(self):
        Insured_Information.PageElements(self).return_to_Admin.click()

    def enter_fte_physician_count(self, doctor_count):
        Insured_Information.PageElements(self).fte_physician_count.clear()
        Insured_Information.PageElements(self).fte_physician_count.send_keys(doctor_count)

    def enter_non_fte_physician_count(self, doctor_count):
        Insured_Information.PageElements(self).non_fte_physician_count.clear()
        Insured_Information.PageElements(self).non_fte_physician_count.send_keys(doctor_count)


