import datetime
import time
from urllib.parse import urlparse, parse_qs
from xml.etree import ElementTree as ET

import xlrd
from faker import address
from faker import company
from faker import name

from pages.producer_center.client_contact_page import ClientContact
from pages.producer_center.client_search_page import ClientSearch
from pages.producer_center.my_policies.my_policies_screens.active_policies import active_policies
from pages.producer_center.navigation_bar import Navigation_Bar
from pages.producer_center.products_programs_page import ProductsAndPrograms
from pages.producer_center.saw.confirm_and_issue import Confirm_and_Issue
from pages.producer_center.saw.confirm_order_details import Confirm_Order_Details
from pages.producer_center.saw.coverage_periods_page import CoveragePeriods
from pages.producer_center.saw.invoice import Invoice
from pages.producer_center.saw.products.NGP.PAF.PAF import PAF

### PCI Coverage Options Classes
from pages.producer_center.saw.products.NGP.coverage_options.PCI_Options.PCI_coverage_options import PCI_Coverage_Options

### Non PCI Coverage Options Classes
from pages.producer_center.saw.products.NGP.coverage_options.No_PCI_Options.No_PCI_coverage_options import No_PCI_Coverage_Options

from pages.producer_center.saw.products.NGP.coverage_options.coverage_options import Coverage_Options
from pages.producer_center.saw.products.NGP.insured_information.insured_information import Insured_Information
from pages.producer_center.saw.products.NGP.select_option.select_option import Select_Option
from pages.producer_center.saw.quote_review import Quote_Review
from pages.producer_center.saw.summary import Summary
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
from utilities.Faker.Data_Generator import Data_Generator
from utilities.Date_Time_Generator.Date_Time_Generator import Date_Time_Generator
from config_globals import *

