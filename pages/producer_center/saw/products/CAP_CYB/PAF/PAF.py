from selenium.webdriver.common.by import By

class PAF():

    def __init__(self, driver):
        self.driver = driver

    #Page Elements

    def Page_Elements(self):

        # Current or prospective Cooperative of American Physicians insured?
        self.existing_insured_yes = self.driver.find_element(By.ID, "cap_cyb_existing_insured-yes")

        self.existing_insured_no = self.driver.find_element(By.ID, "cap_cyb_existing_insured-no")

        # cap policy number:
        self.external_policy_number = self.driver.find_element(By.ID, "external_policy_number")

        # Date operations commenced under current ownership
        self.operation_commence_date = self.driver.find_element(By.ID, "operation-commence-date")

        # Description of operations
        self.operations_description = self.driver.find_element(By.ID, "operation-nature")

        # Annual Gross Revenues

        self.annual_revenue_current_year = self.driver.find_element(By.ID, "annual_revenue_current_year")

        # Current Year Annual Projection

        self.annual_revenue_one_year_ago = self.driver.find_element(By.ID, "annual_revenue_one_year_ago")

        # Do You own any subsidiaries?

        self.subsidiary_inclusion_yes = self.driver.find_element(By.ID, "subsidiary_inclusion-yes")

        self.subsidiary_inclusion_no = self.driver.find_element(By.ID, "subsidiary_inclusion-no")

        # Is coverage requested for any entity or organization other than the Applicant and its Subsidiaries?

        self.coverage_for_other_entity_yes = self.driver.find_element(By.ID, "coverage_for_other_entity-yes")

        self.coverage_for_other_entity_no = self.driver.find_element(By.ID, "coverage_for_other_entity-no")

        # Do You have a HIPAA compliance program in place?

        self.hipaa_compliance_program_yes = self.driver.find_element(By.ID, "cap_cyb_investigated_hipaa-yes")

        self.hipaa_compliance_program_no = self.driver.find_element(By.ID, "cap_cyb_investigated_hipaa-no")

        # Do You use anti-virus software and firewall protection on all desktops, portable devices and mission critical servers?

        self.platform_security_yes = self.driver.find_element(By.ID, "cap_cyb_platform_security-yes")

        self.platform_security_no = self.driver.find_element(By.ID, "cap_cyb_platform_security-no")

        # Do You enforce privacy and security policies, including mandatory employee training, that must be followed by all employees, contractors, or other individuals or organizations with access to patient information?

        self.patient_information_yes = self.driver.find_element(By.ID, "cap_cyb_patient_information-yes")

        self.patient_information_no = self.driver.find_element(By.ID, "cap_cyb_patient_information-no")

        # Does Your organization store personal and/or confidential data on portable devices, including laptops, cell phones, PDAs, back-up tapes, USB thumb drives and external hard drives?

        self.data_security_yes = self.driver.find_element(By.ID, "cap_cyb_data_security-yes")

        self.data_security_no = self.driver.find_element(By.ID, "cap_cyb_data_security-no")

        # DISPLAYS IF YES TO ABOVE QUESTION

        # Is such data encrypted to industry standards?

        self.data_security_encrypted_yes = self.driver.find_element(By.ID, "cap_cyb_data_security_encrypted-yes")

        self.data_security_encrypted_no = self.driver.find_element(By.ID, "cap_cyb_data_security_encrypted-no")

        # Does Your organization process, store, transmit or handle credit or debit card data?

        self.credit_card_data_yes = self.driver.find_element(By.ID, "cap_cyb_credit_card_data-yes")

        self.credit_card_data_no = self.driver.find_element(By.ID, "cap_cyb_credit_card_data-no")

        # DISPLAYS IF YES TO ABOVE QUESTION

        # Are Your data security controls compliant with the Payment Card Industry Data Security Standard (PCI DSS)?

        self.credit_card_data_compliant_yes = self.driver.find_element(By.ID, "cap_cyb_credit_card_data_compliant-yes")

        self.credit_card_data_compliant_no = self.driver.find_element(By.ID, "cap_cyb_credit_card_data_compliant-no")

        # Do Your wire transfer protocols prohibit one employee from controlling a transaction from beginning to end?

        #self.wire_transfer_protocols_yes = self.driver.find_element(By.ID, "cap_cyb_wire_transfer_protocols-yes")

        #self.wire_transfer_protocols_no = self.driver.find_element(By.ID, "cap_cyb_wire_transfer_protocols-no")

        # Does the number of records You store, either electronic or paper, exceed 20,000 records per physician?

        self.records_exceed_20000_yes = self.driver.find_element(By.ID, "cap_cyb_records_exceed_20000-yes")

        self.records_exceed_20000_no = self.driver.find_element(By.ID, "cap_cyb_records_exceed_20000-no")

        # total number of records

        self.records_exceed_20000_total = self.driver.find_element(By.ID, "cap_cyb_records_exceed_20000_total")

        # Has the Applicant or any other organization proposed for this insurance experienced a wire transfer loss in the last five years?

        #self.wire_transfer_loss_yes = self.driver.find_element(By.ID, "cap_cyb_wire_transfer_loss-yes")

        #self.wire_transfer_loss_no = self.driver.find_element(By.ID, "cap_cyb_wire_transfer_loss-no")

        # Have You or any physician in Your group received any complaints or claims or been the subject in litigation involving matters of privacy injury, identity theft, denial of service attacks, computer virus infections, theft of information, damage to third-party networks or Your customer's ability to rely on Your network?

        self.cyber_complaints_litigation_yes = self.driver.find_element(By.ID, "cap_cyb_cyber_complaints_litigation-yes")

        self.cyber_complaints_litigation_no = self.driver.find_element(By.ID, "cap_cyb_cyber_complaints_litigation-no")

        # Are You or any physician in Your group aware of any security breaches, privacy-related events or incidents, or allegations of breach of privacy?

        self.aware_compromised_security_yes = self.driver.find_element(By.ID, "cap_cyb_aware_compromised_security-yes")

        self.aware_compromised_security_no = self.driver.find_element(By.ID, "cap_cyb_aware_compromised_security-no")

        # Have You ever been non-renewed, placed on extension, or declined for similar privacy/security liability coverage?

        self.non_renewed_extention_cyb_yes = self.driver.find_element(By.ID, "cap_cyb_non_renewed_extention_cyb-yes")

        self.non_renewed_extention_cyb_no = self.driver.find_element(By.ID, "cap_cyb_non_renewed_extention_cyb-no")

        return self

    def create_quote_PCI_DSS_No_DQ(self, revenue):

        PAF.Page_Elements(self).existing_insured_yes.click()
        PAF.Page_Elements(self).external_policy_number.send_keys("A111111111")
        PAF.Page_Elements(self).operation_commence_date.send_keys("01-01-2001")
        PAF.Page_Elements(self).operations_description.send_keys("QA TEST")
        PAF.Page_Elements(self).annual_revenue_current_year.send_keys(revenue)
        PAF.Page_Elements(self).annual_revenue_one_year_ago.send_keys(revenue)
        PAF.Page_Elements(self).subsidiary_inclusion_no.click()
        PAF.Page_Elements(self).coverage_for_other_entity_no.click()

        # Cyber Liability Questions
        PAF.Page_Elements(self).hipaa_compliance_program_yes.click()
        PAF.Page_Elements(self).platform_security_yes.click()
        PAF.Page_Elements(self).patient_information_yes.click()
        PAF.Page_Elements(self).data_security_yes.click()
        PAF.Page_Elements(self).data_security_encrypted_yes.click()
        PAF.Page_Elements(self).credit_card_data_yes.click()
        PAF.Page_Elements(self).credit_card_data_compliant_yes.click()
        #PAF.Page_Elements(self).wire_transfer_protocols_yes.click()
        PAF.Page_Elements(self).records_exceed_20000_no.click()
        #PAF.Page_Elements(self).wire_transfer_loss_no.click()
        PAF.Page_Elements(self).cyber_complaints_litigation_no.click()
        PAF.Page_Elements(self).aware_compromised_security_no.click()
        PAF.Page_Elements(self).non_renewed_extention_cyb_no.click()

    def create_quote_No_PCI_DSS_No_DQ(self, revenue):

        PAF.Page_Elements(self).existing_insured_yes.click()
        PAF.Page_Elements(self).external_policy_number.send_keys("A111111111")
        PAF.Page_Elements(self).operation_commence_date.send_keys("01-01-2001")
        PAF.Page_Elements(self).operations_description.send_keys("QA TEST")
        PAF.Page_Elements(self).annual_revenue_current_year.send_keys(revenue)
        PAF.Page_Elements(self).annual_revenue_one_year_ago.send_keys(revenue)
        PAF.Page_Elements(self).subsidiary_inclusion_no.click()
        PAF.Page_Elements(self).coverage_for_other_entity_no.click()

        # Cyber Liability Questions
        PAF.Page_Elements(self).hipaa_compliance_program_yes.click()
        PAF.Page_Elements(self).platform_security_yes.click()
        PAF.Page_Elements(self).patient_information_yes.click()
        PAF.Page_Elements(self).data_security_yes.click()
        PAF.Page_Elements(self).data_security_encrypted_yes.click()
        PAF.Page_Elements(self).credit_card_data_no.click()
        #PAF.Page_Elements(self).credit_card_data_compliant_yes.click()
        #PAF.Page_Elements(self).wire_transfer_protocols_yes.click()
        PAF.Page_Elements(self).records_exceed_20000_no.click()
        #PAF.Page_Elements(self).wire_transfer_loss_no.click()
        PAF.Page_Elements(self).cyber_complaints_litigation_no.click()
        PAF.Page_Elements(self).aware_compromised_security_no.click()
        PAF.Page_Elements(self).non_renewed_extention_cyb_no.click()

    #TODO
    # Ask Dev to create ID for next button
    def click_next(self):
        next_button = self.driver.find_element(By.XPATH, "//form[@id='rate-adjustment-form']/div[5]/a/span[2]/span/span")
        next_button.click()