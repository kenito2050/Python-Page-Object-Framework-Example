from selenium.webdriver.common.by import By

class PAF():

    def __init__(self, driver):
        self.driver = driver

    #Page Elements

    def Page_Elements(self):

        # Number of Years in Business
        self.years_in_business = self.driver.find_element(By.ID, "cryo_business_years_count")

        # Total Staff Count
        self.total_staff_count = self.driver.find_element(By.ID, "cryo_staff_count")

        # Do you sell products?
        self.sell_products_yes = self.driver.find_element(By.ID, "cryo_sell_products-yes")

        self.sell_products_no = self.driver.find_element(By.ID, "cryo_sell_products-no")

        # If “Yes”, Do you label them in your own name?
        self.label_products_yes = self.driver.find_element(By.ID, "cryo_label_products-yes")

        self.label_products_no = self.driver.find_element(By.ID, "cryo_label_products-no")

        # Total Gross Revenue:

        # Last Policy Year:
        self.last_policy_year_revenue = self.driver.find_element(By.ID, "annual_revenue_last_policy_year")

        # Does the Applicant provide any mobile cryotherapy?
        self.mobile_cryotherapy_yes = self.driver.find_element(By.ID, "cryo_mobile_cryotherapy-yes")

        self.mobile_cryotherapy_no = self.driver.find_element(By.ID, "cryo_mobile_cryotherapy-no")


        # Are criminal background checks conducted on all employees?
        self.background_checks_yes = self.driver.find_element(By.ID, "cryo_background_checks-yes")

        self.background_checks_no = self.driver.find_element(By.ID, "cryo_background_checks-no")

        # Does the Application conduct pre-employment screenings and/or any other necessary investigations and credentialing prior to hiring any staff?
        self.hiring_process_yes = self.driver.find_element(By.ID, "cryo_hiring_process-yes")

        self.hiring_process_no = self.driver.find_element(By.ID, "cryo_hiring_process-no")

        # Does the Applicant have a written/formalized risk management/quality assurance program?
        self.written_assurance_program_yes = self.driver.find_element(By.ID, "cryo_written_assurance_program-yes")

        self.written_assurance_program_no = self.driver.find_element(By.ID, "cryo_written_assurance_program-no")

        #  Does the Applicant have written procedures in place for the reporting of incidents?
        self.incident_reporting_yes = self.driver.find_element(By.ID, "cryo_incident_reporting-yes")

        self.incident_reporting_no = self.driver.find_element(By.ID, "cryo_incident_reporting-no")

        #  Do you require a certified cryotherapy operator to be present at all times during cryotherapy sessions?
        self.cryotherapy_sessions_yes = self.driver.find_element(By.ID, "cryo_cryotherapy_sessions-yes")

        self.cryotherapy_sessions_no = self.driver.find_element(By.ID, "cryo_cryotherapy_sessions-no")

        #  Do you provide dry hand and foot protection prior to use of cryotherapy equipment?
        self.cryotherapy_equipment_yes = self.driver.find_element(By.ID, "cryo_cryotherapy_equipment-yes")

        self.cryotherapy_equipment_no = self.driver.find_element(By.ID, "cryo_cryotherapy_equipment-no")

        # If the Applicant provides completely enclosed cryochambers, is dry head protection provided?
        self.dry_head_protection_yes = self.driver.find_element(By.ID, "cryo_dry_head_protection-yes")

        self.dry_head_protection_no = self.driver.find_element(By.ID, "cryo_dry_head_protection-no")

        self.dry_head_protection_no = self.driver.find_element(By.ID, "cryo_dry_head_protection-na")

        # Do you screen for medical conditions that may not be suitable for cryotherapy?
        self.cryo_medical_conditions_yes = self.driver.find_element(By.ID, "cryo_medical_conditions-yes")

        self.cryo_medical_conditions_no = self.driver.find_element(By.ID, "cryo_medical_conditions-no")

        # Do you use nitrogen and/or oxygen monitors in cryotherapy rooms?
        self.oxygen_monitors_yes = self.driver.find_element(By.ID, "cryo_oxygen_monitors-yes")

        self.oxygen_monitors_no = self.driver.find_element(By.ID, "cryo_oxygen_monitors-no")

        # Do you limit cryotherapy sessions to the manufacturer recommended time limit?
        self.cryotherapy_time_limit_yes = self.driver.find_element(By.ID, "cryo_cryotherapy_time_limit-yes")

        self.cryotherapy_time_limit_no = self.driver.find_element(By.ID, "cryo_cryotherapy_time_limit-no")

        # Do you ensure that patients are able to exit cryotherapy machines without assistance?
        self.patients_exit_cryotherapy_yes = self.driver.find_element(By.ID, "cryo_patients_exit_cryotherapy-yes")

        self.patients_exit_cryotherapy_no = self.driver.find_element(By.ID, "cryo_patients_exit_cryotherapy-no")

        self.patients_exit_cryotherapy_na = self.driver.find_element(By.ID, "cryo_patients_exit_cryotherapy-na")

        # Do you require all patients to sign an informed consent from for cryotherapy?
        self.patients_sign_cryotherapy_yes = self.driver.find_element(By.ID, "cryo_patients_sign_cryotherapy-yes")

        self.patients_sign_cryotherapy_no = self.driver.find_element(By.ID, "cryo_patients_sign_cryotherapy-no")

        # Do you regularly inspect and calibrate cryotherapy machines as recommended by the manufacturer?
        self.machines_inspect_yes = self.driver.find_element(By.ID, "cryo_machines_inspect-yes")

        self.machines_inspect_no = self.driver.find_element(By.ID, "cryo_machines_inspect-no")

        # Do you allow staff or patients to provide cryotherapy to themselves?
        self.patients_self_cryotherapy_yes = self.driver.find_element(By.ID, "cryo_patients_self_cryotherapy-yes")

        self.patients_self_cryotherapy_no = self.driver.find_element(By.ID, "cryo_patients_self_cryotherapy-no")

        # If services are provided to minors, do you obtain written consent from a parent or guardian?
        self.consent_from_guardian_yes = self.driver.find_element(By.ID, "cryo_consent_from_guardian-yes")

        self.consent_from_guardian_no = self.driver.find_element(By.ID, "cryo_consent_from_guardian-no")

        self.consent_from_guardian_na = self.driver.find_element(By.ID, "cryo_consent_from_guardian-na")

        # Has the Applicant or any of its providers/employees ever been/had:

        # The subject in disciplinary or investigative proceedings or reprimanded by a governmental or administrative agency, hospital or professional association?
        self.disciplinary_investigative_reprimand_yes = self.driver.find_element(By.ID, "cryo_disciplinary_investigative_reprimand-yes")

        self.disciplinary_investigative_reprimand_no = self.driver.find_element(By.ID, "cryo_disciplinary_investigative_reprimand-no")

        # Convicted of an act committed in violation of any law or ordinance other than traffic offenses?
        self.convict_act_yes = self.driver.find_element(By.ID, "cryo_convict_act-yes")

        self.convict_act_no = self.driver.find_element(By.ID, "cryo_convict_act-no")

        # Treated for alcoholism or drug addiction?
        self.alcohol_addiction_yes = self.driver.find_element(By.ID, "cryo_alcohol_addiction-yes")

        self.alcohol_addiction_no = self.driver.find_element(By.ID, "cryo_alcohol_addiction-no")

        # Any state professional license or license to prescribe or dispense narcotics refused, suspended, revoked, renewal refused or accepted only on special terms, or ever voluntarily surrendered?
        self.license_special_terms_yes = self.driver.find_element(By.ID, "cryo_license_special_terms-yes")

        self.license_special_terms_no = self.driver.find_element(By.ID, "cryo_license_special_terms-no")

        # Do you have any steam rooms, soaking pools or showers:
        self.steam_rooms_yes = self.driver.find_element(By.ID, "cryo_steam_rooms-yes")

        self.steam_rooms_no = self.driver.find_element(By.ID, "cryo_steam_rooms-no")

        # If the Applicant provides infrared saunas, are clients allowed to receive “hot then cold” therapy?
        self.infrared_saunas_yes = self.driver.find_element(By.ID, "cryo_infrared_saunas-yes")

        self.infrared_saunas_no = self.driver.find_element(By.ID, "cryo_infrared_saunas-no")

        self.infrared_saunas_na = self.driver.find_element(By.ID, "cryo_infrared_saunas-na")

        # Is 15% or more of revenue derived from sources other than cryotherapy services?
        self.revenue_sources_yes = self.driver.find_element(By.ID, "cryo_revenue_sources-yes")

        self.revenue_sources_no = self.driver.find_element(By.ID, "cryo_revenue_sources-no")

        # Do you offer any services to professional and/or collegiate athletes?
        self.collegiate_athletes_services_yes = self.driver.find_element(By.ID, "cryo_collegiate_athletes_services-yes")

        self.collegiate_athletes_services_no = self.driver.find_element(By.ID, "cryo_collegiate_athletes_services-no")

        # Have you or any current partners or predecessors in business EVER been declined, cancelled or non-renewed for Professional Liability Insurance?
        self.professional_liability_insurance_yes = self.driver.find_element(By.ID, "cryo_professional_liability_insurance-yes")

        self.professional_liability_insurance_no = self.driver.find_element(By.ID, "cryo_professional_liability_insurance-no")

        # Has any claim EVER been made against the Applicant or any of its employees?
        self.applicant_claims_yes = self.driver.find_element(By.ID, "cryo_applicant_claims-yes")

        self.applicant_claims_no = self.driver.find_element(By.ID, "cryo_applicant_claims-no")

        # Is the applicant aware of any ANY circumstances which may result in a professional liability claim against it, its predecessors in business, or any of its current or former directors, officers, employees or partners?
        self.professional_liability_claim_yes = self.driver.find_element(By.ID, "cryo_professional_liability_claim-yes")

        self.professional_liability_claim_no = self.driver.find_element(By.ID, "cryo_professional_liability_claim-no")

        # Does the Applicant have expiring Professional Liability coverage in place?
        self.expiring_coverages_yes = self.driver.find_element(By.ID, "cryo_expiring_coverages-yes")

        self.expiring_coverages_no = self.driver.find_element(By.ID, "cryo_expiring_coverages-no")

        return self

    def create_quote_include_No_SMML_Sell_Products_Yes(self, years_in_business, staff_count, revenue_current_year):
        PAF.Page_Elements(self).years_in_business.send_keys(years_in_business)
        PAF.Page_Elements(self).total_staff_count.send_keys(staff_count)
        PAF.Page_Elements(self).sell_products_yes.click()
        PAF.Page_Elements(self).label_products_no.click()
        PAF.Page_Elements(self).mobile_cryotherapy_no.click()
        PAF.Page_Elements(self).background_checks_yes.click()
        PAF.Page_Elements(self).hiring_process_yes.click()
        PAF.Page_Elements(self).written_assurance_program_yes.click()
        PAF.Page_Elements(self).incident_reporting_yes.click()
        PAF.Page_Elements(self).cryotherapy_sessions_yes.click()
        PAF.Page_Elements(self).cryotherapy_equipment_yes.click()
        PAF.Page_Elements(self).dry_head_protection_yes.click()
        PAF.Page_Elements(self).cryo_medical_conditions_yes.click()
        PAF.Page_Elements(self).oxygen_monitors_yes.click()
        PAF.Page_Elements(self).cryotherapy_time_limit_yes.click()
        PAF.Page_Elements(self).patients_exit_cryotherapy_yes.click()
        PAF.Page_Elements(self).patients_sign_cryotherapy_yes.click()
        PAF.Page_Elements(self).machines_inspect_yes.click()
        PAF.Page_Elements(self).patients_self_cryotherapy_yes.click()
        PAF.Page_Elements(self).consent_from_guardian_yes.click()
        PAF.Page_Elements(self).disciplinary_investigative_reprimand_no.click()
        PAF.Page_Elements(self).convict_act_no.click()
        PAF.Page_Elements(self).alcohol_addiction_no.click()
        PAF.Page_Elements(self).license_special_terms_no.click()
        PAF.Page_Elements(self).steam_rooms_no.click()
        PAF.Page_Elements(self).infrared_saunas_no.click()
        PAF.Page_Elements(self).revenue_sources_no.click()
        PAF.Page_Elements(self).collegiate_athletes_services_no.click()
        PAF.Page_Elements(self).professional_liability_insurance_no.click()
        PAF.Page_Elements(self).applicant_claims_no.click()
        PAF.Page_Elements(self).professional_liability_claim_no.click()
        PAF.Page_Elements(self).expiring_coverages_no.click()

    def create_quote_include_SMML_Sell_Products_Yes(self, years_in_business, staff_count, revenue_current_year):
        PAF.Page_Elements(self).years_in_business.send_keys(years_in_business)
        PAF.Page_Elements(self).total_staff_count.send_keys(staff_count)
        PAF.Page_Elements(self).sell_products_yes.click()
        PAF.Page_Elements(self).label_products_no.click()
        PAF.Page_Elements(self).mobile_cryotherapy_no.click()
        PAF.Page_Elements(self).background_checks_yes.click()
        PAF.Page_Elements(self).hiring_process_yes.click()
        PAF.Page_Elements(self).written_assurance_program_yes.click()
        PAF.Page_Elements(self).incident_reporting_yes.click()
        PAF.Page_Elements(self).cryotherapy_sessions_yes.click()
        PAF.Page_Elements(self).cryotherapy_equipment_yes.click()
        PAF.Page_Elements(self).dry_head_protection_yes.click()
        PAF.Page_Elements(self).cryo_medical_conditions_yes.click()
        PAF.Page_Elements(self).oxygen_monitors_yes.click()
        PAF.Page_Elements(self).cryotherapy_time_limit_yes.click()
        PAF.Page_Elements(self).patients_exit_cryotherapy_yes.click()
        PAF.Page_Elements(self).patients_sign_cryotherapy_yes.click()
        PAF.Page_Elements(self).machines_inspect_yes.click()
        PAF.Page_Elements(self).patients_self_cryotherapy_yes.click()
        PAF.Page_Elements(self).consent_from_guardian_yes.click()
        PAF.Page_Elements(self).disciplinary_investigative_reprimand_no.click()
        PAF.Page_Elements(self).convict_act_no.click()
        PAF.Page_Elements(self).alcohol_addiction_no.click()
        PAF.Page_Elements(self).license_special_terms_no.click()
        PAF.Page_Elements(self).steam_rooms_no.click()
        PAF.Page_Elements(self).infrared_saunas_no.click()
        PAF.Page_Elements(self).revenue_sources_no.click()
        PAF.Page_Elements(self).collegiate_athletes_services_no.click()
        PAF.Page_Elements(self).professional_liability_insurance_no.click()
        PAF.Page_Elements(self).applicant_claims_no.click()
        PAF.Page_Elements(self).professional_liability_claim_no.click()
        PAF.Page_Elements(self).expiring_coverages_no.click()

    def create_quote_include_No_SMML_Sell_Products_No(self, years_in_business, staff_count, revenue_current_year):
        PAF.Page_Elements(self).years_in_business.send_keys(years_in_business)
        PAF.Page_Elements(self).total_staff_count.send_keys(staff_count)
        PAF.Page_Elements(self).sell_products_no.click()
        PAF.Page_Elements(self).mobile_cryotherapy_no.click()
        PAF.Page_Elements(self).background_checks_yes.click()
        PAF.Page_Elements(self).hiring_process_yes.click()
        PAF.Page_Elements(self).written_assurance_program_yes.click()
        PAF.Page_Elements(self).incident_reporting_yes.click()
        PAF.Page_Elements(self).cryotherapy_sessions_yes.click()
        PAF.Page_Elements(self).cryotherapy_equipment_yes.click()
        PAF.Page_Elements(self).dry_head_protection_yes.click()
        PAF.Page_Elements(self).cryo_medical_conditions_yes.click()
        PAF.Page_Elements(self).oxygen_monitors_yes.click()
        PAF.Page_Elements(self).cryotherapy_time_limit_yes.click()
        PAF.Page_Elements(self).patients_exit_cryotherapy_yes.click()
        PAF.Page_Elements(self).patients_sign_cryotherapy_yes.click()
        PAF.Page_Elements(self).machines_inspect_yes.click()
        PAF.Page_Elements(self).patients_self_cryotherapy_yes.click()
        PAF.Page_Elements(self).consent_from_guardian_yes.click()
        PAF.Page_Elements(self).disciplinary_investigative_reprimand_no.click()
        PAF.Page_Elements(self).convict_act_no.click()
        PAF.Page_Elements(self).alcohol_addiction_no.click()
        PAF.Page_Elements(self).license_special_terms_no.click()
        PAF.Page_Elements(self).steam_rooms_no.click()
        PAF.Page_Elements(self).infrared_saunas_no.click()
        PAF.Page_Elements(self).revenue_sources_no.click()
        PAF.Page_Elements(self).collegiate_athletes_services_no.click()
        PAF.Page_Elements(self).professional_liability_insurance_no.click()
        PAF.Page_Elements(self).applicant_claims_no.click()
        PAF.Page_Elements(self).professional_liability_claim_no.click()
        PAF.Page_Elements(self).expiring_coverages_no.click()

    def create_quote_include_SMML_Sell_Products_No(self, years_in_business, staff_count, revenue_current_year):
        PAF.Page_Elements(self).years_in_business.send_keys(years_in_business)
        PAF.Page_Elements(self).total_staff_count.send_keys(staff_count)
        PAF.Page_Elements(self).sell_products_no.click()
        PAF.Page_Elements(self).mobile_cryotherapy_no.click()
        PAF.Page_Elements(self).background_checks_yes.click()
        PAF.Page_Elements(self).hiring_process_yes.click()
        PAF.Page_Elements(self).written_assurance_program_yes.click()
        PAF.Page_Elements(self).incident_reporting_yes.click()
        PAF.Page_Elements(self).cryotherapy_sessions_yes.click()
        PAF.Page_Elements(self).cryotherapy_equipment_yes.click()
        PAF.Page_Elements(self).dry_head_protection_yes.click()
        PAF.Page_Elements(self).cryo_medical_conditions_yes.click()
        PAF.Page_Elements(self).oxygen_monitors_yes.click()
        PAF.Page_Elements(self).cryotherapy_time_limit_yes.click()
        PAF.Page_Elements(self).patients_exit_cryotherapy_yes.click()
        PAF.Page_Elements(self).patients_sign_cryotherapy_yes.click()
        PAF.Page_Elements(self).machines_inspect_yes.click()
        PAF.Page_Elements(self).patients_self_cryotherapy_yes.click()
        PAF.Page_Elements(self).consent_from_guardian_yes.click()
        PAF.Page_Elements(self).disciplinary_investigative_reprimand_no.click()
        PAF.Page_Elements(self).convict_act_no.click()
        PAF.Page_Elements(self).alcohol_addiction_no.click()
        PAF.Page_Elements(self).license_special_terms_no.click()
        PAF.Page_Elements(self).steam_rooms_no.click()
        PAF.Page_Elements(self).infrared_saunas_no.click()
        PAF.Page_Elements(self).revenue_sources_no.click()
        PAF.Page_Elements(self).collegiate_athletes_services_no.click()
        PAF.Page_Elements(self).professional_liability_insurance_no.click()
        PAF.Page_Elements(self).applicant_claims_no.click()
        PAF.Page_Elements(self).professional_liability_claim_no.click()
        PAF.Page_Elements(self).expiring_coverages_no.click()

    #TODO
    # Ask Dev to create ID for next button
    def click_next(self):
        next_button = self.driver.find_element(By.XPATH, "//form[@id='primary']/div[5]/a/span[2]/span/span")
        next_button.click()