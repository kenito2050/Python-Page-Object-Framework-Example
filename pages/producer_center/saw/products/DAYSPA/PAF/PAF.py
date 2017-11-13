from selenium.webdriver.common.by import By

class PAF():

    def __init__(self, driver):
        self.driver = driver

    #Page Elements

    def Page_Elements(self):

        # Number of Years in Business:
        self.business_years_count = self.driver.find_element(By.ID, "business-years-count")

        # Do you sell products?
        self.sell_products_yes = self.driver.find_element(By.ID, "sell_products-yes")

        self.sell_products_no = self.driver.find_element(By.ID, "sell_products-no")

        # Estimated number of procedures in the next 12 months?
        self.procedure_count = self.driver.find_element(By.ID, "procedure_count")

        # Total Gross Revenue:

        # Last Policy Year
        self.annual_revenue_last_policy_year = self.driver.find_element(By.ID, "annual_revenue_last_policy_year")

        # Next 12 Months (estimate):
        self.annual_revenue_next_12_months = self.driver.find_element(By.ID, "annual_revenue_next_12_months")

        # Are criminal background checks conducted on all employees?
        self.criminal_check_yes = self.driver.find_element(By.ID, "criminal_check-yes")

        self.criminal_check_no = self.driver.find_element(By.ID, "criminal_check-no")

        # Does the Application conduct pre-employment screenings and/or any other necessary investigations and credentialing prior to hiring any staff?
        self.pre_employment_screen_investigation_credentialing_yes = self.driver.find_element(By.ID, "pre_employment_screen_investigation_credentialing-yes")

        self.pre_employment_screen_investigation_credentialing_no = self.driver.find_element(By.ID, "pre_employment_screen_investigation_credentialing-no")

        # Does the Applicant have a written/formalized risk management/quality assurance program

        self.risk_management_quality_assurance_yes = self.driver.find_element(By.ID, "risk_management_quality_assurance-yes")

        self.risk_management_quality_assurance_no = self.driver.find_element(By.ID, "risk_management_quality_assurance-yes")

        # Does the Applicant have written procedures in place for the reporting of incidents

        self.incident_report_yes = self.driver.find_element(By.ID, "incident_report-yes")

        self.incident_report_no = self.driver.find_element(By.ID, "incident_report-no")


        # Has the Applicant or any of its providers/employees ever been/had:

        # The subject in disciplinary or investigative proceedings or reprimanded by a governmental or administrative agency, hospital or professional association?

        self.dayspa_disciplinary_investigative_reprimand_yes = self.driver.find_element(By.ID, "dayspa_disciplinary_investigative_reprimand-yes")

        self.dayspa_disciplinary_investigative_reprimand_no = self.driver.find_element(By.ID, "dayspa_disciplinary_investigative_reprimand-no")

        # Convicted of an act committed in violation of any law or ordinance other than traffic offenses?

        self.dayspa_convict_act_yes = self.driver.find_element(By.ID, "dayspa_convict_act-yes")

        self.dayspa_convict_act_no = self.driver.find_element(By.ID, "dayspa_convict_act-no")

        # Treated for alcoholism or drug addiction?

        self.dayspa_alcohol_drug_yes = self.driver.find_element(By.ID, "dayspa_alcohol_drug-yes")

        self.dayspa_alcohol_drug_no = self.driver.find_element(By.ID, "dayspa_alcohol_drug-no")

        # Any state professional license or license to prescribe or dispense narcotics refused, suspended, revoked, renewal refused or accepted only on special terms, or ever voluntarily surrendered?

        self.dayspa_license_special_terms_yes = self.driver.find_element(By.ID, "dayspa_license_special_terms-yes")

        self.dayspa_license_special_terms_no = self.driver.find_element(By.ID, "dayspa_license_special_terms-no")


        # Do you have any:

        # Saunas/Steam Rooms?

        self.dayspa_sauna_steam_room_yes = self.driver.find_element(By.ID, "dayspa_sauna_steam_room-yes")

        self.dayspa_sauna_steam_room_no = self.driver.find_element(By.ID, "dayspa_sauna_steam_room-no")

        # Soaking pools?

        self.dayspa_soaking_pools_yes = self.driver.find_element(By.ID, "dayspa_soaking_pools-yes")

        self.dayspa_soaking_pools_no = self.driver.find_element(By.ID, "dayspa_soaking_pools-no")

        # Showers?
        self.dayspa_showers_yes = self.driver.find_element(By.ID, "dayspa_showers-yes")

        self.dayspa_showers_no = self.driver.find_element(By.ID, "dayspa_showers-no")

        # Do you offer any Cryotherapy services
        self.dayspa_cryotherapy_yes = self.driver.find_element(By.ID, "dayspa_cryotherapy-yes")

        self.dayspa_cryotherapy_no = self.driver.find_element(By.ID, "dayspa_cryotherapy-no")

        # Do you provide any tanning services
        self.dayspa_tanning_service_yes = self.driver.find_element(By.ID, "dayspa_tanning_service-yes")

        self.dayspa_tanning_service_no = self.driver.find_element(By.ID, "dayspa_tanning_service-no")

        # Do you provide any laser treatment, injections (including but not limited to dermal fillers, Botox or other injectable body/face reduction services), medical dermabrasion, or chemical peels with greater than 30% chemical solution strength?
        self.dayspa_chemical_solution_strength_exceed_30_percent_yes = self.driver.find_element(By.ID, "dayspa_chemical_solution_strength_exceed_30_percent-yes")

        self.dayspa_chemical_solution_strength_exceed_30_percent_no = self.driver.find_element(By.ID, "dayspa_chemical_solution_strength_exceed_30_percent-no")

        # Have you or any current partners or predecessors in business EVER been declined, cancelled or non-renewed for Professional Liability Insurance?
        self.dayspa_professional_liability_insurance_yes = self.driver.find_element(By.ID, "dayspa_professional_liability_insurance-yes")

        self.dayspa_professional_liability_insurance_no = self.driver.find_element(By.ID, "dayspa_professional_liability_insurance-no")

        # Have you or any current partners or predecessors in business EVER been declined, cancelled or non-renewed for Professional Liability Insurance?
        self.dayspa_claim_yes = self.driver.find_element(By.ID, "dayspa_claim-yes")

        self.dayspa_claim_no = self.driver.find_element(By.ID, "dayspa_claim-no")

        # Is the applicant aware of any ANY circumstances which may result in a professional liability claim against it, its predecessors in business, or any of its current or former directors, officers, employees or partners?
        self.dayspa_professional_liability_claim_yes = self.driver.find_element(By.ID, "dayspa_professional_liability_claim-yes")

        self.dayspa_professional_liability_claim_no = self.driver.find_element(By.ID, "dayspa_professional_liability_claim-no")

        # Does the Applicant have expiring Professional Liability coverage in place?
        self.dayspa_professional_liability_expiring_yes = self.driver.find_element(By.ID, "dayspa_professional_liability_expiring-yes")

        self.dayspa_professional_liability_expiring_no = self.driver.find_element(By.ID, "dayspa_professional_liability_expiring-no")

        # Field Displays if Selecting Yes to Above Question
        # If the expiring policy is claims-made, what is the retroactive date?

        self.dayspa_expiring_poliy_retroactive_date = self.driver.find_element(By.ID, "dayspa_expiring_poliy_retroactive_date")

        return self

    def Hidden_Page_Elements(self):

        # Only Displays when Do You Sell Products = Yes

        # Do you label them in your own name
        self.label_products_yes = self.driver.find_element(By.ID, "label_products-yes")
        self.label_products_no = self.driver.find_element(By.ID, "label_products-no")

        return self

    def create_quote_No_Product_Liability(self, years_in_business, number_procedures, revenue_last_year, revenue_upcoming_year, effective_date_formatted):

        PAF.Page_Elements(self).business_years_count.send_keys(years_in_business)
        PAF.Page_Elements(self).sell_products_no.click()
        PAF.Page_Elements(self).procedure_count.send_keys(number_procedures)
        PAF.Page_Elements(self).annual_revenue_last_policy_year.send_keys(revenue_last_year)
        PAF.Page_Elements(self).annual_revenue_next_12_months.send_keys(revenue_upcoming_year)
        PAF.Page_Elements(self).criminal_check_yes.click()
        PAF.Page_Elements(self).pre_employment_screen_investigation_credentialing_yes.click()
        PAF.Page_Elements(self).risk_management_quality_assurance_yes.click()
        PAF.Page_Elements(self).incident_report_yes.click()
        PAF.Page_Elements(self).dayspa_disciplinary_investigative_reprimand_no.click()
        PAF.Page_Elements(self).dayspa_convict_act_no.click()
        PAF.Page_Elements(self).dayspa_alcohol_drug_no.click()
        PAF.Page_Elements(self).dayspa_license_special_terms_no.click()
        PAF.Page_Elements(self).dayspa_sauna_steam_room_no.click()
        PAF.Page_Elements(self).dayspa_soaking_pools_no.click()
        PAF.Page_Elements(self).dayspa_showers_no.click()
        PAF.Page_Elements(self).dayspa_cryotherapy_no.click()
        PAF.Page_Elements(self).dayspa_tanning_service_no.click()
        PAF.Page_Elements(self).dayspa_chemical_solution_strength_exceed_30_percent_no.click()
        PAF.Page_Elements(self).dayspa_professional_liability_insurance_no.click()
        PAF.Page_Elements(self).dayspa_claim_no.click()
        PAF.Page_Elements(self).dayspa_professional_liability_claim_no.click()
        PAF.Page_Elements(self).dayspa_professional_liability_expiring_yes.click()
        PAF.Page_Elements(self).dayspa_expiring_poliy_retroactive_date.send_keys(effective_date_formatted)

    def create_quote_Product_Liability(self, years_in_business, number_procedures, revenue_last_year, revenue_upcoming_year, effective_date_formatted):

        PAF.Page_Elements(self).business_years_count.send_keys(years_in_business)
        PAF.Page_Elements(self).sell_products_yes.click()
        PAF.Hidden_Page_Elements(self).label_products_no.click()
        PAF.Page_Elements(self).procedure_count.send_keys(number_procedures)
        PAF.Page_Elements(self).annual_revenue_last_policy_year.send_keys(revenue_last_year)
        PAF.Page_Elements(self).annual_revenue_next_12_months.send_keys(revenue_upcoming_year)
        PAF.Page_Elements(self).criminal_check_yes.click()
        PAF.Page_Elements(self).pre_employment_screen_investigation_credentialing_yes.click()
        PAF.Page_Elements(self).risk_management_quality_assurance_yes.click()
        PAF.Page_Elements(self).incident_report_yes.click()
        PAF.Page_Elements(self).dayspa_disciplinary_investigative_reprimand_no.click()
        PAF.Page_Elements(self).dayspa_convict_act_no.click()
        PAF.Page_Elements(self).dayspa_alcohol_drug_no.click()
        PAF.Page_Elements(self).dayspa_license_special_terms_no.click()
        PAF.Page_Elements(self).dayspa_sauna_steam_room_no.click()
        PAF.Page_Elements(self).dayspa_soaking_pools_no.click()
        PAF.Page_Elements(self).dayspa_showers_no.click()
        PAF.Page_Elements(self).dayspa_cryotherapy_no.click()
        PAF.Page_Elements(self).dayspa_tanning_service_no.click()
        PAF.Page_Elements(self).dayspa_chemical_solution_strength_exceed_30_percent_no.click()
        PAF.Page_Elements(self).dayspa_professional_liability_insurance_no.click()
        PAF.Page_Elements(self).dayspa_claim_no.click()
        PAF.Page_Elements(self).dayspa_professional_liability_claim_no.click()
        PAF.Page_Elements(self).dayspa_professional_liability_expiring_yes.click()
        PAF.Page_Elements(self).dayspa_expiring_poliy_retroactive_date.send_keys(effective_date_formatted)


    #TODO
    # Ask Dev to create ID for next button
    def click_next(self):
        next_button = self.driver.find_element(By.XPATH, "//form[@id='primary']/div[3]/div[3]/a/span[2]/span/span")
        next_button.click()