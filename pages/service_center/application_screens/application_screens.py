from selenium.webdriver.common.by import By

class Application_Screens():

    def __init__(self, driver):
        self.driver = driver

    def Page_Elements(self):

        self.details_link = self.driver.find_element(By.LINK_TEXT, "Details")

        self.name_address_link = self.driver.find_element(By.LINK_TEXT, "Name/Address")

        self.additional_insured_link = self.driver.find_element(By.LINK_TEXT, "Additional Insureds")

        self.subjectivities_link = self.driver.find_element(By.LINK_TEXT, "Subjectivities")

        self.addl_documents_link = self.driver.find_element(By.LINK_TEXT, "Add'l Documents")

        self.rates_link = self.driver.find_element(By.LINK_TEXT, "Rates")

        self.change_status_link = self.driver.find_element(By.LINK_TEXT, "Change Status")

        self.sl_filer_link = self.driver.find_element(By.LINK_TEXT, "SL Filer")

        self.transfer_to_velocity_link = self.driver.find_element(By.LINK_TEXT, "Transfer to Velocity")

        self.effective_periods_link = self.driver.find_element(By.LINK_TEXT, "Effective Periods")

        self.commissions_and_fees_link = self.driver.find_element(By.LINK_TEXT, "Commissions & Fees")

        self.convert_to_new_link = self.driver.find_element(By.LINK_TEXT, "Convert to New")

        self.issue_policy_link = self.driver.find_element(By.LINK_TEXT, "Issue Policy")

        return self

    def click_Details(self):
        Application_Screens.Page_Elements(self).details_link.click()

    def click_Name_Address(self):
        Application_Screens.Page_Elements(self).name_address_link.click()

    def click_Additional_Insureds(self):
        Application_Screens.Page_Elements(self).additional_insured_link.click()

    def click_Subjectivities(self):
        Application_Screens.Page_Elements(self).subjectivities_link.click()

    def click_Addl_Documents(self):
        Application_Screens.Page_Elements(self).addl_documents_link.click()

    def click_Rates(self):
        Application_Screens.Page_Elements(self).rates_link.click()

    def click_Change_Status(self):
        Application_Screens.Page_Elements(self).change_status_link.click()

    def click_SL_Filer(self):
        Application_Screens.Page_Elements(self).sl_filer_link.click()

    def click_Transfer_to_Velocity(self):
        Application_Screens.Page_Elements(self).transfer_to_velocity_link.click()

    def click_Effective_Periods(self):
        Application_Screens.Page_Elements(self).effective_periods_link.click()

    def click_Commissions_Fees(self):
        Application_Screens.Page_Elements(self).commissions_and_fees_link.click()

    def click_Convert_to_New(self):
        Application_Screens.Page_Elements(self).convert_to_new_link.click()

    def click_Issue_Policy(self):
        Application_Screens.Page_Elements(self).issue_policy_link.click()
