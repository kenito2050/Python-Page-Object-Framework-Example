from selenium.webdriver.common.by import By

class Insured_Information():

    def __init__(self, driver):
        self.driver = driver

    def PageElements(self):
        self.fulltime_count = self.driver.find_element(By.ID, "epl_fulltime_empcount")

        self.parttime_count = self.driver.find_element(By.ID, "epl_parttime_empcount")

        self.seasonal_count = self.driver.find_element(By.ID, "epl_seasonal_empcount")

        self.foreign_count = self.driver.find_element(By.ID, "epl_foreign_empcount")

        self.next_button = self.driver.find_element(By.NAME, "submit")

        self.return_to_Admin = self.driver.find_element(By.LINK_TEXT, "Return to Admin Interface")

        return self

    def click_next(self):
        Insured_Information.PageElements(self).next_button.click()

    def click_return_to_Admin_Interface(self):
        Insured_Information.PageElements(self).return_to_Admin.click()

    def enter_fulltime_count(self, fulltime_count):
        Insured_Information.PageElements(self).fulltime_count.clear()
        Insured_Information.PageElements(self).fulltime_count.send_keys(fulltime_count)

    def enter_parttime_count(self, parttime_count):
        Insured_Information.PageElements(self).parttime_count.clear()
        Insured_Information.PageElements(self).parttime_count.send_keys(parttime_count)

    def enter_seasonal_count(self, seasonal_count):
        Insured_Information.PageElements(self).seasonal_count.clear()
        Insured_Information.PageElements(self).seasonal_count.send_keys(seasonal_count)

    def enter_foreign_count(self, foreign_count):
        Insured_Information.PageElements(self).foreign_count.clear()
        Insured_Information.PageElements(self).foreign_count.send_keys(foreign_count)



