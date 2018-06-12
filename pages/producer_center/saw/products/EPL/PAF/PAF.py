from selenium.webdriver.common.by import By

class PAF():

    def __init__(self, driver):
        self.driver = driver

    #Page Elements

    def Page_Elements(self):

        # Return to Admin Link
        self.return_to_Admin = self.driver.find_element(By.LINK_TEXT, "Return to Admin Interface")

        # Has the Applicant been in business longer than three years?
        self.applicant_longerthan_three_years_yes = self.driver.find_element(By.ID, "epl_applicant_longerthan_three_years-yes")

        self.applicant_longerthan_three_years_no = self.driver.find_element(By.ID, "epl_applicant_longerthan_three_years-no")

        # Is the Applicant a Publicly Held or Public Reporting Company under the Securities Exchange Act of 1934 (as amended), or has it ever been?
        self.applicant_publicly_held_yes = self.driver.find_element(By.ID, "epl_applicant_publicly_held-yes")

        self.applicant_publicly_held_no = self.driver.find_element(By.ID, "epl_applicant_publicly_held-no")

        # a) Has the Applicant been involved in, negotiated, attempted, or transacted any acquisitions, merger, or divestment in the past 18 months, where such transaction would have or did result in a 25% change of the total assets of the company?
        self.change_in_total_assets_yes = self.driver.find_element(By.ID, "epl_change_in_total_assets-yes")

        self.change_in_total_assets_no = self.driver.find_element(By.ID, "epl_change_in_total_assets-no")

        # b) Is the Applicant contemplating such a transaction in the next 18 months?
        self.transaction_in_next_months_yes = self.driver.find_element(By.ID, "epl_transaction_in_next_months-yes")

        self.transaction_in_next_months_no = self.driver.find_element(By.ID, "epl_transaction_in_next_months-no")

        # Has the Applicant purchased similar coverage before, or is the Applicant currently insured for similar coverage through another carrier?
        self.similar_coverage_yes = self.driver.find_element(By.ID, "epl_similar_coverage-yes")

        self.similar_coverage_no = self.driver.find_element(By.ID, "epl_similar_coverage-no")

        # Within the past five years, has any person or entity proposed for this insurance been the subject of, or involved in, any governmental investigation, inquiry, or proceeding, including any investigation by the Department of Labor, the Equal Employment Opportunity Commission, or any similar state or local agency?
        self.investigation_yes = self.driver.find_element(By.ID, "epl_investigation-yes")

        self.investigation_no = self.driver.find_element(By.ID, "epl_investigation-no")

        # Is any person proposed for this insurance aware of any facts, incidents, circumstances, or allegations of wrongful acts which may result in claims being made againstany person or entity proposed for this insurance?
        self.aware_insurance_facts_yes = self.driver.find_element(By.ID, "epl_aware_insurance_facts-yes")

        self.aware_insurance_facts_no = self.driver.find_element(By.ID, "epl_aware_insurance_facts-no")

        # Total employee count:

        # b. Number of highly compensated employees (total annual salary/wages and bonus exceed $100K):
        self.highly_compensated_employee_salary = self.driver.find_element(By.ID, "epl_highly_compensated_employee_salary")

        # c. Estimated total salary/wages and bonuses for all employees, including officers, owners and partners:
        self.employee_total_salary = self.driver.find_element(By.ID, "epl_employee_total_salary")

        # Has the Applicant transacted in the past 12 months, or does it anticipate transacting in the next 12 months, any layoffs, facility closings, relocations, or other reductions in force?
        self.months_transacted_yes = self.driver.find_element(By.ID, "epl_months_transacted-yes")

        self.months_transacted_no = self.driver.find_element(By.ID, "epl_months_transacted-no")

        # Does the Applicant compensate all interns?
        self.applicant_compensate_yes = self.driver.find_element(By.ID, "epl_applicant_compensate-yes")

        self.applicant_compensate_no = self.driver.find_element(By.ID, "epl_applicant_compensate-no")

        # Does the Applicant have guidelines to classify the status of each employee as Non-Exempt or Exempt under the rules and regulations of the Fair Labor Standards Act of 1938 (as amended)?
        self.applicant_guidelines_yes = self.driver.find_element(By.ID, "epl_applicant_guidelines-yes")

        self.applicant_guidelines_no = self.driver.find_element(By.ID, "epl_applicant_guidelines-no")

        # b. Number of highly compensated employees (total annual salary/wages and bonus exceed $100K):
        self.highly_compensated_employee_salary = self.driver.find_element(By.ID, "epl_highly_compensated_employee_salary")

        # c. Estimated total salary/wages and bonuses for all employees, including officers, owners and partners:
        self.employee_total_salary = self.driver.find_element(By.ID, "epl_employee_total_salary")

        # Has the Applicant transacted in the past 12 months, or does it anticipate transacting in the next 12 months, any layoffs, facility closings, relocations, or other reductions in force?
        self.months_transacted_yes = self.driver.find_element(By.ID, "epl_months_transacted-yes")

        self.months_transacted_no = self.driver.find_element(By.ID, "epl_months_transacted-no")

        # Does the Applicant compensate all interns?
        self.applicant_compensate_yes = self.driver.find_element(By.ID, "epl_applicant_compensate-yes")

        self.applicant_compensate_no = self.driver.find_element(By.ID, "epl_applicant_compensate-no")

        # Does the Applicant have guidelines to classify the status of each employee as Non-Exempt or Exempt under the rules and regulations of the Fair Labor Standards Act of 1938 (as amended)? Yes
        self.applicant_guidelines_yes = self.driver.find_element(By.ID, "epl_applicant_guidelines-yes")

        self.applicant_guidelines_no = self.driver.find_element(By.ID, "epl_applicant_guidelines-no")

        # Total turnover for preceding 12 months:

        # Employees:
        self.employee_turnover = self.driver.find_element(By.ID, "epl_turnover_employees")

        # Management:
        self.management_turnover = self.driver.find_element(By.ID, "epl_turnover_management")

        # Officers:
        self.officer_turnover = self.driver.find_element(By.ID, "epl_turnover_officers")

        # Does the Applicant distribute an employee handbook to every employee?
        self.employee_handbook_yes = self.driver.find_element(By.ID, "epl_employee_handbook-yes")

        self.employee_handbook_no = self.driver.find_element(By.ID, "epl_employee_handbook-no")

        # a. Does the handbook include procedures for sexual harassment and complaints of discrimination?
        self.include_harassment_yes = self.driver.find_element(By.ID, "epl_include_harassment-yes")

        self.include_harassment_no = self.driver.find_element(By.ID, "epl_include_harassment-no")

        # b. Does the handbook include procedures for handling employee grievances and complaints?
        self.handbook_grievances_yes = self.driver.find_element(By.ID, "epl_handbook_grievances-yes")

        self.handbook_grievances_no = self.driver.find_element(By.ID, "epl_handbook_grievances-no")

        # c. Has the handbook been reviewed by outside counsel in the past 24 months?
        self.handbook_reviewed_yes = self.driver.find_element(By.ID, "epl_handbook_reviewed-yes")

        self.handbook_reviewed_no = self.driver.find_element(By.ID, "epl_handbook_reviewed-no")

        # Does the Applicant have a Human Resources Department?
        self.applicant_hrdept_yes = self.driver.find_element(By.ID, "epl_applicant_hrdept-yes")

        self.applicant_hrdept_no = self.driver.find_element(By.ID, "epl_applicant_hrdept-no")

        # Have all management staff and officers attended sexual harassment training in the past 18 months?
        self.staff_training_yes = self.driver.find_element(By.ID, "epl_staff_training-yes")

        self.staff_training_no = self.driver.find_element(By.ID, "epl_staff_training-no")

        return self

    def create_quote_EPL_Greater_Than_3years_Yes_10_Percent_Employee_Turnover(self, High_Comp_Salary, Total_Salary_Employee, emp_turnover_rate, mgmt_turnover_rate, officer_turnover_rate):
        PAF.Page_Elements(self).applicant_longerthan_three_years_yes.click()
        PAF.Page_Elements(self).applicant_publicly_held_no.click()
        PAF.Page_Elements(self).change_in_total_assets_no.click()
        PAF.Page_Elements(self).transaction_in_next_months_no.click()
        PAF.Page_Elements(self).similar_coverage_no.click()
        PAF.Page_Elements(self).investigation_no.click()
        PAF.Page_Elements(self).aware_insurance_facts_no.click()
        PAF.Page_Elements(self).highly_compensated_employee_salary.send_keys(High_Comp_Salary)
        PAF.Page_Elements(self).employee_total_salary.send_keys(Total_Salary_Employee)
        PAF.Page_Elements(self).months_transacted_no.click()
        PAF.Page_Elements(self).applicant_compensate_yes.click()
        PAF.Page_Elements(self).applicant_guidelines_yes.click()
        PAF.Page_Elements(self).employee_turnover.send_keys(emp_turnover_rate)
        PAF.Page_Elements(self).management_turnover.send_keys(mgmt_turnover_rate)
        PAF.Page_Elements(self).officer_turnover.send_keys(officer_turnover_rate)
        PAF.Page_Elements(self).employee_handbook_yes.click()
        PAF.Page_Elements(self).include_harassment_yes.click()
        PAF.Page_Elements(self).handbook_grievances_yes.click()
        PAF.Page_Elements(self).handbook_reviewed_yes.click()
        PAF.Page_Elements(self).applicant_hrdept_yes.click()
        PAF.Page_Elements(self).staff_training_yes.click()

    def create_quote_EPL_Greater_Than_3years_Yes_15_Percent_Employee_Turnover(self, High_Comp_Salary, Total_Salary_Employee, emp_turnover_rate, mgmt_turnover_rate, officer_turnover_rate):

        PAF.Page_Elements(self).applicant_longerthan_three_years_yes.click()
        PAF.Page_Elements(self).applicant_publicly_held_no.click()
        PAF.Page_Elements(self).change_in_total_assets_no.click()
        PAF.Page_Elements(self).transaction_in_next_months_no.click()
        PAF.Page_Elements(self).similar_coverage_no.click()
        PAF.Page_Elements(self).investigation_no.click()
        PAF.Page_Elements(self).aware_insurance_facts_no.click()
        PAF.Page_Elements(self).highly_compensated_employee_salary.send_keys(High_Comp_Salary)
        PAF.Page_Elements(self).employee_total_salary.send_keys(Total_Salary_Employee)
        PAF.Page_Elements(self).months_transacted_no.click()
        PAF.Page_Elements(self).applicant_compensate_yes.click()
        PAF.Page_Elements(self).applicant_guidelines_yes.click()
        PAF.Page_Elements(self).employee_turnover.send_keys(emp_turnover_rate)
        PAF.Page_Elements(self).management_turnover.send_keys(mgmt_turnover_rate)
        PAF.Page_Elements(self).officer_turnover.send_keys(officer_turnover_rate)
        PAF.Page_Elements(self).employee_handbook_yes.click()
        PAF.Page_Elements(self).include_harassment_yes.click()
        PAF.Page_Elements(self).handbook_grievances_yes.click()
        PAF.Page_Elements(self).handbook_reviewed_yes.click()
        PAF.Page_Elements(self).applicant_hrdept_yes.click()
        PAF.Page_Elements(self).staff_training_yes.click()

    def create_quote_EPL_Greater_Than_3years_Yes_20_Percent_Employee_Turnover(self, High_Comp_Salary, Total_Salary_Employee, emp_turnover_rate, mgmt_turnover_rate, officer_turnover_rate):
        PAF.Page_Elements(self).applicant_longerthan_three_years_yes.click()
        PAF.Page_Elements(self).applicant_publicly_held_no.click()
        PAF.Page_Elements(self).change_in_total_assets_no.click()
        PAF.Page_Elements(self).transaction_in_next_months_no.click()
        PAF.Page_Elements(self).similar_coverage_no.click()
        PAF.Page_Elements(self).investigation_no.click()
        PAF.Page_Elements(self).aware_insurance_facts_no.click()
        PAF.Page_Elements(self).highly_compensated_employee_salary.send_keys(High_Comp_Salary)
        PAF.Page_Elements(self).employee_total_salary.send_keys(Total_Salary_Employee)
        PAF.Page_Elements(self).months_transacted_no.click()
        PAF.Page_Elements(self).applicant_compensate_yes.click()
        PAF.Page_Elements(self).applicant_guidelines_yes.click()
        PAF.Page_Elements(self).employee_turnover.send_keys(emp_turnover_rate)
        PAF.Page_Elements(self).management_turnover.send_keys(mgmt_turnover_rate)
        PAF.Page_Elements(self).officer_turnover.send_keys(officer_turnover_rate)
        PAF.Page_Elements(self).employee_handbook_yes.click()
        PAF.Page_Elements(self).include_harassment_yes.click()
        PAF.Page_Elements(self).handbook_grievances_yes.click()
        PAF.Page_Elements(self).handbook_reviewed_yes.click()
        PAF.Page_Elements(self).applicant_hrdept_yes.click()
        PAF.Page_Elements(self).staff_training_yes.click()

    def create_quote_EPL_Greater_Than_3years_No_10_Percent_Employee_Turnover(self, High_Comp_Salary, Total_Salary_Employee, emp_turnover_rate, mgmt_turnover_rate, officer_turnover_rate):
        PAF.Page_Elements(self).applicant_longerthan_three_years_no.click()
        PAF.Page_Elements(self).applicant_publicly_held_no.click()
        PAF.Page_Elements(self).change_in_total_assets_no.click()
        PAF.Page_Elements(self).transaction_in_next_months_no.click()
        PAF.Page_Elements(self).similar_coverage_no.click()
        PAF.Page_Elements(self).investigation_no.click()
        PAF.Page_Elements(self).aware_insurance_facts_no.click()
        PAF.Page_Elements(self).highly_compensated_employee_salary.send_keys(High_Comp_Salary)
        PAF.Page_Elements(self).employee_total_salary.send_keys(Total_Salary_Employee)
        PAF.Page_Elements(self).months_transacted_no.click()
        PAF.Page_Elements(self).applicant_compensate_yes.click()
        PAF.Page_Elements(self).applicant_guidelines_yes.click()
        PAF.Page_Elements(self).employee_turnover.send_keys(emp_turnover_rate)
        PAF.Page_Elements(self).management_turnover.send_keys(mgmt_turnover_rate)
        PAF.Page_Elements(self).officer_turnover.send_keys(officer_turnover_rate)
        PAF.Page_Elements(self).employee_handbook_yes.click()
        PAF.Page_Elements(self).include_harassment_yes.click()
        PAF.Page_Elements(self).handbook_grievances_yes.click()
        PAF.Page_Elements(self).handbook_reviewed_yes.click()
        PAF.Page_Elements(self).applicant_hrdept_yes.click()
        PAF.Page_Elements(self).staff_training_yes.click()

    def create_quote_EPL_Greater_Than_3years_No_15_Percent_Employee_Turnover(self, High_Comp_Salary, Total_Salary_Employee, emp_turnover_rate, mgmt_turnover_rate, officer_turnover_rate):
        PAF.Page_Elements(self).applicant_longerthan_three_years_no.click()
        PAF.Page_Elements(self).applicant_publicly_held_no.click()
        PAF.Page_Elements(self).change_in_total_assets_no.click()
        PAF.Page_Elements(self).transaction_in_next_months_no.click()
        PAF.Page_Elements(self).similar_coverage_no.click()
        PAF.Page_Elements(self).investigation_no.click()
        PAF.Page_Elements(self).aware_insurance_facts_no.click()
        PAF.Page_Elements(self).highly_compensated_employee_salary.send_keys(High_Comp_Salary)
        PAF.Page_Elements(self).employee_total_salary.send_keys(Total_Salary_Employee)
        PAF.Page_Elements(self).months_transacted_no.click()
        PAF.Page_Elements(self).applicant_compensate_yes.click()
        PAF.Page_Elements(self).applicant_guidelines_yes.click()
        PAF.Page_Elements(self).employee_turnover.send_keys(emp_turnover_rate)
        PAF.Page_Elements(self).management_turnover.send_keys(mgmt_turnover_rate)
        PAF.Page_Elements(self).officer_turnover.send_keys(officer_turnover_rate)
        PAF.Page_Elements(self).employee_handbook_yes.click()
        PAF.Page_Elements(self).include_harassment_yes.click()
        PAF.Page_Elements(self).handbook_grievances_yes.click()
        PAF.Page_Elements(self).handbook_reviewed_yes.click()
        PAF.Page_Elements(self).applicant_hrdept_yes.click()
        PAF.Page_Elements(self).staff_training_yes.click()

    def create_quote_EPL_Greater_Than_3years_No_20_Percent_Employee_Turnover(self, High_Comp_Salary, Total_Salary_Employee, emp_turnover_rate, mgmt_turnover_rate, officer_turnover_rate):

        PAF.Page_Elements(self).applicant_longerthan_three_years_no.click()
        PAF.Page_Elements(self).applicant_publicly_held_no.click()
        PAF.Page_Elements(self).change_in_total_assets_no.click()
        PAF.Page_Elements(self).transaction_in_next_months_no.click()
        PAF.Page_Elements(self).similar_coverage_no.click()
        PAF.Page_Elements(self).investigation_no.click()
        PAF.Page_Elements(self).aware_insurance_facts_no.click()
        PAF.Page_Elements(self).highly_compensated_employee_salary.send_keys(High_Comp_Salary)
        PAF.Page_Elements(self).employee_total_salary.send_keys(Total_Salary_Employee)
        PAF.Page_Elements(self).months_transacted_no.click()
        PAF.Page_Elements(self).applicant_compensate_yes.click()
        PAF.Page_Elements(self).applicant_guidelines_yes.click()
        PAF.Page_Elements(self).employee_turnover.send_keys(emp_turnover_rate)
        PAF.Page_Elements(self).management_turnover.send_keys(mgmt_turnover_rate)
        PAF.Page_Elements(self).officer_turnover.send_keys(officer_turnover_rate)
        PAF.Page_Elements(self).employee_handbook_yes.click()
        PAF.Page_Elements(self).include_harassment_yes.click()
        PAF.Page_Elements(self).handbook_grievances_yes.click()
        PAF.Page_Elements(self).handbook_reviewed_yes.click()
        PAF.Page_Elements(self).applicant_hrdept_yes.click()
        PAF.Page_Elements(self).staff_training_yes.click()

    def create_quote_EPL_Greater_Than_3years_Yes_10_Percent_Mgmt_Turnover(self, High_Comp_Salary, Total_Salary_Employee, emp_turnover_rate, mgmt_turnover_rate, officer_turnover_rate):
        PAF.Page_Elements(self).applicant_longerthan_three_years_yes.click()
        PAF.Page_Elements(self).applicant_publicly_held_no.click()
        PAF.Page_Elements(self).change_in_total_assets_no.click()
        PAF.Page_Elements(self).transaction_in_next_months_no.click()
        PAF.Page_Elements(self).similar_coverage_no.click()
        PAF.Page_Elements(self).investigation_no.click()
        PAF.Page_Elements(self).aware_insurance_facts_no.click()
        PAF.Page_Elements(self).highly_compensated_employee_salary.send_keys(High_Comp_Salary)
        PAF.Page_Elements(self).employee_total_salary.send_keys(Total_Salary_Employee)
        PAF.Page_Elements(self).months_transacted_no.click()
        PAF.Page_Elements(self).applicant_compensate_yes.click()
        PAF.Page_Elements(self).applicant_guidelines_yes.click()
        PAF.Page_Elements(self).employee_turnover.send_keys(emp_turnover_rate)
        PAF.Page_Elements(self).management_turnover.send_keys(mgmt_turnover_rate)
        PAF.Page_Elements(self).officer_turnover.send_keys(officer_turnover_rate)
        PAF.Page_Elements(self).employee_handbook_yes.click()
        PAF.Page_Elements(self).include_harassment_yes.click()
        PAF.Page_Elements(self).handbook_grievances_yes.click()
        PAF.Page_Elements(self).handbook_reviewed_yes.click()
        PAF.Page_Elements(self).applicant_hrdept_yes.click()
        PAF.Page_Elements(self).staff_training_yes.click()

    def create_quote_EPL_Greater_Than_3years_Yes_15_Percent_Mgmt_Turnover(self, High_Comp_Salary, Total_Salary_Employee, emp_turnover_rate, mgmt_turnover_rate, officer_turnover_rate):
        PAF.Page_Elements(self).applicant_longerthan_three_years_yes.click()
        PAF.Page_Elements(self).applicant_publicly_held_no.click()
        PAF.Page_Elements(self).change_in_total_assets_no.click()
        PAF.Page_Elements(self).transaction_in_next_months_no.click()
        PAF.Page_Elements(self).similar_coverage_no.click()
        PAF.Page_Elements(self).investigation_no.click()
        PAF.Page_Elements(self).aware_insurance_facts_no.click()
        PAF.Page_Elements(self).highly_compensated_employee_salary.send_keys(High_Comp_Salary)
        PAF.Page_Elements(self).employee_total_salary.send_keys(Total_Salary_Employee)
        PAF.Page_Elements(self).months_transacted_no.click()
        PAF.Page_Elements(self).applicant_compensate_yes.click()
        PAF.Page_Elements(self).applicant_guidelines_yes.click()
        PAF.Page_Elements(self).employee_turnover.send_keys(emp_turnover_rate)
        PAF.Page_Elements(self).management_turnover.send_keys(mgmt_turnover_rate)
        PAF.Page_Elements(self).officer_turnover.send_keys(officer_turnover_rate)
        PAF.Page_Elements(self).employee_handbook_yes.click()
        PAF.Page_Elements(self).include_harassment_yes.click()
        PAF.Page_Elements(self).handbook_grievances_yes.click()
        PAF.Page_Elements(self).handbook_reviewed_yes.click()
        PAF.Page_Elements(self).applicant_hrdept_yes.click()
        PAF.Page_Elements(self).staff_training_yes.click()

    def create_quote_EPL_Greater_Than_3years_Yes_20_Percent_Mgmt_Turnover(self, High_Comp_Salary, Total_Salary_Employee, emp_turnover_rate, mgmt_turnover_rate, officer_turnover_rate):
        PAF.Page_Elements(self).applicant_longerthan_three_years_yes.click()
        PAF.Page_Elements(self).applicant_publicly_held_no.click()
        PAF.Page_Elements(self).change_in_total_assets_no.click()
        PAF.Page_Elements(self).transaction_in_next_months_no.click()
        PAF.Page_Elements(self).similar_coverage_no.click()
        PAF.Page_Elements(self).investigation_no.click()
        PAF.Page_Elements(self).aware_insurance_facts_no.click()
        PAF.Page_Elements(self).highly_compensated_employee_salary.send_keys(High_Comp_Salary)
        PAF.Page_Elements(self).employee_total_salary.send_keys(Total_Salary_Employee)
        PAF.Page_Elements(self).months_transacted_no.click()
        PAF.Page_Elements(self).applicant_compensate_yes.click()
        PAF.Page_Elements(self).applicant_guidelines_yes.click()
        PAF.Page_Elements(self).employee_turnover.send_keys(emp_turnover_rate)
        PAF.Page_Elements(self).management_turnover.send_keys(mgmt_turnover_rate)
        PAF.Page_Elements(self).officer_turnover.send_keys(officer_turnover_rate)
        PAF.Page_Elements(self).employee_handbook_yes.click()
        PAF.Page_Elements(self).include_harassment_yes.click()
        PAF.Page_Elements(self).handbook_grievances_yes.click()
        PAF.Page_Elements(self).handbook_reviewed_yes.click()
        PAF.Page_Elements(self).applicant_hrdept_yes.click()
        PAF.Page_Elements(self).staff_training_yes.click()

    def create_quote_EPL_Greater_Than_3years_No_10_Percent_Mgmt_Turnover(self, High_Comp_Salary, Total_Salary_Employee, emp_turnover_rate, mgmt_turnover_rate, officer_turnover_rate):
        PAF.Page_Elements(self).applicant_longerthan_three_years_no.click()
        PAF.Page_Elements(self).applicant_publicly_held_no.click()
        PAF.Page_Elements(self).change_in_total_assets_no.click()
        PAF.Page_Elements(self).transaction_in_next_months_no.click()
        PAF.Page_Elements(self).similar_coverage_no.click()
        PAF.Page_Elements(self).investigation_no.click()
        PAF.Page_Elements(self).aware_insurance_facts_no.click()
        PAF.Page_Elements(self).highly_compensated_employee_salary.send_keys(High_Comp_Salary)
        PAF.Page_Elements(self).employee_total_salary.send_keys(Total_Salary_Employee)
        PAF.Page_Elements(self).months_transacted_no.click()
        PAF.Page_Elements(self).applicant_compensate_yes.click()
        PAF.Page_Elements(self).applicant_guidelines_yes.click()
        PAF.Page_Elements(self).employee_turnover.send_keys(emp_turnover_rate)
        PAF.Page_Elements(self).management_turnover.send_keys(mgmt_turnover_rate)
        PAF.Page_Elements(self).officer_turnover.send_keys(officer_turnover_rate)
        PAF.Page_Elements(self).employee_handbook_yes.click()
        PAF.Page_Elements(self).include_harassment_yes.click()
        PAF.Page_Elements(self).handbook_grievances_yes.click()
        PAF.Page_Elements(self).handbook_reviewed_yes.click()
        PAF.Page_Elements(self).applicant_hrdept_yes.click()
        PAF.Page_Elements(self).staff_training_yes.click()

    def create_quote_EPL_Greater_Than_3years_No_15_Percent_Mgmt_Turnover(self, High_Comp_Salary, Total_Salary_Employee, emp_turnover_rate, mgmt_turnover_rate, officer_turnover_rate):
        PAF.Page_Elements(self).applicant_longerthan_three_years_no.click()
        PAF.Page_Elements(self).applicant_publicly_held_no.click()
        PAF.Page_Elements(self).change_in_total_assets_no.click()
        PAF.Page_Elements(self).transaction_in_next_months_no.click()
        PAF.Page_Elements(self).similar_coverage_no.click()
        PAF.Page_Elements(self).investigation_no.click()
        PAF.Page_Elements(self).aware_insurance_facts_no.click()
        PAF.Page_Elements(self).highly_compensated_employee_salary.send_keys(High_Comp_Salary)
        PAF.Page_Elements(self).employee_total_salary.send_keys(Total_Salary_Employee)
        PAF.Page_Elements(self).months_transacted_no.click()
        PAF.Page_Elements(self).applicant_compensate_yes.click()
        PAF.Page_Elements(self).applicant_guidelines_yes.click()
        PAF.Page_Elements(self).employee_turnover.send_keys(emp_turnover_rate)
        PAF.Page_Elements(self).management_turnover.send_keys(mgmt_turnover_rate)
        PAF.Page_Elements(self).officer_turnover.send_keys(officer_turnover_rate)
        PAF.Page_Elements(self).employee_handbook_yes.click()
        PAF.Page_Elements(self).include_harassment_yes.click()
        PAF.Page_Elements(self).handbook_grievances_yes.click()
        PAF.Page_Elements(self).handbook_reviewed_yes.click()
        PAF.Page_Elements(self).applicant_hrdept_yes.click()
        PAF.Page_Elements(self).staff_training_yes.click()

    def create_quote_EPL_Greater_Than_3years_No_20_Percent_Mgmt_Turnover(self, High_Comp_Salary, Total_Salary_Employee, emp_turnover_rate, mgmt_turnover_rate, officer_turnover_rate):
        PAF.Page_Elements(self).applicant_longerthan_three_years_no.click()
        PAF.Page_Elements(self).applicant_publicly_held_no.click()
        PAF.Page_Elements(self).change_in_total_assets_no.click()
        PAF.Page_Elements(self).transaction_in_next_months_no.click()
        PAF.Page_Elements(self).similar_coverage_no.click()
        PAF.Page_Elements(self).investigation_no.click()
        PAF.Page_Elements(self).aware_insurance_facts_no.click()
        PAF.Page_Elements(self).highly_compensated_employee_salary.send_keys(High_Comp_Salary)
        PAF.Page_Elements(self).employee_total_salary.send_keys(Total_Salary_Employee)
        PAF.Page_Elements(self).months_transacted_no.click()
        PAF.Page_Elements(self).applicant_compensate_yes.click()
        PAF.Page_Elements(self).applicant_guidelines_yes.click()
        PAF.Page_Elements(self).employee_turnover.send_keys(emp_turnover_rate)
        PAF.Page_Elements(self).management_turnover.send_keys(mgmt_turnover_rate)
        PAF.Page_Elements(self).officer_turnover.send_keys(officer_turnover_rate)
        PAF.Page_Elements(self).employee_handbook_yes.click()
        PAF.Page_Elements(self).include_harassment_yes.click()
        PAF.Page_Elements(self).handbook_grievances_yes.click()
        PAF.Page_Elements(self).handbook_reviewed_yes.click()
        PAF.Page_Elements(self).applicant_hrdept_yes.click()
        PAF.Page_Elements(self).staff_training_yes.click()

    def create_quote_EPL_Greater_Than_3years_Yes_10_Percent_Officers_Turnover(self, High_Comp_Salary, Total_Salary_Employee, emp_turnover_rate, mgmt_turnover_rate, officer_turnover_rate):
        PAF.Page_Elements(self).applicant_longerthan_three_years_yes.click()
        PAF.Page_Elements(self).applicant_publicly_held_no.click()
        PAF.Page_Elements(self).change_in_total_assets_no.click()
        PAF.Page_Elements(self).transaction_in_next_months_no.click()
        PAF.Page_Elements(self).similar_coverage_no.click()
        PAF.Page_Elements(self).investigation_no.click()
        PAF.Page_Elements(self).aware_insurance_facts_no.click()
        PAF.Page_Elements(self).highly_compensated_employee_salary.send_keys(High_Comp_Salary)
        PAF.Page_Elements(self).employee_total_salary.send_keys(Total_Salary_Employee)
        PAF.Page_Elements(self).months_transacted_no.click()
        PAF.Page_Elements(self).applicant_compensate_yes.click()
        PAF.Page_Elements(self).applicant_guidelines_yes.click()
        PAF.Page_Elements(self).employee_turnover.send_keys(emp_turnover_rate)
        PAF.Page_Elements(self).management_turnover.send_keys(mgmt_turnover_rate)
        PAF.Page_Elements(self).officer_turnover.send_keys(officer_turnover_rate)
        PAF.Page_Elements(self).employee_handbook_yes.click()
        PAF.Page_Elements(self).include_harassment_yes.click()
        PAF.Page_Elements(self).handbook_grievances_yes.click()
        PAF.Page_Elements(self).handbook_reviewed_yes.click()
        PAF.Page_Elements(self).applicant_hrdept_yes.click()
        PAF.Page_Elements(self).staff_training_yes.click()

    def create_quote_EPL_Greater_Than_3years_Yes_15_Percent_Officers_Turnover(self, High_Comp_Salary, Total_Salary_Employee, emp_turnover_rate, mgmt_turnover_rate, officer_turnover_rate):
        PAF.Page_Elements(self).applicant_longerthan_three_years_yes.click()
        PAF.Page_Elements(self).applicant_publicly_held_no.click()
        PAF.Page_Elements(self).change_in_total_assets_no.click()
        PAF.Page_Elements(self).transaction_in_next_months_no.click()
        PAF.Page_Elements(self).similar_coverage_no.click()
        PAF.Page_Elements(self).investigation_no.click()
        PAF.Page_Elements(self).aware_insurance_facts_no.click()
        PAF.Page_Elements(self).highly_compensated_employee_salary.send_keys(High_Comp_Salary)
        PAF.Page_Elements(self).employee_total_salary.send_keys(Total_Salary_Employee)
        PAF.Page_Elements(self).months_transacted_no.click()
        PAF.Page_Elements(self).applicant_compensate_yes.click()
        PAF.Page_Elements(self).applicant_guidelines_yes.click()
        PAF.Page_Elements(self).employee_turnover.send_keys(emp_turnover_rate)
        PAF.Page_Elements(self).management_turnover.send_keys(mgmt_turnover_rate)
        PAF.Page_Elements(self).officer_turnover.send_keys(officer_turnover_rate)
        PAF.Page_Elements(self).employee_handbook_yes.click()
        PAF.Page_Elements(self).include_harassment_yes.click()
        PAF.Page_Elements(self).handbook_grievances_yes.click()
        PAF.Page_Elements(self).handbook_reviewed_yes.click()
        PAF.Page_Elements(self).applicant_hrdept_yes.click()
        PAF.Page_Elements(self).staff_training_yes.click()

    def create_quote_EPL_Greater_Than_3years_Yes_20_Percent_Officers_Turnover(self, High_Comp_Salary, Total_Salary_Employee, emp_turnover_rate, mgmt_turnover_rate, officer_turnover_rate):
        PAF.Page_Elements(self).applicant_longerthan_three_years_yes.click()
        PAF.Page_Elements(self).applicant_publicly_held_no.click()
        PAF.Page_Elements(self).change_in_total_assets_no.click()
        PAF.Page_Elements(self).transaction_in_next_months_no.click()
        PAF.Page_Elements(self).similar_coverage_no.click()
        PAF.Page_Elements(self).investigation_no.click()
        PAF.Page_Elements(self).aware_insurance_facts_no.click()
        PAF.Page_Elements(self).highly_compensated_employee_salary.send_keys(High_Comp_Salary)
        PAF.Page_Elements(self).employee_total_salary.send_keys(Total_Salary_Employee)
        PAF.Page_Elements(self).months_transacted_no.click()
        PAF.Page_Elements(self).applicant_compensate_yes.click()
        PAF.Page_Elements(self).applicant_guidelines_yes.click()
        PAF.Page_Elements(self).employee_turnover.send_keys(emp_turnover_rate)
        PAF.Page_Elements(self).management_turnover.send_keys(mgmt_turnover_rate)
        PAF.Page_Elements(self).officer_turnover.send_keys(officer_turnover_rate)
        PAF.Page_Elements(self).employee_handbook_yes.click()
        PAF.Page_Elements(self).include_harassment_yes.click()
        PAF.Page_Elements(self).handbook_grievances_yes.click()
        PAF.Page_Elements(self).handbook_reviewed_yes.click()
        PAF.Page_Elements(self).applicant_hrdept_yes.click()
        PAF.Page_Elements(self).staff_training_yes.click()

    def create_quote_EPL_Greater_Than_3years_No_10_Percent_Officers_Turnover(self, High_Comp_Salary, Total_Salary_Employee, emp_turnover_rate, mgmt_turnover_rate, officer_turnover_rate):
        PAF.Page_Elements(self).applicant_longerthan_three_years_no.click()
        PAF.Page_Elements(self).applicant_publicly_held_no.click()
        PAF.Page_Elements(self).change_in_total_assets_no.click()
        PAF.Page_Elements(self).transaction_in_next_months_no.click()
        PAF.Page_Elements(self).similar_coverage_no.click()
        PAF.Page_Elements(self).investigation_no.click()
        PAF.Page_Elements(self).aware_insurance_facts_no.click()
        PAF.Page_Elements(self).highly_compensated_employee_salary.send_keys(High_Comp_Salary)
        PAF.Page_Elements(self).employee_total_salary.send_keys(Total_Salary_Employee)
        PAF.Page_Elements(self).months_transacted_no.click()
        PAF.Page_Elements(self).applicant_compensate_yes.click()
        PAF.Page_Elements(self).applicant_guidelines_yes.click()
        PAF.Page_Elements(self).employee_turnover.send_keys(emp_turnover_rate)
        PAF.Page_Elements(self).management_turnover.send_keys(mgmt_turnover_rate)
        PAF.Page_Elements(self).officer_turnover.send_keys(officer_turnover_rate)
        PAF.Page_Elements(self).employee_handbook_yes.click()
        PAF.Page_Elements(self).include_harassment_yes.click()
        PAF.Page_Elements(self).handbook_grievances_yes.click()
        PAF.Page_Elements(self).handbook_reviewed_yes.click()
        PAF.Page_Elements(self).applicant_hrdept_yes.click()
        PAF.Page_Elements(self).staff_training_yes.click()

    def create_quote_EPL_Greater_Than_3years_No_15_Percent_Officers_Turnover(self, High_Comp_Salary, Total_Salary_Employee, emp_turnover_rate, mgmt_turnover_rate, officer_turnover_rate):
        PAF.Page_Elements(self).applicant_longerthan_three_years_no.click()
        PAF.Page_Elements(self).applicant_publicly_held_no.click()
        PAF.Page_Elements(self).change_in_total_assets_no.click()
        PAF.Page_Elements(self).transaction_in_next_months_no.click()
        PAF.Page_Elements(self).similar_coverage_no.click()
        PAF.Page_Elements(self).investigation_no.click()
        PAF.Page_Elements(self).aware_insurance_facts_no.click()
        PAF.Page_Elements(self).highly_compensated_employee_salary.send_keys(High_Comp_Salary)
        PAF.Page_Elements(self).employee_total_salary.send_keys(Total_Salary_Employee)
        PAF.Page_Elements(self).months_transacted_no.click()
        PAF.Page_Elements(self).applicant_compensate_yes.click()
        PAF.Page_Elements(self).applicant_guidelines_yes.click()
        PAF.Page_Elements(self).employee_turnover.send_keys(emp_turnover_rate)
        PAF.Page_Elements(self).management_turnover.send_keys(mgmt_turnover_rate)
        PAF.Page_Elements(self).officer_turnover.send_keys(officer_turnover_rate)
        PAF.Page_Elements(self).employee_handbook_yes.click()
        PAF.Page_Elements(self).include_harassment_yes.click()
        PAF.Page_Elements(self).handbook_grievances_yes.click()
        PAF.Page_Elements(self).handbook_reviewed_yes.click()
        PAF.Page_Elements(self).applicant_hrdept_yes.click()
        PAF.Page_Elements(self).staff_training_yes.click()

    def create_quote_EPL_Greater_Than_3years_No_20_Percent_Officers_Turnover(self, High_Comp_Salary, Total_Salary_Employee, emp_turnover_rate, mgmt_turnover_rate, officer_turnover_rate):
        PAF.Page_Elements(self).applicant_longerthan_three_years_no.click()
        PAF.Page_Elements(self).applicant_publicly_held_no.click()
        PAF.Page_Elements(self).change_in_total_assets_no.click()
        PAF.Page_Elements(self).transaction_in_next_months_no.click()
        PAF.Page_Elements(self).similar_coverage_no.click()
        PAF.Page_Elements(self).investigation_no.click()
        PAF.Page_Elements(self).aware_insurance_facts_no.click()
        PAF.Page_Elements(self).highly_compensated_employee_salary.send_keys(High_Comp_Salary)
        PAF.Page_Elements(self).employee_total_salary.send_keys(Total_Salary_Employee)
        PAF.Page_Elements(self).months_transacted_no.click()
        PAF.Page_Elements(self).applicant_compensate_yes.click()
        PAF.Page_Elements(self).applicant_guidelines_yes.click()
        PAF.Page_Elements(self).employee_turnover.send_keys(emp_turnover_rate)
        PAF.Page_Elements(self).management_turnover.send_keys(mgmt_turnover_rate)
        PAF.Page_Elements(self).officer_turnover.send_keys(officer_turnover_rate)
        PAF.Page_Elements(self).employee_handbook_yes.click()
        PAF.Page_Elements(self).include_harassment_yes.click()
        PAF.Page_Elements(self).handbook_grievances_yes.click()
        PAF.Page_Elements(self).handbook_reviewed_yes.click()
        PAF.Page_Elements(self).applicant_hrdept_yes.click()
        PAF.Page_Elements(self).staff_training_yes.click()

    #TODO
    # Ask Dev to create ID for next button
    def click_next(self):
        next_button = self.driver.find_element(By.XPATH, "//form[@id='primary']/div[5]/a/span[2]/span/span")
        next_button.click()

    def click_return_to_Admin_Interface(self):
        PAF.Page_Elements(self).return_to_Admin.click()