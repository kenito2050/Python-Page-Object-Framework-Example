from selenium.webdriver.common.by import By

class PAF():

    def __init__(self, driver):
        self.driver = driver

    #Page Elements

    def Page_Elements(self):

        # Current or prospective PSIC insured?
        self.existing_insured_yes = self.driver.find_element(By.ID, "med_ncmic_existing_insured-yes")

        self.existing_insured_no = self.driver.find_element(By.ID, "med_ncmic_existing_insured-no")

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

        self.utilize_cpt_manual_yes = self.driver.find_element(By.ID, "med_ncmic_utilize_cpt_manual-yes")

        self.utilize_cpt_manual_no = self.driver.find_element(By.ID, "med_ncmic_utilize_cpt_manual-no")

        # Do Your billings from federal and state health care programs, such as Medicare and Medicaid, exceed an average of $2,000,000 per physician in Your group?

        self.billings_exceed_two_million_yes = self.driver.find_element(By.ID, "med_ncmic_billings_exceed_one_million-yes")

        self.billings_exceed_two_million_no = self.driver.find_element(By.ID, "med_ncmic_billings_exceed_one_million-no")

        # Have You or any physician in Your group ever been audited or investigated, or received a request for records or other documentation by or on behalf of a commercial payer or government entity?

        self.audited_investigated_yes = self.driver.find_element(By.ID, "med_ncmic_audited_investigated-yes")

        self.audited_investigated_no = self.driver.find_element(By.ID, "med_ncmic_audited_investigated-no")

        # Have You or any physician in Your group ever been placed on pre-payment review with regard to Medicare/Medicaid billing practices or utilization of Medicare/Medicaid services?

        self.audited_investigated_medicare_yes = self.driver.find_element(By.ID, "med_ncmic_audited_investigated_medicare-yes")

        self.audited_investigated_medicare_no = self.driver.find_element(By.ID, "med_ncmic_audited_investigated_medicare-no")

        # Have You or any physician in Your group ever had to refund amounts to Public and/or Private payers in excess of $10,000?

        self.refund_excess_10_thousand_yes = self.driver.find_element(By.ID, "med_ncmic_refund_excess_10_thousand-yes")

        self.refund_excess_10_thousand_no = self.driver.find_element(By.ID, "med_ncmic_refund_excess_10_thousand-no")

        # Have You or any physician in Your group ever been accused of billing errors by any government agency or commercial payer?

        self.accused_billing_errors_yes = self.driver.find_element(By.ID, "med_ncmic_accused_billing_errors-yes")

        self.accused_billing_errors_no = self.driver.find_element(By.ID, "med_ncmic_accused_billing_errors-no")

        # Have You or any physician in Your Group ever:

        # Been investigated or sanctioned by a state medical licensing board?

        self.investigated_sanctioned_yes = self.driver.find_element(By.ID, "med_ncmic_investigated_sanctioned-yes")

        self.investigated_sanctioned_no = self.driver.find_element(By.ID, "med_ncmic_investigated_sanctioned-no")

        # Been involved in Stark/anti-kickback investigation?

        self.anti_kickback_investigation_yes = self.driver.find_element(By.ID, "med_ncmic_anti_kickback_investigation-yes")

        self.anti_kickback_investigation_no = self.driver.find_element(By.ID, "med_ncmic_anti_kickback_investigation-no")

        # Been sued or deselected from a private commercial payer?

        self.sued_deselected_payer_yes = self.driver.find_element(By.ID, "med_ncmic_sued_deselected_payer-yes")

        self.sued_deselected_payer_no = self.driver.find_element(By.ID, "med_ncmic_sued_deselected_payer-no")

        # Been investigated for EMTALA violations?

        self.investigated_emtala_yes = self.driver.find_element(By.ID, "med_ncmic_investigated_emtala-yes")

        self.investigated_emtala_no = self.driver.find_element(By.ID, "med_ncmic_investigated_emtala-no")

        # Been investigated for HIPAA violations?

        self.investigated_hipaa_yes = self.driver.find_element(By.ID, "med_ncmic_investigated_hipaa-yes")

        self.investigated_hipaa_no = self.driver.find_element(By.ID, "med_ncmic_investigated_hipaa-no")

        # Voluntarily disclosed any billing errors or irregular billing practices?

        self.voluntary_disclosure_yes = self.driver.find_element(By.ID, "med_ncmic_voluntary_disclosure-yes")

        self.voluntary_disclosure_no = self.driver.find_element(By.ID, "med_ncmic_voluntary_disclosure-no")

        # Have You ever been non-renewed, placed on extension, or declined from similar regulatory/billing errors insurance?

        self.non_renewed_extention_yes = self.driver.find_element(By.ID, "med_ncmic_non_renewed_extention-yes")

        self.non_renewed_extention_no = self.driver.find_element(By.ID, "med_ncmic_non_renewed_extention-no")

        # Are You or any individual proposed for this insurance been aware of any acts, errors, omissions, facts, circumstances, allegations, situations, events or incidents, that could give rise to a regulatory investigation, regulatory action, or demand for restitution?

        self.regulatory_investigation_yes = self.driver.find_element(By.ID, "med_ncmic_regulatory_investigation-yes")

        self.regulatory_investigation_no = self.driver.find_element(By.ID, "med_ncmic_regulatory_investigation-no")


        # Have You ever been non-renewed, placed on extension, or declined for similar privacy/security liability coverage?

        # self.non_renewed_extention_cyb_yes = self.driver.find_element(By.ID, "med_ncmic_non_renewed_extention-yes")
        #
        # self.non_renewed_extention_cyb_no = self.driver.find_element(By.ID, "med_ncmic_non_renewed_extention-no")

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


    #TODO
    # Ask Dev to create ID for next button
    def click_next(self):
        next_button = self.driver.find_element(By.XPATH, "//form[@id='primary']/div[2]/div[2]/div[3]/a/span[2]/span/span")
        next_button.click()