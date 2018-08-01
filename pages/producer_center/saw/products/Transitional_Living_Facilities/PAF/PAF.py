from selenium.webdriver.common.by import By

class PAF():

    def __init__(self, driver):
        self.driver = driver

    #Page Elements

    def Page_Elements(self):

        # Number of Years in Business
        self.years_in_business = self.driver.find_element(By.ID, "translvg_business_years")

        # Total Staff Count
        self.total_staff_count = self.driver.find_element(By.ID, "translvg_staff_count")

        # Total # of Licensed Beds
        self.total_licensed_beds = self.driver.find_element(By.ID, "translvg_total_beds")

        # On average, are at least 66% of licensed beds occupied?
        self.beds_occupied_yes = self.driver.find_element(By.ID, "translvg_licensed_beds-yes")

        self.beds_occupied_no = self.driver.find_element(By.ID, "translvg_licensed_beds-no")

        # Does the Applicant perform pre-employment screenings and background checks on all staff and volunteers?

        # Are criminal background checks conducted on all employees
        self.background_checks_yes = self.driver.find_element(By.ID, "translvg_background_checks-yes")

        self.background_checks_no = self.driver.find_element(By.ID, "translvg_background_checks-no")

        # If “No”, do you agree to implement them immediately?
        self.implement_immediately_yes = self.driver.find_element(By.ID, "translvg_implement_immediately-yes")

        self.implement_immediately_no = self.driver.find_element(By.ID, "translvg_implement_immediately-no")

        # Does the Applicant have a procedure in place for emergencies?
        self.emergency_procedure_yes = self.driver.find_element(By.ID, "translvg_emergency_procedure-yes")

        self.emergency_procedure_no = self.driver.find_element(By.ID, "translvg_emergency_procedure-no")

        # Does the Applicant have procedures in place to make sure no relationship occurs between staff and client?
        self.client_staff_relationship_yes = self.driver.find_element(By.ID, "translvg_client_staff_relationship-yes")

        self.client_staff_relationship_no = self.driver.find_element(By.ID, "translvg_client_staff_relationship-no")

        # Are all providers/employees licensed in accordance with applicable state and federal regulations if required?
        self.state_licensed_yes = self.driver.find_element(By.ID, "translvg_state_licensed-yes")

        self.state_licensed_no = self.driver.find_element(By.ID, "translvg_state_licensed-no")

        # Does the Applicant have a written/formalized risk management/quality assurance program?
        self.assurance_program_yes = self.driver.find_element(By.ID, "translvg_assurance_program-yes")

        self.assurance_program_no = self.driver.find_element(By.ID, "translvg_assurance_program-no")

        # Has the Applicant or any of its providers/employees ever been/had:

        # The subject in disciplinary or investigative proceedings or reprimanded by a governmental or administrative agency, hospital or professional association?
        self.agency_association_yes = self.driver.find_element(By.ID, "translvg_agency_association-yes")

        self.agency_association_no = self.driver.find_element(By.ID, "translvg_agency_association-no")

        # Convicted of an act committed in violation of any law or ordinance other than traffic offenses?
        self.act_committed_yes = self.driver.find_element(By.ID, "translvg_act_committed-yes")

        self.act_committed_no = self.driver.find_element(By.ID, "translvg_act_committed-no")

        # Any state professional license or license to prescribe or dispense narcotics refused, suspended, revoked, renewal refused or accepted only on specific terms, or ever voluntarily surrendered?
        self.specific_terms_yes = self.driver.find_element(By.ID, "translvg_specific_terms-yes")

        self.specific_terms_no = self.driver.find_element(By.ID, "translvg_specific_terms-no")

        # Do Clients reside at the Applicant’s Facility longer than one year?
        self.applicant_facility_yes = self.driver.find_element(By.ID, "translvg_applicant_facility-yes")

        self.applicant_facility_no = self.driver.find_element(By.ID, "translvg_applicant_facility-no")

        # Does the Applicant provide services to:

        # Adjudicated Sex Offenders or Convicted Felons
        self.convicted_felons_yes = self.driver.find_element(By.ID, "translvg_convicted_felons-yes")

        self.convicted_felons_no = self.driver.find_element(By.ID, "translvg_convicted_felons-no")

        # Minors
        self.minors_yes = self.driver.find_element(By.ID, "translvg_minors-yes")

        self.minors_no = self.driver.find_element(By.ID, "translvg_minors-no")

        # Does the Applicant operate as a lock-down facility?
        self.lock_down_facility_yes = self.driver.find_element(By.ID, "translvg_lock_down_facility-yes")

        self.lock_down_facility_no = self.driver.find_element(By.ID, "translvg_lock_down_facility-no")

        # Does the Applicant accept court-ordered placements?
        self.applicant_placements_yes = self.driver.find_element(By.ID, "translvg_applicant_placements-yes")

        self.applicant_placements_no = self.driver.find_element(By.ID, "translvg_applicant_placements-no")

        # Does the Applicant provide medical services (e.g. skilled nursing, medical treatment, etc.)?
        self.medical_services_yes = self.driver.find_element(By.ID, "translvg_medical_services-yes")

        self.medical_services_no = self.driver.find_element(By.ID, "translvg_medical_services-no")

        # Has any Application for Professional Liability Insurance made on behalf of the Applicant, any predecessors in business or present Partners EVER been declined or has similar insurance ever been cancelled or non-renewed?
        self.insurence_cancelled_yes = self.driver.find_element(By.ID, "translvg_insurence_cancelled-yes")

        self.insurence_cancelled_no = self.driver.find_element(By.ID, "translvg_insurence_cancelled-no")

        # Has any claim EVER been made against the Applicant or any of its employees?
        self.employee_claim_yes = self.driver.find_element(By.ID, "translvg_employee_claim-yes")

        self.employee_claim_no = self.driver.find_element(By.ID, "translvg_employee_claim-no")

        # Is the Applicant aware of ANY circumstances which may result in ANY claim against it, its predecessors in business, or any of its past or present directors, officers, or partners?
        self.applicant_awareness_yes = self.driver.find_element(By.ID, "translvg_applicant_awareness-yes")

        self.applicant_awareness_no = self.driver.find_element(By.ID, "translvg_applicant_awareness-no")

        # a) Does the Applicant have expiring coverage in place? (If retroactive coverage is desired, please submit expiring declaration page and three years of lossrun.)
        self.expiring_coverage_yes = self.driver.find_element(By.ID, "translvg_expiring_coverage-yes")

        self.expiring_coverage_no = self.driver.find_element(By.ID, "translvg_expiring_coverage-no")

        # Is the Applicant interested in Hired and Non-Owned Auto Liability coverage?
        self.hnoa_yes = self.driver.find_element(By.ID, "translvg_hnoa-yes")

        self.hnoa_no = self.driver.find_element(By.ID, "translvg_hnoa-no")

        # If “Yes” to the above, does the Applicant warrant that all providers/employees with driving responsibilities maintain automobile insurance that meets the minimum state requirements, AND does the Applicant access and review Motor Vehicle Reports on all such individuals as a condition of employment?
        self.warrant_yes = self.driver.find_element(By.ID, "translvg_warrant-yes")

        self.warrant_no = self.driver.find_element(By.ID, "translvg_warrant-no")

        return self

    def create_quote_include_HNOA(self, years_in_business, staff_count, total_occupied_beds):
        PAF.Page_Elements(self).years_in_business.send_keys(years_in_business)
        PAF.Page_Elements(self).total_staff_count.send_keys(staff_count)
        PAF.Page_Elements(self).total_licensed_beds.send_keys(total_occupied_beds)
        PAF.Page_Elements(self).beds_occupied_yes.click()
        PAF.Page_Elements(self).background_checks_yes.click()
        PAF.Page_Elements(self).emergency_procedure_yes.click()
        PAF.Page_Elements(self).client_staff_relationship_yes.click()
        PAF.Page_Elements(self).state_licensed_yes.click()
        PAF.Page_Elements(self).assurance_program_yes.click()
        PAF.Page_Elements(self).agency_association_no.click()
        PAF.Page_Elements(self).act_committed_no.click()
        PAF.Page_Elements(self).specific_terms_no.click()
        PAF.Page_Elements(self).applicant_facility_no.click()
        PAF.Page_Elements(self).convicted_felons_no.click()
        PAF.Page_Elements(self).minors_no.click()
        PAF.Page_Elements(self).lock_down_facility_no.click()
        PAF.Page_Elements(self).applicant_placements_no.click()
        PAF.Page_Elements(self).medical_services_no.click()
        PAF.Page_Elements(self).insurence_cancelled_no.click()
        PAF.Page_Elements(self).employee_claim_no.click()
        PAF.Page_Elements(self).applicant_awareness_no.click()
        PAF.Page_Elements(self).expiring_coverage_yes.click()
        PAF.Page_Elements(self).hnoa_yes.click()
        PAF.Page_Elements(self).warrant_yes.click()

    def create_quote_NO_HNOA(self, years_in_business, staff_count, total_occupied_beds):
        PAF.Page_Elements(self).years_in_business.send_keys(years_in_business)
        PAF.Page_Elements(self).total_staff_count.send_keys(staff_count)
        PAF.Page_Elements(self).total_licensed_beds.send_keys(total_occupied_beds)
        PAF.Page_Elements(self).beds_occupied_yes.click()
        PAF.Page_Elements(self).background_checks_yes.click()
        PAF.Page_Elements(self).emergency_procedure_yes.click()
        PAF.Page_Elements(self).client_staff_relationship_yes.click()
        PAF.Page_Elements(self).state_licensed_yes.click()
        PAF.Page_Elements(self).assurance_program_yes.click()
        PAF.Page_Elements(self).agency_association_no.click()
        PAF.Page_Elements(self).act_committed_no.click()
        PAF.Page_Elements(self).specific_terms_no.click()
        PAF.Page_Elements(self).applicant_facility_no.click()
        PAF.Page_Elements(self).convicted_felons_no.click()
        PAF.Page_Elements(self).minors_no.click()
        PAF.Page_Elements(self).lock_down_facility_no.click()
        PAF.Page_Elements(self).applicant_placements_no.click()
        PAF.Page_Elements(self).medical_services_no.click()
        PAF.Page_Elements(self).insurence_cancelled_no.click()
        PAF.Page_Elements(self).employee_claim_no.click()
        PAF.Page_Elements(self).applicant_awareness_no.click()
        PAF.Page_Elements(self).expiring_coverage_yes.click()
        PAF.Page_Elements(self).hnoa_no.click()


    def input_retroactive_date(self, retroactive_date_formatted):
        self.retroactive_date = self.driver.find_element(By.ID, "translvg_expiring_coverage_retroactive_date")
        self.retroactive_date.click()
        self.retroactive_date.send_keys(retroactive_date_formatted)

    #TODO
    # Ask Dev to create ID for next button
    def click_next(self):
        next_button = self.driver.find_element(By.XPATH, "//form[@id='primary']/div[3]/div[3]/a/span[2]/span/span")
        next_button.click()