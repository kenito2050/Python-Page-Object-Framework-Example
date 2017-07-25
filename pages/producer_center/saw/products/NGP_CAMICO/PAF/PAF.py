from selenium.webdriver.common.by import By

class PAF():

    def __init__(self, driver):
        self.driver = driver

    # Page Elements

    def Page_Elements(self):

        self.next_button = self.driver.find_element(By.XPATH, "//form[@id='rate-adjustment-form']/div[2]/div[3]/a/span[2]/span/span")

        # Existing Insured
        self.existing_insured_yes = self.driver.find_element(By.ID, "ngp_camico_existing_insured-yes")

        self.existing_insured_no = self.driver.find_element(By.ID, "ngp_camico_existing_insured-no")

        # Indicate current Cyber Liability limit with CAMICO:
        self.existing_insured_detail_50 = self.driver.find_element(By.ID, "ngp_camico_existing_insured_detail-50")

        self.existing_insured_detail_100 = self.driver.find_element(By.ID, "ngp_camico_existing_insured_detail-100")

        # Date operations commenced under current ownership
        # self.date_operations_commenced = self.driver.find_element(By.ID, "operation-commence-date")

        # Description of Operations
        # self.operations_description = self.driver.find_element(By.ID, "operation-nature")

        # Annual Gross Revenues
        # Current Year Annual Projection - Field is Disabled
        # self.annual_revenue_one_year_ago = self.driver.find_element(By.ID, "annual_revenue_one_year_ago")

        # Intake Questions

        # Do you own any subsidiaries?
        self.subsidiary_inclusion_yes = self.driver.find_element(By.ID, "subsidiary_inclusion-yes")

        self.subsidiary_inclusion_no = self.driver.find_element(By.ID, "subsidiary_inclusion-no")

        # Is coverage requested for any entity or organization other than the Applicant and its Subsidiaries?
        self.coverage_for_other_entity_yes = self.driver.find_element(By.ID, "coverage_for_other_entity-yes")

        self.coverage_for_other_entity_no = self.driver.find_element(By.ID, "coverage_for_other_entity-no")

        # Do You use anti-virus software and firewall protection on all desktops, portable devices and mission critical servers?
        self.platform_security_yes = self.driver.find_element(By.ID, "ngp_camico_platform_security-yes")

        self.platform_security_no = self.driver.find_element(By.ID, "ngp_camico_platform_security-no")

        # Do You enforce privacy and security policies, including mandatory employee training, that must be followed by all employees, contractors, or other individuals or organizations with access to customer information?
        self.customer_information_yes = self.driver.find_element(By.ID, "ngp_camico_customer_information-yes")

        self.customer_information_no = self.driver.find_element(By.ID, "ngp_camico_customer_information-no")

        # Does Your organization store personal and/or confidential data on portable devices, including laptops, cell phones, PDAs, back-up tapes, USB thumb drives and external hard drives?
        self.data_security_yes = self.driver.find_element(By.ID, "ngp_camico_data_security-yes")

        self.data_security_no = self.driver.find_element(By.ID, "ngp_camico_data_security-no")

        ##### If Yes, User prompted to answer the following
        # Is such data encrypted to industry standards?
        self.data_security_encrypted_yes = self.driver.find_element(By.ID, "ngp_camico_data_security_encrypted-yes")

        self.data_security_encrypted_no = self.driver.find_element(By.ID, "ngp_camico_data_security_encrypted-yes")

        # Does Your organization process, store, transmit or handle credit or debit card data?
        self.credit_card_data_yes = self.driver.find_element(By.ID, "ngp_camico_credit_card_data-yes")

        self.credit_card_data_no = self.driver.find_element(By.ID, "ngp_camico_credit_card_data-no")

        ##### If Yes, User prompted to answer the following
        # Are Your data security controls compliant with the Payment Card Industry Data Security Standard (PCI DSS)?
        self.credit_card_data_compliant_yes = self.driver.find_element(By.ID, "ngp_camico_credit_card_data_compliant-yes")

        self.credit_card_data_compliant_no = self.driver.find_element(By.ID, "ngp_camico_credit_card_data_compliant-no")

        # Does the number of records You store, either electronic or paper, exceed 50,000 records?
        # self.records_exceed_50000_yes = self.driver.find_element(By.ID, "ngp_camico_records_exceed_50000-yes")

        # self.records_exceed_50000_no = self.driver.find_element(By.ID, "ngp_camico_records_exceed_50000-no")

        ##### If Yes, User prompted to answer the following
        # Please provide the total number of records stored by the Applicant(s):
        # self.records_exceed_50000_total = self.driver.find_element(By.ID,"ngp_camico_records_exceed_50000_total")

        # Has the Applicant or any other organization proposed for this insurance experienced a wire transfer loss in the past five years?
        # self.wire_transfer_loss_yes = self.driver.find_element(By.ID, "ngp_camico_wire_transfer_loss-yes")

        # self.wire_transfer_loss_no = self.driver.find_element(By.ID, "ngp_camico_wire_transfer_loss-no")

        # Have You or any person or entity proposed for this insurance received any complaints or claims or been the subject in litigation involving matters of privacy injury, identity theft, denial of service attacks, computer virus infections, theft of information, damage to third-party networks or Your customer's ability to rely on Your network?
        self.cyber_complaints_litigation_yes = self.driver.find_element(By.ID,"ngp_camico_cyber_complaints_litigation-yes")

        self.cyber_complaints_litigation_no = self.driver.find_element(By.ID,"ngp_camico_cyber_complaints_litigation-no")

        # Are You or any person or entity proposed for this insurance aware of any security breaches, privacy-related events or incidents, or allegations of breach of privacy?
        self.compromised_security_yes = self.driver.find_element(By.ID,"ngp_camico_aware_compromised_security-yes")

        self.compromised_security_no = self.driver.find_element(By.ID,"ngp_camico_aware_compromised_security-no")

        # Have You or any person or entity proposed for this insurance ever been non-renewed, placed on extension, or declined for similar privacy/security liability coverage?
        self.non_renewed_extention_cyb_yes = self.driver.find_element(By.ID,"ngp_camico_non_renewed_extension_cyb-yes")

        self.non_renewed_extention_cyb_no = self.driver.find_element(By.ID,"ngp_camico_non_renewed_extension_cyb-no")

        return self

    def create_quote_PCI_DSS_No_DQ_50k(self):
        PAF.Page_Elements(self).existing_insured_yes.click()
        PAF.Page_Elements(self).existing_insured_detail_50.click()
        PAF.Page_Elements(self).subsidiary_inclusion_no.click()
        PAF.Page_Elements(self).coverage_for_other_entity_no.click()
        PAF.Page_Elements(self).platform_security_yes.click()
        PAF.Page_Elements(self).customer_information_yes.click()
        PAF.Page_Elements(self).data_security_yes.click()
        PAF.Page_Elements(self).data_security_encrypted_yes.click()
        PAF.Page_Elements(self).credit_card_data_yes.click()
        PAF.Page_Elements(self).credit_card_data_compliant_yes.click()
        #PAF.Page_Elements(self).records_exceed_50000_no.click()
        #PAF.Page_Elements(self).records_exceed_50000_total.send_keys("50000")
        #PAF.Page_Elements(self).wire_transfer_loss_no.click()
        PAF.Page_Elements(self).cyber_complaints_litigation_no.click()
        PAF.Page_Elements(self).compromised_security_no.click()
        PAF.Page_Elements(self).non_renewed_extention_cyb_no.click()
        #PAF.Page_Elements(self).next_button.click()

    def create_quote_PCI_DSS_No_DQ_100k(self):
        PAF.Page_Elements(self).existing_insured_yes.click()
        PAF.Page_Elements(self).existing_insured_detail_100.click()
        PAF.Page_Elements(self).subsidiary_inclusion_no.click()
        PAF.Page_Elements(self).coverage_for_other_entity_no.click()
        PAF.Page_Elements(self).platform_security_yes.click()
        PAF.Page_Elements(self).customer_information_yes.click()
        PAF.Page_Elements(self).data_security_yes.click()
        PAF.Page_Elements(self).data_security_encrypted_yes.click()
        PAF.Page_Elements(self).credit_card_data_yes.click()
        PAF.Page_Elements(self).credit_card_data_compliant_yes.click()
        #PAF.Page_Elements(self).records_exceed_50000_no.click()
        #PAF.Page_Elements(self).records_exceed_50000_total.send_keys("50000")
        #PAF.Page_Elements(self).wire_transfer_loss_no.click()
        PAF.Page_Elements(self).cyber_complaints_litigation_no.click()
        PAF.Page_Elements(self).compromised_security_no.click()
        PAF.Page_Elements(self).non_renewed_extention_cyb_no.click()
        #PAF.Page_Elements(self).next_button.click()

    def create_quote_No_PCI_DSS_No_DQ_50k(self):
        PAF.Page_Elements(self).existing_insured_yes.click()
        PAF.Page_Elements(self).existing_insured_detail_50.click()
        PAF.Page_Elements(self).subsidiary_inclusion_no.click()
        PAF.Page_Elements(self).coverage_for_other_entity_no.click()
        PAF.Page_Elements(self).platform_security_yes.click()
        PAF.Page_Elements(self).customer_information_yes.click()
        PAF.Page_Elements(self).data_security_yes.click()
        PAF.Page_Elements(self).data_security_encrypted_yes.click()
        PAF.Page_Elements(self).credit_card_data_no.click()
        #PAF.Page_Elements(self).credit_card_data_compliant_yes.click()
        #PAF.Page_Elements(self).records_exceed_50000_no.click()
        #PAF.Page_Elements(self).records_exceed_50000_total.send_keys("50000")
        #PAF.Page_Elements(self).wire_transfer_loss_no.click()
        PAF.Page_Elements(self).cyber_complaints_litigation_no.click()
        PAF.Page_Elements(self).compromised_security_no.click()
        PAF.Page_Elements(self).non_renewed_extention_cyb_no.click()
        #PAF.Page_Elements(self).next_button.click()

    def create_quote_No_PCI_DSS_No_DQ_100k(self):
        PAF.Page_Elements(self).existing_insured_yes.click()
        PAF.Page_Elements(self).existing_insured_detail_100.click()
        PAF.Page_Elements(self).subsidiary_inclusion_no.click()
        PAF.Page_Elements(self).coverage_for_other_entity_no.click()
        PAF.Page_Elements(self).platform_security_yes.click()
        PAF.Page_Elements(self).customer_information_yes.click()
        PAF.Page_Elements(self).data_security_yes.click()
        PAF.Page_Elements(self).data_security_encrypted_yes.click()
        PAF.Page_Elements(self).credit_card_data_no.click()
        #PAF.Page_Elements(self).credit_card_data_compliant_yes.click()
        #PAF.Page_Elements(self).records_exceed_50000_no.click()
        #PAF.Page_Elements(self).records_exceed_50000_total.send_keys("50000")
        #PAF.Page_Elements(self).wire_transfer_loss_no.click()
        PAF.Page_Elements(self).cyber_complaints_litigation_no.click()
        PAF.Page_Elements(self).compromised_security_no.click()
        PAF.Page_Elements(self).non_renewed_extention_cyb_no.click()
        #PAF.Page_Elements(self).next_button.click()


    def old_create_quote_NO_PCI_DSS(self):
        # Description of Operations
        operations_description = self.driver.find_element(By.ID, "operation_nature")

        # Does the Applicant use anti-virus software and a securely configured firewall to protect their network?
        platform_security_yes = self.driver.find_element(By.ID, "ngp_camico_platform_security-yes")

        platform_security_no = self.driver.find_element(By.ID, "ngp_camico_platform_security-no")

        # If Your organization stores personal information on portable devices, including laptops, cell phones, PDAs, back-up tapes, USB thumb drivers and external hard drives, is such data encrypted to industry standards
        data_storage_yes = self.driver.find_element(By.ID, "ngp_camico_data_storage-yes")

        data_storage_no = self.driver.find_element(By.ID, "ngp_camico_data_storage-no")

        # If "Yes", is such data encrypted to industry standards

        data_security_standards_yes = self.driver.find_element(By.ID, "ngp_camico_data_security_standards-yes")

        data_security_standards_no = self.driver.find_element(By.ID, "ngp_camico_data_security_standards-no")

        # Does the applicant utilize a cloud provider to store data

        cloud_provider_yes = self.driver.find_element(By.ID, "ngp_camico_cloud_provider-yes")

        cloud_provider_no = self.driver.find_element(By.ID, "ngp_camico_cloud_provider-no")

        # Please name the cloud provider
        ngp_cloud_provider_detail = self.driver.find_element(By.ID, "ngp_camico_cloud_provider_detail")

        # Are you PCI-DSS Compliant
        pci_dss_compliant_yes = self.driver.find_element(By.ID, "ngp_camico_pci_dss_compliant-yes")

        pci_dss_compliant_no = self.driver.find_element(By.ID, "ngp_camico_pci_dss_compliant-no")

        # pci_dss_compliant_na = self.driver.find_element(By.ID, "ngp_pci_dss_compliant-na")

        # Has the Applicant or any other person or entity proposed for this insurance received any complaints or claims, or been the subject in litigation, involving matters of privacy injury, identity theft, denial of service attacks, computer virus infections, theft of information, damage to third party networks, or the ability of customers to rely on the Applicant's network

        complaints_litigation_yes = self.driver.find_element(By.ID, "ngp_camico_complaints_litigation-yes")

        complaints_litigation_no = self.driver.find_element(By.ID, "ngp_camico_complaints_litigation-no")

        # Is the Applicant or any other person or entity proposed for this insurance aware of or have knowledge of any act, events, circumstances or incidents that may give rise to complaints or claims involving matters of privacy injury, identity theft, denial of service attacks, computer virus infections, theft of information, damage to third party networks, or the ability of customers' to rely on the Applicant's network
        regulatory_investigation_yes = self.driver.find_element(By.ID, "ngp_camico_regulatory_investigation-yes")

        regulatory_investigation_no = self.driver.find_element(By.ID, "ngp_camico_regulatory_investigation-no")

        operations_description.send_keys("QA Test")
        platform_security_yes.click()
        data_storage_yes.click()
        data_security_standards_yes.click()
        cloud_provider_yes.click()
        ngp_cloud_provider_detail.send_keys("Amazon")
        pci_dss_compliant_no.click()
        complaints_litigation_no.click()
        regulatory_investigation_no.click()

    def click_next(self):
        PAF.Page_Elements(self).next_button.click()