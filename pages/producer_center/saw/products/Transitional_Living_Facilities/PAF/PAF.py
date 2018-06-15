from selenium.webdriver.common.by import By

class PAF():

    def __init__(self, driver):
        self.driver = driver

    #Page Elements

    def Page_Elements(self):

        # Number of Years in Business
        self.years_in_business = self.driver.find_element(By.ID, "business-years-count")

        # Total Staff Count
        self.total_staff_count = self.driver.find_element(By.ID, "staff_count")

        # Total # of Licensed Beds
        self.total_licensed_beds = self.driver.find_element(By.ID, "licensed_beds")

        # On average, are at least 66% of licensed beds occupied?
        self.beds_occupied_yes = self.driver.find_element(By.ID, "gh_beds_occupied-yes")

        self.beds_occupied_no = self.driver.find_element(By.ID, "gh_beds_occupied-no")

        # Does the Applicant perform pre-employment screenings and background checks on all staff and volunteers?

        # Are criminal background checks conducted on all employees
        self.background_checks_yes = self.driver.find_element(By.ID, "gh_background_checks-yes")

        self.background_checks_no = self.driver.find_element(By.ID, "gh_background_checks-no")

        # If “No”, do you agree to implement them immediately?
        self.implement_immediately_yes = self.driver.find_element(By.ID, "gh_implement_immediately-yes")

        self.implement_immediately_no = self.driver.find_element(By.ID, "gh_implement_immediately-no")

        # Does the Applicant have a staff member on the premises at all times?
        self.smember_premises_yes = self.driver.find_element(By.ID, "gh_smember_premises-yes")

        self.smember_premises_no = self.driver.find_element(By.ID, "gh_smember_premises-no")

        # Does the Applicant have a written emergency evacuationplan and medical emergency protocols?
        self.emergency_protocols_yes = self.driver.find_element(By.ID, "gh_emergency_protocals-yes")

        self.emergency_protocols_no = self.driver.find_element(By.ID, "gh_emergency_protocals-no")

        # Does the Applicant have security measures in place to keep track of clients (e.g. sign in/sign out procedures, video cameras and/or alarmed doors?
        self.security_measures_yes = self.driver.find_element(By.ID, "gh_security_measures-yes")

        self.security_measures_no = self.driver.find_element(By.ID, "gh_security_measures-no")

        # Are clients screened prior to admission to determine eligibility?
        self.screened_prior_yes = self.driver.find_element(By.ID, "gh_screened_prior-yes")

        self.screened_prior_no = self.driver.find_element(By.ID, "gh_screened_prior-no")

        # Are male and female residents separated?
        self.gender_separated_yes = self.driver.find_element(By.ID, "gh_gender_separated-yes")

        self.gender_separated_no = self.driver.find_element(By.ID, "gh_gender_separated-no")

        # Is the Applicant Licensed as an Intermediate Care Facility?
        self.app_licensed_yes = self.driver.find_element(By.ID, "gh_app_licensed-yes")

        self.app_licensed_no = self.driver.find_element(By.ID, "gh_app_licensed-no")

        # Does the Applicant provide services to the following populations:

        # Minors?
        self.minors_yes = self.driver.find_element(By.ID, "gh_minors-yes")

        self.minors_no = self.driver.find_element(By.ID, "gh_minors-no")

        # Elderly?
        self.elderly_yes = self.driver.find_element(By.ID, "gh_elderly-yes")

        self.elderly_no = self.driver.find_element(By.ID, "gh_elderly-no")

        # Bedridden?
        self.bedridden_yes = self.driver.find_element(By.ID, "gh_bedridden-yes")

        self.bedridden_no = self.driver.find_element(By.ID, "gh_bedridden-no")

        # Non-Ambulatory?
        self.ambulatory_yes = self.driver.find_element(By.ID, "gh_ambulatory-yes")

        self.ambulatory_no = self.driver.find_element(By.ID, "gh_ambulatory-no")

        # People on parole, probation or recently released from incarceration?
        self.probation_yes = self.driver.find_element(By.ID, "gh_probation-yes")

        self.probation_no = self.driver.find_element(By.ID, "gh_probation-no")

        # Is the Applicant appointed legal guardian or responsible for financial decisions of residents?
        self.financial_decisions_yes = self.driver.find_element(By.ID, "gh_financial_decisions-yes")

        self.financial_decisions_no = self.driver.find_element(By.ID, "gh_financial_decisions-no")

        # Does the Applicant operate as an alternative to incarceration or a locked down facility?
        self.incarceration_yes = self.driver.find_element(By.ID, "gh_incarceration-yes")

        self.incarceration_no = self.driver.find_element(By.ID, "gh_incarceration-no")

        # Does the Applicant provide field trips?
        self.field_trips_yes = self.driver.find_element(By.ID, "gh_field_trips-yes")

        self.field_trips_no = self.driver.find_element(By.ID, "gh_field_trips-no")

        # Has the Applicant’s License to operate been denied, suspended, revoked, put on probation, or otherwise been restricted in anyway?
        self.license_denied_yes = self.driver.find_element(By.ID, "gh_license_denied-yes")

        self.license_denied_no = self.driver.find_element(By.ID, "gh_license_denied-no")

        # During the last three years has the Applicant:

        # Been issued more than 10 citations?
        self.citations_yes = self.driver.find_element(By.ID, "gh_citations-yes")

        self.citations_no = self.driver.find_element(By.ID, "gh_citations-no")

        # Accepted or provided continuing care to a resident for whom you are not licensed to provide care?
        self.resident_yes = self.driver.find_element(By.ID, "gh_resident-yes")

        self.resident_no = self.driver.find_element(By.ID, "gh_resident-no")

        # Been cited for delaying treatment to an injured resident?
        self.treatment_yes = self.driver.find_element(By.ID, "gh_treatment-yes")

        self.treatment_no = self.driver.find_element(By.ID, "gh_treatment-no")

        # Been the subject of any state informal compliance conference?
        self.informal_yes = self.driver.find_element(By.ID, "gh_informal-yes")

        self.informal_no = self.driver.find_element(By.ID, "gh_informal-no")

        # Been placed on a formal non-compliance plan?
        self.formal_yes = self.driver.find_element(By.ID, "gh_formal-yes")

        self.formal_no = self.driver.find_element(By.ID, "gh_formal-no")

        # Has the Applicant or any of its providers/employees ever been/had:

        # The subject in disciplinary or investigative proceedings or reprimanded by a governmental or administrative agency, hospital or professional association?
        self.sub_disciplinary_yes = self.driver.find_element(By.ID, "gh_sub_disciplinary-yes")

        self.sub_disciplinary_no = self.driver.find_element(By.ID, "gh_sub_disciplinary-no")

        # Convicted of an act committed in violation of any law or ordinance other than traffic offenses?
        self.violation_yes = self.driver.find_element(By.ID, "gh_violation-yes")

        self.violation_no = self.driver.find_element(By.ID, "gh_violation-no")

        # Any state professional license or license to prescribe or dispense narcotics refused, suspended, revoked, renewal refused or accepted only on specific terms, or ever voluntarily surrendered?
        self.prof_license_yes = self.driver.find_element(By.ID, "gh_prof_license-yes")

        self.prof_license_no = self.driver.find_element(By.ID, "gh_prof_license-no")

        # Has any Application for Professional Liability Insurance made on behalf of the Applicant, any predecessors in business or present Partners EVER been declined or has similar insurance ever been cancelled or non-renewed?
        self.similar_insurance_yes = self.driver.find_element(By.ID, "gh_similar_insurance-yes")

        self.similar_insurance_no = self.driver.find_element(By.ID, "gh_similar_insurance-no")

        # Has any claim EVER been made against the Applicant or any of its employees?
        self.claim_yes = self.driver.find_element(By.ID, "gh_claim-yes")

        self.claim_no = self.driver.find_element(By.ID, "gh_claim-no")

        # Is the Applicant aware of ANY circumstances which may result in ANY claim against it, its predecessors in business, or any of its past or present directors, officers, or partners?
        self.aware_partners_yes = self.driver.find_element(By.ID, "gh_aware_partners-yes")

        self.aware_partners_no = self.driver.find_element(By.ID, "gh_aware_partners-no")

        # a) Does the Applicant have expiring coverage in place? (If retroactive coverage is desired, please submit expiring declaration page and three years of lossrun.)
        self.expiring_coverage_yes = self.driver.find_element(By.ID, "gh_expiring_coverage-yes")

        self.expiring_coverage_no = self.driver.find_element(By.ID, "gh_expiring_coverage-no")

        # Is the Applicant interested in Hired and Non-Owned Auto Liability coverage?
        self.hired_yes = self.driver.find_element(By.ID, "gh_hired-yes")

        self.hired_no = self.driver.find_element(By.ID, "gh_hired-no")

        # If “Yes” to the above, does the Applicant warrant that all providers/employees with driving responsibilities maintain automobile insurance that meets the minimum state requirements, AND does the Applicant access and review Motor Vehicle Reports on all such individuals as a condition of employment?
        self.warrant_yes = self.driver.find_element(By.ID, "gh_warrant-yes")

        self.warrant_no = self.driver.find_element(By.ID, "gh_warrant-no")

        return self

    def create_quote_include_HNOA(self, years_in_business, staff_count, total_occupied_beds):
        PAF.Page_Elements(self).years_in_business.send_keys(years_in_business)
        PAF.Page_Elements(self).total_staff_count.send_keys(staff_count)
        PAF.Page_Elements(self).total_licensed_beds.send_keys(total_occupied_beds)
        PAF.Page_Elements(self).beds_occupied_yes.click()
        PAF.Page_Elements(self).background_checks_yes.click()
        PAF.Page_Elements(self).smember_premises_yes.click()
        PAF.Page_Elements(self).emergency_protocols_yes.click()
        PAF.Page_Elements(self).security_measures_yes.click()
        PAF.Page_Elements(self).screened_prior_yes.click()
        PAF.Page_Elements(self).gender_separated_yes.click()
        PAF.Page_Elements(self).app_licensed_no.click()
        PAF.Page_Elements(self).minors_no.click()
        PAF.Page_Elements(self).elderly_no.click()
        PAF.Page_Elements(self).bedridden_no.click()
        PAF.Page_Elements(self).ambulatory_no.click()
        PAF.Page_Elements(self).probation_no.click()
        PAF.Page_Elements(self).financial_decisions_no.click()
        PAF.Page_Elements(self).incarceration_no.click()
        PAF.Page_Elements(self).field_trips_no.click()
        PAF.Page_Elements(self).license_denied_no.click()
        PAF.Page_Elements(self).citations_no.click()
        PAF.Page_Elements(self).resident_no.click()
        PAF.Page_Elements(self).treatment_no.click()
        PAF.Page_Elements(self).informal_no.click()
        PAF.Page_Elements(self).formal_no.click()
        PAF.Page_Elements(self).sub_disciplinary_no.click()
        PAF.Page_Elements(self).violation_no.click()
        PAF.Page_Elements(self).prof_license_no.click()
        PAF.Page_Elements(self).similar_insurance_no.click()
        PAF.Page_Elements(self).claim_no.click()
        PAF.Page_Elements(self).aware_partners_no.click()
        PAF.Page_Elements(self).expiring_coverage_yes.click()
        PAF.Page_Elements(self).hired_yes.click()
        PAF.Page_Elements(self).warrant_yes.click()

    def create_quote_NO_HNOA(self, years_in_business, staff_count, total_occupied_beds):
        PAF.Page_Elements(self).years_in_business.send_keys(years_in_business)
        PAF.Page_Elements(self).total_staff_count.send_keys(staff_count)
        PAF.Page_Elements(self).total_licensed_beds.send_keys(total_occupied_beds)
        PAF.Page_Elements(self).beds_occupied_yes.click()
        PAF.Page_Elements(self).background_checks_yes.click()
        PAF.Page_Elements(self).smember_premises_yes.click()
        PAF.Page_Elements(self).emergency_protocols_yes.click()
        PAF.Page_Elements(self).security_measures_yes.click()
        PAF.Page_Elements(self).screened_prior_yes.click()
        PAF.Page_Elements(self).gender_separated_yes.click()
        PAF.Page_Elements(self).app_licensed_no.click()
        PAF.Page_Elements(self).minors_no.click()
        PAF.Page_Elements(self).elderly_no.click()
        PAF.Page_Elements(self).bedridden_no.click()
        PAF.Page_Elements(self).ambulatory_no.click()
        PAF.Page_Elements(self).probation_no.click()
        PAF.Page_Elements(self).financial_decisions_no.click()
        PAF.Page_Elements(self).incarceration_no.click()
        PAF.Page_Elements(self).field_trips_no.click()
        PAF.Page_Elements(self).license_denied_no.click()
        PAF.Page_Elements(self).citations_no.click()
        PAF.Page_Elements(self).resident_no.click()
        PAF.Page_Elements(self).treatment_no.click()
        PAF.Page_Elements(self).informal_no.click()
        PAF.Page_Elements(self).formal_no.click()
        PAF.Page_Elements(self).sub_disciplinary_no.click()
        PAF.Page_Elements(self).violation_no.click()
        PAF.Page_Elements(self).prof_license_no.click()
        PAF.Page_Elements(self).similar_insurance_no.click()
        PAF.Page_Elements(self).claim_no.click()
        PAF.Page_Elements(self).aware_partners_no.click()
        PAF.Page_Elements(self).expiring_coverage_yes.click()
        PAF.Page_Elements(self).hired_no.click()


    def input_retroactive_date(self, retroactive_date):
        self.retroactive_date = self.driver.find_element(By.ID, "date_retroactive")
        self.retroactive_date.send_keys()

    #TODO
    # Ask Dev to create ID for next button
    def click_next(self):
        next_button = self.driver.find_element(By.XPATH, "//form[@id='primary']/div[3]/div[3]/a/span[2]/span/span")
        next_button.click()