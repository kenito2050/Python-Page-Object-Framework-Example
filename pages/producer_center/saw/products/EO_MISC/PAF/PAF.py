from selenium.webdriver.common.by import By

class PAF():

    def __init__(self, driver):
        self.driver = driver

    # Page Elements

    def Page_Elements(self):

        # Description of Operations
        self.operations_description = self.driver.find_element(By.ID, "operation_nature")

        # Intake Questions

        # Have any claims, suits, or demands been made against the Applicant, a predecessor firm, any past or present principals, partners, officers or employees within the past five (5) years?
        self.eo_misc_investigation_reprimand_yes = self.driver.find_element(By.ID, "eo_misc_investigation_reprimand-yes")

        self.eo_misc_investigation_reprimand_no = self.driver.find_element(By.ID, "eo_misc_investigation_reprimand-no")

        # After inquiry with all principals, partners and officers, is the applicant aware of any dispute, error, omission, act or circumstance that is, or could reasonably be expected to become a claim under the policy for which this application is submitted to the Underwriters?
        self.eo_misc_claim_to_underwriters_yes = self.driver.find_element(By.ID, "eo_misc_claim_to_underwriters-yes")

        self.eo_misc_claim_to_underwriters_no = self.driver.find_element(By.ID, "eo_misc_claim_to_underwriters-no")

        return self

    def create_quote_No_DQ(self):
        PAF.Page_Elements(self).operations_description.send_keys("QA Test")
        PAF.Page_Elements(self).eo_misc_investigation_reprimand_no.click()
        PAF.Page_Elements(self).eo_misc_claim_to_underwriters_no.click()

    #TODO
    # Ask Dev to create ID for next button
    def click_next(self):
        next_button = self.driver.find_element(By.XPATH, "//form[@id='primary-abeo-form']/div[6]/a/span[2]/span/span")
        next_button.click()