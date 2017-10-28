from selenium.webdriver.common.by import By

class PAF():

    def __init__(self, driver):
        self.driver = driver

    #Page Elements

    def Page_Elements(self):

        # Return to Admin Link
        self.return_to_Admin = self.driver.find_element(By.LINK_TEXT, "Return to Admin Interface")

        # Description of operations
        self.operations_description = self.driver.find_element(By.ID, "operation_nature")

        # total number of customer and/or employee records
        self.total_records = self.driver.find_element(By.ID, "ngp_total_records")

        # Does the Applicant use anti-virus software and a securely configured firewall to protect their network?
        self.platform_security_yes = self.driver.find_element(By.ID, "ngp_platform_security-yes")

        self.platform_security_no = self.driver.find_element(By.ID, "ngp_platform_security-no")

        # If Your organization stores personal information on portable devices, including laptops, cell phones, PDAs, back-up tapes, USB thumb drivers and external hard drives, is such data encrypted to industry standards
        self.data_storage_yes = self.driver.find_element(By.ID, "ngp_data_storage-yes")

        self.data_storage_no = self.driver.find_element(By.ID, "ngp_data_storage-no")

        # If "Yes", is such data encrypted to industry standards

        self.data_security_standards_yes = self.driver.find_element(By.ID, "ngp_data_security_standards-yes")

        self.data_security_standards_no = self.driver.find_element(By.ID, "ngp_data_security_standards-no")

        # Does the applicant utilize a cloud provider to store data

        self.cloud_provider_yes = self.driver.find_element(By.ID, "ngp_cloud_provider-yes")

        self.cloud_provider_no = self.driver.find_element(By.ID, "ngp_cloud_provider-no")

        # Please name the cloud provider
        self.cloud_provider_detail = self.driver.find_element(By.ID, "ngp_cloud_provider_detail")

        # Are you PCI-DSS Compliant
        self.pci_dss_compliant_yes = self.driver.find_element(By.ID, "ngp_pci_dss_compliant-yes")

        self.pci_dss_compliant_no = self.driver.find_element(By.ID, "ngp_pci_dss_compliant-no")

        # pci_dss_compliant_na = self.driver.find_element(By.ID, "ngp_pci_dss_compliant-na")

        # Has the Applicant or any other person or entity proposed for this insurance received any complaints or claims, or been the subject in litigation, involving matters of privacy injury, identity theft, denial of service attacks, computer virus infections, theft of information, damage to third party networks, or the ability of customers to rely on the Applicant's network

        self.complaints_litigation_yes = self.driver.find_element(By.ID, "ngp_complaints_litigation-yes")

        self.complaints_litigation_no = self.driver.find_element(By.ID, "ngp_complaints_litigation-no")

        # Is the Applicant or any other person or entity proposed for this insurance aware of or have knowledge of any act, events, circumstances or incidents that may give rise to complaints or claims involving matters of privacy injury, identity theft, denial of service attacks, computer virus infections, theft of information, damage to third party networks, or the ability of customers' to rely on the Applicant's network
        self.regulatory_investigation_yes = self.driver.find_element(By.ID, "ngp_regulatory_investigation-yes")

        self.regulatory_investigation_no = self.driver.find_element(By.ID, "ngp_regulatory_investigation-no")



        return self

    def create_quote_PCI_DSS_No_DQ(self, total_num_records):
        PAF.Page_Elements(self).operations_description.send_keys("QA Test")
        PAF.Page_Elements(self).total_records.send_keys(total_num_records)
        PAF.Page_Elements(self).platform_security_yes.click()
        PAF.Page_Elements(self).data_storage_yes.click()
        PAF.Page_Elements(self).data_security_standards_yes.click()
        PAF.Page_Elements(self).cloud_provider_yes.click()
        PAF.Page_Elements(self).cloud_provider_detail.send_keys("Amazon")
        PAF.Page_Elements(self).pci_dss_compliant_yes.click()
        PAF.Page_Elements(self).complaints_litigation_no.click()
        PAF.Page_Elements(self).regulatory_investigation_no.click()

    def create_quote_No_PCI_DSS_No_DQ(self, total_num_records):
        PAF.Page_Elements(self).operations_description.send_keys("QA Test")
        PAF.Page_Elements(self).total_records.send_keys(total_num_records)
        PAF.Page_Elements(self).platform_security_yes.click()
        PAF.Page_Elements(self).data_storage_yes.click()
        PAF.Page_Elements(self).data_security_standards_yes.click()
        PAF.Page_Elements(self).cloud_provider_yes.click()
        PAF.Page_Elements(self).cloud_provider_detail.send_keys("Amazon")
        PAF.Page_Elements(self).pci_dss_compliant_no.click()
        PAF.Page_Elements(self).complaints_litigation_no.click()
        PAF.Page_Elements(self).regulatory_investigation_no.click()

    def create_quote_trigger_DQ(self, total_num_records):
        PAF.Page_Elements(self).operations_description.send_keys("QA Test")
        PAF.Page_Elements(self).total_records.send_keys(total_num_records)
        # Next Question will trigger DQ
        PAF.Page_Elements(self).platform_security_no.click()
        PAF.Page_Elements(self).data_storage_yes.click()
        PAF.Page_Elements(self).data_security_standards_yes.click()
        PAF.Page_Elements(self).cloud_provider_yes.click()
        PAF.Page_Elements(self).cloud_provider_detail.send_keys("Amazon")
        PAF.Page_Elements(self).pci_dss_compliant_yes.click()
        PAF.Page_Elements(self).complaints_litigation_no.click()
        PAF.Page_Elements(self).regulatory_investigation_no.click()

    #TODO
    # Ask Dev to create ID for next button
    def click_next(self):
        next_button = self.driver.find_element(By.XPATH, "//form[@id='rate-adjustment-form']/div[2]/div[5]/a/span[2]")
        next_button.click()

    def click_return_to_Admin_Interface(self):
        PAF.Page_Elements(self).return_to_Admin.click()