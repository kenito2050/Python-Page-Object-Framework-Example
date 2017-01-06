from selenium.webdriver.common.by import By

class PAF():

    def __init__(self, driver):
        self.driver = driver

    def create_quote_no_DQ(self):
        # Description of Operations
        operations_description = self.driver.find_element(By.ID, "operation_nature")

        #Does the Applicant use anti-virus software and a securely configured firewall to protect their network?
        platform_security_yes = self.driver.find_element(By.ID, "ngp_platform_security-yes")

        platform_security_no = self.driver.find_element(By.ID, "ngp_platform_security-no")

        #If Your organization stores personal information on portable devices, including laptops, cell phones, PDAs, back-up tapes, USB thumb drivers and external hard drives, is such data encrypted to industry standards
        data_storage_yes = self.driver.find_element(By.ID, "ngp_data_storage-yes")

        data_storage_no = self.driver.find_element(By.ID, "ngp_data_storage-no")

        #If "Yes", is such data encrypted to industry standards

        data_security_standards_yes = self.driver.find_element(By.ID, "ngp_data_security_standards-yes")

        data_security_standards_no = self.driver.find_element(By.ID, "ngp_data_security_standards-no")

        #Are you PCI-DSS Compliant
        pci_dss_compliant_yes = self.driver.find_element(By.ID, "ngp_pci_dss_compliant-yes")

        pci_dss_compliant_no = self.driver.find_element(By.ID, "ngp_pci_dss_compliant-no")

        pci_dss_compliant_na = self.driver.find_element(By.ID, "ngp_pci_dss_compliant-na")

        # Has the Applicant or any other person or entity proposed for this insurance received any complaints or claims, or been the subject in litigation, involving matters of privacy injury, identity theft, denial of service attacks, computer virus infections, theft of information, damage to third party networks, or the ability of customers to rely on the Applicant's network

        complaints_litigation_yes = self.driver.find_element(By.ID, "ngp_complaints_litigation-yes")

        complaints_litigation_no = self.driver.find_element(By.ID, "ngp_complaints_litigation-no")

        #Is the Applicant or any other person or entity proposed for this insurance aware of or have knowledge of any act, events, circumstances or incidents that may give rise to complaints or claims involving matters of privacy injury, identity theft, denial of service attacks, computer virus infections, theft of information, damage to third party networks, or the ability of customers' to rely on the Applicant's network
        regulatory_investigation_yes = self.driver.find_element(By.ID, "ngp_regulatory_investigation-yes")

        regulatory_investigation_no = self.driver.find_element(By.ID, "ngp_regulatory_investigation-no")


        operations_description.send_keys("QA Test")
        platform_security_yes.click()
        data_storage_yes.click()
        data_security_standards_yes.click()
        pci_dss_compliant_yes.click()
        complaints_litigation_no.click()
        regulatory_investigation_no.click()

    #TODO
    # Ask Dev to create ID for next button
    def click_next(self):
        next_button = self.driver.find_element(By.XPATH, "//form[@id='rate-adjustment-form']/div[2]/div[5]/a/span[2]/span/span")
        next_button.click()