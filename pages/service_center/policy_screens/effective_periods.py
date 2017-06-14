from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import Select
from datetime import datetime
from dateutil.relativedelta import relativedelta

class Effective_Periods():

    def __init__(self, driver):
        self.driver = driver

    def Page_Elements(self):

        # Effective Date Fields

        self.effective_start_year = self.driver.find_element(By.ID, "effective_start_year")

        self.effective_start_month = self.driver.find_element(By.ID, "effective_start_month")

        self.effective_start_day = self.driver.find_element(By.ID, "effective_start_day")

        # Expiration Date Fields

        self.effective_end_year = self.driver.find_element(By.ID, "effective_end_year")

        self.effective_end_month = self.driver.find_element(By.ID, "effective_end_month")

        self.effective_end_day = self.driver.find_element(By.ID, "effective_end_day")

        # Extended Reporting Date Fields

        self.erp_year = self.driver.find_element(By.ID, "erp_year")

        self.erp_month = self.driver.find_element(By.ID, "erp_month")

        self.erp_day = self.driver.find_element(By.ID, "erp_day")

        # Original Application Signature Date Fields

        self.application_signature_year = self.driver.find_element(By.ID, "application_signature_year")

        self.application_signature_month = self.driver.find_element(By.ID, "application_signature_month")

        self.application_signature_day = self.driver.find_element(By.ID, "application_signature_day")

        # Change Dates Button

        self.change_dates_button = self.driver.find_element(By.ID, "generate-policy-btn")

        return self

    def change_dates_expire_policy_allow_renewal_new(self):

        # Intialize Time Variables

        # This Year
        now = datetime.now()

        # Last Year
        last_year = datetime.now() - relativedelta(years=1)

        current_year = now.year
        previous_year = last_year.year

        # Date in 4 days
        date_plus_4_days = datetime.now() + relativedelta(days=4)

        # Month and Day values of Date in 4 days
        expiration_month = date_plus_4_days.strftime('%B')
        expiration_day = date_plus_4_days.strftime('%d').lstrip('0')

        # Set Effective Start Year to Previous Year
        Effective_Periods.Page_Elements(self).effective_start_year.send_keys(previous_year)

        # Set End Year to Current Year
        Effective_Periods.Page_Elements(self).effective_end_year.send_keys(current_year)



        # Add 4 days to Effective End Day

        # This line works
        #select_month = Select(Effective_Periods.Page_Elements(self).effective_end_month).select_by_visible_text(expiration_month)
        #select_month.select_by_visible_text(expiration_month)

        select_month = Select(Effective_Periods.Page_Elements(self).effective_end_month)
        select_month.select_by_visible_text(expiration_month)

        select_day = Select(Effective_Periods.Page_Elements(self).effective_end_day)
        select_day.select_by_visible_text(expiration_day)


        Effective_Periods.Page_Elements(self).change_dates_button.click()


        select_month = Select(self.driver.effective_end_month)
        select_month.select_by_visible_text(expiration_month)


        Effective_Periods.Page_Elements(self).effective_end_day.click()

        self.driver.implicitly_wait(2)

        Effective_Periods.Page_Elements(self).effective_end_day.select_by_visible_text(expiration_day)

        # Set Month of Expiration Date
        Effective_Periods.Page_Elements(self).effective_end_month.click()
        Effective_Periods.Page_Elements(self).effective_end_month.select_by_visible_text(expiration_month)



    def change_dates_expire_policy_allow_renewal(self):

        # Intialize Time Variables

        # This Year
        now = datetime.now()

        # Last Year
        last_year = datetime.now() - relativedelta(years=1)

        current_year = now.year
        previous_year = last_year.year

        # Find Current Date and Add 4 days
        current_date_plus_4_days = datetime.now() + relativedelta(days=4)

        # Month and Day values of Date in 4 days
        expiration_month = current_date_plus_4_days.strftime('%B')
        expiration_day = current_date_plus_4_days.strftime('%d').lstrip('0')
        expiration_year = current_date_plus_4_days.strftime('%Y')

        # Set Effective Start Year to Previous Year
        Effective_Periods.Page_Elements(self).effective_start_year.send_keys(previous_year)

        # Set Expiration Year to Year from the date_plus_4_days
        Effective_Periods.Page_Elements(self).effective_end_year.send_keys(expiration_year)

        # Add 4 days to Effective End Day

        # These lines do NOT work
        #Effective_Periods.Page_Elements(self).effective_end_day.click()
        #Effective_Periods.Page_Elements(self).effective_end_day.select_by_visible_text(expiration_day)

        # These lines ARE working
        select_day = Select(Effective_Periods.Page_Elements(self).effective_end_day)
        select_day.select_by_visible_text(expiration_day)

        # Set Month of Expiration Date

        # These lines do NOT work
        #Effective_Periods.Page_Elements(self).effective_end_month.click()
        #Effective_Periods.Page_Elements(self).effective_end_month.select_by_visible_text(expiration_month)

        # These lines ARE working
        select_month = Select(Effective_Periods.Page_Elements(self).effective_end_month)
        select_month.select_by_visible_text(expiration_month)

    def click_update_dates(self):
        Effective_Periods.Page_Elements(self).change_dates_button.click()