from urllib.parse import urlparse, parse_qs
from xml.etree import ElementTree as ET
import time
import xlrd
from pages.producer_center.client_contact_page import ClientContact
from pages.producer_center.my_policies.my_policies_screens.active_policies import active_policies
from pages.producer_center.navigation_bar import Navigation_Bar
from pages.producer_center.client_search_page import ClientSearch
from pages.producer_center.products_programs_page import ProductsAndPrograms

# Begin Generic SAW Pages
from pages.producer_center.saw.coverage_periods_page import CoveragePeriods

##### CHANGE THESE VALUES WHEN CREATING A NEW PRODUCT
# Begin Product Specific Pages - SAW Pages
from pages.producer_center.saw.products.EO_MISC.insured_information.insured_information import Insured_Information
from pages.producer_center.saw.products.EO_MISC.PAF.PAF import PAF
from pages.producer_center.saw.products.EO_MISC.coverage_options.coverage_options import Coverage_Options
from pages.producer_center.saw.products.EO_MISC.select_option.select_option import Select_Option

# Continue Generic SAW Pages
from pages.producer_center.saw.quote_review import Quote_Review
from pages.producer_center.saw.confirm_order_details import Confirm_Order_Details
from pages.producer_center.saw.confirm_and_issue import Confirm_and_Issue
from pages.producer_center.saw.thank_you_page import Thank_You_Page
from pages.producer_center.saw.invoice import Invoice
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
from utilities.state_capitals.state_capitals import StateCapitals
from utilities.zip_codes_state_capitals.zip_codes import ZipCodes
from utilities.Faker.Data_Generator import Data_Generator
from utilities.Date_Time_Generator.Date_Time_Generator import Date_Time_Generator
from config_globals import *

