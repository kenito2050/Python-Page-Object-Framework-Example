from datetime import datetime
from datetime import timedelta
from selenium.webdriver.common.by import By

class Coverage_Periods_Renewal():

    def __init__(self, driver):
        self.driver = driver

    def PageElements(self):

        self.date_effective_start = self.driver.find_element(By.ID, "date_effective_start")

        self.return_to_Admin = self.driver.find_element(By.LINK_TEXT, "Return to Admin Interface")

        return self


    def dates(self):

        self.effectiveDate_June_1 = "06/01/2017"

        return self

    def enter_current_date_as_effective_date(self, date_today):

        # Declare Date variables
        current_date = datetime.now().strftime("%m-%d-%Y")
        #current_date = datetime.now()


        Coverage_Periods_Renewal.PageElements(self).date_effective_start.click()
        Coverage_Periods_Renewal.PageElements(self).date_effective_start.clear()
        Coverage_Periods_Renewal.PageElements(self).date_effective_start.send_keys(date_today)

        # Declare effective start date field; Enter current Date
        # effective_start_date_field = self.driver.find_element(By.ID, "date_effective_start")
        # effective_start_date_field.clear()
        # effective_start_date_field.send_keys(current_date)

    def enter_ad_hoc_effective_date(self, ad_hoc_effectiveDate):

        # Declare Date variables
        #current_date = datetime.now().strftime("%m-%d-%Y")
        ##current_date = datetime("06/01/2017")

        Coverage_Periods_Renewal.PageElements(self).date_effective_start.click()
        Coverage_Periods_Renewal.PageElements(self).date_effective_start.clear()
        Coverage_Periods_Renewal.PageElements(self).date_effective_start.send_keys(ad_hoc_effectiveDate)

        # Declare effective start date field; Enter current Date
        ##effective_start_date_field = self.driver.find_element(By.ID, "date_effective_start")
        ##effective_start_date_field.clear()
        ##effective_start_date_field.send_keys(current_date)

    def click_has_existing_coverage(self):
        placeholder = "this is placeholder"

    def click_next(self):
        next_button = self.driver.find_element(By.XPATH, "//form[@id='primary-epli-form']/div[4]/a/span[2]/span/span")
        next_button.click()

    def click_return_to_Admin_Interface(self):
        Coverage_Periods_Renewal.PageElements(self).return_to_Admin.click()