class TestCreateQuote:

    def test_login_search_for_agent_create_quote(self, browser, env):

        Product = "NGP"
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
        global revenue
        global total_num_records
        global _OLD_scenario
        global limit
        global deductible

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
                test_scenario = str(round(sh.cell_value(i, 1)))
                effective_date = sh.cell_value(i, 2)
                contract_class = sh.cell_value(i, 3)
                agent = sh.cell_value(i, 4)
                state = sh.cell_value(i, 5)
                revenue = str(round(sh.cell_value(i, 6)))
                total_num_records = (sh.cell_value(i, 7))
                _OLD_scenario = sh.cell_value(i, 8)
                limit = sh.cell_value(i, 9)
                deductible = sh.cell_value(i, 10)

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

            # Date Variables

            # Create Today's Date
            date_today = dtg.return_date_today()

            ## Determine Test Environment to run scripts

            ## Select Appropriate URL based on the Environment Value from above
            base_URL = Environments.return_environments(env)

            # Access XML to retrieve login credentials
            tree = ET.parse(str(config_file_directory /'resources.xml'))
            login_credentials = tree.getroot()
            username = (login_credentials[1][0].text)
            password = (login_credentials[1][1].text)

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
            pp.click_NGP()

            # The following lines added on 10-09-17 work
            pp.click_contract_class_drop_down_select_contract_class(contract_class)
            pp.click_continue_on_contract_class_modal()

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
            cp.click_return_to_Admin_Interface()

            time.sleep(3)

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

            # Declare an app details class for Agents & Sub-Agents
            app_details = App_Details(driver)
            app_details_sub_agent = App_Details_sub_agent(driver)

            # Update the Create Date to the Ad Hoc Effective Date Value
            # app_details.update_create_date(effective_date_formatted)

            # This section if agent is direct
            # Click Update Button
            app_details.click_update_button()

            # Click on Agent Link to return to Producer Center
            app_details.click_agent_text_link()
            # Click on Agent Link to return to Producer Center

            # This section if agent is Sub-Agent
            # app_details_sub_agent.update_create_date(effective_date_formatted)
            # app_details_sub_agent.click_update_button()
            # app_details_sub_agent.click_sub_agent_text_link()

            # Return to Coverage Periods screen

            # Enter an Ad Hoc Effective Date
            # cp.enter_ad_hoc_effective_date(effective_date_formatted)

            # Enter Today's Date as Effective Date
            cp.enter_current_date_as_effective_date(date_today)

            # End Comment Section

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

            ### eMD / Higher Limits Test Scenarios - PCI & Non-PCI

            ### eMD and Higher Limits PCI Scenarios
            # PCI_Coverage_Options_eMD_Higher_Limits(driver)                - Test Scenario 1

            ### eMD and Higher Limits Non-PCI Scenarios
            # No_PCI_Coverage_Options_eMD_Higher_Limits(driver)             - Test Scenario 2


            ### Broad Regulatory Only Test Scenarios
            # Doctor_Count_1_Broad_Reg_Protect(driver)                      - Test Scenario 3
            # Doctor_Count_2_Broad_Reg_Protect(driver)                      - Test Scenario 4
            # Doctor_Count_3_Broad_Reg_Protect(driver)                      - Test Scenario 5
            # Doctor_Count_4_Broad_Reg_Protect(driver)                      - Test Scenario 6
            # Doctor_Count_5_Broad_Reg_Protect(driver)                      - Test Scenario 7

            ### Broad Regulatory Combined - Test Scenarios - PCI

            # PCI_Doctor_Count_1_Broad_Reg_Protect_Combined(driver)         - Test Scenario 8
            # PCI_Doctor_Count_2_Broad_Reg_Protect_Combined(driver)         - Test Scenario 9
            # PCI_Doctor_Count_3_Broad_Reg_Protect_Combined(driver)         - Test Scenario 10
            # PCI_Doctor_Count_4_Broad_Reg_Protect_Combined(driver)         - Test Scenario 11
            # PCI_Doctor_Count_5_Broad_Reg_Protect_Combined(driver)         - Test Scenario 12

            ### Broad Regulatory Combined - Test Scenarios - Non-PCI

            # No_PCI_Doctor_Count_1_Broad_Reg_Protect_Combined(driver)      - Test Scenario 13
            # No_PCI_Doctor_Count_2_Broad_Reg_Protect_Combined(driver)      - Test Scenario 14
            # No_PCI_Doctor_Count_3_Broad_Reg_Protect_Combined(driver)      - Test Scenario 15
            # No_PCI_Doctor_Count_4_Broad_Reg_Protect_Combined(driver)      - Test Scenario 16
            # No_PCI_Doctor_Count_5_Broad_Reg_Protect_Combined(driver)      - Test Scenario 17


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
                # saw_CC_in_use.test_ken(limit)

                # Assert Limits Display
                _NGP_with_BrandGuard_PCI_Assessment_250K_limit_label_text = saw_CC_in_use.return_NGP_with_BrandGuard_PCI_Assessment_250K_limit_label_text()
                assert _NGP_with_BrandGuard_PCI_Assessment_250K_limit_label_text == "$250,000 (Full Sublimits) ($250K PCI)"

                _NGP_with_BrandGuard_PCI_Assessment_500K_limit_label_text = saw_CC_in_use.return_NGP_with_BrandGuard_PCI_Assessment_500K_limit_label_text()
                assert _NGP_with_BrandGuard_PCI_Assessment_500K_limit_label_text == "$500,000 (Full Sublimits) ($500K PCI)"

                _NGP_with_BrandGuard_PCI_Assessment_1MM_limit_label_text = saw_CC_in_use.return_NGP_with_BrandGuard_PCI_Assessment_1MM_limit_label_text()
                assert _NGP_with_BrandGuard_PCI_Assessment_1MM_limit_label_text == "$1,000,000 (Full Sublimits) ($1MM PCI)"

                _NGP_with_BrandGuard_PCI_Assessment_2MM_limit_label_text = saw_CC_in_use.return_NGP_with_BrandGuard_PCI_Assessment_2MM_limit_label_text()
                assert _NGP_with_BrandGuard_PCI_Assessment_2MM_limit_label_text == "$2,000,000 (Full Sublimits) ($2MM PCI)"

                _NGP_with_BrandGuard_PCI_Assessment_Sublimit_Per_Identity_250K_limit_label_text = saw_CC_in_use.return_NGP_with_BrandGuard_PCI_Assessment_Sublimit_Per_Identity_250K_limit_label_text()
                assert _NGP_with_BrandGuard_PCI_Assessment_Sublimit_Per_Identity_250K_limit_label_text == "$250,000 (Full Sublimits) ($250K PCI)"

                _NGP_with_BrandGuard_PCI_Assessment_Sublimit_Per_Identity_500K_limit_label_text = saw_CC_in_use.return_NGP_with_BrandGuard_PCI_Assessment_Sublimit_Per_Identity_500K_limit_label_text()
                assert _NGP_with_BrandGuard_PCI_Assessment_Sublimit_Per_Identity_500K_limit_label_text == "$500,000 (Full Sublimits) ($500K PCI)"

                _NGP_with_BrandGuard_PCI_Assessment_Sublimit_Per_Identity_1MM_limit_label_text = saw_CC_in_use.return_NGP_with_BrandGuard_PCI_Assessment_Sublimit_Per_Identity_1MM_limit_label_text()
                assert _NGP_with_BrandGuard_PCI_Assessment_Sublimit_Per_Identity_1MM_limit_label_text == "$1,000,000 (Full Sublimits) ($1MM PCI)"

                _NGP_with_BrandGuard_PCI_Assessment_Sublimit_Per_Identity_2MM_limit_label_text = saw_CC_in_use.return_NGP_with_BrandGuard_PCI_Assessment_Sublimit_Per_Identity_2MM_limit_label_text()
                assert _NGP_with_BrandGuard_PCI_Assessment_Sublimit_Per_Identity_2MM_limit_label_text == "$2,000,000 (Full Sublimits) ($2MM PCI)"

                # Assert Deductibles Display
                _NGP_with_BrandGuard_PCI_Assessment_500_deductible_label_text = saw_CC_in_use.return_NGP_with_BrandGuard_PCI_Assessment_500_deductible_label_text()
                assert _NGP_with_BrandGuard_PCI_Assessment_500_deductible_label_text == "$500"

                _NGP_with_BrandGuard_PCI_Assessment_1k_deductible_label_text = saw_CC_in_use.return_NGP_with_BrandGuard_PCI_Assessment_1k_deductible_label_text()
                assert _NGP_with_BrandGuard_PCI_Assessment_1k_deductible_label_text == "$1,000"

                _NGP_with_BrandGuard_PCI_Assessment_2pt5k_deductible_label_text = saw_CC_in_use.return_NGP_with_BrandGuard_PCI_Assessment_2pt5k_deductible_label_text()
                assert _NGP_with_BrandGuard_PCI_Assessment_2pt5k_deductible_label_text == "$2,500"

                _NGP_with_BrandGuard_PCI_Assessment_5k_deductible_label_text = saw_CC_in_use.return_NGP_with_BrandGuard_PCI_Assessment_5k_deductible_label_text()
                assert _NGP_with_BrandGuard_PCI_Assessment_5k_deductible_label_text == "$5,000"

                _NGP_with_BrandGuard_PCI_Assessment_10k_deductible_label_text = saw_CC_in_use.return_NGP_with_BrandGuard_PCI_Assessment_10k_deductible_label_text()
                assert _NGP_with_BrandGuard_PCI_Assessment_10k_deductible_label_text == "$10,000"

                _NGP_with_BrandGuard_PCI_Assessment_25k_deductible_label_text = saw_CC_in_use.return_NGP_with_BrandGuard_PCI_Assessment_25k_deductible_label_text()
                assert _NGP_with_BrandGuard_PCI_Assessment_25k_deductible_label_text == "$25,000"

                _NGP_with_BrandGuard_PCI_Assessment_Sublimit_Per_Identity_500_deductible_label_text = saw_CC_in_use.return_NGP_with_BrandGuard_PCI_Assessment_Sublimit_Per_Identity_500_deductible_label_text()
                assert _NGP_with_BrandGuard_PCI_Assessment_Sublimit_Per_Identity_500_deductible_label_text == "$500"

                _NGP_with_BrandGuard_PCI_Assessment_Sublimit_Per_Identity_1k_deductible_label_text = saw_CC_in_use.return_NGP_with_BrandGuard_PCI_Assessment_Sublimit_Per_Identity_1k_deductible_label_text()
                assert _NGP_with_BrandGuard_PCI_Assessment_Sublimit_Per_Identity_1k_deductible_label_text == "$1,000"

                _NGP_with_BrandGuard_PCI_Assessment_Sublimit_Per_Identity_2pt5k_deductible_label_text = saw_CC_in_use.return_NGP_with_BrandGuard_PCI_Assessment_Sublimit_Per_Identity_2pt5k_deductible_label_text()
                assert _NGP_with_BrandGuard_PCI_Assessment_Sublimit_Per_Identity_2pt5k_deductible_label_text == "$2,500"

                _NGP_with_BrandGuard_PCI_Assessment_Sublimit_Per_Identity_5k_deductible_label_text = saw_CC_in_use.return_NGP_with_BrandGuard_PCI_Assessment_Sublimit_Per_Identity_5k_deductible_label_text()
                assert _NGP_with_BrandGuard_PCI_Assessment_Sublimit_Per_Identity_5k_deductible_label_text == "$5,000"

                _NGP_with_BrandGuard_PCI_Assessment_Sublimit_Per_Identity_10k_deductible_label_text = saw_CC_in_use.return_NGP_with_BrandGuard_PCI_Assessment_Sublimit_Per_Identity_10k_deductible_label_text()
                assert _NGP_with_BrandGuard_PCI_Assessment_Sublimit_Per_Identity_10k_deductible_label_text == "$10,000"

                _NGP_with_BrandGuard_PCI_Assessment_Sublimit_Per_Identity_25k_deductible_label_text = saw_CC_in_use.return_NGP_with_BrandGuard_PCI_Assessment_Sublimit_Per_Identity_25k_deductible_label_text()
                assert _NGP_with_BrandGuard_PCI_Assessment_Sublimit_Per_Identity_25k_deductible_label_text == "$25,000"

                saw_CC_in_use.assert_deductibles_and_labels_display()

                # Run Test Scenario listed on Excel Spreadsheet
                getattr(saw_CC_in_use, _OLD_scenario)()

            ### Non-PCI Scenarios
            elif test_scenario == "2":
                saw_CC_in_use = No_PCI_Coverage_Options(driver)

                # Run Test Scenario listed on Excel Spreadsheet
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