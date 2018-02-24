from selenium.webdriver.common.by import By

class PAF():

    def __init__(self, driver):
        self.driver = driver

    #Page Elements

    def Page_Elements(self):

        # Return to Admin Link
        self.return_to_Admin = self.driver.find_element(By.LINK_TEXT, "Return to Admin Interface")

        # Number of Years in Business
        self.years_in_business = self.driver.find_element(By.ID, "years-in-business")

        # Legal Structure

        # Corporation
        self.legal_structure_corporation = self.driver.find_element(By.ID, "legal-structure-corporation")

        # Individual Proprietor
        self.legal_structure_individual = self.driver.find_element(By.ID, "legal-structure-individual")

        # Limited Liabilty Company
        self.legal_structure_llc = self.driver.find_element(By.ID, "legal-structure-llc")

        # Paternship / Joint Venture
        self.legal_structure_partnership = self.driver.find_element(By.ID, "legal-structure-partnership")

        # Other
        self.legal_structure_oth = self.driver.find_element(By.ID, "legal-structure-oth")

        # Other (Text Field)
        self.legal_structure_other = self.driver.find_element(By.ID, "legal-structure-other")

        # Total annual revenue for Property Management / Leasing Services:
        self.revenue_current_year = self.driver.find_element(By.ID, "annual_revenue_current_year")

        # Does the Applicant own greater than 25% of managed/leased properties
        self.leased_property_percentage_25_yes = self.driver.find_element(By.ID, "leased_property_percentage_25-yes")

        self.leased_property_percentage_25_no = self.driver.find_element(By.ID, "leased_property_percentage_25-no")

        # Does the Applicant desire E&O coverage for services other than Property Management, Leasing and Owner Representation Services
        self.desire_eo_yes = self.driver.find_element(By.ID, "eo_pm_desire_eo-yes")

        self.desire_eo_no = self.driver.find_element(By.ID, "eo_pm_desire_eo-no")

        # Does the Applicant have written anti-discrimination policies
        self.fair_housing_compliance_yes = self.driver.find_element(By.ID,"eo_pm_fair_housing_compliance-yes")

        self.fair_housing_compliance_no = self.driver.find_element(By.ID,"eo_pm_fair_housing_compliance-no")

        # If your organization stores personal information on portable devices, including laptops, cell phones, PDAs, back-up tapes, USB thumb drivers and external hard drives, is such data encrypted to industry standards?
        self.data_security_yes = self.driver.find_element(By.ID,"eo_pm_data_security-yes")

        self.data_security_no = self.driver.find_element(By.ID,"eo_pm_data_security-no")

        self.data_security_na = self.driver.find_element(By.ID,"eo_pm_data_security-na")

        # Do the Applicant's facilities have access for the disabled in compliance with A.D.A
        self.ada_compliance_yes = self.driver.find_element(By.ID,"eo_pm_ada_compliance-yes")

        self.ada_compliance_no = self.driver.find_element(By.ID,"eo_pm_ada_compliance-no")

        # Does the Applicant use anti-virus software and firewall protection on all desktops, portable devices and mission critical servers, and is it updated in accordance with the software provider’s recommendations
        self.platform_security_yes = self.driver.find_element(By.ID,"eo_pm_platform_security-yes")

        self.platform_security_no = self.driver.find_element(By.ID,"eo_pm_platform_security-no")

        # Insurance History

        # Do you have current Professional Liability Insurance Coverage in place
        self.current_coverage_yes = self.driver.find_element(By.ID,"eo_pm_current_coverage_yes")

        self.current_coverage_no = self.driver.find_element(By.ID,"eo_pm_current_coverage_no")

        # Retroactive Date
        self.current_coverage_retro_date = self.driver.find_element(By.ID,"eo_pm_current_coverage_retro_date")

        # Claim History
        # Have any claims, suits, or demands been made against the Applicant, a predecessor firm, or any past or present principals, partners, officers, or employees within the past five (5) years
        self.past_claim_yes = self.driver.find_element(By.ID,"eo_pm_past_claim_yes")

        self.past_claim_no = self.driver.find_element(By.ID,"eo_pm_past_claim_no")

        # After inquiry with all principals, partners and officers, is the Applicant aware of any dispute, error, omission, act, circumstance or fact that is, or could reasonably be expected to become, a claim under the policy for which this Application is submitted to the Underwriters
        self.potential_claim_yes = self.driver.find_element(By.ID,"eo_pm_potential_claim_yes")

        self.potential_claim_no = self.driver.find_element(By.ID,"eo_pm_potential_claim_no")

        return self

    def create_quote_Corporation_Property_Management_Company(self, number_years_in_business, revenue_current_year, retroactive_date_formatted):
        PAF.Page_Elements(self).years_in_business.send_keys(number_years_in_business)
        PAF.Page_Elements(self).legal_structure_corporation.click()
        PAF.Page_Elements(self).revenue_current_year.send_keys(revenue_current_year)
        PAF.Page_Elements(self).leased_property_percentage_25_no.click()
        PAF.Page_Elements(self).desire_eo_no.click()
        PAF.Page_Elements(self).fair_housing_compliance_yes.click()
        PAF.Page_Elements(self).data_security_yes.click()
        PAF.Page_Elements(self).ada_compliance_yes.click()
        PAF.Page_Elements(self).platform_security_yes.click()
        PAF.Page_Elements(self).current_coverage_yes.click()
        PAF.Page_Elements(self).current_coverage_retro_date.clear()
        PAF.Page_Elements(self).current_coverage_retro_date.send_keys(retroactive_date_formatted)
        PAF.Page_Elements(self).past_claim_no.click()
        PAF.Page_Elements(self).potential_claim_no.click()

    def create_quote_Individual_Proprietor_Property_Management_Company(self, number_years_in_business, revenue_current_year, retroactive_date_formatted):
        PAF.Page_Elements(self).years_in_business.send_keys(number_years_in_business)
        PAF.Page_Elements(self).legal_structure_individual.click()
        PAF.Page_Elements(self).revenue_current_year.send_keys(revenue_current_year)
        PAF.Page_Elements(self).leased_property_percentage_25_no.click()
        PAF.Page_Elements(self).desire_eo_no.click()
        PAF.Page_Elements(self).fair_housing_compliance_yes.click()
        PAF.Page_Elements(self).data_security_yes.click()
        PAF.Page_Elements(self).ada_compliance_yes.click()
        PAF.Page_Elements(self).platform_security_yes.click()
        PAF.Page_Elements(self).current_coverage_yes.click()
        PAF.Page_Elements(self).current_coverage_retro_date.clear()
        PAF.Page_Elements(self).current_coverage_retro_date.send_keys(retroactive_date_formatted)
        PAF.Page_Elements(self).past_claim_no.click()
        PAF.Page_Elements(self).potential_claim_no.click()

    def create_quote_Limited_Liability_Company_Property_Management_Company(self, number_years_in_business, revenue_current_year, retroactive_date_formatted):
        PAF.Page_Elements(self).years_in_business.send_keys(number_years_in_business)
        PAF.Page_Elements(self).legal_structure_llc.click()
        PAF.Page_Elements(self).revenue_current_year.send_keys(revenue_current_year)
        PAF.Page_Elements(self).leased_property_percentage_25_no.click()
        PAF.Page_Elements(self).desire_eo_no.click()
        PAF.Page_Elements(self).fair_housing_compliance_yes.click()
        PAF.Page_Elements(self).data_security_yes.click()
        PAF.Page_Elements(self).ada_compliance_yes.click()
        PAF.Page_Elements(self).platform_security_yes.click()
        PAF.Page_Elements(self).current_coverage_yes.click()
        PAF.Page_Elements(self).current_coverage_retro_date.clear()
        PAF.Page_Elements(self).current_coverage_retro_date.send_keys(retroactive_date_formatted)
        PAF.Page_Elements(self).past_claim_no.click()
        PAF.Page_Elements(self).potential_claim_no.click()

    def create_quote_Partnership_Joint_Venture_Property_Management_Company(self, number_years_in_business, revenue_current_year, retroactive_date_formatted):
        PAF.Page_Elements(self).years_in_business.send_keys(number_years_in_business)
        PAF.Page_Elements(self).legal_structure_partnership.click()
        PAF.Page_Elements(self).revenue_current_year.send_keys(revenue_current_year)
        PAF.Page_Elements(self).leased_property_percentage_25_no.click()
        PAF.Page_Elements(self).desire_eo_no.click()
        PAF.Page_Elements(self).fair_housing_compliance_yes.click()
        PAF.Page_Elements(self).data_security_yes.click()
        PAF.Page_Elements(self).ada_compliance_yes.click()
        PAF.Page_Elements(self).platform_security_yes.click()
        PAF.Page_Elements(self).current_coverage_yes.click()
        PAF.Page_Elements(self).current_coverage_retro_date.clear()
        PAF.Page_Elements(self).current_coverage_retro_date.send_keys(retroactive_date_formatted)
        PAF.Page_Elements(self).past_claim_no.click()
        PAF.Page_Elements(self).potential_claim_no.click()

    def create_quote_Other_Property_Management_Company(self, number_years_in_business, revenue_current_year, retroactive_date_formatted, company_name_string):
        PAF.Page_Elements(self).years_in_business.send_keys(number_years_in_business)
        PAF.Page_Elements(self).legal_structure_oth.click()
        PAF.Page_Elements(self).legal_structure_other.send_keys(company_name_string)
        PAF.Page_Elements(self).revenue_current_year.send_keys(revenue_current_year)
        PAF.Page_Elements(self).leased_property_percentage_25_no.click()
        PAF.Page_Elements(self).desire_eo_no.click()
        PAF.Page_Elements(self).fair_housing_compliance_yes.click()
        PAF.Page_Elements(self).data_security_yes.click()
        PAF.Page_Elements(self).ada_compliance_yes.click()
        PAF.Page_Elements(self).platform_security_yes.click()
        PAF.Page_Elements(self).current_coverage_yes.click()
        PAF.Page_Elements(self).current_coverage_retro_date.clear()
        PAF.Page_Elements(self).current_coverage_retro_date.send_keys(retroactive_date_formatted)
        PAF.Page_Elements(self).past_claim_no.click()
        PAF.Page_Elements(self).potential_claim_no.click()

    #TODO
    # Ask Dev to create ID for next button
    def click_next(self):
        next_button = self.driver.find_element(By.XPATH, "//form[@id='primary-abeo-form']/div[6]/a/span[2]/span/span")
        next_button.click()

    def click_return_to_Admin_Interface(self):
        PAF.Page_Elements(self).return_to_Admin.click()