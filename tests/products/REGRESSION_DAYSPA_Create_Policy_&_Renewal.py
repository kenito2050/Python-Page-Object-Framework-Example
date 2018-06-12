import csv
import datetime
import os
import time
import unittest
from urllib.parse import urlparse, parse_qs
from xml.etree import ElementTree as ET

import xlrd
from faker import address
from faker import company
from faker import name
from selenium import webdriver

from pages.producer_center.products_programs_page import ProductsAndPrograms
from pages.producer_center.client_search_page import ClientSearch
from pages.producer_center.my_policies.my_policies_screens.active_policies import active_policies
from pages.producer_center.navigation_bar import Navigation_Bar
from pages.producer_center.client_contact_page import ClientContact
from pages.producer_center.saw.coverage_periods_page import CoveragePeriods
from pages.producer_center.saw.products.DAYSPA.insured_information.insured_information import Insured_Information
from pages.producer_center.saw.products.DAYSPA.PAF.PAF import PAF
from pages.producer_center.saw.products.DAYSPA.coverage_options.coverage_options import Coverage_Options
from pages.producer_center.saw.products.DAYSPA.coverage_options.Product_Liability.Product_Liability_coverage_options import Product_Liability_Coverage_Options
from pages.producer_center.saw.products.DAYSPA.coverage_options.No_Product_Liability.No_Product_Liability_coverage_options import No_Product_Liability_Coverage_Options
from pages.producer_center.saw.products.DAYSPA.select_option.select_option import Select_Option
from pages.producer_center.saw.quote_review import Quote_Review
from pages.producer_center.saw.invoice import Invoice
from pages.producer_center.saw.confirm_order_details import Confirm_Order_Details
from pages.producer_center.saw.confirm_and_issue import Confirm_and_Issue
from pages.producer_center.saw.thank_you_page import Thank_You_Page
from pages.producer_center.saw.summary import Summary
from pages.service_center.agents_page import AgentsPage
from pages.service_center.applications_page import ApplicationsPage
from pages.service_center.application_screens.details import App_Details
from pages.service_center.login_page import LoginPage
from pages.service_center.navigation_bar import NavigationBar
from pages.service_center.policies_page import PoliciesPage
from pages.service_center.policy_screens.policy_screens import Policy_Screens
from pages.service_center.policy_screens.details import Details
from pages.service_center.agent_screens.agent_details import Agent_Details
from pages.service_center.policy_screens.effective_periods import Effective_Periods
from pages.service_center.subjectivities import Subjectivities
from utilities.Environments.Environments import Environments
from utilities.contract_classes.contract_classes_Medical import ContractClasses_Medical
from utilities.state_capitals.state_capitals import StateCapitals
from utilities.zip_codes.zip_codes import ZipCodes


