from selenium.webdriver.common.by import By

class PAF():

    def __init__(self, driver):
        self.driver = driver

    #Page Elements

    def Page_Elements(self):

        # Current or prospective insured?
        self.existing_insured_yes = self.driver.find_element(By.ID, "cyb_omsnic_current_insured-yes")


        self.existing_insured_no = self.driver.find_element(By.ID, "cyb_omsnic_current_insured-no")

        # policy number:
        self.policy_number = self.driver.find_element(By.ID, "external_policy_number")

        # Date operations commenced under current ownership
        self.operation_commence_date = self.driver.find_element(By.ID, "cyb_omsnic_operation_commence_date")

        # Description of operations
        self.operations_description = self.driver.find_element(By.ID, "cyb_omsnic_operation_nature")

        # Annual Gross Revenues

        # Current Year Annual Projection:

        self.annual_revenue_current_year = self.driver.find_element(By.ID, "annual_revenue_current_year")

        # Prior Year:

        self.annual_revenue_one_year_ago = self.driver.find_element(By.ID, "annual_revenue_one_year_ago")

        # Is Your organization formally engaged with Black Talon Security?

        self.black_talon_security_yes = self.driver.find_element(By.ID, "cyb_omsnic_black_talon_security-yes")

        self.black_talon_security_no = self.driver.find_element(By.ID, "cyb_omsnic_black_talon_security-no")

        # Do You own any subsidiaries?

        self.subsidiary_inclusion_yes = self.driver.find_element(By.ID, "cyb_omsnic_subsidiary_inclusion-yes")

        self.subsidiary_inclusion_no = self.driver.find_element(By.ID, "cyb_omsnic_subsidiary_inclusion-no")

        # Is coverage requested for any entity or organization other than the Applicant and its Subsidiaries?

        self.coverage_for_other_entity_yes = self.driver.find_element(By.ID, "cyb_omsnic_coverage_for_other_entity-yes")

        self.coverage_for_other_entity_no = self.driver.find_element(By.ID, "cyb_omsnic_coverage_for_other_entity-no")

        # Cyber Liability Questions

        # Do You have a HIPAA compliance program in place?

        self.hipaa_compliance_program_yes = self.driver.find_element(By.ID, "cyb_omsnic_hipaa_compliance_program-yes")

        self.hipaa_compliance_program_no = self.driver.find_element(By.ID, "cyb_omsnic_hipaa_compliance_program-no")

        # Do You use anti-virus software and firewall protection on all desktops, portable devices and mission critical servers?

        self.platform_security_yes = self.driver.find_element(By.ID, "cyb_omsnic_platform_security-yes")

        self.platform_security_no = self.driver.find_element(By.ID, "cyb_omsnic_platform_security-no")

        # Do You enforce privacy and security policies, including mandatory employee training, that must be followed by all employees, contractors, or other individuals or organizations with access to patient information?

        self.patient_information_yes = self.driver.find_element(By.ID, "cyb_omsnic_patient_information-yes")

        self.patient_information_no = self.driver.find_element(By.ID, "cyb_omsnic_patient_information-no")

        # Does Your organization store personal and/or confidential data on portable devices, including laptops, cell phones, PDAs, back-up tapes, USB thumb drives and external hard drives?

        self.data_security_yes = self.driver.find_element(By.ID, "cyb_omsnic_data_security-yes")

        self.data_security_no = self.driver.find_element(By.ID, "cyb_omsnic_data_security-no")

        # Does Your organization process, store, transmit or handle credit or debit card data?

        self.credit_card_data_yes = self.driver.find_element(By.ID, "cyb_omsnic_credit_card_data-yes")

        self.credit_card_data_no = self.driver.find_element(By.ID, "cyb_omsnic_credit_card_data-no")

        # Does the number of records You store, either electronic or paper, exceed 20,000 records per physician?

        self.records_exceed_20000_yes = self.driver.find_element(By.ID, "cyb_omsnic_records_exceed_20000-yes")

        self.records_exceed_20000_no = self.driver.find_element(By.ID, "cyb_omsnic_records_exceed_20000-no")

        # total number of records

        self.records_exceed_20000_total = self.driver.find_element(By.ID, "cyb_omsnic_records_exceed_20000_total")

        # Have You or any physician in Your group received any complaints or claims or been the subject in litigation involving matters of privacy injury, identity theft, denial of service attacks, computer virus infections, theft of information, damage to third-party networks or Your customer's ability to rely on Your network?

        self.cyber_complaints_litigation_yes = self.driver.find_element(By.ID, "cyb_omsnic_cyber_complaints_litigation-yes")

        self.cyber_complaints_litigation_no = self.driver.find_element(By.ID, "cyb_omsnic_cyber_complaints_litigation-no")

        # Are You or any physician in Your group aware of any security breaches, privacy-related events or incidents, or allegations of breach of privacy?

        self.aware_compromised_security_yes = self.driver.find_element(By.ID, "cyb_omsnic_aware_compromised_security-yes")

        self.aware_compromised_security_no = self.driver.find_element(By.ID, "cyb_omsnic_aware_compromised_security-no")

        # Have You ever been non-renewed, placed on extension, or declined for similar privacy/security liability coverage?

        self.non_renewed_extention_cyb_yes = self.driver.find_element(By.ID, "cyb_omsnic_non_renewed_extension-yes")

        self.non_renewed_extention_cyb_no = self.driver.find_element(By.ID, "cyb_omsnic_non_renewed_extension-no")

        return self

    def create_quote_PCI_DSS_Compliance_No_DQ(self, current_revenue, previous_revenue):
        PAF.Page_Elements(self).existing_insured_yes.click()
        PAF.Page_Elements(self).policy_number.send_keys("A111111111")
        PAF.Page_Elements(self).operation_commence_date.send_keys("01-01-2001")
        PAF.Page_Elements(self).operations_description.send_keys("QA TEST")
        PAF.Page_Elements(self).annual_revenue_current_year.send_keys(current_revenue)
        PAF.Page_Elements(self).annual_revenue_one_year_ago.send_keys(previous_revenue)
        PAF.Page_Elements(self).black_talon_security_no.click()
        PAF.Page_Elements(self).subsidiary_inclusion_no.click()
        PAF.Page_Elements(self).coverage_for_other_entity_no.click()

        # Cyber Liability Questions
        PAF.Page_Elements(self).hipaa_compliance_program_yes.click()
        PAF.Page_Elements(self).platform_security_yes.click()
        PAF.Page_Elements(self).patient_information_yes.click()
        PAF.Page_Elements(self).data_security_yes.click()
        # Questions 13a and 13b were hidden but now display
        # call the is_data_encrypted_yes or is_data_encrypted_no method to answer questions 13a and 13b

        PAF.Page_Elements(self).credit_card_data_yes.click()
        # Question 14a displays if Yes
        PAF.Page_Elements(self).records_exceed_20000_no.click()
        PAF.Page_Elements(self).cyber_complaints_litigation_no.click()
        PAF.Page_Elements(self).aware_compromised_security_no.click()
        PAF.Page_Elements(self).non_renewed_extention_cyb_no.click()

    def create_quote_No_Data_Encryption_No_PCI_DSS_Compliance_No_DQ(self, current_revenue, previous_revenue):
        PAF.Page_Elements(self).existing_insured_yes.click()
        PAF.Page_Elements(self).policy_number.send_keys("A111111111")
        PAF.Page_Elements(self).operation_commence_date.send_keys("01-01-2001")
        PAF.Page_Elements(self).operations_description.send_keys("QA TEST")
        PAF.Page_Elements(self).annual_revenue_current_year.send_keys(current_revenue)
        PAF.Page_Elements(self).annual_revenue_one_year_ago.send_keys(previous_revenue)
        PAF.Page_Elements(self).black_talon_security_no.click()
        PAF.Page_Elements(self).subsidiary_inclusion_no.click()
        PAF.Page_Elements(self).coverage_for_other_entity_no.click()

        # Cyber Liability Questions
        PAF.Page_Elements(self).hipaa_compliance_program_yes.click()
        PAF.Page_Elements(self).platform_security_yes.click()
        PAF.Page_Elements(self).patient_information_yes.click()
        PAF.Page_Elements(self).data_security_yes.click()
        # Questions 13a and 13b were hidden but now display
        # call the is_data_encrypted_yes or is_data_encrypted_no method to answer questions 13a and 13b

        PAF.Page_Elements(self).credit_card_data_no.click()
        PAF.Page_Elements(self).records_exceed_20000_no.click()
        PAF.Page_Elements(self).cyber_complaints_litigation_no.click()
        PAF.Page_Elements(self).aware_compromised_security_no.click()
        PAF.Page_Elements(self).non_renewed_extention_cyb_no.click()

    def create_quote_Data_Encryption_No_PCI_DSS_Compliance_No_DQ(self, current_revenue, previous_revenue):
        PAF.Page_Elements(self).existing_insured_yes.click()
        PAF.Page_Elements(self).policy_number.send_keys("A111111111")
        PAF.Page_Elements(self).operation_commence_date.send_keys("01-01-2001")
        PAF.Page_Elements(self).operations_description.send_keys("QA TEST")
        PAF.Page_Elements(self).annual_revenue_current_year.send_keys(current_revenue)
        PAF.Page_Elements(self).annual_revenue_one_year_ago.send_keys(previous_revenue)
        PAF.Page_Elements(self).black_talon_security_no.click()
        PAF.Page_Elements(self).subsidiary_inclusion_no.click()
        PAF.Page_Elements(self).coverage_for_other_entity_no.click()

        # Cyber Liability Questions
        PAF.Page_Elements(self).hipaa_compliance_program_yes.click()
        PAF.Page_Elements(self).platform_security_yes.click()
        PAF.Page_Elements(self).patient_information_yes.click()
        PAF.Page_Elements(self).data_security_yes.click()
        # Questions 13a and 13b were hidden but now display
        # call the is_data_encrypted_yes or is_data_encrypted_no method to answer questions 13a and 13b

        PAF.Page_Elements(self).credit_card_data_yes.click()
        # Question 14a displays if Yes
        PAF.Page_Elements(self).records_exceed_20000_no.click()
        PAF.Page_Elements(self).cyber_complaints_litigation_no.click()
        PAF.Page_Elements(self).aware_compromised_security_no.click()
        PAF.Page_Elements(self).non_renewed_extention_cyb_no.click()

        # If user selects Yes to Question 13 (organization store personal and/or confidential data on portable devices), Then Questions 13a & 13b display
        # Next methods will answer Questions 13a and 13b

    def is_data_encrypted_yes(self):
        # Define the page objects

        # Question 13a
        # If “YES”, Is such data encrypted to industry standards?
        self.data_security_encrypted_yes = self.driver.find_element(By.ID, "cyb_omsnic_data_security_encrypted-yes")

        self.data_security_encrypted_no = self.driver.find_element(By.ID, "cyb_omsnic_data_security_encrypted-no")

        # Question 13b
        # If “NO”, to question 13.a., please describe on a separate page the type of devices used, the nature of data/information stored, and the security measures You have in place to protect such data/information.
        # self.device_type_yes = self.driver.find_element(By.ID, "cyb_omsnic_device_type-yes")
        #
        # self.device_type_no = self.driver.find_element(By.ID, "cyb_omsnic_device_type-no")

        # Select Yes for question 13a and 13b
        self.data_security_encrypted_yes.click()
        # self.device_type_yes.click()

    def is_data_encrypted_no(self):
        # Question 13a
        # If “YES”, Is such data encrypted to industry standards?
        self.data_security_encrypted_yes = self.driver.find_element(By.ID, "cyb_omsnic_data_security_encrypted-yes")

        self.data_security_encrypted_no = self.driver.find_element(By.ID, "cyb_omsnic_data_security_encrypted-no")

        # Question 13b
        # If “NO”, to question 13.a., please describe on a separate page the type of devices used, the nature of data/information stored, and the security measures You have in place to protect such data/information.
        # self.device_type_yes = self.driver.find_element(By.ID, "cyb_omsnic_device_type-yes")
        #
        # self.device_type_no = self.driver.find_element(By.ID, "cyb_omsnic_device_type-no")

        # Select No for question 13a and 13b
        self.data_security_encrypted_no.click()
        # self.device_type_no.click()

    def credit_card_compliant_yes(self):

        # Question 14a ONLY DISPLAYS IF YES TO QUESTION "organization process, store, transmit or handle credit or debit card data"

        # Are Your data security controls compliant with the Payment Card Industry Data Security Standard (PCI DSS)?

        self.pci_dss_yes = self.driver.find_element(By.ID, "cyb_omsnic_pci_dss-yes")

        self.pci_dss_no = self.driver.find_element(By.ID, "cyb_omsnic_pci_dss-no")

        self.pci_dss_yes.click()

    def credit_card_compliant_no(self):
        # Question 14a ONLY DISPLAYS IF YES TO QUESTION "organization process, store, transmit or handle credit or debit card data"

        # Are Your data security controls compliant with the Payment Card Industry Data Security Standard (PCI DSS)?

        self.pci_dss_yes = self.driver.find_element(By.ID, "cyb_omsnic_pci_dss-yes")

        self.pci_dss_no = self.driver.find_element(By.ID, "cyb_omsnic_pci_dss-no")

        self.pci_dss_no.click()

    def click_next(self):
        next_button = self.driver.find_element(By.XPATH, "//form[@id='rate-adjustment-form']/div[5]/a/span[2]/span/span")
        next_button.click()