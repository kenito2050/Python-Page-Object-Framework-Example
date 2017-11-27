from selenium.webdriver.common.by import By

class PAF():

    def __init__(self, driver):
        self.driver = driver

    #Page Elements

    def Page_Elements(self):

        # Return to Admin Link
        self.return_to_Admin = self.driver.find_element(By.LINK_TEXT, "Return to Admin Interface")

        # Legal Structure

        # Corporation
        self.legal_structure_corporation = self.driver.find_element(By.ID, "legal-structure-corporation")

        # Individual Proprietor
        self.legal_structure_individual_proprietor = self.driver.find_element(By.ID, "legal-structure-individual_proprietor")

        # Limited Liabilty Company
        self.legal_structure_llc = self.driver.find_element(By.ID, "legal-structure-llc")

        # Paternship / Joint Venture
        self.legal_structure_partnership = self.driver.find_element(By.ID, "legal-structure-partnership")

        # Public Agency
        self.legal_structure_agency = self.driver.find_element(By.ID, "legal-structure-public_agency")

        # Other
        self.legal_structure_oth = self.driver.find_element(By.ID, "legal-structure-oth")

        # Other (Text Field)
        self.legal_structure_other = self.driver.find_element(By.ID, "legal-structure-other")

        # Full Corporation Name
        self.legal_structure_corporation_name = self.driver.find_element(By.ID, "legal_structure_corporation_name")

        # Applicant Type

        # Property Management Company
        self.applicant_type_management_company = self.driver.find_element(By.ID, "lexr_tenant_applicant_type_management_company")

        # Property Owner
        self.applicant_type_owner = self.driver.find_element(By.ID, "lexr_tenant_applicant_type_owner")

        # Number of Years in Business
        self.years_in_business = self.driver.find_element(By.ID, "years-in-business")

        # Is the Applicant seeking coverage for all properties disclosed in question 3 above
        self.coverage_properties_yes = self.driver.find_element(By.ID, "lexr_tenant_coverage_properties-yes")
        self.coverage_properties_no = self.driver.find_element(By.ID, "lexr_tenant_coverage_properties-no")

        # Is the Applicant seeking coverage for any other person(s) or organization(s)
        self.coverage_organizations_yes = self.driver.find_element(By.ID, "lexr_tenant_coverage_organizations-yes")
        self.coverage_organizations_no = self.driver.find_element(By.ID, "lexr_tenant_coverage_organizations-no")

        # Does the Applicant, or any other person or entity proposed for coverage, own or manage any mobile homes
        self.mobile_home_yes = self.driver.find_element(By.ID, "lexr_tenant_mobile_home-yes")
        self.mobile_home_no = self.driver.find_element(By.ID, "lexr_tenant_mobile_home-no")

        # Is the Applicant, or any other person or entity proposed for coverage, involved in real estate development activities, other than routine upgrades or renovations to leased premises
        self.real_estate_yes = self.driver.find_element(By.ID, "lexr_tenant_real_estate-yes")
        self.real_estate_no = self.driver.find_element(By.ID, "lexr_tenant_real_estate-no")

        # Does the Applicant have written anti-discrimination policies
        self.anti_discrimination_policies_yes = self.driver.find_element(By.ID, "lexr_tenant_anti_discrimination_policies-yes")
        self.anti_discrimination_policies_no = self.driver.find_element(By.ID, "lexr_tenant_anti_discrimination_policies-no")

        # Does the Applicant have written procedures in place for handling tenant discrimination complaints
        self.procedures_complaints_yes = self.driver.find_element(By.ID, "lexr_tenant_procedures_complaints-yes")
        self.procedures_complaints_no = self.driver.find_element(By.ID, "lexr_tenant_procedures_complaints-no")

        # Has any person or entity proposed for coverage been the subject in or involved in any tenant discrimination claims within the last five (5) years
        self.discrimination_yes = self.driver.find_element(By.ID, "lexr_tenant_discrimination_claims-yes")
        self.discrimination_no = self.driver.find_element(By.ID, "lexr_tenant_discrimination_claims-no")

        # Is the Applicant, or any person or entity proposed for coverage, aware of any facts, incidents, circumstances, or allegations of discrimination which may result in a tenant discrimination claim
        self.allegations_yes = self.driver.find_element(By.ID, "lexr_tenant_allegations-yes")
        self.allegations_no = self.driver.find_element(By.ID, "lexr_tenant_allegations-no")

        # ADA Warranty Compliance Statement is true
        self.compliacne_statement = self.driver.find_element(By.ID, "lexr_tenant_compliacne_statement")

        return self

    def create_quote_Corporation_Property_Management_Company(self, number_years_in_business, company_name_string):
        PAF.Page_Elements(self).legal_structure_corporation.click()
        PAF.Page_Elements(self).legal_structure_corporation_name.send_keys(company_name_string)
        PAF.Page_Elements(self).applicant_type_management_company.click()
        PAF.Page_Elements(self).years_in_business.send_keys(number_years_in_business)
        PAF.Page_Elements(self).coverage_properties_yes.click()
        PAF.Page_Elements(self).coverage_organizations_no.click()
        PAF.Page_Elements(self).mobile_home_no.click()
        PAF.Page_Elements(self).real_estate_no.click()
        PAF.Page_Elements(self).anti_discrimination_policies_yes.click()
        PAF.Page_Elements(self).procedures_complaints_yes.click()
        PAF.Page_Elements(self).discrimination_no.click()
        PAF.Page_Elements(self).allegations_no.click()
        PAF.Page_Elements(self).compliacne_statement.click()

    def create_quote_Individual_Proprietor_Property_Management_Company(self, number_years_in_business):
        PAF.Page_Elements(self).legal_structure_individual_proprietor.click()
        PAF.Page_Elements(self).applicant_type_management_company.click()
        PAF.Page_Elements(self).years_in_business.send_keys(number_years_in_business)
        PAF.Page_Elements(self).coverage_properties_yes.click()
        PAF.Page_Elements(self).coverage_organizations_no.click()
        PAF.Page_Elements(self).mobile_home_no.click()
        PAF.Page_Elements(self).real_estate_no.click()
        PAF.Page_Elements(self).anti_discrimination_policies_yes.click()
        PAF.Page_Elements(self).procedures_complaints_yes.click()
        PAF.Page_Elements(self).discrimination_no.click()
        PAF.Page_Elements(self).allegations_no.click()
        PAF.Page_Elements(self).compliacne_statement.click()

    def create_quote_Limited_Liability_Company_Property_Management_Company(self, number_years_in_business):
        PAF.Page_Elements(self).legal_structure_llc.click()
        PAF.Page_Elements(self).applicant_type_management_company.click()
        PAF.Page_Elements(self).years_in_business.send_keys(number_years_in_business)
        PAF.Page_Elements(self).coverage_properties_yes.click()
        PAF.Page_Elements(self).coverage_organizations_no.click()
        PAF.Page_Elements(self).mobile_home_no.click()
        PAF.Page_Elements(self).real_estate_no.click()
        PAF.Page_Elements(self).anti_discrimination_policies_yes.click()
        PAF.Page_Elements(self).procedures_complaints_yes.click()
        PAF.Page_Elements(self).discrimination_no.click()
        PAF.Page_Elements(self).allegations_no.click()
        PAF.Page_Elements(self).compliacne_statement.click()

    def create_quote_Partnership_Joint_Venture_Property_Management_Company(self, number_years_in_business):
        PAF.Page_Elements(self).legal_structure_partnership.click()
        PAF.Page_Elements(self).applicant_type_management_company.click()
        PAF.Page_Elements(self).years_in_business.send_keys(number_years_in_business)
        PAF.Page_Elements(self).coverage_properties_yes.click()
        PAF.Page_Elements(self).coverage_organizations_no.click()
        PAF.Page_Elements(self).mobile_home_no.click()
        PAF.Page_Elements(self).real_estate_no.click()
        PAF.Page_Elements(self).anti_discrimination_policies_yes.click()
        PAF.Page_Elements(self).procedures_complaints_yes.click()
        PAF.Page_Elements(self).discrimination_no.click()
        PAF.Page_Elements(self).allegations_no.click()
        PAF.Page_Elements(self).compliacne_statement.click()

    def create_quote_Public_Agency_Property_Management_Company(self, number_years_in_business):
        PAF.Page_Elements(self).legal_structure_agency.click()
        PAF.Page_Elements(self).applicant_type_management_company.click()
        PAF.Page_Elements(self).years_in_business.send_keys(number_years_in_business)
        PAF.Page_Elements(self).coverage_properties_yes.click()
        PAF.Page_Elements(self).coverage_organizations_no.click()
        PAF.Page_Elements(self).mobile_home_no.click()
        PAF.Page_Elements(self).real_estate_no.click()
        PAF.Page_Elements(self).anti_discrimination_policies_yes.click()
        PAF.Page_Elements(self).procedures_complaints_yes.click()
        PAF.Page_Elements(self).discrimination_no.click()
        PAF.Page_Elements(self).allegations_no.click()
        PAF.Page_Elements(self).compliacne_statement.click()

    def create_quote_Other_Property_Management_Company(self, number_years_in_business, company_name_string):
        PAF.Page_Elements(self).legal_structure_oth.click()
        PAF.Page_Elements(self).legal_structure_other.send_keys(company_name_string)
        PAF.Page_Elements(self).applicant_type_management_company.click()
        PAF.Page_Elements(self).years_in_business.send_keys(number_years_in_business)
        PAF.Page_Elements(self).coverage_properties_yes.click()
        PAF.Page_Elements(self).coverage_organizations_no.click()
        PAF.Page_Elements(self).mobile_home_no.click()
        PAF.Page_Elements(self).real_estate_no.click()
        PAF.Page_Elements(self).anti_discrimination_policies_yes.click()
        PAF.Page_Elements(self).procedures_complaints_yes.click()
        PAF.Page_Elements(self).discrimination_no.click()
        PAF.Page_Elements(self).allegations_no.click()
        PAF.Page_Elements(self).compliacne_statement.click()

    def create_quote_Corporation_Property_Owner(self, number_years_in_business, company_name_string):
        PAF.Page_Elements(self).legal_structure_corporation.click()
        PAF.Page_Elements(self).legal_structure_corporation_name.send_keys(company_name_string)
        PAF.Page_Elements(self).applicant_type_owner.click()
        PAF.Page_Elements(self).years_in_business.send_keys(number_years_in_business)
        PAF.Page_Elements(self).coverage_properties_yes.click()
        PAF.Page_Elements(self).coverage_organizations_no.click()
        PAF.Page_Elements(self).mobile_home_no.click()
        PAF.Page_Elements(self).real_estate_no.click()
        PAF.Page_Elements(self).anti_discrimination_policies_yes.click()
        PAF.Page_Elements(self).procedures_complaints_yes.click()
        PAF.Page_Elements(self).discrimination_no.click()
        PAF.Page_Elements(self).allegations_no.click()
        PAF.Page_Elements(self).compliacne_statement.click()

    def create_quote_Individual_Proprietor_Property_Owner(self, number_years_in_business):
        PAF.Page_Elements(self).legal_structure_individual_proprietor.click()
        PAF.Page_Elements(self).applicant_type_owner.click()
        PAF.Page_Elements(self).years_in_business.send_keys(number_years_in_business)
        PAF.Page_Elements(self).coverage_properties_yes.click()
        PAF.Page_Elements(self).coverage_organizations_no.click()
        PAF.Page_Elements(self).mobile_home_no.click()
        PAF.Page_Elements(self).real_estate_no.click()
        PAF.Page_Elements(self).anti_discrimination_policies_yes.click()
        PAF.Page_Elements(self).procedures_complaints_yes.click()
        PAF.Page_Elements(self).discrimination_no.click()
        PAF.Page_Elements(self).allegations_no.click()
        PAF.Page_Elements(self).compliacne_statement.click()

    def create_quote_Limited_Liability_Company_Property_Owner(self, number_years_in_business):
        PAF.Page_Elements(self).legal_structure_llc.click()
        PAF.Page_Elements(self).applicant_type_owner.click()
        PAF.Page_Elements(self).years_in_business.send_keys(number_years_in_business)
        PAF.Page_Elements(self).coverage_properties_yes.click()
        PAF.Page_Elements(self).coverage_organizations_no.click()
        PAF.Page_Elements(self).mobile_home_no.click()
        PAF.Page_Elements(self).real_estate_no.click()
        PAF.Page_Elements(self).anti_discrimination_policies_yes.click()
        PAF.Page_Elements(self).procedures_complaints_yes.click()
        PAF.Page_Elements(self).discrimination_no.click()
        PAF.Page_Elements(self).allegations_no.click()
        PAF.Page_Elements(self).compliacne_statement.click()

    def create_quote_Partnership_Joint_Venture_Property_Owner(self, number_years_in_business):
        PAF.Page_Elements(self).legal_structure_partnership.click()
        PAF.Page_Elements(self).applicant_type_owner.click()
        PAF.Page_Elements(self).years_in_business.send_keys(number_years_in_business)
        PAF.Page_Elements(self).coverage_properties_yes.click()
        PAF.Page_Elements(self).coverage_organizations_no.click()
        PAF.Page_Elements(self).mobile_home_no.click()
        PAF.Page_Elements(self).real_estate_no.click()
        PAF.Page_Elements(self).anti_discrimination_policies_yes.click()
        PAF.Page_Elements(self).procedures_complaints_yes.click()
        PAF.Page_Elements(self).discrimination_no.click()
        PAF.Page_Elements(self).allegations_no.click()
        PAF.Page_Elements(self).compliacne_statement.click()

    def create_quote_Public_Agency_Property_Property_Owner(self, number_years_in_business):
        PAF.Page_Elements(self).legal_structure_agency.click()
        PAF.Page_Elements(self).applicant_type_owner.click()
        PAF.Page_Elements(self).years_in_business.send_keys(number_years_in_business)
        PAF.Page_Elements(self).coverage_properties_yes.click()
        PAF.Page_Elements(self).coverage_organizations_no.click()
        PAF.Page_Elements(self).mobile_home_no.click()
        PAF.Page_Elements(self).real_estate_no.click()
        PAF.Page_Elements(self).anti_discrimination_policies_yes.click()
        PAF.Page_Elements(self).procedures_complaints_yes.click()
        PAF.Page_Elements(self).discrimination_no.click()
        PAF.Page_Elements(self).allegations_no.click()
        PAF.Page_Elements(self).compliacne_statement.click()

    def create_quote_Other_Property_Management_Property_Owner(self, number_years_in_business, company_name_string):
        PAF.Page_Elements(self).legal_structure_oth.click()
        PAF.Page_Elements(self).legal_structure_other.send_keys(company_name_string)
        PAF.Page_Elements(self).applicant_type_owner.click()
        PAF.Page_Elements(self).years_in_business.send_keys(number_years_in_business)
        PAF.Page_Elements(self).coverage_properties_yes.click()
        PAF.Page_Elements(self).coverage_organizations_no.click()
        PAF.Page_Elements(self).mobile_home_no.click()
        PAF.Page_Elements(self).real_estate_no.click()
        PAF.Page_Elements(self).anti_discrimination_policies_yes.click()
        PAF.Page_Elements(self).procedures_complaints_yes.click()
        PAF.Page_Elements(self).discrimination_no.click()
        PAF.Page_Elements(self).allegations_no.click()
        PAF.Page_Elements(self).compliacne_statement.click()


    #TODO
    # Ask Dev to create ID for next button
    def click_next(self):
        next_button = self.driver.find_element(By.XPATH, "//form[@id='primary-application-form']/div[5]/a/span[2]/span/span")
        next_button.click()

    def click_return_to_Admin_Interface(self):
        PAF.Page_Elements(self).return_to_Admin.click()