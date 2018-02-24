from selenium.webdriver.common.by import By

class PAF():

    def __init__(self, driver):
        self.driver = driver

    #Page Elements

    def Page_Elements(self):

        # Organization Legal Structure

        # Corporation
        self.corporation = self.driver.find_element(By.ID, "legal-structure-corporation")

        # Partnership
        self.partnership = self.driver.find_element(By.ID, "legal-structure-partnership")

        # LLC
        self.llc = self.driver.find_element(By.ID, "legal-structure-llc")

        # Individual
        self.individual = self.driver.find_element(By.ID, "legal-structure-individual")

        # Other
        self.other = self.driver.find_element(By.ID, "legal-structure-oth")

        # Other (Text Field)
        self.other_text_field = self.driver.find_element(By.ID, "legal-structure-other")

        # Total Revenue
        self.total_revenue = self.driver.find_element(By.ID, "annual_revenue_current_year")

        # Does the applicant utilize a cloud provider to store data

        self.cloud_provider_yes = self.driver.find_element(By.ID, "ngp_sbdia_cloud_provider-yes")

        self.cloud_provider_no = self.driver.find_element(By.ID, "ngp_sbdia_cloud_provider-no")

        # Please name the cloud provider
        self.cloud_provider_name = self.driver.find_element(By.ID, "ngp_sbdia_cloud_provider_name")

        # Does the Applicant have firewall protection that is securely configured?
        self.network_security_yes = self.driver.find_element(By.ID, "ngp_sbdia_network_security-yes")

        self.network_security_no = self.driver.find_element(By.ID, "ngp_sbdia_network_security-no")

        # Does the Applicant use anti-virus software and a securely configured firewall to protect their network?
        self.platform_security_yes = self.driver.find_element(By.ID, "ngp_sbdia_platform_security-yes")

        self.platform_security_no = self.driver.find_element(By.ID, "ngp_sbdia_platform_security-no")

        # Does your company have a formal process to disable or restrict access to information systems upon termination of employees?
        self.formal_process_access_yes = self.driver.find_element(By.ID, "ngp_sbdia_formal_process_access-yes")

        self.formal_process_access_no = self.driver.find_element(By.ID, "ngp_sbdia_formal_process_access-no")

        # Does your organization store personal information on portable devices, including laptops, cell phones, PDAs, back-up tapes, USB thumb drivers and external hard drives
        self.data_security_yes = self.driver.find_element(By.ID, "ngp_sbdia_data_security-yes")

        self.data_security_no = self.driver.find_element(By.ID, "ngp_sbdia_data_security-no")

        # If "Yes", is such data encrypted to industry standards
        self.data_security_encryption_yes = self.driver.find_element(By.ID, "ngp_sbdia_data_security_encryption-yes")

        self.data_security_encryption_no = self.driver.find_element(By.ID, "ngp_sbdia_data_security_encryption-no")

        # Are you PCI-DSS Compliant
        self.pci_dss_compliant_yes = self.driver.find_element(By.ID, "ngp_sbdia_pci_dss-yes")

        self.pci_dss_compliant_no = self.driver.find_element(By.ID, "ngp_sbdia_pci_dss-no")

        # In the last five (5) years, have you experienced any claims or are you aware of any circumstances that may give rise to a claim that would have been covered by this Policy
        self.past_potential_claim_yes = self.driver.find_element(By.ID, "ngp_sbdia_past_potential_claim-yes")

        self.past_potential_claim_no = self.driver.find_element(By.ID, "ngp_sbdia_past_potential_claim-no")

        # Has the Applicant experienced a financial loss resulting from wire transfer fraud, telecommunications fraud or a phishing attack in the past three (3) years?
        # If "Yes", Cyber Crime will not be available.

        self.past_financial_loss_yes = self.driver.find_element(By.ID, "ngp_sbdia_past_financial_loss-yes")

        self.past_financial_loss_no = self.driver.find_element(By.ID, "ngp_sbdia_past_financial_loss-no")

        return self

    def create_quote_PCI_DSS_No_DQ_corporation(self, total_revenue):
        PAF.Page_Elements(self).corporation.click()
        PAF.Page_Elements(self).total_revenue.send_keys(total_revenue)
        PAF.Page_Elements(self).cloud_provider_yes.click()
        PAF.Page_Elements(self).cloud_provider_name.send_keys("Amazon")
        PAF.Page_Elements(self).network_security_yes.click()
        PAF.Page_Elements(self).platform_security_yes.click()
        PAF.Page_Elements(self).formal_process_access_yes.click()
        PAF.Page_Elements(self).data_security_yes.click()
        PAF.Page_Elements(self).data_security_encryption_yes.click()
        PAF.Page_Elements(self).pci_dss_compliant_yes.click()
        PAF.Page_Elements(self).past_potential_claim_no.click()
        PAF.Page_Elements(self).past_financial_loss_no.click()

    def create_quote_PCI_DSS_No_DQ_partnership(self, total_revenue):
        PAF.Page_Elements(self).partnership.click()
        PAF.Page_Elements(self).total_revenue.send_keys(total_revenue)
        PAF.Page_Elements(self).cloud_provider_yes.click()
        PAF.Page_Elements(self).cloud_provider_name.send_keys("Amazon")
        PAF.Page_Elements(self).network_security_yes.click()
        PAF.Page_Elements(self).platform_security_yes.click()
        PAF.Page_Elements(self).formal_process_access_yes.click()
        PAF.Page_Elements(self).data_security_yes.click()
        PAF.Page_Elements(self).data_security_encryption_yes.click()
        PAF.Page_Elements(self).pci_dss_compliant_yes.click()
        PAF.Page_Elements(self).past_potential_claim_no.click()
        PAF.Page_Elements(self).past_financial_loss_no.click()


    def create_quote_PCI_DSS_No_DQ_llc(self, total_revenue):
        PAF.Page_Elements(self).llc.click()
        PAF.Page_Elements(self).total_revenue.send_keys(total_revenue)
        PAF.Page_Elements(self).cloud_provider_yes.click()
        PAF.Page_Elements(self).cloud_provider_name.send_keys("Amazon")
        PAF.Page_Elements(self).network_security_yes.click()
        PAF.Page_Elements(self).platform_security_yes.click()
        PAF.Page_Elements(self).formal_process_access_yes.click()
        PAF.Page_Elements(self).data_security_yes.click()
        PAF.Page_Elements(self).data_security_encryption_yes.click()
        PAF.Page_Elements(self).pci_dss_compliant_yes.click()
        PAF.Page_Elements(self).past_potential_claim_no.click()
        PAF.Page_Elements(self).past_financial_loss_no.click()

    def create_quote_PCI_DSS_No_DQ_individual(self, total_revenue):
        PAF.Page_Elements(self).individual.click()
        PAF.Page_Elements(self).total_revenue.send_keys(total_revenue)
        PAF.Page_Elements(self).cloud_provider_yes.click()
        PAF.Page_Elements(self).cloud_provider_name.send_keys("Amazon")
        PAF.Page_Elements(self).network_security_yes.click()
        PAF.Page_Elements(self).platform_security_yes.click()
        PAF.Page_Elements(self).formal_process_access_yes.click()
        PAF.Page_Elements(self).data_security_yes.click()
        PAF.Page_Elements(self).data_security_encryption_yes.click()
        PAF.Page_Elements(self).pci_dss_compliant_yes.click()
        PAF.Page_Elements(self).past_potential_claim_no.click()
        PAF.Page_Elements(self).past_financial_loss_no.click()

    def create_quote_PCI_DSS_No_DQ_other(self, total_revenue):
        PAF.Page_Elements(self).other.click()
        PAF.Page_Elements(self).other_text_field.send_keys("Sole Proprietorship")
        PAF.Page_Elements(self).total_revenue.send_keys(total_revenue)
        PAF.Page_Elements(self).cloud_provider_yes.click()
        PAF.Page_Elements(self).cloud_provider_name.send_keys("Amazon")
        PAF.Page_Elements(self).network_security_yes.click()
        PAF.Page_Elements(self).platform_security_yes.click()
        PAF.Page_Elements(self).formal_process_access_yes.click()
        PAF.Page_Elements(self).data_security_yes.click()
        PAF.Page_Elements(self).data_security_encryption_yes.click()
        PAF.Page_Elements(self).pci_dss_compliant_yes.click()
        PAF.Page_Elements(self).past_potential_claim_no.click()
        PAF.Page_Elements(self).past_financial_loss_no.click()

    def create_quote_No_PCI_DSS_No_DQ_corporation(self, total_revenue):
        PAF.Page_Elements(self).corporation.click()
        PAF.Page_Elements(self).total_revenue.send_keys(total_revenue)
        PAF.Page_Elements(self).cloud_provider_yes.click()
        PAF.Page_Elements(self).cloud_provider_name.send_keys("Amazon")
        PAF.Page_Elements(self).network_security_yes.click()
        PAF.Page_Elements(self).platform_security_yes.click()
        PAF.Page_Elements(self).formal_process_access_yes.click()
        PAF.Page_Elements(self).data_security_yes.click()
        PAF.Page_Elements(self).data_security_encryption_yes.click()
        PAF.Page_Elements(self).pci_dss_compliant_no.click()
        PAF.Page_Elements(self).past_potential_claim_no.click()
        PAF.Page_Elements(self).past_financial_loss_no.click()

    def create_quote_No_PCI_DSS_No_DQ_partnership(self, total_revenue):
        PAF.Page_Elements(self).partnership.click()
        PAF.Page_Elements(self).total_revenue.send_keys(total_revenue)
        PAF.Page_Elements(self).cloud_provider_yes.click()
        PAF.Page_Elements(self).cloud_provider_name.send_keys("Amazon")
        PAF.Page_Elements(self).network_security_yes.click()
        PAF.Page_Elements(self).platform_security_yes.click()
        PAF.Page_Elements(self).formal_process_access_yes.click()
        PAF.Page_Elements(self).data_security_yes.click()
        PAF.Page_Elements(self).data_security_encryption_yes.click()
        PAF.Page_Elements(self).pci_dss_compliant_no.click()
        PAF.Page_Elements(self).past_potential_claim_no.click()
        PAF.Page_Elements(self).past_financial_loss_no.click()

    def create_quote_No_PCI_DSS_No_DQ_llc(self, total_revenue):
        PAF.Page_Elements(self).llc.click()
        PAF.Page_Elements(self).total_revenue.send_keys(total_revenue)
        PAF.Page_Elements(self).cloud_provider_yes.click()
        PAF.Page_Elements(self).cloud_provider_name.send_keys("Amazon")
        PAF.Page_Elements(self).network_security_yes.click()
        PAF.Page_Elements(self).platform_security_yes.click()
        PAF.Page_Elements(self).formal_process_access_yes.click()
        PAF.Page_Elements(self).data_security_yes.click()
        PAF.Page_Elements(self).data_security_encryption_yes.click()
        PAF.Page_Elements(self).pci_dss_compliant_no.click()
        PAF.Page_Elements(self).past_potential_claim_no.click()
        PAF.Page_Elements(self).past_financial_loss_no.click()

    def create_quote_No_PCI_DSS_No_DQ_individual(self, total_revenue):
        PAF.Page_Elements(self).individual.click()
        PAF.Page_Elements(self).total_revenue.send_keys(total_revenue)
        PAF.Page_Elements(self).cloud_provider_yes.click()
        PAF.Page_Elements(self).cloud_provider_name.send_keys("Amazon")
        PAF.Page_Elements(self).network_security_yes.click()
        PAF.Page_Elements(self).platform_security_yes.click()
        PAF.Page_Elements(self).formal_process_access_yes.click()
        PAF.Page_Elements(self).data_security_yes.click()
        PAF.Page_Elements(self).data_security_encryption_yes.click()
        PAF.Page_Elements(self).pci_dss_compliant_no.click()
        PAF.Page_Elements(self).past_potential_claim_no.click()
        PAF.Page_Elements(self).past_financial_loss_no.click()

    def create_quote_No_PCI_DSS_No_DQ_other(self, total_revenue):
        PAF.Page_Elements(self).other.click()
        PAF.Page_Elements(self).other_text_field.send_keys("Sole Proprietorship")
        PAF.Page_Elements(self).total_revenue.send_keys(total_revenue)
        PAF.Page_Elements(self).cloud_provider_yes.click()
        PAF.Page_Elements(self).cloud_provider_name.send_keys("Amazon")
        PAF.Page_Elements(self).network_security_yes.click()
        PAF.Page_Elements(self).platform_security_yes.click()
        PAF.Page_Elements(self).formal_process_access_yes.click()
        PAF.Page_Elements(self).data_security_yes.click()
        PAF.Page_Elements(self).data_security_encryption_yes.click()
        PAF.Page_Elements(self).pci_dss_compliant_no.click()
        PAF.Page_Elements(self).past_potential_claim_no.click()
        PAF.Page_Elements(self).past_financial_loss_no.click()

    #TODO
    # Ask Dev to create ID for next button
    def click_next(self):
        next_button = self.driver.find_element(By.XPATH, "//form[@id='rate-adjustment-form']/div[2]/div[7]/a/span[2]/span/span")
        next_button.click()