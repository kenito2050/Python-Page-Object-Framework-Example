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
from pages.producer_center.saw.products.MEDEMD.PAF.PAF import PAF
from pages.producer_center.saw.products.MEDEMD.coverage_options.coverage_options import Coverage_Options
from pages.producer_center.saw.products.MEDEMD.coverage_options.Healthcare_Facilities.PCI.HCF_PCI_Coverage_options_10MM_or_Less import HCF_PCI_Coverage_Options_10MM_or_Less
from pages.producer_center.saw.products.MEDEMD.coverage_options.Healthcare_Facilities.PCI.HCF_PCI_coverage_options_10MM_to_25MM import HCF_PCI_Coverage_Options_10MM_to_25MM
from pages.producer_center.saw.products.MEDEMD.coverage_options.Healthcare_Facilities.PCI.HCF_PCI_coverage_options_25MM_or_Greater import HCF_PCI_Coverage_Options_25MM_or_Greater
from pages.producer_center.saw.products.MEDEMD.coverage_options.Healthcare_Facilities.No_PCI.HCF_No_PCI_coverage_options_10MM_or_Less import HCF_No_PCI_Coverage_Options_10MM_or_Less
from pages.producer_center.saw.products.MEDEMD.coverage_options.Healthcare_Facilities.No_PCI.HCF_NoPCI_Coverage_options_10MM_to_25MM import HCF_No_PCI_Coverage_Options_10MM_to_25MM
from pages.producer_center.saw.products.MEDEMD.coverage_options.Healthcare_Facilities.No_PCI.HCF_NoPCI_Coverage_options_25MM_or_Greater import HCF_No_PCI_Coverage_Options_25MM_or_Greater
from pages.producer_center.saw.products.MEDEMD.coverage_options.Non_Healthcare_Facilities.Non_HCF_PCI_coverage_options import Non_HCF_PCI_Coverage_Options
from pages.producer_center.saw.products.MEDEMD.coverage_options.Non_Healthcare_Facilities.Non_HCF_No_PCI_coverage_options import Non_HCF_No_PCI_Coverage_Options
from pages.producer_center.saw.products.MEDEMD.insured_information.Healthcare_Facilities.insured_information import Insured_Information_Healthcare_Facilities
from pages.producer_center.saw.products.MEDEMD.insured_information.insured_information import Insured_Information
from pages.producer_center.saw.products.MEDEMD.select_option.select_option import Select_Option
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
from utilities.contract_classes.contract_classes_Medical import ContractClasses_Medical
from utilities.state_capitals.state_capitals import StateCapitals
from utilities.zip_codes_state_capitals.zip_codes import ZipCodes
from config_globals import *

