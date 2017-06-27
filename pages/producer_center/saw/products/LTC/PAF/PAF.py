from selenium.webdriver.common.by import By

class PAF():

    def __init__(self, driver):
        self.driver = driver

    #Page Elements

    def Page_Elements(self):

        # Date established:
        self.operation_commence_date = self.driver.find_element(By.ID, "operation_commence_date")

        # Total number of occupied beds:
        self.bed_count = self.driver.find_element(By.ID, "bed_count")

        # Facility License Number:
        self.facility_license_number = self.driver.find_element(By.ID, "ltc_license_number")

        # Will a mortgagee or landlord be named as an additional insured?
        self.additional_insured_yes = self.driver.find_element(By.ID, "additional_insured-yes")

        self.additional_insured_no = self.driver.find_element(By.ID, "additional_insured-no")

        # Is the Applicant currently licensed as an Assisted Living Facility (level 4 or below), RCFE or Personal Care Home per state requirements?
        self.ltc_licensed_yes = self.driver.find_element(By.ID, "ltc_licensed-yes")

        self.ltc_licensed_no = self.driver.find_element(By.ID, "ltc_licensed-no")

        # Has the Applicant completed the most recent state survey (per state requirements), without any deficiencies or with a Plan of Correction accepted by the state?:
        self.ltc_state_mandate_survey_yes = self.driver.find_element(By.ID, "ltc_state_mandate_survey-yes")

        self.ltc_state_mandate_survey_no = self.driver.find_element(By.ID, "ltc_state_mandate_survey-no")

        # Is the facility owner or a staff member on the premises at all times?
        self.ltc_staff_client_ratio_yes = self.driver.find_element(By.ID, "ltc_staff_client_ratio-yes")

        self.ltc_staff_client_ratio_no = self.driver.find_element(By.ID, "ltc_staff_client_ratio-no")

        # Are there protocols in place to prevent residents from wandering?
        self.ltc_wandering_risk_assessment_yes = self.driver.find_element(By.ID, "ltc_wandering_risk_assessment-yes")

        self.ltc_wandering_risk_assessment_no = self.driver.find_element(By.ID, "ltc_wandering_risk_assessment-no")

        # Is a nursing assessment conducted for new patients, including evaluation of skin breakdowns, history of prior injuries including falls, assistance with ADLs, wandering risk and current medications?:

        self.ltc_nursing_assessment_yes = self.driver.find_element(By.ID, "ltc_nursing_assessment-yes")

        self.ltc_nursing_assessment_no = self.driver.find_element(By.ID, "ltc_nursing_assessment-no")

        # Does the Applicant have a system to ensure timely reassessments and identify when a resident needs to be transferred to another level of care?:

        self.ltc_reassessment_system_yes = self.driver.find_element(By.ID, "ltc_reassessment_system-yes")

        self.ltc_reassessment_system_no = self.driver.find_element(By.ID, "ltc_reassessment_system-no")

        # Has any resident(s) eloped from your facility in the last five (5) years?

        self.ltc_resident_eloped_yes = self.driver.find_element(By.ID, "ltc_resident_eloped-yes")

        self.ltc_resident_eloped_no = self.driver.find_element(By.ID, "ltc_resident_eloped-no")

        # Have there been any complaints investigated by the State in the last two (2) years?

        self.ltc_complaint_investigated_yes = self.driver.find_element(By.ID, "ltc_complaint_investigated-yes")

        self.ltc_complaint_investigated_no = self.driver.find_element(By.ID, "ltc_complaint_investigated-no")

        #Has any application for Professional Liability insurance made on behalf of the facility, ever been declined, or has the insurance ever been cancelled or renewal refused?

        self.ltc_insurance_declined_yes = self.driver.find_element(By.ID, "ltc_insurance_declined-yes")

        self.ltc_insurance_declined_no = self.driver.find_element(By.ID, "ltc_insurance_declined-no")

        # Has any license or accreditation ever been suspended, denied or revoked?

        self.ltc_license_problem_yes = self.driver.find_element(By.ID, "ltc_license_problem-yes")

        self.ltc_license_problem_no = self.driver.find_element(By.ID, "ltc_license_problem-no")

        # Has any claim ever been made against the facility or any of its employees?

        self.ltc_past_claim_yes = self.driver.find_element(By.ID, "ltc_past_claim-yes")

        self.ltc_past_claim_no = self.driver.find_element(By.ID, "ltc_past_claim-no")

        # Is the Applicant aware of any circumstances which may result in any claim against the facility or any of the present or past Partners or Officers?

        self.ltc_potential_claim_yes = self.driver.find_element(By.ID, "ltc_potential_claim-yes")

        self.ltc_potential_claim_no = self.driver.find_element(By.ID, "ltc_potential_claim-no")

        # Include Hired Auto and Non-Owned Auto Liability ($100K/$300K Limits)
        self.ltc_include_hnoa = self.driver.find_element(By.ID, "ltc_include_hnoa")

        # Questions display if Include hnoa is clicked

        # Does the Applicant warrant that all employees, independent contractors and volunteers with driving responsibilities maintain automobile insurance that meet the minimum state requirements?:
        self.ltc_warrant_min_insurance_yes = self.driver.find_element(By.ID, "ltc_warrant_min_insurance-yes")

        self.ltc_warrant_min_insurance_no = self.driver.find_element(By.ID, "ltc_warrant_min_insurance-no")

        # Next Question Displays if Answer "Yes" to Above Question

        # Does the Applicant require evidence of such insurance?:
        self.ltc_warrant_min_insurance_detail_yes = self.driver.find_element(By.ID, "ltc_warrant_min_insurance_detail-yes")

        self.ltc_warrant_min_insurance_detail_no = self.driver.find_element(By.ID, "ltc_warrant_min_insurance_detail-no")

        # Does the Applicant access and review Motor Vehicle Reports on all employees with driving responsibilities as a condition of employment?:
        self.ltc_review_reports_yes = self.driver.find_element(By.ID, "ltc_review_reports-yes")

        self.ltc_review_reports_no = self.driver.find_element(By.ID, "ltc_review_reports-no")

        # Next Question Displays if Answer "Yes" to Above Question

        # How frequently is the review conducted?:
        self.ltc_review_reports_detail = self.driver.find_element(By.ID, "ltc_review_reports_detail")

        # Has the Applicant ever been notified of a claim arising from an automobile accident involving an employee who was driving during the course of providing services on behalf of the Applicant?:
        self.ltc_vehicle_prior_claims_yes = self.driver.find_element(By.ID, "ltc_vehicle_prior_claims-yes")

        self.ltc_vehicle_prior_claims_no = self.driver.find_element(By.ID, "ltc_vehicle_prior_claims-no")

        return self

    def create_quote_include_HNOA(self, bed_count):

        PAF.Page_Elements(self).operation_commence_date.send_keys("01-01-2001")
        PAF.Page_Elements(self).bed_count.send_keys(bed_count)
        PAF.Page_Elements(self).facility_license_number.send_keys("A1111111")
        PAF.Page_Elements(self).additional_insured_no.click()
        PAF.Page_Elements(self).ltc_licensed_yes.click()
        PAF.Page_Elements(self).ltc_state_mandate_survey_yes.click()
        PAF.Page_Elements(self).ltc_staff_client_ratio_yes.click()
        PAF.Page_Elements(self).ltc_wandering_risk_assessment_yes.click()
        PAF.Page_Elements(self).ltc_nursing_assessment_yes.click()
        PAF.Page_Elements(self).ltc_reassessment_system_yes.click()
        PAF.Page_Elements(self).ltc_resident_eloped_no.click()
        PAF.Page_Elements(self).ltc_complaint_investigated_no.click()
        PAF.Page_Elements(self).ltc_insurance_declined_no.click()
        PAF.Page_Elements(self).ltc_license_problem_no.click()
        PAF.Page_Elements(self).ltc_past_claim_no.click()
        PAF.Page_Elements(self).ltc_potential_claim_no.click()

        # Include Hired Auto and Non-Owned Auto Liability ($100K/$300K Limits)

        PAF.Page_Elements(self).ltc_include_hnoa.click()
        PAF.Page_Elements(self).ltc_warrant_min_insurance_yes.click()
        # Next question displays if "Yes" to Previous
        PAF.Page_Elements(self).ltc_warrant_min_insurance_detail_yes.click()
        PAF.Page_Elements(self).ltc_review_reports_yes.click()
        PAF.Page_Elements(self).ltc_review_reports_detail.send_keys("Quarterly")
        PAF.Page_Elements(self).ltc_vehicle_prior_claims_no.click()

    def create_quote_NO_HNOA(self, bed_count):
        PAF.Page_Elements(self).operation_commence_date.send_keys("01-01-2001")
        PAF.Page_Elements(self).bed_count.send_keys(bed_count)
        PAF.Page_Elements(self).facility_license_number.send_keys("A1111111")
        PAF.Page_Elements(self).additional_insured_no.click()
        PAF.Page_Elements(self).ltc_licensed_yes.click()
        PAF.Page_Elements(self).ltc_state_mandate_survey_yes.click()
        PAF.Page_Elements(self).ltc_staff_client_ratio_yes.click()
        PAF.Page_Elements(self).ltc_wandering_risk_assessment_yes.click()
        PAF.Page_Elements(self).ltc_nursing_assessment_yes.click()
        PAF.Page_Elements(self).ltc_reassessment_system_yes.click()
        PAF.Page_Elements(self).ltc_resident_eloped_no.click()
        PAF.Page_Elements(self).ltc_complaint_investigated_no.click()
        PAF.Page_Elements(self).ltc_insurance_declined_no.click()
        PAF.Page_Elements(self).ltc_license_problem_no.click()
        PAF.Page_Elements(self).ltc_past_claim_no.click()
        PAF.Page_Elements(self).ltc_potential_claim_no.click()

        # #Include Hired Auto and Non-Owned Auto Liability ($100K/$300K Limits)

        # PAF.Page_Elements(self).ltc_include_hnoa.click()
        # PAF.Page_Elements(self).ltc_warrant_min_insurance_yes.click()
        # #Next question displays if "Yes" to Previous
        # PAF.Page_Elements(self).ltc_warrant_min_insurance_detail_yes.click()
        # PAF.Page_Elements(self).ltc_review_reports_yes.click()
        # PAF.Page_Elements(self).ltc_review_reports_detail.send_keys("Quarterly")
        # PAF.Page_Elements(self).ltc_vehicle_prior_claims_no.click()


    #TODO
    # Ask Dev to create ID for next button
    def click_next(self):
        next_button = self.driver.find_element(By.XPATH, "//form[@id='rate-adjustment-form']/div[2]/div[5]/a/span[2]/span/span")
        next_button.click()