from datetime import datetime
from datetime import timedelta
from selenium.webdriver.common.by import By

class CoveragePeriods():

    def __init__(self, driver):
        self.driver = driver

    def PageElements(self):

        self.date_effective_start = self.driver.find_element(By.ID, "date_effective_start")

        return self


    def dates(self):

        self.effectiveDate_June_1 = "06/01/2017"

        return self

    def enter_current_date_as_effective_date(self, date_today):

        # Declare Date variables
        current_date = datetime.now().strftime("%m-%d-%Y")
        #current_date = datetime.now()


        CoveragePeriods.PageElements(self).date_effective_start.click()
        CoveragePeriods.PageElements(self).date_effective_start.clear()
        CoveragePeriods.PageElements(self).date_effective_start.send_keys(date_today)

        # Declare effective start date field; Enter current Date
        # effective_start_date_field = self.driver.find_element(By.ID, "date_effective_start")
        # effective_start_date_field.clear()
        # effective_start_date_field.send_keys(current_date)

    def enter_ad_hoc_effective_date(self, ad_hoc_effectiveDate):

        # Declare Date variables
        #current_date = datetime.now().strftime("%m-%d-%Y")
        ##current_date = datetime("06/01/2017")

        CoveragePeriods.PageElements(self).date_effective_start.click()
        CoveragePeriods.PageElements(self).date_effective_start.clear()
        CoveragePeriods.PageElements(self).date_effective_start.send_keys(ad_hoc_effectiveDate)

        # Declare effective start date field; Enter current Date
        ##effective_start_date_field = self.driver.find_element(By.ID, "date_effective_start")
        ##effective_start_date_field.clear()
        ##effective_start_date_field.send_keys(current_date)


    def click_has_existing_coverage(self):
        placeholder = "this is placeholder"

    def click_next(self):
        next_button = self.driver.find_element(By.XPATH, "//form[@id='primary-epli-form']/div[4]/a/span[2]/span/span")
        next_button.click()