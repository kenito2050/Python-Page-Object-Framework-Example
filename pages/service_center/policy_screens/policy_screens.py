from selenium.webdriver.common.by import By

class Policy_Screens():

    def __init__(self, driver):
        self.driver = driver

    def Page_Elements(self):

        self.details_link = self.driver.find_element(By.LINK_TEXT, "Details")

        self.name_address_link = self.driver.find_element(By.LINK_TEXT, "Name/Address")

        self.prem_adjustment_link = self.driver.find_element(By.LINK_TEXT, "Prem Adjustment")

        self.additional_documents_link = self.driver.find_element(By.LINK_TEXT, "Add'l Documents")

        self.edit_policy_nmbr_link = self.driver.find_element(By.LINK_TEXT, "Edit Policy Nmbr")

        self.sl_filer_link = self.driver.find_element(By.LINK_TEXT, "SL Filer")

        self.renewal_rate_link = self.driver.find_element(By.LINK_TEXT, "Renewal Rate")

        self.re_rate_application_link = self.driver.find_element(By.LINK_TEXT, "Re-Rate Application")

        self.effective_periods_link = self.driver.find_element(By.LINK_TEXT, "Effective Periods")

        self.cancel_policy_link = self.driver.find_element(By.LINK_TEXT, "Cancel Policy")

        return self

    def click_Details(self):

        Policy_Screens.Page_Elements(self).details_link.click()

    def click_Name_Address(self):

        Policy_Screens.Page_Elements(self).name_address_link.click()

    def click_Prem_Adjustment(self):

        Policy_Screens.Page_Elements(self).prem_adjustment_link.click()

    def click_addl_Documents(self):

        Policy_Screens.Page_Elements(self).additional_documents_link.click()

    def click_Edit_Policy_Number(self):

        Policy_Screens.Page_Elements(self).edit_policy_nmbr_link.click()

    def click_SL_Filer(self):

        Policy_Screens.Page_Elements(self).sl_filer_link.click()

    def click_Renewal_Rate(self):

        Policy_Screens.Page_Elements(self).renewal_rate_link.click()

    def click_Re_Rate_Application(self):

        Policy_Screens.Page_Elements(self).re_rate_application_link.click()

    def click_Effective_Periods(self):

        Policy_Screens.Page_Elements(self).effective_periods_link.click()

    def click_Cancel_Policy(self):

        Policy_Screens.Page_Elements(self).cancel_policy_link.click()
