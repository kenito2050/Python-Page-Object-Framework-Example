import time
from urllib.parse import urlparse, parse_qs
from xml.etree import ElementTree as ET
import xlrd
from pages.producer_center.client_contact_page import ClientContact
from pages.producer_center.client_search_page import ClientSearch
from pages.producer_center.my_policies.my_policies_screens.active_policies import active_policies
from pages.producer_center.my_policies.my_policies_screens.policy_details import policy_details
from pages.producer_center.navigation_bar import Navigation_Bar
from pages.producer_center.products_programs_page import ProductsAndPrograms
from pages.producer_center.saw.confirm_and_issue import Confirm_and_Issue
from pages.producer_center.saw.confirm_order_details import Confirm_Order_Details
from pages.producer_center.saw.coverage_periods_page import CoveragePeriods
from pages.producer_center.saw.invoice import Invoice
from pages.producer_center.saw.products.CYB_OMSNIC.PAF.PAF import PAF

### PCI Coverage Options Classes
from pages.producer_center.saw.products.CYB_OMSNIC.coverage_options.PCI_Options.PCI_coverage_options import PCI_Coverage_Options

### Non PCI Coverage Options Classes
from pages.producer_center.saw.products.CYB_OMSNIC.coverage_options.No_PCI_Options.No_PCI_coverage_options import No_PCI_Coverage_Options

from pages.producer_center.saw.products.CYB_OMSNIC.coverage_options.coverage_options import Coverage_Options
from pages.producer_center.saw.products.CYB_OMSNIC.insured_information.insured_information import Insured_Information
from pages.producer_center.saw.products.CYB_OMSNIC.select_option.select_option import Select_Option
from pages.producer_center.saw.quote_review import Quote_Review
from pages.producer_center.saw.summary import Summary
from pages.producer_center.saw.thank_you_page import Thank_You_Page
from pages.producer_center.saw.products.CYB_OMSNIC.Renewal.client_contact_page import Client_Contact_Renewal
from pages.producer_center.saw.products.CYB_OMSNIC.Renewal.coverage_periods import Coverage_Periods_Renewal
from pages.producer_center.saw.products.CYB_OMSNIC.Renewal.insured_information import Insured_Information_Renewal
from pages.producer_center.saw.products.CYB_OMSNIC.Renewal.PAF_Renewal import PAF_Renewal
from pages.producer_center.saw.products.CYB_OMSNIC.Renewal.coverage_options.coverage_options_renewal import Coverage_Options_Renewal
from pages.producer_center.saw.products.CYB_OMSNIC.Renewal.coverage_options.PCI_coverage_options_Renewal import PCI_Coverage_Options_Renewal
from pages.producer_center.saw.products.CYB_OMSNIC.Renewal.coverage_options.No_PCI_coverage_options_Renewal import No_PCI_Coverage_Options_Renewal
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
from utilities.state_capitals.state_capitals import StateCapitals
from utilities.zip_codes_state_capitals.zip_codes import ZipCodes
from utilities.Faker.Data_Generator import Data_Generator
from utilities.Date_Time_Generator.Date_Time_Generator import Date_Time_Generator
from config_globals import *

