from selenium.webdriver.common.by import By

class PAF():

    def __init__(self, driver):
        self.driver = driver

    #Page Elements

    def Page_Elements(self):

        # Number of Years in Business
        self.years_in_business = self.driver.find_element(By.ID, "years-in-business")

        # Total Staff Count
        self.total_staff_count = self.driver.find_element(By.ID, "hhol_staff_count")

        # Does the Applicant have any providers/employees that are physicians, chiropractors, acupuncturists, CRNAs, Nurse Practitioners, or Physician's Assistants
        self.staff_type_yes = self.driver.find_element(By.ID, "hhol_staff_type-yes")

        self.staff_type_no = self.driver.find_element(By.ID, "hhol_staff_type-no")

        # If "Yes" to the above, do all of these individuals carry their own coverage
        self.staff_type_own_coverage_yes = self.driver.find_element(By.ID, "hhol_staff_own_coverage-yes")

        self.staff_type_own_coverage_no = self.driver.find_element(By.ID, "hhol_staff_own_coverage-no")

        self.staff_type_own_coverage_na = self.driver.find_element(By.ID, "hhol_staff_own_coverage-na")

        # Are all providers/employees licensed in accordance with applicable state and federal regulations
        self.employees_licensed_yes = self.driver.find_element(By.ID, "hhol_employees_licensed-yes")

        self.employees_licensed_no = self.driver.find_element(By.ID, "hhol_employees_licensed-no")

        # Are criminal background checks conducted on all employees
        self.background_checks_yes = self.driver.find_element(By.ID, "hhol_background_checks-yes")

        self.background_checks_no = self.driver.find_element(By.ID, "hhol_background_checks-no")

        # Does the Applicant conduct pre-employment screenings and/or any other necessary investigations and credentialing prior to hiring any staff
        self.employees_screened_yes = self.driver.find_element(By.ID, "hhol_employees_screened-yes")

        self.employees_screened_no = self.driver.find_element(By.ID, "hhol_employees_screened-no")

        # Does the Applicant have a written/formalized risk management/quality assurance program
        self.qa_program_yes = self.driver.find_element(By.ID, "hhol_qa_program-yes")

        self.qa_program_no = self.driver.find_element(By.ID, "hhol_qa_program-no")

        # Does the Applicant have written procedures in place for the reporting all incidents
        self.incidents_procedure_yes = self.driver.find_element(By.ID, "hhol_incidents_procedure-yes")

        self.incidents_procedure_no = self.driver.find_element(By.ID, "hhol_incidents_procedure-no")

        # Has the Applicant or any of its providers/employees ever...

        #  Been the subject in disciplinary or investigative proceedings or reprimanded by a governmental or administrative agency, hospital or professional association
        self.employees_investigated_yes = self.driver.find_element(By.ID, "hhol_employees_investigated-yes")

        self.employees_investigated_no = self.driver.find_element(By.ID, "hhol_employees_investigated-no")

        #  Been convicted of an act committed in violation of any law or ordinance other than traffic offenses
        self.employees_violation_yes = self.driver.find_element(By.ID, "hhol_employees_violation-yes")

        self.employees_violation_no = self.driver.find_element(By.ID, "hhol_employees_violation-no")

        # Been treated for alcoholism or drug addiction
        self.employees_addiction_yes = self.driver.find_element(By.ID, "hhol_employees_addiction-yes")

        self.employees_addiction_no = self.driver.find_element(By.ID, "hhol_employees_addiction-no")

        # Had any state professional license or license to prescribe or dispense narcotics refused, suspended, revoked, renewal refused or accepted only on special terms, or ever voluntarily surrendered
        self.employees_revoked_yes = self.driver.find_element(By.ID, "hhol_employees_revoked-yes")

        self.employees_revoked_no = self.driver.find_element(By.ID, "hhol_employees_revoked-no")

        # Are greater than 15% of the Applicant's services rendered at, or involve, any of the following

        # Hospitals
        self.services_hospitals_yes = self.driver.find_element(By.ID, "hhol_services_hospitals-yes")

        self.services_hospitals_no = self.driver.find_element(By.ID, "hhol_services_hospitals-no")

        # Pediatric care
        self.services_pediatric_yes = self.driver.find_element(By.ID, "hhol_services_pediatric-yes")

        self.services_pediatric_no = self.driver.find_element(By.ID, "hhol_services_pediatric-no")

        # Skilled nursing
        self.services_nursing_yes = self.driver.find_element(By.ID, "hhol_services_nursing-yes")

        self.services_nursing_no = self.driver.find_element(By.ID, "hhol_services_nursing-no")

        # Does the Applicant perform or provide the following:

        # Services to correctional facilities
        self.perform_correctional_yes = self.driver.find_element(By.ID, "hhol_perform_correctional-yes")

        self.perform_correctional_no = self.driver.find_element(By.ID, "hhol_perform_correctional-no")

        # Is the Applicant's estimated gross revenue for the next 12 months expected to exceed $2 million
        self.gross_million_yes = self.driver.find_element(By.ID, "hhol_gross_million-yes")

        self.gross_million_no = self.driver.find_element(By.ID, "hhol_gross_million-no")

        # Amount Last Policy Year
        self.annual_revenue_last_policy_year = self.driver.find_element(By.ID, "annual_revenue_last_policy_year")

        # Has any application for Professional Liability Insurance made on behalf of the Applicant, any predecessors in business or present Partners EVER been declined or has the insurance ever been cancelled or non-renewed
        self.insurance_declined_yes = self.driver.find_element(By.ID, "hhol_insurance_declined-yes")

        self.insurance_declined_no = self.driver.find_element(By.ID, "hhol_insurance_declined-no")

        # Has any claim EVER been made against the Applicant or any of its employees
        self.past_claim_yes = self.driver.find_element(By.ID, "hhol_past_claim-yes")

        self.past_claim_no = self.driver.find_element(By.ID, "hhol_past_claim-no")

        # Does the Applicant have expiring coverage in place? (If retroactive coverage is desired, please submit expiring declaration page and a five-year loss run.)
        self.expiring_coverage_yes = self.driver.find_element(By.ID, "hhol_expiring_coverage-yes")

        self.expiring_coverage_no = self.driver.find_element(By.ID, "hhol_expiring_coverage-no")

        # Is the Applicant aware of ANY circumstances which may result in ANY claim against it, the entity, its predecessors in business, or any of its past or present directors, officers, or partners
        self.potential_claims_yes = self.driver.find_element(By.ID, "hhol_potential_claim-yes")

        self.potential_claims_no = self.driver.find_element(By.ID, "hhol_potential_claim-no")

        # Is the Applicant interested in Hired and Non-Owned Auto Liability coverage
        self.include_hnoa_yes = self.driver.find_element(By.ID, "hhol_include_hnoa-yes")

        self.include_hnoa_no = self.driver.find_element(By.ID, "hhol_include_hnoa-no")

        # Does the Applicant warrant that all providers/employees with driving responsibilities maintain automobile insurance that meets the minimum state requirements, AND does the Applicant access and review Motor Vehicle Reports on all such individuals as a condition of employment
        self.warrant_min_insurance_yes = self.driver.find_element(By.ID, "hhol_warrant_min_insurance-yes")

        self.warrant_min_insurance_no = self.driver.find_element(By.ID, "hhol_warrant_min_insurance-no")

        self.warrant_min_insurance_na = self.driver.find_element(By.ID, "hhol_warrant_min_insurance-na")

        return self

    def create_quote_include_HNOA(self, years_in_business, staff_count, revenue_current_year):
        PAF.Page_Elements(self).years_in_business.send_keys(years_in_business)
        PAF.Page_Elements(self).total_staff_count.send_keys(staff_count)
        PAF.Page_Elements(self).staff_type_no.click()
        PAF.Page_Elements(self).employees_licensed_yes.click()
        PAF.Page_Elements(self).background_checks_yes.click()
        PAF.Page_Elements(self).employees_screened_yes.click()
        PAF.Page_Elements(self).qa_program_yes.click()
        PAF.Page_Elements(self).incidents_procedure_yes.click()
        PAF.Page_Elements(self).employees_investigated_no.click()
        PAF.Page_Elements(self).employees_violation_no.click()
        PAF.Page_Elements(self).employees_addiction_no.click()
        PAF.Page_Elements(self).employees_revoked_no.click()
        PAF.Page_Elements(self).services_hospitals_no.click()
        PAF.Page_Elements(self).services_pediatric_no.click()
        PAF.Page_Elements(self).services_nursing_no.click()
        PAF.Page_Elements(self).perform_correctional_no.click()
        PAF.Page_Elements(self).gross_million_no.click()
        # PAF.Page_Elements(self).annual_revenue_last_policy_year.send_keys(revenue_current_year)
        PAF.Page_Elements(self).insurance_declined_no.click()
        PAF.Page_Elements(self).past_claim_no.click()
        PAF.Page_Elements(self).insurance_declined_no.click()
        PAF.Page_Elements(self).potential_claims_no.click()
        PAF.Page_Elements(self).expiring_coverage_no.click()
        PAF.Page_Elements(self).include_hnoa_yes.click()
        PAF.Page_Elements(self).warrant_min_insurance_yes.click()

    def create_quote_NO_HNOA(self, years_in_business, staff_count, revenue_current_year):
        PAF.Page_Elements(self).years_in_business.send_keys(years_in_business)
        PAF.Page_Elements(self).total_staff_count.send_keys(staff_count)
        PAF.Page_Elements(self).staff_type_no.click()
        PAF.Page_Elements(self).employees_licensed_yes.click()
        PAF.Page_Elements(self).background_checks_yes.click()
        PAF.Page_Elements(self).employees_screened_yes.click()
        PAF.Page_Elements(self).qa_program_yes.click()
        PAF.Page_Elements(self).incidents_procedure_yes.click()
        PAF.Page_Elements(self).employees_investigated_no.click()
        PAF.Page_Elements(self).employees_violation_no.click()
        PAF.Page_Elements(self).employees_addiction_no.click()
        PAF.Page_Elements(self).employees_revoked_no.click()
        PAF.Page_Elements(self).services_hospitals_no.click()
        PAF.Page_Elements(self).services_pediatric_no.click()
        PAF.Page_Elements(self).services_nursing_no.click()
        PAF.Page_Elements(self).perform_correctional_no.click()
        PAF.Page_Elements(self).gross_million_no.click()
        # PAF.Page_Elements(self).annual_revenue_last_policy_year.send_keys(revenue_current_year)
        PAF.Page_Elements(self).insurance_declined_no.click()
        PAF.Page_Elements(self).past_claim_no.click()
        PAF.Page_Elements(self).insurance_declined_no.click()
        PAF.Page_Elements(self).potential_claims_no.click()
        PAF.Page_Elements(self).expiring_coverage_no.click()
        PAF.Page_Elements(self).include_hnoa_no.click()
        PAF.Page_Elements(self).warrant_min_insurance_na.click()

    #TODO
    # Ask Dev to create ID for next button
    def click_next(self):
        next_button = self.driver.find_element(By.XPATH, "//form[@id='primary']/div[5]/a/span[2]/span/span")
        next_button.click()