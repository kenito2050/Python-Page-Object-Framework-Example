from selenium.webdriver.common.by import By

class PAF():

    def __init__(self, driver):
        self.driver = driver

    #Page Elements

    def Page_Elements(self):

        # Return to Admin Link
        self.return_to_Admin = self.driver.find_element(By.LINK_TEXT, "Return to Admin Interface")

        # Current or prospective Texas Lawyers Insurance Exchange insured?
        self.exchange_insured_yes = self.driver.find_element(By.ID, "tlie_exchange_insured-yes")

        self.exchange_insured_no = self.driver.find_element(By.ID, "tlie_exchange_insured-no")

        # Texas Lawyer Insurance Exchange policy number (if available):
        self.exchange_policy_number = self.driver.find_element(By.ID, "tlie_exchange_policy_number")

        # Date operations commenced under current ownership:
        self.operation_commence_date = self.driver.find_element(By.ID, "tlie_operation_commence_date")

        # Description of operations:
        self.operation_nature = self.driver.find_element(By.ID, "tlie_operation_nature")

        # Annual Gross Revenues

        # Current Year Annual Projection
        self.annual_revenue_current_year = self.driver.find_element(By.ID, "annual_revenue_current_year")

        # Prior Year:
        self.annual_revenue_one_year_ago = self.driver.find_element(By.ID, "annual_revenue_one_year_ago")

        # Number of Attorneys:
        self.attorneys_number = self.driver.find_element(By.ID, "tlie_attorneys_number")

        # Do You own any subsidiaries?
        self.subsidiary_inclusion_yes = self.driver.find_element(By.ID, "tlie_subsidiary_inclusion-yes")

        self.subsidiary_inclusion_no = self.driver.find_element(By.ID, "tlie_subsidiary_inclusion-no")

        # Is coverage requested for any entity or organization other than the Applicant and its Subsidiaries?
        self.coverage_for_other_entity_yes = self.driver.find_element(By.ID, "tlie_coverage_subsidiaries-yes")

        self.coverage_for_other_entity_no = self.driver.find_element(By.ID, "tlie_coverage_subsidiaries-no")

        # Do You use anti-virus software and firewall protection on all desktops, portable devices and mission critical servers?
        self.desktop_protection_yes = self.driver.find_element(By.ID, "tlie_desktop_protection-yes")

        self.desktop_protection_no = self.driver.find_element(By.ID, "tlie_desktop_protection-no")

        # Do You enforce privacy and security policies, including mandatory employee training, that must be followed by all employees, contractors, or other individuals or organizations with access to patient information?
        self.security_policies_yes = self.driver.find_element(By.ID, "tlie_security_policies-yes")

        self.security_policies_no = self.driver.find_element(By.ID, "tlie_security_policies-no")

        # Does Your organization store personal and/or confidential data on portable devices, including laptops, cell phones, PDAs, back-up tapes, USB thumb drives and external hard drives?
        self.store_data_yes = self.driver.find_element(By.ID, "tlie_store_data-yes")

        self.store_data_no = self.driver.find_element(By.ID, "tlie_store_data-no")

        # If “YES”, is such data encrypted to industry standards?
        self.data_encrypted_yes = self.driver.find_element(By.ID, "tlie_data_encrypted-yes")

        self.data_encrypted_no = self.driver.find_element(By.ID, "tlie_data_encrypted-no")

        # Does Your organization process, store, transmit or handle credit or debit card data?
        self.card_process_yes = self.driver.find_element(By.ID, "tlie_card_process-yes")

        self.card_process_no = self.driver.find_element(By.ID, "tlie_card_process-no")

        # If “YES”, are Your data security controls compliant with the Payment Card Industry Data Security Standard (PCI DSS)?
        self.PCI_DSS_yes = self.driver.find_element(By.ID, "tlie_PCI_DSS-yes")

        self.PCI_DSS_no = self.driver.find_element(By.ID, "tlie_PCI_DSS-no")

        # Do Your wire transfer protocols prohibit one employee from controlling a transaction from beginning to end?
        self.transfer_protocols_yes = self.driver.find_element(By.ID, "tlie_transfer_protocols-yes")

        self.transfer_protocols_no = self.driver.find_element(By.ID, "tlie_transfer_protocols-no")

        # Does the number of records You store, either electronic or paper, exceed 50,000 records?
        self.number_of_records_yes = self.driver.find_element(By.ID, "tlie_number_of_records-yes")

        self.number_of_records_no = self.driver.find_element(By.ID, "tlie_number_of_records-no")

        # If “YES”, please provide the total number of records stored by the Applicant(s):
        self.records_exceed_50000_total = self.driver.find_element(By.ID, "tlie_records_exceed_50000_total")

        # Has the Applicant or any other organization proposed for this insurance experienced a wire transfer loss in the past five years?
        self.wire_transfer_loss_yes = self.driver.find_element(By.ID, "tlie_wire_transfer_loss-yes")

        self.wire_transfer_loss_no = self.driver.find_element(By.ID, "tlie_wire_transfer_loss-no")

        # Have You or any person or entity proposed for this insurance received any complaints or claims or been the subject in litigation involving matters of privacy injury, identity theft, denial of service attacks, computer virus infections, theft of information, damage to third-party networks or Your customer’s ability to rely on Your network?
        self.service_attacks_yes = self.driver.find_element(By.ID, "tlie_service_attacks-yes")

        self.service_attacks_no = self.driver.find_element(By.ID, "tlie_service_attacks-no")

        # Are You or any person or organization proposed for this insurance aware of any security breaches, privacy-related events or incidents, or allegations of breach of privacy?.
        self.security_breaches_yes = self.driver.find_element(By.ID, "tlie_security_breaches-yes")

        self.security_breaches_no = self.driver.find_element(By.ID, "tlie_security_breaches-no")

        # Have You or any person or organization proposed for this insurance ever been non-renewed, placed on extension, or declined for similar privacy/security liability coverage?
        self.security_liability_yes = self.driver.find_element(By.ID, "tlie_security_liability-yes")

        self.security_liability_no = self.driver.find_element(By.ID, "tlie_security_liability-no")

        return self

    def create_quote_PCI_DSS_No_DQ(self, revenue, staff_count):
        PAF.Page_Elements(self).exchange_insured_yes.click()
        PAF.Page_Elements(self).exchange_policy_number.send_keys("A1111111")
        PAF.Page_Elements(self).operation_commence_date.send_keys("01/01/2001")
        PAF.Page_Elements(self).operation_nature.send_keys("QA Test")
        PAF.Page_Elements(self).annual_revenue_one_year_ago.send_keys(revenue)
        PAF.Page_Elements(self).attorneys_number.click()
        PAF.Page_Elements(self).attorneys_number.send_keys(staff_count)
        PAF.Page_Elements(self).subsidiary_inclusion_no.click()
        PAF.Page_Elements(self).coverage_for_other_entity_no.click()
        PAF.Page_Elements(self).desktop_protection_yes.click()
        PAF.Page_Elements(self).security_policies_yes.click()
        PAF.Page_Elements(self).store_data_yes.click()
        PAF.Page_Elements(self).data_encrypted_yes.click()
        PAF.Page_Elements(self).card_process_yes.click()
        PAF.Page_Elements(self).PCI_DSS_yes.click()
        PAF.Page_Elements(self).transfer_protocols_yes.click()
        PAF.Page_Elements(self).number_of_records_no.click()
        PAF.Page_Elements(self).wire_transfer_loss_no.click()
        PAF.Page_Elements(self).service_attacks_no.click()
        PAF.Page_Elements(self).security_breaches_no.click()
        PAF.Page_Elements(self).security_liability_no.click()

    def create_quote_No_PCI_DSS_No_DQ(self, revenue, staff_count):
        PAF.Page_Elements(self).exchange_insured_yes.click()
        PAF.Page_Elements(self).exchange_policy_number.send_keys("A1111111")
        PAF.Page_Elements(self).operation_commence_date.send_keys("01/01/2001")
        PAF.Page_Elements(self).operation_nature.send_keys("QA Test")
        PAF.Page_Elements(self).annual_revenue_one_year_ago.send_keys(revenue)
        PAF.Page_Elements(self).attorneys_number.click()
        PAF.Page_Elements(self).attorneys_number.send_keys(staff_count)
        PAF.Page_Elements(self).subsidiary_inclusion_no.click()
        PAF.Page_Elements(self).coverage_for_other_entity_no.click()
        PAF.Page_Elements(self).desktop_protection_yes.click()
        PAF.Page_Elements(self).security_policies_yes.click()
        PAF.Page_Elements(self).store_data_yes.click()
        PAF.Page_Elements(self).data_encrypted_yes.click()
        PAF.Page_Elements(self).card_process_no.click()
        PAF.Page_Elements(self).transfer_protocols_yes.click()
        PAF.Page_Elements(self).number_of_records_no.click()
        PAF.Page_Elements(self).wire_transfer_loss_no.click()
        PAF.Page_Elements(self).service_attacks_no.click()
        PAF.Page_Elements(self).security_breaches_no.click()
        PAF.Page_Elements(self).security_liability_no.click()

    #TODO
    # Ask Dev to create ID for next button
    def click_next(self):
        next_button = self.driver.find_element(By.XPATH, "//*[@id='rate-adjustment-form']/div[2]/div[5]/a/span[1]")
        next_button.click()

    def click_return_to_Admin_Interface(self):
        PAF.Page_Elements(self).return_to_Admin.click()