class TestCreateQuote():

    def test_login_search_for_agent_create_quote(self, browser, env):

        Product = "EO_MISC"
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
        wb = xlrd.open_workbook(str(test_case_directory / Product) + '.xlsx')
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

            # Check to see if cell is NOT empty
            # If cell is not empty, read in the values
            if empty_cell == False:
                test_summary = sh.cell_value(i, 0)
                test_scenario = str(round(sh.cell_value(i, 1)))
                effective_date = sh.cell_value(i, 2)
                test_scenario_number = str(round(sh.cell_value(i, 3)))
                contract_class = sh.cell_value(i, 4)
                agent = sh.cell_value(i, 5)
                state = sh.cell_value(i, 6)
                revenue = str(round(sh.cell_value(i, 7)))
                total_num_records = (sh.cell_value(i, 8))
                _OLD_scenario = sh.cell_value(i, 9)
                _OLD_scenario_number = str(round(sh.cell_value(i, 10)))

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

        # Maximize Window; Launch URL
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
        pp.click_EO_MISC()

        pp.click_contract_class_drop_down_select_contract_class(contract_class)
        pp.click_continue_on_contract_class_modal_after_selecting_contract_class()

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

        saw_ii = Insured_Information(driver)
        saw_ii.enter_annual_revenue(revenue)
        saw_ii.click_next()
        saw_PAF = PAF(driver)
        saw_PAF.create_quote_No_DQ()
        saw_PAF.click_next()
        saw_CC = Coverage_Options(driver)

        saw_CC.select_deselect_all()

        # saw_CC.select_Netguard_Plus_option_limits_deductibles()

        # Miscellaneous E&O with NetGuard™ Plus Section

        # saw_CC.select_Netguard_Plus_500K_500K_with_25K_NGP_1K_Deductible()
        # saw_CC.select_Netguard_Plus_500K_500K_with_100K_NGP_1K_Deductible()
        # saw_CC.select_Netguard_Plus_1MM_1MM_with_25K_NGP_1K_Deductible()
        # saw_CC.select_Netguard_Plus_1MM_1MM_with_100K_NGP_1K_Deductible()
        # saw_CC.select_Netguard_Plus_1MM_2MM_with_25K_NGP_1K_Deductible()
        # saw_CC.select_Netguard_Plus_1MM_2MM_with_100K_NGP_1K_Deductible()
        # saw_CC.select_Netguard_Plus_500K_500K_with_25K_NGP_2pt5K_Deductible()
        # saw_CC.select_Netguard_Plus_500K_500K_with_100K_NGP_2pt5K_Deductible()
        # saw_CC.select_Netguard_Plus_1MM_1MM_with_25K_NGP_2pt5K_Deductible()
        # saw_CC.select_Netguard_Plus_1MM_1MM_with_100K_NGP_2pt5K_Deductible()
        # saw_CC.select_Netguard_Plus_1MM_2MM_with_25K_NGP_2pt5K_Deductible()
        # saw_CC.select_Netguard_Plus_1MM_2MM_with_100K_NGP_2pt5K_Deductible()
        # saw_CC.select_Netguard_Plus_500K_500K_with_25K_NGP_5K_Deductible()
        # saw_CC.select_Netguard_Plus_500K_500K_with_100K_NGP_5K_Deductible()
        # saw_CC.select_Netguard_Plus_1MM_1MM_with_25K_NGP_5K_Deductible()
        # saw_CC.select_Netguard_Plus_1MM_1MM_with_100K_NGP_5K_Deductible()
        # saw_CC.select_Netguard_Plus_1MM_2MM_with_25K_NGP_5K_Deductible()
        # saw_CC.select_Netguard_Plus_1MM_2MM_with_100K_NGP_5K_Deductible()
        # saw_CC.select_Netguard_Plus_500K_500K_with_25K_NGP_10K_Deductible()
        # saw_CC.select_Netguard_Plus_500K_500K_with_100K_NGP_10K_Deductible()
        # saw_CC.select_Netguard_Plus_1MM_1MM_with_25K_NGP_10K_Deductible()
        # saw_CC.select_Netguard_Plus_1MM_1MM_with_100K_NGP_10K_Deductible()
        # saw_CC.select_Netguard_Plus_1MM_2MM_with_25K_NGP_10K_Deductible()
        # saw_CC.select_Netguard_Plus_1MM_2MM_with_100K_NGP_10K_Deductible()
        # saw_CC.select_Netguard_Plus_500K_500K_with_25K_NGP_15K_Deductible()
        # saw_CC.select_Netguard_Plus_500K_500K_with_100K_NGP_15K_Deductible()
        # saw_CC.select_Netguard_Plus_1MM_1MM_with_25K_NGP_15K_Deductible()
        # saw_CC.select_Netguard_Plus_1MM_1MM_with_100K_NGP_15K_Deductible()
        # saw_CC.select_Netguard_Plus_1MM_2MM_with_25K_NGP_15K_Deductible()
        # saw_CC.select_Netguard_Plus_1MM_2MM_with_100K_NGP_15K_Deductible()

        # Miscellaneous E&O with NetGuard™ Plus and Additional Claims Expenses Section

        # saw_CC.select_Netguard_Plus_Additional_Claims_Expenses_500K_500K_with_25K_NGP_1K_Deductible()
        # saw_CC.select_Netguard_Plus_Additional_Claims_Expenses_500K_500K_with_100K_NGP_1K_Deductible()
        # saw_CC.select_Netguard_Plus_Additional_Claims_Expenses_1MM_1MM_with_25K_NGP_1K_Deductible()
        # saw_CC.select_Netguard_Plus_Additional_Claims_Expenses_1MM_1MM_with_100K_NGP_1K_Deductible()
        # saw_CC.select_Netguard_Plus_Additional_Claims_Expenses_1MM_2MM_with_25K_NGP_1K_Deductible()
        # saw_CC.select_Netguard_Plus_Additional_Claims_Expenses_1MM_2MM_with_100K_NGP_1K_Deductible()
        # saw_CC.select_Netguard_Plus_Additional_Claims_Expenses_500K_500K_with_25K_NGP_2pt5K_Deductible()
        # saw_CC.select_Netguard_Plus_Additional_Claims_Expenses_500K_500K_with_100K_NGP_2pt5K_Deductible()
        # saw_CC.select_Netguard_Plus_Additional_Claims_Expenses_1MM_1MM_with_25K_NGP_2pt5K_Deductible()
        # saw_CC.select_Netguard_Plus_Additional_Claims_Expenses_1MM_1MM_with_100K_NGP_2pt5K_Deductible()
        # saw_CC.select_Netguard_Plus_Additional_Claims_Expenses_1MM_2MM_with_25K_NGP_2pt5K_Deductible()
        # saw_CC.select_Netguard_Plus_Additional_Claims_Expenses_1MM_2MM_with_100K_NGP_2pt5K_Deductible()
        # saw_CC.select_Netguard_Plus_Additional_Claims_Expenses_500K_500K_with_25K_NGP_5K_Deductible()
        # saw_CC.select_Netguard_Plus_Additional_Claims_Expenses_500K_500K_with_100K_NGP_5K_Deductible()
        # saw_CC.select_Netguard_Plus_Additional_Claims_Expenses_1MM_1MM_with_25K_NGP_5K_Deductible()
        # saw_CC.select_Netguard_Plus_Additional_Claims_Expenses_1MM_1MM_with_100K_NGP_5K_Deductible()
        # saw_CC.select_Netguard_Plus_Additional_Claims_Expenses_1MM_2MM_with_25K_NGP_5K_Deductible()
        # saw_CC.select_Netguard_Plus_Additional_Claims_Expenses_1MM_2MM_with_100K_NGP_5K_Deductible()
        # saw_CC.select_Netguard_Plus_Additional_Claims_Expenses_500K_500K_with_25K_NGP_10K_Deductible()
        # saw_CC.select_Netguard_Plus_Additional_Claims_Expenses_500K_500K_with_100K_NGP_10K_Deductible()
        # saw_CC.select_Netguard_Plus_Additional_Claims_Expenses_1MM_1MM_with_25K_NGP_10K_Deductible()
        # saw_CC.select_Netguard_Plus_Additional_Claims_Expenses_1MM_1MM_with_100K_NGP_10K_Deductible()
        # saw_CC.select_Netguard_Plus_Additional_Claims_Expenses_1MM_2MM_with_25K_NGP_10K_Deductible()
        # saw_CC.select_Netguard_Plus_Additional_Claims_Expenses_1MM_2MM_with_100K_NGP_10K_Deductible()
        # saw_CC.select_Netguard_Plus_Additional_Claims_Expenses_500K_500K_with_25K_NGP_15K_Deductible()
        # saw_CC.select_Netguard_Plus_Additional_Claims_Expenses_500K_500K_with_100K_NGP_15K_Deductible()
        # saw_CC.select_Netguard_Plus_Additional_Claims_Expenses_1MM_1MM_with_25K_NGP_15K_Deductible()
        # saw_CC.select_Netguard_Plus_Additional_Claims_Expenses_1MM_1MM_with_100K_NGP_15K_Deductible()
        # saw_CC.select_Netguard_Plus_Additional_Claims_Expenses_1MM_2MM_with_25K_NGP_15K_Deductible()
        # saw_CC.select_Netguard_Plus_Additional_Claims_Expenses_1MM_2MM_with_100K_NGP_15K_Deductible()

        # First Dollar Defense Scenarios

        # saw_CC.select_Netguard_Plus_500K_500K_with_25K_NGP_1K_Deductible_1st_Dollar_Defense()
        # saw_CC.select_Netguard_Plus_500K_500K_with_100K_NGP_2pt5K_Deductible_1st_Dollar_Defense()
        # saw_CC.select_Netguard_Plus_1MM_1MM_with_25K_NGP_5K_Deductible_1st_Dollar_Defense()
        # saw_CC.select_Netguard_Plus_Additional_Claims_Expenses_500K_500K_with_25K_NGP_5K_Deductible_1st_Dollar_Defense()
        # saw_CC.select_Netguard_Plus_Additional_Claims_Expenses_500K_500K_with_100K_NGP_10K_Deductible_1st_Dollar_Defense()
        # saw_CC.select_Netguard_Plus_Additional_Claims_Expenses_1MM_1MM_with_25K_NGP_15K_Deductible_1st_Dollar_Defense()

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

        # Wait
        driver.implicitly_wait(3)

        # Close Browser
        driver.quit()