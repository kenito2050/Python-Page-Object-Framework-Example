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

from pages.producer_center.client_contact_page import ClientContact
from pages.producer_center.client_search_page import ClientSearch
from pages.producer_center.my_policies.my_policies_screens.active_policies import active_policies
from pages.producer_center.navigation_bar import Navigation_Bar
from pages.producer_center.products_programs_page import ProductsAndPrograms
from pages.producer_center.saw.confirm_and_issue import Confirm_and_Issue
from pages.producer_center.saw.confirm_order_details import Confirm_Order_Details
from pages.producer_center.saw.coverage_periods_page import CoveragePeriods
from pages.producer_center.saw.invoice import Invoice
from pages.producer_center.saw.products.LEXR_TENANT.PAF.PAF import PAF
from pages.producer_center.saw.products.LEXR_TENANT.coverage_options.coverage_options import Coverage_Options
from pages.producer_center.saw.products.LEXR_TENANT.insured_information.insured_information import Insured_Information
from pages.producer_center.saw.products.LEXR_TENANT.select_option.select_option import Select_Option
from pages.producer_center.saw.quote_review import Quote_Review
from pages.producer_center.saw.summary import Summary
from pages.producer_center.saw.thank_you_page import Thank_You_Page
from pages.service_center.agent_screens.agent_details import Agent_Details
from pages.service_center.agents_page import AgentsPage
from pages.service_center.application_screens.details import App_Details
from pages.service_center.applications_page import ApplicationsPage
from pages.service_center.login_page import LoginPage
from pages.service_center.navigation_bar import NavigationBar
from pages.service_center.policies_page import PoliciesPage
from pages.service_center.policy_screens.details import Details
from pages.service_center.policy_screens.effective_periods import Effective_Periods
from pages.service_center.policy_screens.policy_screens import Policy_Screens
from pages.service_center.subjectivities import Subjectivities
from utilities.Environments.Environments import Environments
from utilities.state_capitals.state_capitals import StateCapitals
from utilities.zip_codes_state_capitals.zip_codes import ZipCodes
from config_globals import *

