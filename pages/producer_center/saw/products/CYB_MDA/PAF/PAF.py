from selenium.webdriver.common.by import By

class PAF():

    def __init__(self, driver):
        self.driver = driver

    #Page Elements

    def Page_Elements(self):

        # Are you insured by MDAdvantage for Professional Liability Coverage?
        self.existing_insured_yes = self.driver.find_element(By.ID, "cyb-mda-existing-insured-yes")

        self.existing_insured_no = self.driver.find_element(By.ID, "cyb-mda-existing-insured-no")

        # Policy Number
        self.external_policy_number = self.driver.find_element(By.ID, "external_policy_number")

        # Broker Name
        self.referring_broker = self.driver.find_element(By.ID, "referring-broker")

        # Organization Legal Structure

        # Corporation
        self.corporation = self.driver.find_element(By.ID, "legal-structure-corporation")

        # Partnership
        self.partnership = self.driver.find_element(By.ID, "legal-structure-partnership")

        # LLC
        self.llc = self.driver.find_element(By.ID, "legal-structure-llc")

        # Other
        self.other = self.driver.find_element(By.ID, "legal-structure-oth")

        # Other (Text Field)
        self.other_text_field = self.driver.find_element(By.ID, "legal-structure-other")

        # Number of Physicians to be covered under policy:?
        self.physician_count = self.driver.find_element(By.ID, "physician-count")

        # Do you own any subsidiaries?
        self.subsidiary_inclusion_yes = self.driver.find_element(By.ID, "subsidiary_inclusion-yes")

        self.subsidiary_inclusion_no = self.driver.find_element(By.ID, "subsidiary_inclusion-no")

        # Description of operations:
        self.operation_nature = self.driver.find_element(By.ID, "operation-nature")

        # Date operations commenced under current ownership:
        self.operation_commence_date = self.driver.find_element(By.ID, "operation-commence-date")

        # Have you acquired any practices in the last 5 years?
        self.acquired_practices_5y_yes = self.driver.find_element(By.ID, "cyb_mda_acqired_practices_5y-yes")

        self.acquired_practices_5y_no = self.driver.find_element(By.ID, "cyb_mda_acqired_practices_5y-no")

        # Do you handle billings for any hospitals or provider services not provided by your medical group?
        self.handle_billings_yes = self.driver.find_element(By.ID, "cyb_mda_handle_billings-yes")

        self.handle_billings_no = self.driver.find_element(By.ID, "cyb_mda_handle_billings-no")

        # Has the entity or any physician in your medical group ever been audited, investigated, sanctioned or placed on prepayment review by any local, state or federal government agency or any private or commercial payer regarding the delivery of healthcare services or reimbursement thereof?
        self.past_investigation_government_yes = self.driver.find_element(By.ID, "cyb_mda_past_investigation_government-yes")

        self.past_investigation_government_no = self.driver.find_element(By.ID, "cyb_mda_past_investigation_government-no")

        # Does your medical group's billings from federal and state health care programs, such as Medicare and Medicaid, exceed an average of $1,000,000 per each physician in your group?
        self.per_physician_over_1m_yes = self.driver.find_element(By.ID, "cyb_mda_per_physician_over_1m-yes")

        self.per_physician_over_1m_no = self.driver.find_element(By.ID, "cyb_mda_per_physician_over_1m-no")

        # Has the entity or any physician in your medical group ever been audited, investigated, sanctioned or placed on prepayment review by any local, state or federal government agency or any private or commercial payer regarding the delivery of healthcare services or reimbursement thereof?
        self.past_refund_yes = self.driver.find_element(By.ID, "cyb_mda_past_refund-yes")

        self.past_refund_no = self.driver.find_element(By.ID, "cyb_mda_past_refund-no")

        # Has the entity or any physician in your medical group ever been audited, investigated, or placed on prepayment review with regard to Medicare/Medicaid billing practices or utilization of Medicare/Medicaid services?
        self.past_investigation_medicare_yes = self.driver.find_element(By.ID, "cyb_mda_past_investigation_medicare-yes")

        self.past_investigation_medicare_no = self.driver.find_element(By.ID, "cyb_mda_past_investigation_medicare-no")

        # Has the entity or any physician in your medical group ever been accused of billing errors by any government agency or commercial payer?
        self.accused_billing_errors_yes = self.driver.find_element(By.ID, "cyb_mda_accused_billing_errors-yes")

        self.accused_billing_errors_no = self.driver.find_element(By.ID, "cyb_mda_accused_billing_errors-no")

        # Has the entity or any physician in your medical group paid a regulatory or administrative fine or penalty as a result of a billing error, HIPAA, EMTALA, or Stark Proceeding?
        self.past_penalty_yes = self.driver.find_element(By.ID, "cyb_mda_past_penalty-yes")

        self.past_penalty_no = self.driver.find_element(By.ID, "cyb_mda_past_penalty-no")

        # Does the Applicant have knowledge of any specific facts, circumstances, situations, events or transactions (within the past 5 years) that may result in a regulatory investigation, regulatory action, or demand for restitution?
        self.past_potential_claim_yes = self.driver.find_element(By.ID, "cyb_mda_past_potential_claim-yes")

        self.past_potential_claim_no = self.driver.find_element(By.ID, "cyb_mda_past_potential_claim-no")

        # Do the entities and/or persons who perform billing services for you comply with current standardized billing procedures?
        self.standard_billing_procedures_yes = self.driver.find_element(By.ID, "cyb_mda_standard_billing_procedures-yes")

        self.standard_billing_procedures_no = self.driver.find_element(By.ID, "cyb_mda_standard_billing_procedures-no")

        # Are you HIPAA compliant?
        self.hipaa_compliance_yes = self.driver.find_element(By.ID, "cyb_mda_hipaa_compliance-yes")

        self.hipaa_compliance_no = self.driver.find_element(By.ID, "cyb_mda_hipaa_compliance-no")

        # Does your company use anti-virus software and firewall protection on all desktops, portable devices and mission critical servers, and is this software updated in accordance with the software provider's recommendations?
        self.platform_security_yes = self.driver.find_element(By.ID, "cyb_mda_platform_security-yes")

        self.platform_security_no = self.driver.find_element(By.ID, "cyb_mda_platform_security-no")

        # If you store personal information on portable devices, including laptops, PDA's, back-up tapes, USB thumb drives and external hard drives, is such data encrypted to industry standards?
        self.data_security_yes = self.driver.find_element(By.ID, "cyb_mda_data_security-yes")

        self.data_security_no = self.driver.find_element(By.ID, "cyb_mda_data_security-no")

        # Does your company have a formal process to disable or restrict access to information systems upon termination of employees?
        self.formal_process_access_yes = self.driver.find_element(By.ID, "cyb_mda_formal_process_access-yes")

        self.formal_process_access_no = self.driver.find_element(By.ID, "cyb_mda_formal_process_access-no")

        # Does your company enforce privacy and security policies that must be followed by all employees, contractors, or other individuals or organizations with access to patient information?
        self.patient_information_yes = self.driver.find_element(By.ID, "cyb_mda_patient_information-yes")

        self.patient_information_no = self.driver.find_element(By.ID, "cyb_mda_patient_information-no")

        # Do your privacy and security policies include mandatory training for all employees?
        self.mandatory_training_yes = self.driver.find_element(By.ID, "cyb_mda_manditory_training-yes")

        self.mandatory_training_no = self.driver.find_element(By.ID, "cyb_mda_manditory_training-no")

        # In the last five (5) years, have you received any complaints, claims or been the subject of litigation involving matters of privacy injury/privacy breaches, security breaches, identity theft, denial or service attacks, computer virus infections, theft of information, damage to third party networks or your patients’ ability to rely on your network?
        self.cyber_complaints_litigation_yes = self.driver.find_element(By.ID, "cyb_mda_cyber_complaints_litigation-yes")

        self.cyber_complaints_litigation_no = self.driver.find_element(By.ID, "cyb_mda_cyber_complaints_litigation-no")

        # Have you applied for similar coverage with any insurance company, including MDAdvantage, in the past 5 years?
        self.nonrenew_decline_history_yes = self.driver.find_element(By.ID, "cyb_mda_nonrenew_decline_history-yes")

        self.nonrenew_decline_history_no = self.driver.find_element(By.ID, "cyb_mda_nonrenew_decline_history-no")

        # Have you had similar coverage in force in the past 5 years that was canceled or non-renewed, or voluntarily discontinued?
        self.nonrenew_decline_history_5yr_yes = self.driver.find_element(By.ID, "cyb_mda_nonrenew_decline_history_5yr-yes")

        self.nonrenew_decline_history_5yr_no = self.driver.find_element(By.ID, "cyb_mda_nonrenew_decline_history_5yr-no")

        return self

    def create_quote_No_DQ_corporation(self, broker, staff_count):
        PAF.Page_Elements(self).existing_insured_yes.click()
        PAF.Page_Elements(self).external_policy_number.send_keys("A11111111")
        PAF.Page_Elements(self).referring_broker.click()
        PAF.Page_Elements(self).referring_broker.send_keys(broker)
        PAF.Page_Elements(self).corporation.click()
        PAF.Page_Elements(self).physician_count.send_keys(staff_count)
        PAF.Page_Elements(self).subsidiary_inclusion_no.click()
        PAF.Page_Elements(self).operation_nature.send_keys("QA Test")
        PAF.Page_Elements(self).operation_commence_date.send_keys("01/01/2001")
        PAF.Page_Elements(self).acquired_practices_5y_no.click()
        PAF.Page_Elements(self).handle_billings_no.click()
        PAF.Page_Elements(self).past_investigation_government_no.click()
        PAF.Page_Elements(self).per_physician_over_1m_no.click()
        PAF.Page_Elements(self).past_refund_no.click()
        PAF.Page_Elements(self).past_investigation_medicare_no.click()
        PAF.Page_Elements(self).accused_billing_errors_no.click()
        PAF.Page_Elements(self).past_penalty_no.click()
        PAF.Page_Elements(self).past_potential_claim_no.click()
        PAF.Page_Elements(self).standard_billing_procedures_yes.click()
        PAF.Page_Elements(self).hipaa_compliance_yes.click()
        PAF.Page_Elements(self).platform_security_yes.click()
        PAF.Page_Elements(self).data_security_yes.click()
        PAF.Page_Elements(self).formal_process_access_yes.click()
        PAF.Page_Elements(self).patient_information_yes.click()
        PAF.Page_Elements(self).mandatory_training_yes.click()
        PAF.Page_Elements(self).cyber_complaints_litigation_no.click()
        PAF.Page_Elements(self).nonrenew_decline_history_no.click()
        PAF.Page_Elements(self).nonrenew_decline_history_5yr_no.click()

    def create_quote_No_DQ_Partnership(self, broker, staff_count):
        PAF.Page_Elements(self).existing_insured_yes.click()
        PAF.Page_Elements(self).external_policy_number.send_keys("A11111111")
        PAF.Page_Elements(self).referring_broker.click()
        PAF.Page_Elements(self).referring_broker.send_keys(broker)
        PAF.Page_Elements(self).partnership.click()
        PAF.Page_Elements(self).physician_count.send_keys(staff_count)
        PAF.Page_Elements(self).subsidiary_inclusion_no.click()
        PAF.Page_Elements(self).operation_nature.send_keys("QA Test")
        PAF.Page_Elements(self).operation_commence_date.send_keys("01/01/2001")
        PAF.Page_Elements(self).acquired_practices_5y_no.click()
        PAF.Page_Elements(self).handle_billings_no.click()
        PAF.Page_Elements(self).past_investigation_government_no.click()
        PAF.Page_Elements(self).per_physician_over_1m_no.click()
        PAF.Page_Elements(self).past_refund_no.click()
        PAF.Page_Elements(self).past_investigation_medicare_no.click()
        PAF.Page_Elements(self).accused_billing_errors_no.click()
        PAF.Page_Elements(self).past_penalty_no.click()
        PAF.Page_Elements(self).past_potential_claim_no.click()
        PAF.Page_Elements(self).standard_billing_procedures_yes.click()
        PAF.Page_Elements(self).hipaa_compliance_yes.click()
        PAF.Page_Elements(self).platform_security_yes.click()
        PAF.Page_Elements(self).data_security_yes.click()
        PAF.Page_Elements(self).formal_process_access_yes.click()
        PAF.Page_Elements(self).patient_information_yes.click()
        PAF.Page_Elements(self).mandatory_training_yes.click()
        PAF.Page_Elements(self).cyber_complaints_litigation_no.click()
        PAF.Page_Elements(self).nonrenew_decline_history_no.click()
        PAF.Page_Elements(self).nonrenew_decline_history_5yr_no.click()

    def create_quote_No_DQ_LLC(self, broker, staff_count):
        PAF.Page_Elements(self).existing_insured_yes.click()
        PAF.Page_Elements(self).external_policy_number.send_keys("A11111111")
        PAF.Page_Elements(self).referring_broker.click()
        PAF.Page_Elements(self).referring_broker.send_keys(broker)
        PAF.Page_Elements(self).llc.click()
        PAF.Page_Elements(self).physician_count.send_keys(staff_count)
        PAF.Page_Elements(self).subsidiary_inclusion_no.click()
        PAF.Page_Elements(self).operation_nature.send_keys("QA Test")
        PAF.Page_Elements(self).operation_commence_date.send_keys("01/01/2001")
        PAF.Page_Elements(self).acquired_practices_5y_no.click()
        PAF.Page_Elements(self).handle_billings_no.click()
        PAF.Page_Elements(self).past_investigation_government_no.click()
        PAF.Page_Elements(self).per_physician_over_1m_no.click()
        PAF.Page_Elements(self).past_refund_no.click()
        PAF.Page_Elements(self).past_investigation_medicare_no.click()
        PAF.Page_Elements(self).accused_billing_errors_no.click()
        PAF.Page_Elements(self).past_penalty_no.click()
        PAF.Page_Elements(self).past_potential_claim_no.click()
        PAF.Page_Elements(self).standard_billing_procedures_yes.click()
        PAF.Page_Elements(self).hipaa_compliance_yes.click()
        PAF.Page_Elements(self).platform_security_yes.click()
        PAF.Page_Elements(self).data_security_yes.click()
        PAF.Page_Elements(self).formal_process_access_yes.click()
        PAF.Page_Elements(self).patient_information_yes.click()
        PAF.Page_Elements(self).mandatory_training_yes.click()
        PAF.Page_Elements(self).cyber_complaints_litigation_no.click()
        PAF.Page_Elements(self).nonrenew_decline_history_no.click()
        PAF.Page_Elements(self).nonrenew_decline_history_5yr_no.click()

    def create_quote_No_DQ_other(self, broker, staff_count):
        PAF.Page_Elements(self).existing_insured_yes.click()
        PAF.Page_Elements(self).external_policy_number.send_keys("A11111111")
        PAF.Page_Elements(self).referring_broker.click()
        PAF.Page_Elements(self).referring_broker.send_keys(broker)
        PAF.Page_Elements(self).other.click()
        PAF.Page_Elements(self).other_text_field.send_keys("Sole Proprietorship")
        PAF.Page_Elements(self).physician_count.send_keys(staff_count)
        PAF.Page_Elements(self).subsidiary_inclusion_no.click()
        PAF.Page_Elements(self).operation_nature.send_keys("QA Test")
        PAF.Page_Elements(self).operation_commence_date.send_keys("01/01/2001")
        PAF.Page_Elements(self).acquired_practices_5y_no.click()
        PAF.Page_Elements(self).handle_billings_no.click()
        PAF.Page_Elements(self).past_investigation_government_no.click()
        PAF.Page_Elements(self).per_physician_over_1m_no.click()
        PAF.Page_Elements(self).past_refund_no.click()
        PAF.Page_Elements(self).past_investigation_medicare_no.click()
        PAF.Page_Elements(self).accused_billing_errors_no.click()
        PAF.Page_Elements(self).past_penalty_no.click()
        PAF.Page_Elements(self).past_potential_claim_no.click()
        PAF.Page_Elements(self).standard_billing_procedures_yes.click()
        PAF.Page_Elements(self).hipaa_compliance_yes.click()
        PAF.Page_Elements(self).platform_security_yes.click()
        PAF.Page_Elements(self).data_security_yes.click()
        PAF.Page_Elements(self).formal_process_access_yes.click()
        PAF.Page_Elements(self).patient_information_yes.click()
        PAF.Page_Elements(self).mandatory_training_yes.click()
        PAF.Page_Elements(self).cyber_complaints_litigation_no.click()
        PAF.Page_Elements(self).nonrenew_decline_history_no.click()
        PAF.Page_Elements(self).nonrenew_decline_history_5yr_no.click()


    #TODO
    # Ask Dev to create ID for next button
    def click_next(self):
        next_button = self.driver.find_element(By.XPATH, "//form[@id='rate-adjustment-form']/div[2]/div[2]/a/span[2]/span/span")
        next_button.click()