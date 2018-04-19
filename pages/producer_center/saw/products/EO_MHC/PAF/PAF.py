from selenium.webdriver.common.by import By

class PAF():

    def __init__(self, driver):
        self.driver = driver

    # Page Elements

    def Page_Elements(self):

        # Total expected revenue as a consultant for the upcoming policy period:
        self.total_expected_revenue = self.driver.find_element(By.ID, "annual_consulting_revenue_next_year")

        # Current year revenue earned as a consultant:
        self.total_current_year_revenue = self.driver.find_element(By.ID, "annual_consulting_revenue_current_year")

        # Prior year revenue earned as a consultant:
        self.previous_year_revenue = self.driver.find_element(By.ID, "annual_consulting_revenue_previous_year")

        # Please check off all consulting services performed by the Applicant:

        # Expert Witness
        self.expert_witness = self.driver.find_element(By.ID, "insured_services_expert_witness")

        # Disability Evaluation
        self.disability_evaluation = self.driver.find_element(By.ID, "insured_services_disability_evaluation")

        # Managed Care Contracting
        self.managed_care_contracting = self.driver.find_element(By.ID, "insured_services_managed_care_contracting")

        # Independent Medical Record Review
        self.independent_medical_review = self.driver.find_element(By.ID, "insured_services_independent_medical_review")

        # Workers' Compensation Evaluation
        self.workers_compensation_evaluation = self.driver.find_element(By.ID, "insured_services_workers_compensation_evaluation")

        # Other
        self.other = self.driver.find_element(By.ID, "insured_services_other")

        # Other (Text Field)
        self.other_text = self.driver.find_element(By.ID, "insured_services_other_text")

        # Is the Applicant currently covered by a Medical Professional Liability policy?
        self.currently_covered_mpl_yes = self.driver.find_element(By.ID, "eo_mhc_currently_covered_mpl_yes")

        self.currently_covered_mpl_no = self.driver.find_element(By.ID, "eo_mhc_currently_covered_mpl_no")

        # If "Yes", who is your medical professional liability carrier?:
        self.currently_covered_mpl_detail = self.driver.find_element(By.ID, "eo_mhc_currently_covered_mpl_detail")

        # Is the Applicant or any person proposed for this insurance retired from the practice of medicine?
        self.currently_retired_yes = self.driver.find_element(By.ID, "eo_mhc_currently_retired-yes")

        self.currently_retired_no = self.driver.find_element(By.ID, "eo_mhc_currently_retired-no")

        # If "Yes", please provide details:
        self.currently_retired_detail = self.driver.find_element(By.ID, "eo_mhc_currently_retired_detail")


        # Does the Applicant's revenue attributable to consulting services involving direct patient contact exceed 15% of the Applicant’s total revenue as a consultant?
        self.patient_contact_yes = self.driver.find_element(By.ID, "eo_mhc_patient_contact_yes")

        self.patient_contact_no = self.driver.find_element(By.ID, "eo_mhc_patient_contact_no")

        # Does the Applicant currently provide consulting services to any governmental entities or plan to do so in the future?
        self.governmental_services_yes = self.driver.find_element(By.ID, "eo_mhc_governmental_services_yes")

        self.governmental_services_no = self.driver.find_element(By.ID, "eo_mhc_governmental_services_no")

        # Have any claims, suits, or demands been made against the Applicant, a predecessor firm, any past or present principals, partners, officers, or employees within the past five(5) years?
        self.past_claim_yes = self.driver.find_element(By.ID, "eo_mhc_past_claim_yes")

        self.past_claim_no = self.driver.find_element(By.ID, "eo_mhc_past_claim_no")

        # Does the Applicant have knowledge of any dispute, error, omission, act or circumstance that is, or could reasonably be expected to become a claim under the policy for which this application is submitted?
        self.potential_claim_yes = self.driver.find_element(By.ID, "eo_mhc_potential_claim_yes")

        self.potential_claim_no = self.driver.find_element(By.ID, "eo_mhc_potential_claim_no")

        # For questions 11-12, if the answer is "no", coverage cannot be bound per the terms and conditions of this program. If you desire an indication outside the program, please provide details for the "no" answers.

        # If the Applicant handles patient data, is there a compliance program in place for HIPAA?
        self.hipaa_compliance_yes = self.driver.find_element(By.ID, "eo_mhc_hipaa_compliance_yes")

        self.hipaa_compliance_no = self.driver.find_element(By.ID, "eo_mhc_hipaa_compliance_no")

        # Does the Applicant firm use a written contract with clients describing the services provided?
        self.written_contract_yes = self.driver.find_element(By.ID, "eo_mhc_written_contract_yes")

        self.written_contract_no = self.driver.find_element(By.ID, "eo_mhc_written_contract_no")

        return self

    def create_quote_No_DQ_expert_witness(self, revenue_next_year, revenue_current_year, revenue_previous_year):
        PAF.Page_Elements(self).total_expected_revenue.send_keys(revenue_next_year)
        PAF.Page_Elements(self).total_current_year_revenue.send_keys(revenue_current_year)
        PAF.Page_Elements(self).previous_year_revenue.send_keys(revenue_previous_year)
        PAF.Page_Elements(self).expert_witness.click()
        PAF.Page_Elements(self).currently_covered_mpl_yes.click()
        PAF.Page_Elements(self).currently_covered_mpl_detail.send_keys("QA Test")
        PAF.Page_Elements(self).currently_retired_no.click()
        PAF.Page_Elements(self).patient_contact_no.click()
        PAF.Page_Elements(self).governmental_services_no.click()
        PAF.Page_Elements(self).past_claim_no.click()
        PAF.Page_Elements(self).potential_claim_no.click()
        PAF.Page_Elements(self).hipaa_compliance_yes.click()
        PAF.Page_Elements(self).written_contract_yes.click()

    def create_quote_No_DQ_disability_evaluation(self, revenue_next_year, revenue_current_year, revenue_previous_year):
        PAF.Page_Elements(self).total_expected_revenue.send_keys(revenue_next_year)
        PAF.Page_Elements(self).total_current_year_revenue.send_keys(revenue_current_year)
        PAF.Page_Elements(self).previous_year_revenue.send_keys(revenue_previous_year)
        PAF.Page_Elements(self).disability_evaluation.click()
        PAF.Page_Elements(self).currently_covered_mpl_yes.click()
        PAF.Page_Elements(self).currently_covered_mpl_detail.send_keys("QA Test")
        PAF.Page_Elements(self).currently_retired_no.click()
        PAF.Page_Elements(self).patient_contact_no.click()
        PAF.Page_Elements(self).governmental_services_no.click()
        PAF.Page_Elements(self).past_claim_no.click()
        PAF.Page_Elements(self).potential_claim_no.click()
        PAF.Page_Elements(self).hipaa_compliance_yes.click()
        PAF.Page_Elements(self).written_contract_yes.click()

    def create_quote_No_DQ_managed_care_contracting(self, revenue_next_year, revenue_current_year, revenue_previous_year):
        PAF.Page_Elements(self).total_expected_revenue.send_keys(revenue_next_year)
        PAF.Page_Elements(self).total_current_year_revenue.send_keys(revenue_current_year)
        PAF.Page_Elements(self).previous_year_revenue.send_keys(revenue_previous_year)
        PAF.Page_Elements(self).managed_care_contracting.click()
        PAF.Page_Elements(self).currently_covered_mpl_yes.click()
        PAF.Page_Elements(self).currently_covered_mpl_detail.send_keys("QA Test")
        PAF.Page_Elements(self).currently_retired_no.click()
        PAF.Page_Elements(self).patient_contact_no.click()
        PAF.Page_Elements(self).governmental_services_no.click()
        PAF.Page_Elements(self).past_claim_no.click()
        PAF.Page_Elements(self).potential_claim_no.click()
        PAF.Page_Elements(self).hipaa_compliance_yes.click()
        PAF.Page_Elements(self).written_contract_yes.click()

    def create_quote_No_DQ_independent_medical_review(self, revenue_next_year, revenue_current_year, revenue_previous_year):
        PAF.Page_Elements(self).total_expected_revenue.send_keys(revenue_next_year)
        PAF.Page_Elements(self).total_current_year_revenue.send_keys(revenue_current_year)
        PAF.Page_Elements(self).previous_year_revenue.send_keys(revenue_previous_year)
        PAF.Page_Elements(self).independent_medical_review.click()
        PAF.Page_Elements(self).currently_covered_mpl_yes.click()
        PAF.Page_Elements(self).currently_covered_mpl_detail.send_keys("QA Test")
        PAF.Page_Elements(self).currently_retired_no.click()
        PAF.Page_Elements(self).patient_contact_no.click()
        PAF.Page_Elements(self).governmental_services_no.click()
        PAF.Page_Elements(self).past_claim_no.click()
        PAF.Page_Elements(self).potential_claim_no.click()
        PAF.Page_Elements(self).hipaa_compliance_yes.click()
        PAF.Page_Elements(self).written_contract_yes.click()

    def create_quote_No_DQ_workers_compensation_evaluation(self, revenue_next_year, revenue_current_year, revenue_previous_year):
        PAF.Page_Elements(self).total_expected_revenue.send_keys(revenue_next_year)
        PAF.Page_Elements(self).total_current_year_revenue.send_keys(revenue_current_year)
        PAF.Page_Elements(self).previous_year_revenue.send_keys(revenue_previous_year)
        PAF.Page_Elements(self).workers_compensation_evaluation.click()
        PAF.Page_Elements(self).currently_covered_mpl_yes.click()
        PAF.Page_Elements(self).currently_covered_mpl_detail.send_keys("QA Test")
        PAF.Page_Elements(self).currently_retired_no.click()
        PAF.Page_Elements(self).patient_contact_no.click()
        PAF.Page_Elements(self).governmental_services_no.click()
        PAF.Page_Elements(self).past_claim_no.click()
        PAF.Page_Elements(self).potential_claim_no.click()
        PAF.Page_Elements(self).hipaa_compliance_yes.click()
        PAF.Page_Elements(self).written_contract_yes.click()

    def create_quote_No_DQ_other(self, revenue_next_year, revenue_current_year, revenue_previous_year):
        PAF.Page_Elements(self).total_expected_revenue.send_keys(revenue_next_year)
        PAF.Page_Elements(self).total_current_year_revenue.send_keys(revenue_current_year)
        PAF.Page_Elements(self).previous_year_revenue.send_keys(revenue_previous_year)
        PAF.Page_Elements(self).other.click()
        PAF.Page_Elements(self).other_text.send_keys("QA Test")
        PAF.Page_Elements(self).currently_covered_mpl_yes.click()
        PAF.Page_Elements(self).currently_covered_mpl_detail.send_keys("QA Test")
        PAF.Page_Elements(self).currently_retired_no.click()
        PAF.Page_Elements(self).patient_contact_no.click()
        PAF.Page_Elements(self).governmental_services_no.click()
        PAF.Page_Elements(self).past_claim_no.click()
        PAF.Page_Elements(self).potential_claim_no.click()
        PAF.Page_Elements(self).hipaa_compliance_yes.click()
        PAF.Page_Elements(self).written_contract_yes.click()

    #TODO
    # Ask Dev to create ID for next button
    def click_next(self):
        next_button = self.driver.find_element(By.XPATH, "//form[@id='primary-abeo-form']/div[5]/a/span[2]/span/span")
        next_button.click()