class TestCreateQuote:

    def test_login_search_for_agent_create_quote(self, browser, env):

        Product = "MEDEMD"
        driver = browser

        ## Directory Locations

        tests_directory = ROOT_DIR / 'tests'
        framework_directory = ROOT_DIR
        config_file_directory = CONFIG_PATH
        test_case_directory = framework_directory / 'utilities' / 'Excel_Sheets' / 'Products'
        test_results_directory = framework_directory / 'utilities' / 'Excel_Sheets' / 'Test_Results'

        global test_summary
        global test_scenario
        global effective_date
        global test_scenario_number
        global regression
        global smoke
        global sanity
        global contract_class
        global agent
        global state
        global revenue
        global staff_count
        global limit
        global deductible
        global _OLD_scenario
        global revenue_tier

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
                test_scenario = sh.cell_value(i, 1)
                effective_date = sh.cell_value(i, 2)
                test_scenario_number = str(round(sh.cell_value(i, 3)))
                contract_class = sh.cell_value(i, 4)
                agent = sh.cell_value(i, 5)
                state = sh.cell_value(i, 6)
                revenue = str(round(sh.cell_value(i, 7)))
                staff_count = str(round(sh.cell_value(i, 8)))
                _OLD_scenario = sh.cell_value(i, 9)
                revenue_tier = str(round(sh.cell_value(i, 10)))

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
            pp.click_MEDEMD()

            # The following lines added on 5-15-17 work
            pp.click_contract_class_drop_down_select_contract_class(contract_class)
            # pp.select_contract_class_dropdown()

            # pp.select_contract_class(contract_class)  # Script Ends Here
            pp.click_continue_on_contract_class_modal_after_selecting_contract_class()

            # These next (2) lines commented out
            # No prompt for Contract Class

            # pp.click_contract_class_modal()
            # pp.select_contract_class_dropdown()
            # pp.select_contract_class(contract_class_int_value)
            # pp.click_continue_on_contract_class_modal()

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

            # Instantiate Insured Information

            saw_ii = Insured_Information(driver)
            saw_ii_HCF = Insured_Information_Healthcare_Facilities(driver)

            if contract_class == "Healthcare Facilities":
                saw_ii_HCF.enter_physician_count(staff_count)
                saw_ii_HCF.enter_annual_revenue(revenue)
                saw_ii_HCF.click_next()
            else:
                saw_ii.enter_physician_count(staff_count)
                saw_ii.click_next()

            saw_PAF = PAF(driver)

            #### If / ELSE Section to Determine how PAF is completed

            if test_scenario_number == "1":
                saw_PAF.create_quote_PCI_DSS_No_DQ_HealthCare_Facilities(revenue)
            elif test_scenario_number == "2":
                saw_PAF.create_quote_PCI_DSS_No_DQ_Not_HealthCare_Facilities(revenue)
            elif test_scenario_number == "3":
                saw_PAF.create_quote_No_PCI_DSS_No_DQ_HealthCare_Facilities(revenue)
            elif test_scenario_number == "4":
                saw_PAF.create_quote_No_PCI_DSS_No_DQ_Not_HealthCare_Facilities(revenue)

            # Click Next on PAF Screen
            saw_PAF.click_next()

            ## Coverage Options Section  ###
            ##                           ###

            ### Declare instances of Coverage Options

            HCF_PCI_options_10MM_or_less = HCF_PCI_Coverage_Options_10MM_or_Less(driver)
            HCF_PCI_options_10MM_to_25MM = HCF_PCI_Coverage_Options_10MM_to_25MM(driver)
            HCF_PCI_options_25MM_or_Greater = HCF_PCI_Coverage_Options_25MM_or_Greater(driver)
            HCF_No_PCI_options_10MM_or_less = HCF_No_PCI_Coverage_Options_10MM_or_Less(driver)
            HCF_No_PCI_options_10MM_to_25MM = HCF_No_PCI_Coverage_Options_10MM_to_25MM(driver)
            HCF_No_PCI_options_25MM_or_Greater = HCF_No_PCI_Coverage_Options_25MM_or_Greater(driver)
            Non_HCF_PCI_options = Non_HCF_PCI_Coverage_Options(driver)
            Non_HCF_No_PCI_options = Non_HCF_No_PCI_Coverage_Options(driver)

            #### This class is for generic objects that display on the Coverage Options page
            saw_CC = Coverage_Options(driver)

            ### Clear All selections on Coverage Options Screen
            # saw_CC.select_all_deselect_all()

            #### If / ELSE to Determine which Coverage Options are selected based on Test Scenario
            ####

            ### Declare the Coverage Options Driver Variable

            ### This section tests to see if the correct test scenario is executed, given the test_scenario_number & revenue tier
            ### TODO: Read the values from the OLD_Scenario variable; Run that scenario

            if test_scenario_number == "1" and revenue_tier == "1":
                saw_CC_in_use = HCF_PCI_Coverage_Options_10MM_or_Less(driver)
                # getattr(saw_CC_in_use, _OLD_scenario)()
                # saw_CC_in_use.select_MEDEFENSE_Plus_Only_1MM_1MM_limit_2pt5K_Deduct()

            elif test_scenario_number == "1" and revenue_tier == "2":
                saw_CC_in_use = HCF_PCI_Coverage_Options_10MM_to_25MM(driver)
                getattr(saw_CC_in_use, _OLD_scenario)()
                # saw_CC_in_use.select_Medefense_Plus_and_eMD_Higher_Limits_With_PCI_and_Cyber_Crime_Combined_3MM_3MM_100K_250K_limit_5K_Deduct()

            elif test_scenario_number == "1" and revenue_tier == "3":
                saw_CC_in_use = HCF_PCI_Coverage_Options_25MM_or_Greater(driver)
                # getattr(saw_CC_in_use, _OLD_scenario)()
                # saw_CC_in_use.select_Medefense_Plus_and_eMD_Higher_Limits_With_PCI_and_Cyber_Crime_Combined_3MM_3MM_100K_250K_limit_10K_Deduct()

            elif test_scenario_number == "3" and revenue_tier == "1":
                saw_CC_in_use = HCF_No_PCI_Coverage_Options_10MM_or_Less(driver)
                # getattr(saw_CC_in_use, _OLD_scenario)()
                # saw_CC_in_use.select_MEDEFENSE_Plus_and_eMD_Without_PCI_and_Cyber_Crime_Combined_1MM_1MM_100K_250K_limit_2pt5K_Deduct()

            elif test_scenario_number == "3" and revenue_tier == "2":
                saw_CC_in_use = HCF_No_PCI_Coverage_Options_10MM_to_25MM(driver)
                # getattr(saw_CC_in_use, _OLD_scenario)()
                # saw_CC_in_use.select_Medefense_Plus_and_eMD_Higher_Limits_Without_PCI_and_Cyber_Crime_Combined_2MM_2MM_100K_250K_limit_5K_Deduct()

            elif test_scenario_number == "3" and revenue_tier == "3":
                saw_CC_in_use = HCF_No_PCI_Coverage_Options_25MM_or_Greater(driver)
                # getattr(saw_CC_in_use, _OLD_scenario)()
                # saw_CC_in_use.select_Medefense_Plus_and_eMD_Higher_Limits_Without_PCI_and_Cyber_Crime_Combined_3MM_3MM_100K_250K_limit_10K_Deduct()

            elif test_scenario_number == "2":
                saw_CC_in_use = Non_HCF_PCI_Coverage_Options(driver)
                # getattr(saw_CC_in_use, _OLD_scenario)()
                # saw_CC_in_use.select_MEDEFENSE_Plus_and_eMD_With_PCI_and_Cyber_Crime_Combined_1MM_1MM_100K_250K_limit_1K_Deduct()

            elif test_scenario_number == "4":
                saw_CC_in_use = Non_HCF_No_PCI_Coverage_Options(driver)
                # getattr(saw_CC_in_use, _OLD_scenario)()
                # saw_CC_in_use.select_MEDEFENSE_Plus_and_eMD_Without_PCI_and_Cyber_Crime_Combined_1MM_1MM_100K_250K_limit_1K_Deduct()

            ### FIXED: Renamed method proceed_to_quote to click_proceed_to_quote; This code now works
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
