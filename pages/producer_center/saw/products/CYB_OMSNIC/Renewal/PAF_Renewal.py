from selenium.webdriver.common.by import By

class PAF_Renewal():

    def __init__(self, driver):
        self.driver = driver

    #Page Elements

    def PageElements(self):

        # Do you have a completed renewal application?

        self.completed_renewal_yes = self.driver.find_element(By.ID, "completed_renewal-yes")

        self.completed_renewal_no = self.driver.find_element(By.ID, "completed_renewal-no")

        # Return to Admin Link
        self.return_to_Admin = self.driver.find_element(By.LINK_TEXT, "Return to Admin Interface")

        # Is Your organization formally engaged with Black Talon Security?

        self.black_talon_security_yes = self.driver.find_element(By.ID, "cyb_omsnic_black_talon_security-yes")

        self.black_talon_security_no = self.driver.find_element(By.ID, "cyb_omsnic_black_talon_security-no")

        # Have You acquired, created, sold, merged into, or consolidated with another entity within the last twelve (12) months, or are You currently contemplating any such sale, merger or acquisition?

        self.entity_create_yes = self.driver.find_element(By.ID, "cyb_omsnic_entity_create-yes")

        self.entity_create_no = self.driver.find_element(By.ID, "cyb_omsnic_entity_create-no")

        # Have You acquired or created any Subsidiaries within the last twelve (12) months?

        self.subsidiaries_acquired_yes = self.driver.find_element(By.ID, "cyb_omsnic_subsidiaries_acquired-yes")

        self.subsidiaries_acquired_no = self.driver.find_element(By.ID, "cyb_omsnic_subsidiaries_acquired-no")

        # Is coverage requested for any entity or organization other than the Applicant and its Subsidiaries?

        self.coverage_request_yes = self.driver.find_element(By.ID, "cyb_omsnic_coverage_request-yes")

        self.coverage_request_no = self.driver.find_element(By.ID, "cyb_omsnic_coverage_request-no")

        # Does Your organization process, store, transmit or handle credit or debit card data?

        self.credit_card_data_yes = self.driver.find_element(By.ID, "cyb_omsnic_credit_card_data-yes")

        self.credit_card_data_no = self.driver.find_element(By.ID, "cyb_omsnic_credit_card_data-no")

        # Are Your data security controls compliant with the Payment Card Industry Data Security Standard (PCI DSS)?

        self.pci_dss_yes = self.driver.find_element(By.ID, "cyb_omsnic_pci_dss-yes")

        self.pci_dss_no = self.driver.find_element(By.ID, "cyb_omsnic_pci_dss-no")

        # Have any claims, lawsuits, proceedings, actions, complaints, demand letters, or investigations/inquiries regarding security or privacy-related incidents (including denial of service attacks, computer virus infections, theft or loss of confidential information, damage to third-party networks,or the ability of third parties to rely on Your network) been made against You or any other person or entity proposed for this insurance within the last twelve (12)months?

        self.claims_yes = self.driver.find_element(By.ID, "cyb_omsnic_claims-yes")

        self.claims_no = self.driver.find_element(By.ID, "cyb_omsnic_claims-no")

        # If You answered “YES” to question 9 above, have all such claims, lawsuits, proceedings, actions, complaints, demand letters, or investigations/inquiries been reported to NAS?

        self.claims_reporting_yes = self.driver.find_element(By.ID, "cyb_omsnic_claims_reporting-yes")

        self.claims_reporting_no = self.driver.find_element(By.ID, "cyb_omsnic_claims_reporting-no")

        # Next Button
        self.next_button = self.driver.find_element(By.XPATH, "//form[@id='rate-adjustment-form']/div[4]/a/span[2]/span/span")

        return self

    def click_yes_completed_renewal(self):
        PAF_Renewal.PageElements(self).completed_renewal_yes.click()

    def create_quote_PCI_DSS_No_DQ(self):
        PAF_Renewal.PageElements(self).entity_create_no.click()
        PAF_Renewal.PageElements(self).subsidiaries_acquired_no.click()
        PAF_Renewal.PageElements(self).coverage_request_no.click()
        PAF_Renewal.PageElements(self).credit_card_data_yes.click()
        PAF_Renewal.PageElements(self).claims_no.click()
        PAF_Renewal.PageElements(self).claims_reporting_no.click()

    def mark_yes_pci_dss(self):
        PAF_Renewal.PageElements(self).pci_dss_yes.click()

    def mark_no_pci_dss(self):
        PAF_Renewal.PageElements(self).pci_dss_no.click()

    def create_quote_No_PCI_DSS_No_DQ(self):
        PAF_Renewal.PageElements(self).entity_create_no.click()
        PAF_Renewal.PageElements(self).subsidiaries_acquired_no.click()
        PAF_Renewal.PageElements(self).coverage_request_no.click()
        PAF_Renewal.PageElements(self).credit_card_data_no.click()
        PAF_Renewal.PageElements(self).claims_no.click()
        PAF_Renewal.PageElements(self).claims_reporting_no.click()

    def create_quote_trigger_DQ(self):
        PAF_Renewal.PageElements(self).entity_create_no.click()
        PAF_Renewal.PageElements(self).subsidiaries_acquired_no.click()
        PAF_Renewal.PageElements(self).coverage_request_no.click()
        PAF_Renewal.PageElements(self).credit_card_data_yes.click()
        PAF_Renewal.PageElements(self).claims_no.click()
        PAF_Renewal.PageElements(self).claims_reporting_no.click()


    def click_next(self):
        PAF_Renewal.PageElements(self).next_button.click()

    def click_return_to_Admin_Interface(self):
        PAF_Renewal.PageElements(self).return_to_Admin.click()