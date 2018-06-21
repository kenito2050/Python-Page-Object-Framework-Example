from selenium.webdriver.common.by import By

class PAF():

    def __init__(self, driver):
        self.driver = driver

    #Page Elements

    def Page_Elements(self):

        # Return to Admin Link
        self.return_to_Admin = self.driver.find_element(By.LINK_TEXT, "Return to Admin Interface")

        # Number of Years in Business
        self.years_in_business = self.driver.find_element(By.ID, "years_in_business")

        # Legal Structure

        # Corporation
        self.legal_structure_corporation = self.driver.find_element(By.ID, "corporation")

        # Individual Proprietor
        self.legal_structure_individual = self.driver.find_element(By.ID, "Individual")

        # Limited Liabilty Company
        self.legal_structure_llc = self.driver.find_element(By.ID, "Limited Liability Company")

        # Paternship / Joint Venture
        self.legal_structure_partnership = self.driver.find_element(By.ID, "Partnership or Joint Venture")

        # Total annual revenue for Property Management / Leasing Services:
        self.annual_revenue = self.driver.find_element(By.ID, "rpm_annual_revenue")

        # Most Recent Fiscal Year End Revenues:
        self.recent_revenue = self.driver.find_element(By.ID, "rpm_recent_revenue")

        # Is E&O coverage being sought for services other than Property Management, Leasing and Owner Representation Services?
        self.eo_other_services_yes = self.driver.find_element(By.ID, "rpm_eo_other_services-yes")

        self.eo_other_services_no = self.driver.find_element(By.ID, "rpm_eo_other_services-no")

        # Does the Applicant own more than 25% of the properties it manages/leases?
        self.own_twenty_five_percent_yes = self.driver.find_element(By.ID, "rpm_own_twenty_five_percent-yes")

        self.own_twenty_five_percent_no = self.driver.find_element(By.ID, "rpm_own_twenty_five_percent-no")

        # Have any claims, suits, or demands been made against the Applicant, a predecessor firm, or any of its past or present principals, partners, officers, or employees within the past five (5) years?
        self.past_claims_yes = self.driver.find_element(By.ID,"rpm_past_claims-yes")

        self.past_claims_no = self.driver.find_element(By.ID,"rpm_past_claims-no")

        # Is the Applicant aware of any claim arising from an automobile accident involving an employee who was driving during the course of providing services on behalf of the Applicant?
        self.aware_auto_claims_yes = self.driver.find_element(By.ID,"rpm_aware_auto_claims-yes")

        self.aware_auto_claims_no = self.driver.find_element(By.ID,"rpm_aware_auto_claims-no")

        # After inquiry with all principals, partners and officers, is the Applicant aware of any injury, dispute, error, omission, act, circumstance or fact could result in an E&O claim or General Liability claim?
        self.aware_eo_claims_yes = self.driver.find_element(By.ID,"rpm_aware_eo_claims-yes")

        self.aware_eo_claims_no = self.driver.find_element(By.ID,"rpm_aware_eo_claims-no")

        # For any property managed by the Applicant, does the Applicant always confirm that property owners carry General Liability Insurance?
        self.confirm_gl_insurance_yes = self.driver.find_element(By.ID,"rpm_confirm_gl_insurance-yes")

        self.confirm_gl_insurance_no = self.driver.find_element(By.ID,"rpm_confirm_gl_insurance-no")

        # Does the Applicant have written policies in place designed to prevent Fair Housing claims?
        self.written_policies_yes = self.driver.find_element(By.ID,"rpm_written_policies-yes")

        self.written_policies_no = self.driver.find_element(By.ID,"rpm_written_policies-no")

        # Number of Residential Units Managed/Owned
        self.number_residential_units = self.driver.find_element(By.ID,"rpm_number_residential_units")

        # Commercial square footage Managed/Owned
        self.commercial_square_footage = self.driver.find_element(By.ID,"rpm_commercial_square_footage")

        # total units
        self.total_units = self.driver.find_element(By.ID,"rpm_total_units")

        # If your applicant stores personal information on portable devices, including laptops, cell phones, PDAs, back-up tapes, USB thumb drivers and external hard drives, is such data encrypted to industry standards?
        self.data_encrypted_yes = self.driver.find_element(By.ID,"rpm_data_encrypted-yes")

        self.data_encrypted_no = self.driver.find_element(By.ID,"rpm_data_encrypted-no")

        self.data_encrypted_na = self.driver.find_element(By.ID,"rpm_data_encrypted-na")

        # Does the Applicant use anti-virus software and firewall protection on all desktops, portable devices and mission critical servers, and is it updated in accordance with the software provider’s recommendations
        self.anti_virus_software_yes = self.driver.find_element(By.ID,"rpm_anti_virus_software-yes")

        self.anti_virus_software_no = self.driver.find_element(By.ID,"rpm_anti_virus_software-no")

        # If “Yes”, is it updated in accordance with the software provider’s recommendations?
        self.software_updated_yes = self.driver.find_element(By.ID,"rpm_software_updated-yes")

        self.software_updated_no = self.driver.find_element(By.ID,"rpm_software_updated-no")

        # Are you (or your credit card point of sale vendor, if applicable) PCI-DSS Compliant?
        self.pci_dss_compliant_yes = self.driver.find_element(By.ID,"rpm_pci_dss_compliant-yes")

        self.pci_dss_compliant_no = self.driver.find_element(By.ID,"rpm_pci_dss_compliant-no")

        # Does the Applicant outsource property maintenance and repair services?
        self.outsource_maintenance_yes = self.driver.find_element(By.ID,"rpm_outsource_maintenance-yes")

        self.outsource_maintenance_no = self.driver.find_element(By.ID,"rpm_outsource_maintenance-no")

        # Are bank accounts reconciled at least monthly?
        self.accounts_reconciled_yes = self.driver.find_element(By.ID,"rpm_accounts_reconciled-yes")

        self.accounts_reconciled_no = self.driver.find_element(By.ID,"rpm_accounts_reconciled-no")

        # Are all incoming checks stamped “for deposit” immediately upon receipt?
        self.stamped_deposit_yes = self.driver.find_element(By.ID,"rpm_stamped_deposit-yes")

        self.stamped_deposit_no = self.driver.find_element(By.ID,"rpm_stamped_deposit-no")

        # Does the Applicant conduct a prior employment check and criminal background check on all new hires?
        self.background_check_yes = self.driver.find_element(By.ID,"rpm_background_check-yes")

        self.background_check_no = self.driver.find_element(By.ID,"rpm_background_check-no")

        # a) Does the Applicant require all employees, independent contractors and volunteers with driving responsibilities to maintain limits of automobile liability insurance that meet the minimum state requirements?
        self.maintain_auto_liability_yes = self.driver.find_element(By.ID,"rpm_maintain_auto_liability-yes")

        self.maintain_auto_liability_no = self.driver.find_element(By.ID,"rpm_maintain_auto_liability-no")

        # b) Does the Applicant require evidence of such insurance?
        self.evidence_insurance_yes = self.driver.find_element(By.ID,"rpm_evidence_insurance-yes")

        self.evidence_insurance_no = self.driver.find_element(By.ID,"rpm_evidence_insurance-no")

        # Does the Applicant access and review Motor Vehicle Reports (MVRs) on all employees with driving responsibilities as a condition of employment?
        self.review_mvr_reports_yes = self.driver.find_element(By.ID,"rpm_review_mvr_reports-yes")

        self.review_mvr_reports_no = self.driver.find_element(By.ID,"rpm_review_mvr_reports-no")

        # If “Yes”, how frequently is the MVR review conducted?
        self.review_mvr_frequency = self.driver.find_element(By.ID,"rpm_review_mvr_frequency")

        # Name of Insurer:
        self.eo_carrier_name = self.driver.find_element(By.ID,"rpm_eo_carrier_name")

        # Policy Period:
        self.eo_policy_period = self.driver.find_element(By.ID,"rpm_eo_policy_period")

        # Limits of Liability:
        self.eo_limits = self.driver.find_element(By.ID,"rpm_eo_limits")

        # Retention:
        self.eo_retention = self.driver.find_element(By.ID,"rpm_eo_retention")

        # Premium
        self.eo_premium = self.driver.find_element(By.ID,"rpm_eo_premium")

        # Does the Applicant’s current Errors and Omissions or Professional Liability Insurance Policy have a prior acts limitation or retroactive date?
        self.current_eo_retroactive_date_yes = self.driver.find_element(By.ID,"rpm_current_eo_retroactive_date-yes")

        self.current_eo_retroactive_date_no = self.driver.find_element(By.ID,"rpm_current_eo_retroactive_date-no")

        # Retroactive Date
        self.current_coverage_retro_date = self.driver.find_element(By.ID,"rpm_current_eo_retroactive_date_detail")

        return self

    def create_quote_corporation_PCI_DSS_No_DQ(self, years_in_business, revenue, residential_units, commerical_sq_ft, previous_year, retroactive_date_formatted):
        PAF.Page_Elements(self).years_in_business.send_keys(years_in_business)
        PAF.Page_Elements(self).legal_structure_corporation.click()
        PAF.Page_Elements(self).annual_revenue.send_keys(revenue)
        PAF.Page_Elements(self).recent_revenue.send_keys(revenue)
        PAF.Page_Elements(self).eo_other_services_no.click()
        PAF.Page_Elements(self).own_twenty_five_percent_no.click()
        PAF.Page_Elements(self).past_claims_no.click()
        PAF.Page_Elements(self).aware_auto_claims_no.click()
        PAF.Page_Elements(self).aware_eo_claims_no.click()
        PAF.Page_Elements(self).confirm_gl_insurance_yes.click()
        PAF.Page_Elements(self).written_policies_yes.click()
        PAF.Page_Elements(self).number_residential_units.send_keys(residential_units)
        PAF.Page_Elements(self).commercial_square_footage.send_keys(commerical_sq_ft)
        PAF.Page_Elements(self).data_encrypted_yes.click()
        PAF.Page_Elements(self).anti_virus_software_yes.click()
        PAF.Page_Elements(self).software_updated_yes.click()
        PAF.Page_Elements(self).pci_dss_compliant_yes.click()
        PAF.Page_Elements(self).outsource_maintenance_yes.click()
        PAF.Page_Elements(self).accounts_reconciled_yes.click()
        PAF.Page_Elements(self).stamped_deposit_yes.click()
        PAF.Page_Elements(self).background_check_yes.click()
        PAF.Page_Elements(self).maintain_auto_liability_yes.click()
        PAF.Page_Elements(self).evidence_insurance_yes.click()
        PAF.Page_Elements(self).review_mvr_reports_yes.click()
        PAF.Page_Elements(self).review_mvr_frequency.send_keys("Quarterly")
        PAF.Page_Elements(self).eo_carrier_name.send_keys("All State")
        PAF.Page_Elements(self).eo_policy_period.send_keys(previous_year)
        PAF.Page_Elements(self).eo_limits.send_keys("50,000")
        PAF.Page_Elements(self).eo_retention.send_keys("1,000")
        PAF.Page_Elements(self).eo_premium.send_keys("2,000")
        PAF.Page_Elements(self).current_eo_retroactive_date_yes.click()
        PAF.Page_Elements(self).current_coverage_retro_date.send_keys(retroactive_date_formatted)

    def create_quote_individual_PCI_DSS_No_DQ(self, years_in_business, revenue, residential_units, commerical_sq_ft, previous_year, retroactive_date_formatted):
        PAF.Page_Elements(self).years_in_business.send_keys(years_in_business)
        PAF.Page_Elements(self).legal_structure_individual.click()
        PAF.Page_Elements(self).annual_revenue.send_keys(revenue)
        PAF.Page_Elements(self).recent_revenue.send_keys(revenue)
        PAF.Page_Elements(self).eo_other_services_no.click()
        PAF.Page_Elements(self).own_twenty_five_percent_no.click()
        PAF.Page_Elements(self).past_claims_no.click()
        PAF.Page_Elements(self).aware_auto_claims_no.click()
        PAF.Page_Elements(self).aware_eo_claims_no.click()
        PAF.Page_Elements(self).confirm_gl_insurance_yes.click()
        PAF.Page_Elements(self).written_policies_yes.click()
        PAF.Page_Elements(self).number_residential_units.send_keys(residential_units)
        PAF.Page_Elements(self).commercial_square_footage.send_keys(commerical_sq_ft)
        PAF.Page_Elements(self).data_encrypted_yes.click()
        PAF.Page_Elements(self).anti_virus_software_yes.click()
        PAF.Page_Elements(self).software_updated_yes.click()
        PAF.Page_Elements(self).pci_dss_compliant_yes.click()
        PAF.Page_Elements(self).outsource_maintenance_yes.click()
        PAF.Page_Elements(self).accounts_reconciled_yes.click()
        PAF.Page_Elements(self).stamped_deposit_yes.click()
        PAF.Page_Elements(self).background_check_yes.click()
        PAF.Page_Elements(self).maintain_auto_liability_yes.click()
        PAF.Page_Elements(self).evidence_insurance_yes.click()
        PAF.Page_Elements(self).review_mvr_reports_yes.click()
        PAF.Page_Elements(self).review_mvr_frequency.send_keys("Quarterly")
        PAF.Page_Elements(self).eo_carrier_name.send_keys("All State")
        PAF.Page_Elements(self).eo_policy_period.send_keys(previous_year)
        PAF.Page_Elements(self).eo_limits.send_keys("50,000")
        PAF.Page_Elements(self).eo_retention.send_keys("1,000")
        PAF.Page_Elements(self).eo_premium.send_keys("2,000")
        PAF.Page_Elements(self).current_eo_retroactive_date_yes.click()
        PAF.Page_Elements(self).current_coverage_retro_date.send_keys(retroactive_date_formatted)

    def create_quote_llc_PCI_DSS_No_DQ(self, years_in_business, revenue, residential_units, commerical_sq_ft, previous_year, retroactive_date_formatted):
        PAF.Page_Elements(self).years_in_business.send_keys(years_in_business)
        PAF.Page_Elements(self).legal_structure_llc.click()
        PAF.Page_Elements(self).annual_revenue.send_keys(revenue)
        PAF.Page_Elements(self).recent_revenue.send_keys(revenue)
        PAF.Page_Elements(self).eo_other_services_no.click()
        PAF.Page_Elements(self).own_twenty_five_percent_no.click()
        PAF.Page_Elements(self).past_claims_no.click()
        PAF.Page_Elements(self).aware_auto_claims_no.click()
        PAF.Page_Elements(self).aware_eo_claims_no.click()
        PAF.Page_Elements(self).confirm_gl_insurance_yes.click()
        PAF.Page_Elements(self).written_policies_yes.click()
        PAF.Page_Elements(self).number_residential_units.send_keys(residential_units)
        PAF.Page_Elements(self).commercial_square_footage.send_keys(commerical_sq_ft)
        PAF.Page_Elements(self).data_encrypted_yes.click()
        PAF.Page_Elements(self).anti_virus_software_yes.click()
        PAF.Page_Elements(self).software_updated_yes.click()
        PAF.Page_Elements(self).pci_dss_compliant_yes.click()
        PAF.Page_Elements(self).outsource_maintenance_yes.click()
        PAF.Page_Elements(self).accounts_reconciled_yes.click()
        PAF.Page_Elements(self).stamped_deposit_yes.click()
        PAF.Page_Elements(self).background_check_yes.click()
        PAF.Page_Elements(self).maintain_auto_liability_yes.click()
        PAF.Page_Elements(self).evidence_insurance_yes.click()
        PAF.Page_Elements(self).review_mvr_reports_yes.click()
        PAF.Page_Elements(self).review_mvr_frequency.send_keys("Quarterly")
        PAF.Page_Elements(self).eo_carrier_name.send_keys("All State")
        PAF.Page_Elements(self).eo_policy_period.send_keys(previous_year)
        PAF.Page_Elements(self).eo_limits.send_keys("50,000")
        PAF.Page_Elements(self).eo_retention.send_keys("1,000")
        PAF.Page_Elements(self).eo_premium.send_keys("2,000")
        PAF.Page_Elements(self).current_eo_retroactive_date_yes.click()
        PAF.Page_Elements(self).current_coverage_retro_date.send_keys(retroactive_date_formatted)

    def create_quote_partnership_PCI_DSS_No_DQ(self, years_in_business, revenue, residential_units, commerical_sq_ft, previous_year, retroactive_date_formatted):
        PAF.Page_Elements(self).years_in_business.send_keys(years_in_business)
        PAF.Page_Elements(self).legal_structure_partnership.click()
        PAF.Page_Elements(self).annual_revenue.send_keys(revenue)
        PAF.Page_Elements(self).recent_revenue.send_keys(revenue)
        PAF.Page_Elements(self).eo_other_services_no.click()
        PAF.Page_Elements(self).own_twenty_five_percent_no.click()
        PAF.Page_Elements(self).past_claims_no.click()
        PAF.Page_Elements(self).aware_auto_claims_no.click()
        PAF.Page_Elements(self).aware_eo_claims_no.click()
        PAF.Page_Elements(self).confirm_gl_insurance_yes.click()
        PAF.Page_Elements(self).written_policies_yes.click()
        PAF.Page_Elements(self).number_residential_units.send_keys(residential_units)
        PAF.Page_Elements(self).commercial_square_footage.send_keys(commerical_sq_ft)
        PAF.Page_Elements(self).data_encrypted_yes.click()
        PAF.Page_Elements(self).anti_virus_software_yes.click()
        PAF.Page_Elements(self).software_updated_yes.click()
        PAF.Page_Elements(self).pci_dss_compliant_yes.click()
        PAF.Page_Elements(self).outsource_maintenance_yes.click()
        PAF.Page_Elements(self).accounts_reconciled_yes.click()
        PAF.Page_Elements(self).stamped_deposit_yes.click()
        PAF.Page_Elements(self).background_check_yes.click()
        PAF.Page_Elements(self).maintain_auto_liability_yes.click()
        PAF.Page_Elements(self).evidence_insurance_yes.click()
        PAF.Page_Elements(self).review_mvr_reports_yes.click()
        PAF.Page_Elements(self).review_mvr_frequency.send_keys("Quarterly")
        PAF.Page_Elements(self).eo_carrier_name.send_keys("All State")
        PAF.Page_Elements(self).eo_policy_period.send_keys(previous_year)
        PAF.Page_Elements(self).eo_limits.send_keys("50,000")
        PAF.Page_Elements(self).eo_retention.send_keys("1,000")
        PAF.Page_Elements(self).eo_premium.send_keys("2,000")
        PAF.Page_Elements(self).current_eo_retroactive_date_yes.click()
        PAF.Page_Elements(self).current_coverage_retro_date.send_keys(retroactive_date_formatted)

    def create_quote_DQ(self, years_in_business, revenue, residential_units, commerical_sq_ft, previous_year, retroactive_date_formatted):
        PAF.Page_Elements(self).years_in_business.send_keys(years_in_business)
        PAF.Page_Elements(self).legal_structure_corporation.click()
        PAF.Page_Elements(self).annual_revenue.send_keys(revenue)
        PAF.Page_Elements(self).recent_revenue.send_keys(revenue)
        PAF.Page_Elements(self).eo_other_services_no.click()
        PAF.Page_Elements(self).own_twenty_five_percent_no.click()
        PAF.Page_Elements(self).past_claims_no.click()
        PAF.Page_Elements(self).aware_auto_claims_no.click()
        PAF.Page_Elements(self).aware_eo_claims_no.click()
        PAF.Page_Elements(self).confirm_gl_insurance_yes.click()
        PAF.Page_Elements(self).written_policies_yes.click()
        PAF.Page_Elements(self).number_residential_units.send_keys(residential_units)
        PAF.Page_Elements(self).commercial_square_footage.send_keys(commerical_sq_ft)
        PAF.Page_Elements(self).data_encrypted_yes.click()
        PAF.Page_Elements(self).anti_virus_software_yes.click()
        PAF.Page_Elements(self).software_updated_yes.click()
        PAF.Page_Elements(self).pci_dss_compliant_no.click()
        PAF.Page_Elements(self).outsource_maintenance_yes.click()
        PAF.Page_Elements(self).accounts_reconciled_yes.click()
        PAF.Page_Elements(self).stamped_deposit_yes.click()
        PAF.Page_Elements(self).background_check_yes.click()
        PAF.Page_Elements(self).maintain_auto_liability_yes.click()
        PAF.Page_Elements(self).evidence_insurance_yes.click()
        PAF.Page_Elements(self).review_mvr_reports_yes.click()
        PAF.Page_Elements(self).review_mvr_frequency.send_keys("Quarterly")
        PAF.Page_Elements(self).eo_carrier_name.send_keys("All State")
        PAF.Page_Elements(self).eo_policy_period.send_keys(previous_year)
        PAF.Page_Elements(self).eo_limits.send_keys("50,000")
        PAF.Page_Elements(self).eo_retention.send_keys("1,000")
        PAF.Page_Elements(self).eo_premium.send_keys("2,000")
        PAF.Page_Elements(self).current_eo_retroactive_date_yes.click()
        PAF.Page_Elements(self).current_coverage_retro_date.send_keys(retroactive_date_formatted)


    #TODO
    # Ask Dev to create ID for next button
    def click_next(self):
        next_button = self.driver.find_element(By.XPATH, "//form[@id='primary-hhpl-form']/div[5]/a/span[2]/span/span")
        next_button.click()

    def click_return_to_Admin_Interface(self):
        PAF.Page_Elements(self).return_to_Admin.click()