class TestCreateQuote:

    def test_login_search_for_agent_create_quote(self, browser, env):

        Product = "CYB_OMSNIC"
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
        global contract_class
        global agent
        global state
        global staff_count
        global current_revenue
        global previous_revenue
        global _OLD_scenario
        global limit
        global deductible

        # Open Test Scenario Workbook; Instantiate worksheet object
        # 0 - First Worksheet
        # 1 - Second Worksheet...etc

        wb = xlrd.open_workbook(str(test_case_directory / Product) + '.xlsx')
        sh = wb.sheet_by_index(2)

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
                test_scenario = str(round(sh.cell_value(i, 1)))
                effective_date = sh.cell_value(i, 2)
                contract_class = sh.cell_value(i, 3)
                agent = sh.cell_value(i, 4)
                state = sh.cell_value(i, 5)
                staff_count = str(round(sh.cell_value(i, 6)))
                current_revenue = str(round(sh.cell_value(i, 7)))
                previous_revenue = str(round(sh.cell_value(i, 8)))
                _OLD_scenario = sh.cell_value(i, 9)
                limit = sh.cell_value(i, 10)
                deductible = sh.cell_value(i, 11)

            # Else, the cell is empty
            # End the Loop
            else:
                break

            # Create Instance of Data Generator
            dg = Data_Generator()

            # Create Company Name Value
            company_name_string = dg.create_full_company_name()
            # Create Street Address Value
            address_value = dg.create_street_address()
            city = StateCapitals.return_state_capital(state)
            postal_code = ZipCodes.return_zip_codes(state)

            # Create Instance of Date Time Generator
            dtg = Date_Time_Generator()
            # Create Today's Date
            date_today = dtg.return_date_today()

            # Access XML to retrieve login credentials
            tree = ET.parse(str(config_file_directory / 'resources.xml'))
            login_credentials = tree.getroot()
            username = (login_credentials[1][0].text)
            password = (login_credentials[1][1].text)

            ## Test Environment
            ## Select Appropriate URL based on the Environment Value (env)
            baseURL = Environments.return_environments(env)

            driver.get(baseURL)

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
            pp.click_CYB_OMSNIC()

            cs = ClientSearch(driver)
            cs.input_bogus_client_data(postal_code)
            cs.manually_input_new_client()
            cs.enter_new_client_name_address(company_name_string, address_value, city, state)
            cc = ClientContact(driver)

            # Get the Application ID from URL -- THIS WORKS
            # Code parses URL String & retrieves application ID
            current_url = driver.current_url
            first_url_string = urlparse(current_url)
            query_dict = parse_qs(first_url_string.query)
            application_id = (query_dict['app_id'][0])

            cc.click_next()

            cp = CoveragePeriods(driver)

            # Click Next
            cp.click_next()

            # Instantiate Insured Information;
            saw_ii = Insured_Information(driver)
            saw_ii.enter_physician_count(staff_count)
            saw_ii.click_next()
            saw_PAF = PAF(driver)

            # Return to Admin Interface / Set Creation Date
            # saw_PAF.click_return_to_Admin_Interface()

            #### If / ELSE Section to Determine how PAF is completed

            # Scenario 1: PCI Options
            # Scenario 2 and 3 : No PCI Options

            if test_scenario == "1":
                saw_PAF.create_quote_PCI_DSS_Compliance_No_DQ(current_revenue, previous_revenue)
                saw_PAF.is_data_encrypted_yes()
                saw_PAF.credit_card_compliant_yes()
            elif test_scenario == "2":
                saw_PAF.create_quote_No_Data_Encryption_No_PCI_DSS_Compliance_No_DQ(current_revenue, previous_revenue)
                saw_PAF.is_data_encrypted_yes()
            elif test_scenario == "3":
                saw_PAF.create_quote_Data_Encryption_No_PCI_DSS_Compliance_No_DQ(current_revenue, previous_revenue)
                saw_PAF.is_data_encrypted_yes()
                saw_PAF.credit_card_compliant_no()

            # Click Next on PAF Screen
            saw_PAF.click_next()

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

                # Assert Limits Display
                _eMD_Cyber_Liability_PCI_Assessment_1MM_limit_label_text = saw_CC_in_use.return_eMD_Cyber_Liability_PCI_Assessment_1MM_limit_label_text()
                assert _eMD_Cyber_Liability_PCI_Assessment_1MM_limit_label_text == "$1MM/$1MM"

                # Assert Deductibles Display
                _eMD_Cyber_Liability_PCI_Assessment_0_deductible_label_text = saw_CC_in_use.return_eMD_Cyber_Liability_PCI_Assessment_0_deductible_label_text()
                assert _eMD_Cyber_Liability_PCI_Assessment_0_deductible_label_text == "$0"

                # Run Test Scenario listed on Excel Spreadsheet
                # Commented out the next line because Limit and Deductible are selected by default
                # getattr(saw_CC_in_use, _OLD_scenario)()

            ### Non-PCI Scenarios
            elif test_scenario == "2" or test_scenario == "3":
                saw_CC_in_use = No_PCI_Coverage_Options(driver)

                # Assert Limits Display
                _eMD_Cyber_Liability_without_PCI_DSS_1MM_limit_label_text = saw_CC_in_use.return_eMD_Cyber_Liability_without_PCI_DSS_1MM_limit_label_text()
                assert _eMD_Cyber_Liability_without_PCI_DSS_1MM_limit_label_text == "$1MM/$1MM"

                # Assert Deductibles Display
                _eMD_Cyber_Liability_without_PCI_DSS_0_deductible_label_text = saw_CC_in_use.return_eMD_Cyber_Liability_without_PCI_DSS_0_deductible_label_text()
                assert _eMD_Cyber_Liability_without_PCI_DSS_0_deductible_label_text == "$0"

                # Run Test Scenario listed on Excel Spreadsheet
                # Commented out the next line because Limit and Deductible are selected by default
                # getattr(saw_CC_in_use, _OLD_scenario)()

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
            saw_confirm_issue.click_return_to_Admin_Interface()

            time.sleep(2)

            # Click Applications link on Navigation Bar
            nb.click_applications()

            # Enter Application ID, click Search
            app_page = ApplicationsPage(driver)
            app_page.enter_application_id(application_id)
            app_page.click_search_button()

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
            sub.click_submit()
            sub.click_agent_link()

            # Return to Producer Center; Issue Policy
            saw_confirm_issue.input_signature()
            saw_confirm_issue.click_accept_terms_issue_policy()
            # Retrieve Policy Number of Policy that was issued; Policy Number stored in policy_text
            thank_you = Thank_You_Page(driver)
            policy_text = thank_you.retrieve_store_policy_number()

            # Wait
            driver.implicitly_wait(3)

            # Close Browser
            driver.quit()