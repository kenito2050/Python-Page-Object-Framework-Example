from selenium.webdriver.common.by import By

class PAF_Renewal():

    def __init__(self, driver):
        self.driver = driver

    #Page Elements

    def PageElements(self):

        # Return to Admin Link
        self.return_to_Admin = self.driver.find_element(By.LINK_TEXT, "Return to Admin Interface")

        # Next Button
        self.next_button = self.driver.find_element(By.XPATH, "//form[@id='rate-adjustment-form']/div[2]/div[3]/a/span[2]")

        # total number of customer and/or employee records
        self.total_records = self.driver.find_element(By.ID, "ngp_total_records")

        # Have there been any material changes in the Applicant's nature of operations or data security/media controls in the last twelve (12) months?
        self.material_changes_yes = self.driver.find_element(By.ID, "ngp_material_changes-yes")

        self.material_changes_no = self.driver.find_element(By.ID, "ngp_material_changes-no")

        # Are you or your credit card point of sale vendor (if applicable) PCI-DSS Compliant?
        self.pci_dss_compliant_yes = self.driver.find_element(By.ID, "ngp_pci_dss_compliant-yes")

        self.pci_dss_compliant_no = self.driver.find_element(By.ID, "ngp_pci_dss_compliant-no")

        # Have any claims, lawsuits, proceedings, actions, complaints, demand letters, or investigations/inquiries regarding security or privacy-related incidents (including denial of service attacks, computer virus infections, theft or loss of confidential information, damage to third-party networks, or the ability of third parties to rely on your network) been made against you or any other person or entity proposed for this insurance within the last twelve (12) months?

        self.known_issues_yes = self.driver.find_element(By.ID, "ngp_known_issues-yes")

        self.known_issues_no = self.driver.find_element(By.ID, "ngp_known_issues-no")

        return self

    def create_quote_PCI_DSS_No_DQ(self, total_num_records):
        PAF_Renewal.PageElements(self).total_records.send_keys(total_num_records)
        PAF_Renewal.PageElements(self).material_changes_no.click()
        PAF_Renewal.PageElements(self).pci_dss_compliant_yes.click()
        PAF_Renewal.PageElements(self).known_issues_no.click()
        PAF_Renewal.PageElements(self).next_button.click()

    def create_quote_No_PCI_DSS_No_DQ(self, total_num_records):
        PAF_Renewal.PageElements(self).total_records.send_keys(total_num_records)
        PAF_Renewal.PageElements(self).material_changes_no.click()
        PAF_Renewal.PageElements(self).pci_dss_compliant_no.click()
        PAF_Renewal.PageElements(self).known_issues_no.click()
        PAF_Renewal.PageElements(self).next_button.click()

    def create_quote_trigger_DQ(self, total_num_records):
        PAF_Renewal.PageElements(self).total_records.send_keys(total_num_records)
        PAF_Renewal.PageElements(self).material_changes_no.click()
        PAF_Renewal.PageElements(self).pci_dss_compliant_yes.click()
        PAF_Renewal.PageElements(self).known_issues_yes.click()
        PAF_Renewal.PageElements(self).next_button.click()

    #TODO
    # Ask Dev to create ID for next button
    def click_next(self):
        next_button = self.driver.find_element(By.XPATH, "//form[@id='rate-adjustment-form']/div[2]/div[3]/a/span[2]")
        next_button.click()

    def click_return_to_Admin_Interface(self):
        PAF_Renewal.PageElements(self).return_to_Admin.click()