class TestCreateQuote:

    def test_login_search_for_agent_create_quote(self, browser, env):

        Product = "LEXR_TENANT"
        driver = browser

        ## Directory Locations

        tests_directory = ROOT_DIR / 'tests'
        framework_directory = ROOT_DIR
        config_file_directory = CONFIG_PATH
        test_case_directory = framework_directory / 'utilities' / 'Excel_Sheets' / 'Products'
        test_results_directory = framework_directory / 'utilities' / 'Excel_Sheets' / 'Test_Results'

        global test_summary
        global test_scenario_number
        global test_scenario
        global effective_date
        global regression
        global smoke
        global sanity
        global agent
        global state
        global number_years_in_business
        global number_locations
        global number_residential_units
        global retail_sq_ft
        global office_sq_ft
        global industrial_sq_ft
        global _OLD_scenario
        global _OLD_scenario_Number

        # Open Test Scenario Workbook; Instantiate worksheet object
        # 0 - First Worksheet
        # 1 - Second Worksheet...etc

        wb = xlrd.open_workbook(str(test_case_directory / Product) + '.xlsx')
        sh = wb.sheet_by_index(1)

        ## Begin For Loop to iterate through Test Scenarios
        i = 1
        rows = sh.nrows
        empty_cell = False
        for i in range(1, sh.nrows):

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
                test_scenario_number = str(round(sh.cell_value(i, 1)))
                test_scenario = str((sh.cell_value(i, 2)))
                effective_date = sh.cell_value(i, 3)
                regression = sh.cell_value(i, 4)
                smoke = sh.cell_value(i, 5)
                sanity = sh.cell_value(i, 6)
                agent = sh.cell_value(i, 7)
                state = sh.cell_value(i, 8)
                number_years_in_business = str(round(sh.cell_value(i, 9)))
                number_locations = str(round(sh.cell_value(i, 10)))
                number_residential_units = str(round(sh.cell_value(i, 11)))
                retail_sq_ft = str(round(sh.cell_value(i, 12)))
                office_sq_ft = str(round(sh.cell_value(i, 13)))
                industrial_sq_ft = str(round(sh.cell_value(i, 14)))
                _OLD_scenario = sh.cell_value(i, 15)
                _OLD_scenario_Number = str(round(sh.cell_value(i, 16)))

            # Else, the cell is empty
            # End the Loop
            else:
                break

            ## Determine Test Environment to run scripts

            ## Read in value from test_environment.xml
            # tree = ET.parse(os.path.join(config_file_directory, 'test_environment.xml'))
            # test_environment = tree.getroot()
            # environment = (test_environment[0][0].text)

            ## Select Appropriate URL based on the Environment Value from above
            base_URL = Environments.return_environments(env)

            first_name = name.first_name()
            last_name = name.last_name()
            company_name = company.company_name()
            # company_name_string = company_name
            company_name_string = "QA Test" + " " + "-" + " " + "Dr." + " " + first_name + " " + last_name + " " + "dba" + " " + company_name
            address_value = address.street_address()
            city = StateCapitals.return_state_capital(state)
            postal_code = ZipCodes.return_zip_codes(state)

            # Access XML to retrieve login credentials
            tree = ET.parse(str(config_file_directory /'resources.xml'))
            login_credentials = tree.getroot()
            username = (login_credentials[1][0].text)
            password = (login_credentials[1][1].text)

            # Date Variables
            date_today = time.strftime("%m/%d/%Y")
            ad_hoc_effectiveDate = "09/06/2017"

            # Convert effective_date value to format MM/DD/YYYY
            d = xlrd.xldate_as_tuple(int(effective_date), 0)
            # convert date tuple in mm-dd-yyyy format
            d = datetime.datetime(*(d[0:3]))
            effective_date_formatted = d.strftime("%m/%d/%Y")

            # driver.get(baseURL)

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
            pp.click_LEXR_TENANT()

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

            # Click Next
            cp.click_next()

            # Instantiate Insured Information;
            saw_ii = Insured_Information(driver)

            # Fill out Insured Information Screen According to test scenario number
            saw_ii.create_quote_01(number_locations, number_residential_units, retail_sq_ft, office_sq_ft,
                                   industrial_sq_ft)

            # Click Next
            saw_ii.click_next()

            saw_PAF = PAF(driver)

            if test_scenario_number == "1":
                saw_PAF.create_quote_Corporation_Property_Management_Company(number_years_in_business,
                                                                             company_name_string)
            elif test_scenario_number == "2":
                saw_PAF.create_quote_Individual_Proprietor_Property_Management_Company(number_years_in_business)
            elif test_scenario_number == "3":
                saw_PAF.create_quote_Limited_Liability_Company_Property_Management_Company(number_years_in_business)
            elif test_scenario_number == "4":
                saw_PAF.create_quote_Partnership_Joint_Venture_Property_Management_Company(number_years_in_business)
            elif test_scenario_number == "5":
                saw_PAF.create_quote_Public_Agency_Property_Management_Company(number_years_in_business)
            elif test_scenario_number == "6":
                saw_PAF.create_quote_Other_Property_Management_Company(number_years_in_business, company_name_string)
            elif test_scenario_number == "7":
                saw_PAF.create_quote_Corporation_Property_Owner(number_years_in_business, company_name_string)
            elif test_scenario_number == "8":
                saw_PAF.create_quote_Individual_Proprietor_Property_Owner(number_years_in_business)
            elif test_scenario_number == "9":
                saw_PAF.create_quote_Limited_Liability_Company_Property_Owner(number_years_in_business)
            elif test_scenario_number == "10":
                saw_PAF.create_quote_Partnership_Joint_Venture_Property_Owner(number_years_in_business)
            elif test_scenario_number == "11":
                saw_PAF.create_quote_Public_Agency_Property_Property_Owner(number_years_in_business)
            elif test_scenario_number == "12":
                saw_PAF.create_quote_Other_Property_Management_Property_Owner(number_years_in_business,
                                                                              company_name_string)

            # Click Next on PAF Screen
            saw_PAF.click_next()

            time.sleep(3)

            ## Coverage Options Section  ###
            ##                           ###

            #### This class is for generic objects that display on the Coverage Options page
            saw_CC = Coverage_Options(driver)

            # Next line uses the text in the _OLD_scenario column (in Excel Spreadsheet) as
            # the method name
            # getattr(saw_CC, _OLD_scenario)()

            ### Clear All selections on Coverage Options Screen
            saw_CC.select_all_deselect_all()

            ### Commented out next line; Moved Proceed to Quote button Call into the PCI / Non-PCI Methods
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

            time.sleep(3)

            # At this point, script is re-directed to service center login screen
            # This works on DEV
            # TODO: FIX redirection; should redirect back to Service Center
            saw_confirm_issue.click_return_to_Admin_Interface()

            time.sleep(2)

            # This section is necessary ONLY on STAGE
            # Call Login methods from Pages.home.login_page.py
            # lp = LoginPage(driver)
            # lp.login(username, password)
            # nb = NavigationBar(driver)

            # Click Applications link on Navigation Bar
            nb.click_applications()

            # Enter Application ID, click Search
            app_page = ApplicationsPage(driver)
            app_page.enter_application_id(application_id)
            app_page.click_search_button()

            # Click on application id link
            # THIS IS NOT WORKING
            # app_page.click_application_id_link(application_id)

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
            sub = Subjectivities(driver)
            sub.set_all_subjectivities_to_recieved()
            # sub.change_open_subjectivities_to_received()
            # sub.select_yes_to_subjectivities_met()
            sub.click_submit()
            sub.click_agent_link()

            # Return to Producer Center; Issue Policy
            saw_confirm_issue.input_signature()
            saw_confirm_issue.click_accept_terms_issue_policy()
            # Retrieve Policy Number of Policy that was issued; Policy Number stored in policy_text
            thank_you = Thank_You_Page(driver)
            policy_text = thank_you.retrieve_store_policy_number()

            # Code works up to this point

            # Wait
            driver.implicitly_wait(3)

            # Close Browser
            driver.quit()
