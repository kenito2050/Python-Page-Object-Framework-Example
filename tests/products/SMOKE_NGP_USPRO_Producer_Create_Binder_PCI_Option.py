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

from pages.producer_center.login_page import Producer_LoginPage
from pages.producer_center.client_contact_page import ClientContact
from pages.producer_center.client_search_page import ClientSearch
from pages.producer_center.my_policies.my_policies_screens.active_policies import active_policies
from pages.producer_center.navigation_bar import Navigation_Bar
from pages.producer_center.products_programs_page import ProductsAndPrograms
from pages.producer_center.saw.confirm_and_issue import Confirm_and_Issue
from pages.producer_center.saw.confirm_order_details import Confirm_Order_Details
from pages.producer_center.saw.producer_coverage_periods_page import Producer_CoveragePeriods
from pages.producer_center.saw.invoice import Invoice
from pages.producer_center.saw.products.NGP_USPRO.PAF.PAF import PAF

### Generic Coverage Options Classes
from pages.producer_center.saw.products.NGP_USPRO.coverage_options.coverage_options import Coverage_Options

### PCI Coverage Options Classes
from pages.producer_center.saw.products.NGP_USPRO.coverage_options.PCI_Options.PCI_coverage_options import PCI_Coverage_Options

### Non PCI Coverage Options Classes
from pages.producer_center.saw.products.NGP_USPRO.coverage_options.No_PCI_Options.No_PCI_coverage_options import No_PCI_Coverage_Options

from pages.producer_center.saw.products.NGP_USPRO.insured_information.insured_information import Insured_Information
from pages.producer_center.saw.products.NGP_USPRO.select_option.select_option import Select_Option
from pages.producer_center.saw.quote_review import Quote_Review
from pages.producer_center.saw.summary import Summary
from pages.producer_center.saw.ouststanding_subjectivities import Outstanding_Subjectivities
from pages.producer_center.saw.binder_status import Binder_Status
from pages.producer_center.saw.thank_you_page import Thank_You_Page
from pages.service_center.agent_screens.agent_details import Agent_Details
from pages.service_center.agents_page import AgentsPage
from pages.service_center.application_screens.details import App_Details
from pages.service_center.application_screens.sub_agent_details import App_Details_sub_agent
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

        Product = "NGP_USPRO"
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
        global total_num_records
        global limit
        global deductible
        global _OLD_scenario
        global _OLD_scenario_number

        # Open Test Scenario Workbook; Instantiate worksheet object
        # 0 - First Worksheet
        # 1 - Second Worksheet...etc

        wb = xlrd.open_workbook(str(test_case_directory / Product) + '.xlsx')
        sh = wb.sheet_by_index(2)

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
                contract_class = sh.cell_value(i, 3)
                agent = sh.cell_value(i, 4)
                state = sh.cell_value(i, 5)
                revenue = str(round(sh.cell_value(i, 6)))
                total_num_records = (sh.cell_value(i, 7))
                _OLD_scenario = sh.cell_value(i, 8)

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
            tree = ET.parse(str(config_file_directory /'producer_resources.xml'))
            login_credentials = tree.getroot()
            username = (login_credentials[0][0].text)
            password = (login_credentials[0][1].text)

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
            lp = Producer_LoginPage(driver)
            lp.login(username, password)
            lp.click_login_button()

            # Navigate to Products and Programs
            current_url = driver.current_url
            slashparts = current_url.split('/')
            # Now join back the first three sections 'http:', '' and 'example.com'
            base_url = '/'.join(slashparts[:3]) + '/'

            index = 'index.php'

            products_programs_string = "?c=pcs.select_product"

            products_programs_screen = base_url + index + products_programs_string

            # Navigate to Application Subjectivities Screen
            driver.get(products_programs_screen)

            # nb = NavigationBar(driver)
            # nb.click_products_and_programs()

            pp = ProductsAndPrograms(driver)
            pp.click_NGP_USPRO()

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

            time.sleep(5)

            cc.click_next()

            cp = Producer_CoveragePeriods(driver)

            # Enter an Ad Hoc Effective Date
            # cp.enter_ad_hoc_effective_date(effective_date_formatted)

            # Enter Today's Date as Effective Date
            cp.enter_current_date_as_effective_date(date_today)

            # Click Next
            cp.click_next()

            # Instantiate Insured Information;
            saw_ii = Insured_Information(driver)
            saw_ii.enter_annual_revenue(revenue)
            saw_ii.click_next()
            saw_PAF = PAF(driver)

            # Return to Admin Interface / Set Creation Date
            # saw_PAF.click_return_to_Admin_Interface()

            #### If / ELSE Section to Determine how PAF is completed

            # Scenario 1: PCI Options
            # Scenario 2: No PCI Options

            if test_scenario == "1":
                saw_PAF.create_quote_PCI_DSS_No_DQ(total_num_records)
            elif test_scenario == "2":
                saw_PAF.create_quote_No_PCI_DSS_No_DQ(total_num_records)

            # Click Next on PAF Screen
            saw_PAF.click_next()

            ## Coverage Options Section  ###
            ##                           ###

            #### This class is for generic objects that display on the Coverage Options page
            saw_CC = Coverage_Options(driver)

            ## Coverage Options Section  ###
            ##                           ###

            #### This class is for generic objects that display on the Coverage Options page
            saw_CC = Coverage_Options(driver)

            ### Clear All selections on Coverage Options Screen
            # saw_CC.select_all_deselect_all()

            ### If / Then Block to determine which instance of Coverage Options to use

            ### PCI & Non-PCI Test Scenarios

            ### PCI Scenarios
            if test_scenario == "1":
                saw_CC_in_use = PCI_Coverage_Options(driver)
                getattr(saw_CC_in_use, _OLD_scenario)()

            ### Non-PCI Scenarios
            elif test_scenario == "2":
                saw_CC_in_use = No_PCI_Coverage_Options(driver)
                getattr(saw_CC_in_use, _OLD_scenario)()

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
            saw_outstanding_subjectivities = Outstanding_Subjectivities(driver)
            saw_outstanding_subjectivities.click_proceed_to_binding()
            saw_binder_status = Binder_Status(driver)
            saw_binder_status.click_create_binder()

            # Wait
            driver.implicitly_wait(3)

            # Close Browser
            driver.quit()