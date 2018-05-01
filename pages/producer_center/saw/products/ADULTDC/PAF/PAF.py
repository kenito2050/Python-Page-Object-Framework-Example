from selenium.webdriver.common.by import By

class PAF():

    def __init__(self, driver):
        self.driver = driver

    #Page Elements

    def Page_Elements(self):

        # Number of Years in Business
        self.years_in_business = self.driver.find_element(By.ID, "years-in-business")

        # Total Staff Count
        self.total_staff_count = self.driver.find_element(By.ID, "staff_count")

        # Maximum Number of Licensed Participants Allowed:
        self.participants_count = self.driver.find_element(By.ID, "adc_participants_count")

        # Is the Applicant licensed to provide services as an Adult Daycare?
        self.licensed_yes = self.driver.find_element(By.ID, "adc_licensed-yes")

        self.licensed_no = self.driver.find_element(By.ID, "adc_licensed-no")

        # Does the Applicant maintain a staff to client ratio of at least 1 to 8?
        self.staff_to_client_ratio_yes = self.driver.find_element(By.ID, "staff_to_client_ratio-yes")

        self.staff_to_client_ratio_no = self.driver.find_element(By.ID, "staff_to_client_ratio-no")

        # Does the Applicant ensure at least one staff member on duty is trained in first aid/CPR?
        self.trained_in_CPR_yes = self.driver.find_element(By.ID, "adc_trained_in_CPR-yes")

        self.trained_in_CPR_no = self.driver.find_element(By.ID, "adc_trained_in_CPR-no")

        # If administered, does the Applicant keep medications in a locked area?
        self.applicant_medications_yes = self.driver.find_element(By.ID, "adc_applicant_medications-yes")

        self.applicant_medications_no = self.driver.find_element(By.ID, "adc_applicant_medications-no")

        # Does the Applicant have protocols in place to prevent residents from leaving the facility unattended?
        self.applicant_protocols_yes = self.driver.find_element(By.ID, "adc_applicant_protocols-yes")

        self.applicant_protocols_no = self.driver.find_element(By.ID, "adc_applicant_protocols-no")

        # Does the Applicant have written procedures in the event of a medical emergency?
        self.written_procedures_yes = self.driver.find_element(By.ID, "adc_written_procedures-yes")

        self.written_procedures_no = self.driver.find_element(By.ID, "adc_written_procedures-no")

        # Does the Applicant have incident reporting procedures?
        self.reporting_procedures_yes = self.driver.find_element(By.ID, "adc_reporting_procedures-yes")

        self.reporting_procedures_no = self.driver.find_element(By.ID, "adc_reporting_procedures-no")

        # Does the Applicant want coverage for any physician/psychiatrist?
        self.coverage_yes = self.driver.find_element(By.ID, "adc_coverage-yes")

        self.coverage_no = self.driver.find_element(By.ID, "adc_coverage-no")

        # Does the Applicant provide services to minors?
        self.minor_services_yes = self.driver.find_element(By.ID, "adc_minor_services-yes")

        self.minor_services_no = self.driver.find_element(By.ID, "adc_minor_services-no")

        # Does the Applicant provide services to individuals who are a danger to themselvesor others?
        self.individual_services_yes = self.driver.find_element(By.ID, "adc_individual_services-yes")

        self.individual_services_no = self.driver.find_element(By.ID, "adc_individual_services-no")

        # Does the Applicant provide off-premises field trips?
        self.applicant_trips_yes = self.driver.find_element(By.ID, "adc_applicant_trips-yes")

        self.applicant_trips_no = self.driver.find_element(By.ID, "adc_applicant_trips-no")

        # Has the Applicant or any of its providers/employees ever been/had:

        # a) The subject in disciplinary or investigative proceedings or reprimanded by a governmental or administrative agency, hospital or professional association?
        self.subjects_yes = self.driver.find_element(By.ID, "adc_subjects-yes")

        self.subjects_no = self.driver.find_element(By.ID, "adc_subjects-no")

        # b) Convicted of an act committed in violation of any law or ordinance other than traffic offenses?
        self.act_committed_yes = self.driver.find_element(By.ID, "adc_act_committed-yes")

        self.act_committed_no = self.driver.find_element(By.ID, "adc_act_committed-no")

        # c) Any state professional license or license to prescribe or dispense narcotics refused, suspended, revoked, renewal refused or accepted only on special terms, or ever voluntarily surrendered?
        self.license_yes = self.driver.find_element(By.ID, "adc_license-yes")

        self.license_no = self.driver.find_element(By.ID, "adc_license-no")

        # Has any Application for Professional Liability Insurance made on behalf of the Applicant, any predecessors in business or present Partners EVER been declined or has similar insurance ever been cancelled or non-renewed?
        self.similar_insurance_yes = self.driver.find_element(By.ID, "adc_similar_insurance-yes")

        self.similar_insurance_no = self.driver.find_element(By.ID, "adc_similar_insurance-no")

        # Has any claim EVER been made against the Applicant or any of its employees?
        self.applicant_claim_yes = self.driver.find_element(By.ID, "adc_applicant_claim-yes")

        self.applicant_claim_no = self.driver.find_element(By.ID, "adc_applicant_claim-no")

        # Is the Applicant aware of ANY circumstances which may result in ANY claim against it, its predecessors in business, or any of its past or present directors, officers, or partners?
        self.aware_partners_yes = self.driver.find_element(By.ID, "adc_aware_partners-yes")

        self.aware_partners_no = self.driver.find_element(By.ID, "adc_aware_partners-no")

        # a) Does the Applicant have expiring coverage in place? (If retroactive coverage is desired, pleasesubmit expiring declaration page and three years of loss run).

        self.expiring_coverage_yes = self.driver.find_element(By.ID, "adc_expiring_coverage-yes")

        self.expiring_coverage_no = self.driver.find_element(By.ID, "adc_expiring_coverage-no")

        # b) If the expiring policy is claims-made, what is the retroactive date ?:
        self.edate_retroactive = self.driver.find_element(By.ID, "date_retroactive")

        # a) Is the Applicant interested in Hired and Non-Owned Auto Liability coverage?
        self.hnoa_yes = self.driver.find_element(By.ID, "adc_hnoa-yes")

        self.hnoa_no = self.driver.find_element(By.ID, "adc_hnoa-no")

        # b) If “Yes” to the above, does the Applicant warrant that all providers/employees with driving responsibilities maintain automobile insurance that meets the minimum state requirements, AND does the Applicant access and review Motor Vehicle Reports on all such individuals as a condition of employment?
        self.applicant_warrant_yes = self.driver.find_element(By.ID, "adc_applicant_warrant-yes")

        self.applicant_warrant_no = self.driver.find_element(By.ID, "adc_applicant_warrant-no")

        return self

    def create_quote_include_HNOA(self, years_in_business, staff_count, number_daily_participants):
        PAF.Page_Elements(self).years_in_business.send_keys(years_in_business)
        PAF.Page_Elements(self).total_staff_count.send_keys(staff_count)
        PAF.Page_Elements(self).participants_count.send_keys(number_daily_participants)
        PAF.Page_Elements(self).licensed_yes.click()
        PAF.Page_Elements(self).staff_to_client_ratio_yes.click()
        PAF.Page_Elements(self).trained_in_CPR_yes.click()
        PAF.Page_Elements(self).applicant_medications_yes.click()
        PAF.Page_Elements(self).applicant_protocols_yes.click()
        PAF.Page_Elements(self).written_procedures_yes.click()
        PAF.Page_Elements(self).reporting_procedures_yes.click()
        PAF.Page_Elements(self).coverage_no.click()
        PAF.Page_Elements(self).minor_services_no.click()
        PAF.Page_Elements(self).individual_services_no.click()
        PAF.Page_Elements(self).applicant_trips_no.click()
        PAF.Page_Elements(self).subjects_no.click()
        PAF.Page_Elements(self).act_committed_no.click()
        PAF.Page_Elements(self).license_no.click()
        PAF.Page_Elements(self).similar_insurance_no.click()
        PAF.Page_Elements(self).applicant_claim_no.click()
        PAF.Page_Elements(self).aware_partners_no.click()
        PAF.Page_Elements(self).expiring_coverage_no.click()
        PAF.Page_Elements(self).hnoa_yes.click()
        PAF.Page_Elements(self).applicant_warrant_yes.click()

    def create_quote_NO_HNOA(self, years_in_business, staff_count, number_daily_participants):
        PAF.Page_Elements(self).years_in_business.send_keys(years_in_business)
        PAF.Page_Elements(self).total_staff_count.send_keys(staff_count)
        PAF.Page_Elements(self).participants_count.send_keys(number_daily_participants)
        PAF.Page_Elements(self).licensed_yes.click()
        PAF.Page_Elements(self).staff_to_client_ratio_yes.click()
        PAF.Page_Elements(self).trained_in_CPR_yes.click()
        PAF.Page_Elements(self).applicant_medications_yes.click()
        PAF.Page_Elements(self).applicant_protocols_yes.click()
        PAF.Page_Elements(self).written_procedures_yes.click()
        PAF.Page_Elements(self).reporting_procedures_yes.click()
        PAF.Page_Elements(self).coverage_no.click()
        PAF.Page_Elements(self).minor_services_no.click()
        PAF.Page_Elements(self).individual_services_no.click()
        PAF.Page_Elements(self).applicant_trips_no.click()
        PAF.Page_Elements(self).subjects_no.click()
        PAF.Page_Elements(self).act_committed_no.click()
        PAF.Page_Elements(self).license_no.click()
        PAF.Page_Elements(self).similar_insurance_no.click()
        PAF.Page_Elements(self).applicant_claim_no.click()
        PAF.Page_Elements(self).aware_partners_no.click()
        PAF.Page_Elements(self).expiring_coverage_no.click()
        PAF.Page_Elements(self).hnoa_no.click()

    #TODO
    # Ask Dev to create ID for next button
    def click_next(self):
        next_button = self.driver.find_element(By.XPATH, "//form[@id='primary']/div[5]/a/span[2]/span/span")
        next_button.click()