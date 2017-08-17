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
from pages.producer_center.saw.products.CYB_TMLT.PAF.PAF import PAF
from pages.producer_center.saw.products.CYB_TMLT.coverage_options.coverage_options import Coverage_Options
from pages.producer_center.saw.products.CYB_TMLT.coverage_options.PCI_coverage_options import PCI_Coverage_Options
from pages.producer_center.saw.products.CYB_TMLT.coverage_options.No_PCI_coverage_options import No_PCI_Coverage_Options
from pages.producer_center.saw.products.CYB_TMLT.insured_information.insured_information import Insured_Information
from pages.producer_center.saw.products.CYB_TMLT.select_option.select_option import Select_Option
from pages.producer_center.saw.quote_review import Quote_Review
from pages.producer_center.saw.summary import Summary
from pages.producer_center.saw.thank_you_page import Thank_You_Page
from pages.service_center.agent_screens.agent_details import Agent_Details
from pages.service_center.agents_page import AgentsPage
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
from utilities.zip_codes.zip_codes import ZipCodes


class CreateQuote(unittest.TestCase):

    def login_search_for_agent_create_quote(self):

        Product = "CYB_TMLT"

        ## Directory Locations

        tests_directory = os.path.abspath(os.pardir)
        framework_directory = os.path.abspath(os.path.join(tests_directory, os.pardir))
        config_file_directory = os.path.abspath(os.path.join(framework_directory, 'config_files'))
        test_case_directory = os.path.abspath(os.path.join(framework_directory, 'utilities\Excel_Sheets\Products'))
        test_results_directory = os.path.abspath(os.path.join(framework_directory, 'utilities\Excel_Sheets\Test_Results'))

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

        wb = xlrd.open_workbook(os.path.join(test_case_directory, Product + '.xlsx'))
        sh = wb.sheet_by_index(0)

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


            regression_check = round(sh.cell_value(i, 3))
            smoke_check = round(sh.cell_value(i, 4))
            sanity_check = round(sh.cell_value(i, 5))

            # If / Else Section to check if a test needs to be run
            #### CODE NOT WORKING YET - Ken 8-2-17
            #### Program is running ALL rows & NOT skipping rows

            if (test_run_type_value == 3 and sanity_check == 0):
                    continue
            elif (test_run_type_value == 2 and smoke_check == 0):
                    continue
            elif (test_run_type_value == 1 and regression_check == 0):
                    continue

            # Check to see if cell is NOT empty
            # If cell is not empty, read in the values
            if empty_cell == False:
                test_summary = sh.cell_value(i, 0)
                test_scenario = sh.cell_value(i, 1)
                test_scenario_number = str(round(sh.cell_value(i, 2)))
                regression = round(sh.cell_value(i, 3))
                smoke = round(sh.cell_value(i, 4))
                sanity = round(sh.cell_value(i, 5))
                contract_class = sh.cell_value(i, 6)
                agent = sh.cell_value(i, 7)
                state = sh.cell_value(i, 8)
                revenue = str(round(sh.cell_value(i, 9)))
                staff_count = str(round(sh.cell_value(i, 10)))
                _OLD_scenario = sh.cell_value(i, 11)
                revenue_tier = str(round(sh.cell_value(i, 12)))


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

            # Test Scenarios

            # 1 - PCI_50K_embedded_limit
            # 2 - PCI_100K_embedded_limit
            # 3 - No_PCI_50K_embedded_limit
            # 4 - No_PCI_100K_embedded_limit

            # test_scenario = '1'

            # Create "Fake" Variables
            # state = frandom.us_state()
            # state = "California"
            # state = Create_Insured_Address.return_alabama(state_value)

            # Determine the Revenue Tier for this Test Scenario
            ### THIS SECTION NOT WORKING

            # if revenue < "10,000,000":
            #     revenue_tier = 1
            # elif revenue == "10,000,000":
            #     revenue_tier = 1
            # elif revenue > "25,000,000":
            #     revenue_tier = 3
            # else:
            #     revenue_tier = 2

            first_name = name.first_name()
            last_name = name.last_name()
            company_name = company.company_name()
            # company_name_string = company_name
            company_name_string = "QA Test" + " " + "-" + " " + "Dr." + " " + first_name + " " + last_name + " " + "dba" + " " + company_name
            address_value = address.street_address()
            city = StateCapitals.return_state_capital(state)
            postal_code = ZipCodes.return_zip_codes(state)

            # revenue = "20,000,000"
            total_num_records = '1 to 100,000'
            # cpa_count = "9"

            # 1 to 100,000
            # 100,001 to 250,000
            # 250,001 to 500,000
            # Over 500,000
            # Uncertain

            # Access XML to retrieve login credentials
            tree = ET.parse('resources.xml')
            login_credentials = tree.getroot()
            username = (login_credentials[0][0].text)
            password = (login_credentials[0][1].text)

            # Access XML to retrieve the agent to search for
            # tree = ET.parse('Agents.xml')
            # agents = tree.getroot()
            # agent = (agents[5][0].text)

            # 0,0 = Crump Tester                -- Wholesale Agent - Crump Insurance Services, Boston - Test Account
            # 1,0 = Susan Leeming - TEST        -- Sub Agent of Wholesale Agency
            # 2,0 = Retail Agent                -- Retail Agent - Boston Retail Insurance
            # 3,0 = Preferred Agent             -- Preferred Agent - Preferred Agency
            # 4,0 = CYB_TMLT Test User              -- Account to Test COMM2 Scenarios
            # 5,0 = QA Agent                    -- QA Agent
            # 6,0 = Janice Quinn                -- Janice Quinn - Boston Retail

            # TODO: NEED TO FIX SO THAT SCRIPT USES STRING VALUE CONTAINED IN contract_class variable
            # Access XML to retrieve contract_class

            # NOTE: For XML, the array count starts at 0
            # I have inserted a placeholder element at 0 -- Ken
            # Array will be 1 - 74
            # For List of Contract Classes, See Contract_Classes.xml
            # tree = ET.parse('Contract_Classes.xml')
            # contract_classes_XML = tree.getroot()
            # contract_class = (contract_classes_XML[0][43].text)

            # Retail Sales          - 57
            # Online Retailer       - 46
            # Restaurant            - 56
            # Misc Consultant       - 43
            # Hospitality           - 30
            # Title/Escrow Services - 63

            # tree = ET.parse('Contract_Classes_Medical.xml')
            # contract_classes_XML = tree.getroot()
            # contract_class = (contract_classes_XML[0][1].text)

            # NOTE: For contract_classes.py, the array count starts at 1
            # Array will be 1 - 74
            contract_class_int_value = ContractClasses_Medical.return_contract_class_values(contract_class)

            # To Debug, contract_class, uncomment the next line; set value to an integer from the utilities.contract_classes.py class
            # contract_class_value = "74"

            # Date Variables
            date_today = time.strftime("%m/%d/%Y")
            ad_hoc_effectiveDate = "08/01/2017"

            # Initialize Driver; Launch URL
            # baseURL = "https://svcdemo1.wn.nasinsurance.com/"
            driver = webdriver.Chrome('C:\ChromeDriver\chromedriver.exe')

            # Maximize Window; Launch URL
            driver.maximize_window()
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
            pp.click_CYB_TMLT()

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

            # Enter an Ad Hoc Effective Date
            # cp.enter_ad_hoc_effective_date(ad_hoc_effectiveDate)

            # Enter Today's Date as Effective Date
            cp.enter_current_date_as_effective_date(date_today)

            cp.click_next()

            # Instantiate Insured Information

            saw_ii = Insured_Information(driver)
            saw_ii.enter_physician_count(staff_count)
            saw_ii.click_next()

            saw_PAF = PAF(driver)

            #### If / ELSE Section to Determine how PAF is completed

            if test_scenario_number == "1":
                saw_PAF.create_quote_PCI_DSS_No_DQ(revenue)
            elif test_scenario_number == "2":
                saw_PAF.create_quote_No_PCI_DSS_No_DQ(revenue)

            # Click Next on PAF Screen
            saw_PAF.click_next()

            ## Coverage Options Section  ###
            ##                           ###

            ### Declare instances of Coverage Options

            PCI_options = PCI_Coverage_Options(driver)
            No_PCI_options = No_PCI_Coverage_Options(driver)

            #### This class is for generic objects that display on the Coverage Options page
            saw_CC = Coverage_Options(driver)


            ### Clear All selections on Coverage Options Screen
            saw_CC.select_all_deselect_all()

            #### If / ELSE to Determine which Coverage Options are selected based on Test Scenario
            ####

            ### Declare the Coverage Options Driver Variable

            ### This section tests to see if the correct test scenario is executed, given the test_scenario_number & revenue tier
            ### TODO: Read the values from the OLD_Scenario variable; Run that scenario

            if test_scenario_number == "1":
                saw_CC_in_use = PCI_Coverage_Options(driver)
                getattr(saw_CC_in_use, _OLD_scenario)()
                # saw_CC_in_use.select_MEDEFENSE_Plus_Only_1MM_1MM_limit_2pt5K_Deduct()

            elif test_scenario_number == "2":
                saw_CC_in_use = No_PCI_Coverage_Options(driver)
                getattr(saw_CC_in_use, _OLD_scenario)()
                # saw_CC_in_use.select_MEDEFENSE_Plus_and_eMD_With_PCI_and_Cyber_Crime_Combined_1MM_1MM_100K_250K_limit_1K_Deduct()



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

            # Return to Admin Interface
            saw_confirm_issue.click_return_to_Admin_Interface()

            # Click on Policies link; Navigate to Policy that was just issued
            nb.click_policies()

            pp = PoliciesPage(driver)
            # On Policies Page, Click All link
            pp.click_all_link()

            # Enter Policy Number & Click Search
            pp.enter_policy_name(policy_text)
            pp.click_search_button()

            # Click on the Policy link, Open Policy Details
            pp.click_policy_link(policy_text)

            # Click Effective Periods
            ps = Policy_Screens(driver)
            ps.click_Effective_Periods()

            # Change Effective Periods Dates to allow renewals
            ep = Effective_Periods(driver)
            ep.change_dates_expire_policy_allow_renewal()
            ep.click_update_dates()

            # Click Details link to display the Policy Details screen
            ps.click_Details()

            # On Details Screen, Click on the Agent that issued the Policy
            details = Details(driver)
            details.click_agent_link(agent)

            # Agent Details Screen Displays
            ag = Agent_Details(driver)

            # Click "Submit New Application as" link
            ag.click_submit_new_application_as_agent()

            # Click My Policies on Navigation Bar
            pnb = Navigation_Bar(driver)
            pnb.click_my_policies()

            # Locate Policy that was issued
            ap = active_policies(driver)
            ap.enter_policy_name(policy_text)
            ap.click_search_button()

            # Click Policy
            ap.click_policy_link(policy_text)

            # Code works up to this point

            # Wait
            driver.implicitly_wait(3)

            # Close Browser
            driver.quit()

            i += 1

            print(test_scenario_number, test_scenario, agent, state, revenue, staff_count)

cq = CreateQuote()
cq.login_search_for_agent_create_quote()