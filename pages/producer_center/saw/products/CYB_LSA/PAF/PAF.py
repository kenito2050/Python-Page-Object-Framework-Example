from selenium.webdriver.common.by import By

from selenium.webdriver.common.by import By

class PAF():

    def __init__(self, driver):
        self.driver = driver

    #Page Elements

    def Page_Elements(self):

        # Current or prospective insured?
        self.existing_insured_yes = self.driver.find_element(By.ID, "cyb_lsa_existing_insured-yes")

        self.existing_insured_no = self.driver.find_element(By.ID, "cyb_lsa_existing_insured-no")

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

        # MEDEFENSE™ Plus Questions

        # Are You utilizing a current edition of the CPT manual to ensure billing compliance?

        self.utilize_cpt_manual_yes = self.driver.find_element(By.ID, "cyb_lsa_utilize_cpt_manual-yes")

        self.utilize_cpt_manual_no = self.driver.find_element(By.ID, "cyb_lsa_utilize_cpt_manual-no")

        # Do Your billings from federal and state health care programs, such as Medicare and Medicaid, exceed an average of $2,000,000 per physician in Your group?

        self.billings_exceed_two_million_yes = self.driver.find_element(By.ID, "cyb_lsa_billings_exceed_one_million-yes")

        self.billings_exceed_two_million_no = self.driver.find_element(By.ID, "cyb_lsa_billings_exceed_one_million-no")

        # Have You or any physician in Your group ever been audited or investigated, or received a request for records or other documentation by or on behalf of a commercial payer or government entity?

        self.audited_investigated_yes = self.driver.find_element(By.ID, "cyb_lsa_audited_investigated-yes")

        self.audited_investigated_no = self.driver.find_element(By.ID, "cyb_lsa_audited_investigated-no")

        # Have You or any physician in Your group ever been placed on pre-payment review with regard to Medicare/Medicaid billing practices or utilization of Medicare/Medicaid services?

        self.audited_investigated_medicare_yes = self.driver.find_element(By.ID, "cyb_lsa_audited_investigated_medicare-yes")

        self.audited_investigated_medicare_no = self.driver.find_element(By.ID, "cyb_lsa_audited_investigated_medicare-no")

        # Have You or any physician in Your group ever had to refund amounts to Public and/or Private payers in excess of $10,000?

        self.refund_excess_10_thousand_yes = self.driver.find_element(By.ID, "cyb_lsa_refund_excess_10_thousand-yes")

        self.refund_excess_10_thousand_no = self.driver.find_element(By.ID, "cyb_lsa_refund_excess_10_thousand-no")

        # Have You or any physician in Your group ever been accused of billing errors by any government agency or commercial payer?

        self.accused_billing_errors_yes = self.driver.find_element(By.ID, "cyb_lsa_accused_billing_errors-yes")

        self.accused_billing_errors_no = self.driver.find_element(By.ID, "cyb_lsa_accused_billing_errors-no")

        # Have You or any physician in Your Group ever:

        # Been investigated or sanctioned by a state medical licensing board?

        self.investigated_sanctioned_yes = self.driver.find_element(By.ID, "cyb_lsa_investigated_sanctioned-yes")

        self.investigated_sanctioned_no = self.driver.find_element(By.ID, "cyb_lsa_investigated_sanctioned-no")

        # Been involved in Stark/anti-kickback investigation?

        self.anti_kickback_investigation_yes = self.driver.find_element(By.ID, "cyb_lsa_anti_kickback_investigation-yes")

        self.anti_kickback_investigation_no = self.driver.find_element(By.ID, "cyb_lsa_anti_kickback_investigation-no")

        # Been sued or deselected from a private commercial payer?

        self.sued_deselected_payer_yes = self.driver.find_element(By.ID, "cyb_lsa_sued_deselected_payer-yes")

        self.sued_deselected_payer_no = self.driver.find_element(By.ID, "cyb_lsa_sued_deselected_payer-no")

        # Been investigated for EMTALA violations?

        self.investigated_emtala_yes = self.driver.find_element(By.ID, "cyb_lsa_investigated_emtala-yes")

        self.investigated_emtala_no = self.driver.find_element(By.ID, "cyb_lsa_investigated_emtala-no")

        # Been investigated for HIPAA violations?

        self.investigated_hipaa_yes = self.driver.find_element(By.ID, "cyb_lsa_investigated_hipaa-yes")

        self.investigated_hipaa_no = self.driver.find_element(By.ID, "cyb_lsa_investigated_hipaa-no")

        # Voluntarily disclosed any billing errors or irregular billing practices?

        self.voluntary_disclosure_yes = self.driver.find_element(By.ID, "cyb_lsa_voluntary_disclosure-yes")

        self.voluntary_disclosure_no = self.driver.find_element(By.ID, "cyb_lsa_voluntary_disclosure-no")

        # Have You ever been non-renewed, placed on extension, or declined from similar regulatory/billing errors insurance?

        self.non_renewed_extention_yes = self.driver.find_element(By.ID, "cyb_lsa_non_renewed_extention-yes")

        self.non_renewed_extention_no = self.driver.find_element(By.ID, "cyb_lsa_non_renewed_extention-no")

        # Are You or any individual proposed for this insurance been aware of any acts, errors, omissions, facts, circumstances, allegations, situations, events or incidents, that could give rise to a regulatory investigation, regulatory action, or demand for restitution?

        self.regulatory_investigation_yes = self.driver.find_element(By.ID, "cyb_lsa_regulatory_investigation-yes")

        self.regulatory_investigation_no = self.driver.find_element(By.ID, "cyb_lsa_regulatory_investigation-no")

        # Include Cyber Liability coverage

        self.include_cyber = self.driver.find_element(By.NAME, "cyb_lsa_include_cyber")

        # Cyber Liability Questions

        # Do You have a HIPAA compliance program in place?

        self.hipaa_compliance_program_yes = self.driver.find_element(By.ID, "cyb_lsa_hipaa_compliance_program-yes")

        self.hipaa_compliance_program_no = self.driver.find_element(By.ID, "cyb_lsa_hipaa_compliance_program-no")

        # Do You use anti-virus software and firewall protection on all desktops, portable devices and mission critical servers?

        self.platform_security_yes = self.driver.find_element(By.ID, "cyb_lsa_platform_security-yes")

        self.platform_security_no = self.driver.find_element(By.ID, "cyb_lsa_platform_security-no")

        # Do You enforce privacy and security policies, including mandatory employee training, that must be followed by all employees, contractors, or other individuals or organizations with access to patient information?

        self.patient_information_yes = self.driver.find_element(By.ID, "cyb_lsa_patient_information-yes")

        self.patient_information_no = self.driver.find_element(By.ID, "cyb_lsa_patient_information-no")

        # Does Your organization store personal and/or confidential data on portable devices, including laptops, cell phones, PDAs, back-up tapes, USB thumb drives and external hard drives?

        self.data_security_yes = self.driver.find_element(By.ID, "cyb_lsa_data_security-yes")

        self.data_security_no = self.driver.find_element(By.ID, "cyb_lsa_data_security-no")

        # DISPLAYS IF YES TO ABOVE QUESTION

        # Is such data encrypted to industry standards?

        self.data_security_encrypted_yes = self.driver.find_element(By.ID, "cyb_lsa_data_security_encrypted-yes")

        self.data_security_encrypted_no = self.driver.find_element(By.ID, "cyb_lsa_data_security_encrypted-no")

        # Does Your organization process, store, transmit or handle credit or debit card data?

        self.credit_card_data_yes = self.driver.find_element(By.ID, "cyb_lsa_credit_card_data-yes")

        self.credit_card_data_no = self.driver.find_element(By.ID, "cyb_lsa_credit_card_data-no")

        # DISPLAYS IF YES TO ABOVE QUESTION

        # Are Your data security controls compliant with the Payment Card Industry Data Security Standard (PCI DSS)?

        self.credit_card_data_compliant_yes = self.driver.find_element(By.ID, "cyb_lsa_credit_card_data_compliant-yes")

        self.credit_card_data_compliant_no = self.driver.find_element(By.ID, "cyb_lsa_credit_card_data_compliant-no")

        # Do Your wire transfer protocols prohibit one employee from controlling a transaction from beginning to end?

        self.wire_transfer_protocols_yes = self.driver.find_element(By.ID, "cyb_lsa_wire_transfer_protocols-yes")

        self.wire_transfer_protocols_no = self.driver.find_element(By.ID, "cyb_lsa_wire_transfer_protocols-no")

        # Does the number of records You store, either electronic or paper, exceed 20,000 records per physician?

        self.records_exceed_20000_yes = self.driver.find_element(By.ID, "cyb_lsa_records_exceed_20000-yes")

        self.records_exceed_20000_no = self.driver.find_element(By.ID, "cyb_lsa_records_exceed_20000-no")

        # total number of records

        self.records_exceed_20000_total = self.driver.find_element(By.ID, "cyb_lsa_records_exceed_20000_total")

        # Has the Applicant or any other organization proposed for this insurance experienced a wire transfer loss in the last five years?

        self.wire_transfer_loss_yes = self.driver.find_element(By.ID, "cyb_lsa_wire_transfer_loss-yes")

        self.wire_transfer_loss_no = self.driver.find_element(By.ID, "cyb_lsa_wire_transfer_loss-no")

        # Have You or any physician in Your group received any complaints or claims or been the subject in litigation involving matters of privacy injury, identity theft, denial of service attacks, computer virus infections, theft of information, damage to third-party networks or Your customer's ability to rely on Your network?

        self.cyber_complaints_litigation_yes = self.driver.find_element(By.ID, "cyb_lsa_cyber_complaints_litigation-yes")

        self.cyber_complaints_litigation_no = self.driver.find_element(By.ID, "cyb_lsa_cyber_complaints_litigation-no")

        # Are You or any physician in Your group aware of any security breaches, privacy-related events or incidents, or allegations of breach of privacy?

        self.aware_compromised_security_yes = self.driver.find_element(By.ID, "cyb_lsa_aware_compromised_security-yes")

        self.aware_compromised_security_no = self.driver.find_element(By.ID, "cyb_lsa_aware_compromised_security-no")

        # Have You ever been non-renewed, placed on extension, or declined for similar privacy/security liability coverage?

        self.non_renewed_extention_cyb_yes = self.driver.find_element(By.ID, "cyb_lsa_non_renewed_extension_cyb-yes")

        self.non_renewed_extention_cyb_no = self.driver.find_element(By.ID, "cyb_lsa_non_renewed_extension_cyb-no")

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
        PAF.Page_Elements(self).utilize_cpt_manual_yes.click()
        PAF.Page_Elements(self).billings_exceed_two_million_no.click()
        PAF.Page_Elements(self).audited_investigated_no.click()
        PAF.Page_Elements(self).audited_investigated_medicare_no.click()
        PAF.Page_Elements(self).refund_excess_10_thousand_no.click()
        PAF.Page_Elements(self).accused_billing_errors_no.click()
        PAF.Page_Elements(self).investigated_sanctioned_no.click()
        PAF.Page_Elements(self).anti_kickback_investigation_no.click()
        PAF.Page_Elements(self).sued_deselected_payer_no.click()
        PAF.Page_Elements(self).investigated_emtala_no.click()
        PAF.Page_Elements(self).investigated_hipaa_no.click()
        PAF.Page_Elements(self).voluntary_disclosure_no.click()
        PAF.Page_Elements(self).non_renewed_extention_no.click()
        PAF.Page_Elements(self).regulatory_investigation_no.click()

        # Cyber Liability Questions
        PAF.Page_Elements(self).hipaa_compliance_program_yes.click()
        PAF.Page_Elements(self).platform_security_yes.click()
        PAF.Page_Elements(self).patient_information_yes.click()
        PAF.Page_Elements(self).data_security_yes.click()
        PAF.Page_Elements(self).data_security_encrypted_yes.click()
        PAF.Page_Elements(self).credit_card_data_yes.click()
        PAF.Page_Elements(self).credit_card_data_compliant_yes.click()
        PAF.Page_Elements(self).wire_transfer_protocols_yes.click()
        PAF.Page_Elements(self).records_exceed_20000_no.click()
        PAF.Page_Elements(self).wire_transfer_loss_no.click()
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
        PAF.Page_Elements(self).utilize_cpt_manual_yes.click()
        PAF.Page_Elements(self).billings_exceed_two_million_no.click()
        PAF.Page_Elements(self).audited_investigated_no.click()
        PAF.Page_Elements(self).audited_investigated_medicare_no.click()
        PAF.Page_Elements(self).refund_excess_10_thousand_no.click()
        PAF.Page_Elements(self).accused_billing_errors_no.click()
        PAF.Page_Elements(self).investigated_sanctioned_no.click()
        PAF.Page_Elements(self).anti_kickback_investigation_no.click()
        PAF.Page_Elements(self).sued_deselected_payer_no.click()
        PAF.Page_Elements(self).investigated_emtala_no.click()
        PAF.Page_Elements(self).investigated_hipaa_no.click()
        PAF.Page_Elements(self).voluntary_disclosure_no.click()
        PAF.Page_Elements(self).non_renewed_extention_no.click()
        PAF.Page_Elements(self).regulatory_investigation_no.click()

        # Cyber Liability Questions
        PAF.Page_Elements(self).hipaa_compliance_program_yes.click()
        PAF.Page_Elements(self).platform_security_yes.click()
        PAF.Page_Elements(self).patient_information_yes.click()
        PAF.Page_Elements(self).data_security_yes.click()
        PAF.Page_Elements(self).data_security_encrypted_yes.click()
        PAF.Page_Elements(self).credit_card_data_no.click()
        #PAF.Page_Elements(self).credit_card_data_compliant_yes.click()
        PAF.Page_Elements(self).wire_transfer_protocols_yes.click()
        PAF.Page_Elements(self).records_exceed_20000_no.click()
        PAF.Page_Elements(self).wire_transfer_loss_no.click()
        PAF.Page_Elements(self).cyber_complaints_litigation_no.click()
        PAF.Page_Elements(self).aware_compromised_security_no.click()
        PAF.Page_Elements(self).non_renewed_extention_cyb_no.click()

    #TODO
    # Ask Dev to create ID for next button
    def click_next(self):
        next_button = self.driver.find_element(By.XPATH, "//form[@id='rate-adjustment-form']/div[2]/div[4]/a/span[2]/span/span")
        next_button.click()