class CreateQuote():

    def test_login_search_for_agent_create_quote(self):

        Product = "DAYSPA"

        ## Directory Locations

        tests_directory = os.path.abspath(os.pardir)
        framework_directory = os.path.abspath(os.path.join(tests_directory, os.pardir))
        config_file_directory = os.path.abspath(os.path.join(framework_directory, 'config_files'))
        test_case_directory = os.path.abspath(os.path.join(framework_directory, 'utilities\Excel_Sheets\Products'))
        test_results_directory = os.path.abspath(
            os.path.join(framework_directory, 'utilities\Excel_Sheets\Test_Results'))

        # Determine the Test Run Type
        # Get Test Run Type Text from config file
        tree = ET.parse(os.path.join(config_file_directory, 'test_environment.xml'))
        test_environment = tree.getroot()
        test_run_type = (test_environment[1][0].text)
        test_run_type_value = ''

        # If / Else to convert test_run_type text to a value
        if test_run_type == "Regression":
            test_run_type_value = '1'
        elif test_run_type == "Smoke":
            test_run_type_value = '2'
        elif test_run_type == "Sanity":
            test_run_type_value = '3'

        global test_summary
        global test_scenario
        global effective_date
        global test_scenario_number
        global regression
        global smoke
        global sanity
        global agent
        global city
        global state
        global zip
        global number_locations
        global years_in_business
        global staff_count
        global number_procedures
        global revenue_last_year
        global revenue_upcoming_year
        global _OLD_scenario
        global _OLD_scenario_number


        # Open Test Scenario Workbook; Instantiate worksheet object
        wb = xlrd.open_workbook(os.path.join(test_case_directory, Product + '.xlsx'))
        sh = wb.sheet_by_index(1)

        ## Begin For Loop to iterate through Test Scenarios
        i = 1
        rows = sh.nrows
        empty_cell = False
        for x in range(1, sh.nrows):

            cell_val = sh.cell(i, 0).value
            if cell_val == '':
                # If Cell Value is empty, set empty_cell to True
                empty_cell = True
            else:
                # If Cell Value is NOT empty, set empty_cell to False
                empty_cell = False


            # Check to see if cell is NOT empty
            # If cell is not empty, read in the values
            if empty_cell == False:
                test_summary = sh.cell_value(i, 0)
                test_scenario = str(round(sh.cell_value(i, 1)))
                effective_date = sh.cell_value(i, 2)
                test_scenario_number = str(round(sh.cell_value(i, 3)))
                regression = sh.cell_value(i, 4)
                smoke = sh.cell_value(i, 5)
                sanity = sh.cell_value(i, 6)
                agent = sh.cell_value(i, 7)
                city = sh.cell_value(i, 8)
                state = sh.cell_value(i, 9)
                zip = str(round(sh.cell_value(i, 10)))
                number_locations = str(round(sh.cell_value(i, 11)))
                years_in_business = str(round(sh.cell_value(i, 12)))
                staff_count = str(round(sh.cell_value(i, 13)))
                number_procedures = str(round(sh.cell_value(i, 14)))
                revenue_last_year = str(round(sh.cell_value(i, 15)))
                revenue_upcoming_year = str(round(sh.cell_value(i, 16)))
                _OLD_scenario = sh.cell_value(i, 17)
                _OLD_scenario_number = str(round(sh.cell_value(i, 18)))

            # Else, the cell is empty
            # End the Loop
            else:
                break

        ## Determine Test Environment to run scripts

        ## Read in value from test_environment.xml
        tree = ET.parse(os.path.join(config_file_directory, 'test_environment.xml'))
        test_environment = tree.getroot()
        environment = (test_environment[0][0].text)

        ## Select Appropriate URL based on the Environment Value from above
        base_URL = Environments.return_environments(environment)

        first_name = name.first_name()
        last_name = name.last_name()
        company_name = company.company_name()
        # company_name_string = company_name
        company_name_string = "QA Test" + " " + "-" + " " + first_name + " " + last_name + " " + "dba" + " " + company_name
        address_value = address.street_address()
        city = StateCapitals.return_state_capital(state)
        postal_code = ZipCodes.return_zip_codes(state)

        # bed_count = "5"

        # Access XML to retrieve login credentials
        tree = ET.parse(os.path.join(config_file_directory, 'resources.xml'))
        login_credentials = tree.getroot()
        username = (login_credentials[0][0].text)
        password = (login_credentials[1][1].text)

        # Access XML to retrieve the agent to search for
        # tree = ET.parse('Agents.xml')
        # agents = tree.getroot()
        # agent = (agents[5][0].text)

        # Date Variables
        date_today = time.strftime("%m/%d/%Y")
        ad_hoc_effectiveDate = "09/06/2017"

        # Convert effective_date value to format MM/DD/YYYY
        d = xlrd.xldate_as_tuple(int(effective_date), 0)
        # convert date tuple in mm-dd-yyyy format
        d = datetime.datetime(*(d[0:3]))
        effective_date_formatted = d.strftime("%m/%d/%Y")


        # Initialize Driver
        # baseURL = "https://svcdemo2.wn.nasinsurance.com/"
        driver = webdriver.Chrome(os.path.join(config_file_directory, 'chromedriver.exe'))

        # Maximize Window; Launch URL
        driver.maximize_window()
        driver.get(base_URL)
        driver.implicitly_wait(3)

        # Call Login methods from Pages.home.login_page.py
        lp = LoginPage(driver)
        lp.login(username, password)
        lp.click_login_button()
        nb = NavigationBar(driver)
        nb.click_agents()
        ap = AgentsPage(driver)
        ap.search_for_agent(agent)
        ap.click_submit_new_application_as_agent()

        pp = ProductsAndPrograms(driver)
        pp.click_DAYSPA()

        # The following lines added on 5-15-17 work
        #pp.click_contract_class_drop_down_select_contract_class(contract_class)
        #pp.select_contract_class_dropdown()

        #pp.select_contract_class(contract_class)  # Script Ends Here
        #pp.click_continue_on_contract_class_modal_after_selecting_contract_class()

        cs = ClientSearch(driver)
        cs.input_bogus_client_data(postal_code)
        cs.manually_input_new_client()
        cs.enter_new_client_name_address(company_name_string, address_value, city, state)
        cc = ClientContact(driver)

        # TODO:
        # Code now parses URL String & retrieves application ID
        # cc.parse_url_get_app_id()

        # Get the Application ID from URL -- THIS WORKS
        current_url = driver.current_url
        first_url_string = urlparse(current_url)
        query_dict = parse_qs(first_url_string.query)
        application_id = (query_dict['app_id'][0])

        cc.click_next()

        cp = CoveragePeriods(driver)

        time.sleep(3)

        cp.click_return_to_Admin_Interface()

        # Navigate to Application Details page
        current_url_2 = driver.current_url
        slashparts = current_url_2.split('/')
        # Now join back the first three sections 'http:', '' and 'example.com'
        base_url_2 = '/'.join(slashparts[:3]) + '/'

        app_details_string = "?c=app.view&id="
        # app_subjectivities_string = "?c=app.track_subjectivities&id="

        application_details_screen = base_url_2 + app_details_string + application_id

        # Navigate to Application Subjectivities Screen
        driver.get(application_details_screen)

        app_details = App_Details(driver)

        # Update the Create Date to the Ad Hoc Effective Date Value
        app_details.update_create_date(date_today)

        # Click Update Button
        app_details.click_update_button()

        # Click on Agent Link to return to Producer Center
        app_details.click_agent_text_link()

        # Return to Coverage Periods screen

        # Enter an Ad Hoc Effective Date
        # cp.enter_ad_hoc_effective_date(effective_date_formatted)

        # Enter Today's Date as Effective Date
        cp.enter_current_date_as_effective_date(date_today)

        cp.click_next()

        # Enter Today's Date as Effective Date
        # cp.enter_current_date_as_effective_date(date_today)

        saw_ii = Insured_Information(driver)
        saw_ii.enter_location_count(number_locations)
        saw_ii.click_next()

        saw_PAF = PAF(driver)

        # Fill out PAF

        # Else / If to determine how PAF will be filled in
        # test_scenario 1, No Product Liability
        # test_scenario 2, Product Liability

        if test_scenario == "1":
            saw_PAF.create_quote_No_Product_Liability(years_in_business, staff_count, number_procedures, revenue_last_year, revenue_upcoming_year, effective_date_formatted)
        elif test_scenario == "2":
            saw_PAF.create_quote_Product_Liability(years_in_business, staff_count, number_procedures, revenue_last_year, revenue_upcoming_year, effective_date_formatted)

        # saw_PAF.create_quote_No_Product_Liability(years_in_business, number_procedures, revenue_last_year, revenue_upcoming_year, effective_date_formatted)

        # saw_PAF.create_quote_Product_Liability(years_in_business, number_procedures, revenue_last_year, revenue_upcoming_year, effective_date_formatted)

        # Click Next on PAF screen
        saw_PAF.click_next()

        #### This class is for generic objects that display on the Coverage Options page
        saw_CC = Coverage_Options(driver)

        # saw_CC.select_all_deselect_all()

        # No Product Liability
        if test_scenario_number == "1":
            saw_CC_in_use = No_Product_Liability_Coverage_Options(driver)
            # getattr(saw_CC_in_use, _OLD_scenario)()

        # Product Liability
        elif test_scenario_number == "2":
            saw_CC_in_use = Product_Liability_Coverage_Options(driver)
            # getattr(saw_CC_in_use, _OLD_scenario)()


        saw_CC.click_proceed_to_quote()

        saw_summary = Summary(driver)
        saw_summary.click_generate_quote()
        saw_quote_review = Quote_Review(driver)
        saw_quote_review.click_select_option()
        saw_select_option = Select_Option(driver)
        saw_select_option.select_premium()
        saw_select_option.click_accept_rate_and_continue()
        saw_confirm_order_details = Confirm_Order_Details(driver)
        saw_confirm_order_details.click_next()
        saw_invoice = Invoice(driver)
        saw_invoice.click_proceed_to_issuing()

        # Click Return to Admin Interface
        saw_confirm_issue = Confirm_and_Issue(driver)

        # At this point, script is re-directed to service center login screen
        # This works on DEV
        # TODO: FIX redirection; should redirect back to Service Center
        saw_confirm_issue.click_return_to_Admin_Interface()

        time.sleep(3)

        #This section is necessary ONLY on STAGE
        # Call Login methods from Pages.home.login_page.py
        #lp = LoginPage(driver)
        #lp.login(username, password)
        #nb = NavigationBar(driver)

        # Click Applications link on Navigation Bar
        nb.click_applications()

        # Enter Application ID, click Search
        app_page = ApplicationsPage(driver)
        app_page.enter_application_id(application_id)
        app_page.click_search_button()

        # Click on application id link
        # THIS IS NOT WORKING
        #app_page.click_application_id_link(application_id)

        # Navigate to Application Details page
        new_current_url = driver.current_url
        slashparts = new_current_url.split('/')
        # Now join back the first three sections 'http:', '' and 'example.com'
        new_base_url = '/'.join(slashparts[:3]) + '/'

        app_details_string = "?c=app.view&id="
        app_subjectivities_string = "?c=app.track_subjectivities&id="

        application_details_screen = new_base_url + app_details_string + application_id
        application_subjectivites_screen = new_base_url + app_subjectivities_string + application_id

        # Navigate to Application Subjectivities Screen
        driver.get(application_subjectivites_screen)

        # Approve Subjectivities
        # Added Anna's Subjectivities Code 5-15-17
        sub = Subjectivities(driver)
        sub.set_all_subjectivities_to_recieved()
        #sub.change_open_subjectivities_to_received()
        #sub.select_yes_to_subjectivities_met()
        sub.click_submit()
        sub.click_agent_link()

        # Return to Producer Center; Issue Policy
        saw_confirm_issue.input_signature()
        saw_confirm_issue.click_accept_terms_issue_policy()

        # Retrieve Policy Number of Policy that was issued; Policy Number stored in policy_text
        thank_you = Thank_You_Page(driver)
        policy_text = thank_you.retrieve_store_policy_number()

        # # Return to Admin Interface
        # saw_confirm_issue.click_return_to_Admin_Interface()
        #
        # # Click on Policies link; Navigate to Policy that was just issued
        # nb.click_policies()
        #
        # pp = PoliciesPage(driver)
        # # On Policies Page, Click All link
        # pp.click_all_link()
        #
        # # Enter Policy Number & Click Search
        # pp.enter_policy_name(policy_text)
        # pp.click_search_button()
        #
        # # Click on the Policy link, Open Policy Details
        # pp.click_policy_link(policy_text)
        #
        # # Click Effective Periods
        # ps = Policy_Screens(driver)
        # ps.click_Effective_Periods()
        #
        # # Change Effective Periods Dates to allow renewals
        # ep = Effective_Periods(driver)
        # ep.change_dates_expire_policy_allow_renewal()
        # ep.click_update_dates()
        #
        # # Click Details link to display the Policy Details screen
        # ps.click_Details()
        #
        # # On Details Screen, Click on the Agent that issued the Policy
        # details = Details(driver)
        # details.click_agent_link(agent)
        #
        # # Agent Details Screen Displays
        # ag = Agent_Details(driver)
        #
        # # Click "Submit New Application as" link
        # ag.click_submit_new_application_as_agent()
        #
        # # Click My Policies on Navigation Bar
        # pnb = Navigation_Bar(driver)
        # pnb.click_my_policies()
        #
        # # Locate Policy that was issued
        # ap = active_policies(driver)
        # ap.enter_policy_name(policy_text)
        # ap.click_search_button()
        #
        # # Click Policy
        # ap.click_policy_link(policy_text)

        # Code works up to this point

        # Declare the values that will be outputted to csv
        values = [test_summary, company_name_string, application_id, policy_text]

        # Declare Directory of csv file
        download_dir = os.path.join(test_results_directory, 'Regressions', Product + '_Regression_Test_Results.csv')

        # This Section Writes the output to the csv file
        with open(download_dir, "a") as f:
            writer = csv.writer(f, lineterminator='\n')  # lineterminator='\n'
            writer.writerow(values)

        # Declare the values that will be outputted to csv
        values = [test_summary, company_name_string, application_id, policy_text]

        # Declare Directory of csv file
        download_dir = os.path.join(test_results_directory, 'Regressions',
                                    Product + '_Regression_Test_Results.csv')  # where you want the file to be downloaded to

        with open(download_dir, "w") as f:

            writer = csv.writer(f)
            writer.writerow(
                {'Test Summary': test_summary, 'Insured': company_name_string, 'Application ID': application_id,
                 'Policy': policy_text})
            writer.writerow(values)

        # Wait
        driver.implicitly_wait(3)

        # Close Browser
        driver.quit()

        i += 1

cq = CreateQuote()
cq.test_login_search_for_agent_create_quote()