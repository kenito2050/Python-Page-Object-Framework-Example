import unittest
from urllib.parse import urlparse, parse_qs
from xml.etree import ElementTree as ET

from faker import address
from faker import company
from faker import name
from selenium import webdriver
import time

import os
import xlrd
import pytest

from pages.producer_center.products_programs_page import ProductsAndPrograms
from pages.producer_center.client_search_page import ClientSearch
from pages.producer_center.my_policies.my_policies_screens.active_policies import active_policies
from pages.producer_center.navigation_bar import Navigation_Bar
from pages.producer_center.client_contact_page import ClientContact

# Begin Generic SAW Pages
from pages.producer_center.saw.coverage_periods_page import CoveragePeriods

##### CHANGE THESE VALUES WHEN CREATING A NEW PRODUCT
# Begin Product Specific Pages - SAW Pages
from pages.producer_center.saw.products.NGP_CAMICO.insured_information.insured_information import Insured_Information
from pages.producer_center.saw.products.NGP_CAMICO.PAF.PAF import PAF
from pages.producer_center.saw.products.NGP_CAMICO.coverage_options.PCI_50k_coverage_options import PCI_50k_Coverage_Options
from pages.producer_center.saw.products.NGP_CAMICO.coverage_options.PCI_100k_coverage_options import PCI_100k_Coverage_Options
from pages.producer_center.saw.products.NGP_CAMICO.coverage_options.No_PCI_50k_coverage_options import No_PCI_50k_Coverage_Options
from pages.producer_center.saw.products.NGP_CAMICO.coverage_options.No_PCI_100k_coverage_options import No_PCI_100k_Coverage_Options
from pages.producer_center.saw.products.NGP_CAMICO.coverage_options.coverage_options import Coverage_Options
from pages.producer_center.saw.products.NGP_CAMICO.select_option.select_option import Select_Option

# Continue Generic SAW Pages
from pages.producer_center.saw.quote_review import Quote_Review
from pages.producer_center.saw.invoice import Invoice
from pages.producer_center.saw.confirm_order_details import Confirm_Order_Details
from pages.producer_center.saw.confirm_and_issue import Confirm_and_Issue
from pages.producer_center.saw.thank_you_page import Thank_You_Page
from pages.producer_center.saw.summary import Summary
from pages.service_center.agents_page import AgentsPage
from pages.service_center.applications_page import ApplicationsPage
from pages.service_center.application_screens.application_screens import Application_Screens
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
from utilities.contract_classes.contract_classes import ContractClasses
from utilities.state_capitals.state_capitals import StateCapitals
from utilities.zip_codes.zip_codes import ZipCodes

class CreateQuote():

    def test_login_search_for_agent_create_quote(self):

        ## Determine Test Environment to run scripts

        Product = "NGP_CAMICO"

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

        ## Read in value from test_environment.xml
        tree = ET.parse(os.path.join(config_file_directory, 'test_environment.xml'))
        test_environment = tree.getroot()
        environment = (test_environment[0][0].text)

        ## Select Appropriate URL based on the Environment Value from above
        baseURL = Environments.return_environments(environment)

        # Test Scenarios

        # 1 - PCI_50K_embedded_limit_CPA_Count_10
        # 2 - PCI_100K_embedded_limit_CPA_Count_10
        # 3 - No_PCI_50K_embedded_limit_CPA_Count_10
        # 4 - No_PCI_100K_embedded_limit_CPA_Count_10
        # 5 - PCI_50K_embedded_limit_CPA_Count_11
        # 6 - PCI_100K_embedded_limit_CPA_Count_11
        # 7 - No_PCI_50K_embedded_limit_CPA_Count_11
        # 8 - No_PCI_100K_embedded_limit_CPA_Count_11

        test_scenario = "3"

        # Create "Fake" Variables
        #state = frandom.us_state()
        state = "California"
        #state = Create_Insured_Address.return_alabama(state_value)

        first_name = name.first_name()
        last_name = name.last_name()
        company_name = company.company_name()
        #company_name_string = company_name
        company_name_string = "QA Test" + " " + "-" + " " + first_name + " " + last_name + " " + "dba" + " " + company_name
        address_value = address.street_address()
        city = StateCapitals.return_state_capital(state)
        postal_code = ZipCodes.return_zip_codes(state)

        revenue = "20,000,000"
        total_num_records = '1 to 100,000'
        cpa_count = "10"

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
        tree = ET.parse('Agents.xml')
        agents = tree.getroot()
        agent = (agents[5][0].text)

        # 0,0 = Crump Tester                -- Wholesale Agent - Crump Insurance Services, Boston - Test Account
        # 1,0 = Susan Leeming - TEST        -- Sub Agent of Wholesale Agency
        # 2,0 = Retail Agent                -- Retail Agent - Boston Retail Insurance
        # 3,0 = Preferred Agent             -- Preferred Agent - Preferred Agency
        # 4,0 = TMLT Test User              -- Account to Test COMM2 Scenarios
        # 5,0 = QA Agent                    -- QA Agent
        # 6,0 = Janice Quinn                -- Janice Quinn - Boston Retail

        # TODO: NEED TO FIX SO THAT SCRIPT USES STRING VALUE CONTAINED IN contract_class variable
        # Access XML to retrieve contract_class

        # NOTE: For XML, the array count starts at 0
        # I have inserted a placeholder element at 0 -- Ken
        # Array will be 1 - 74
        # For List of Contract Classes, See Contract_Classes.xml
        tree = ET.parse('Contract_Classes.xml')
        contract_classes_XML = tree.getroot()
        contract_class = (contract_classes_XML[0][43].text)

        # Retail Sales          - 57
        # Online Retailer       - 46
        # Restaurant            - 56
        # Misc Consultant       - 43
        # Hospitality           - 30
        # Title/Escrow Services - 63

        # NOTE: For contract_classes.py, the array count starts at 1
        # Array will be 1 - 74
        contract_class_int_value = ContractClasses.return_contract_class_values(contract_class)

        # To Debug, contract_class, uncomment the next line; set value to an integer from the utilities.contract_classes.py class
        #contract_class_value = "74"

        # Date Variables
        date_today = time.strftime("%m/%d/%Y")
        ad_hoc_effectiveDate = "07/01/2017"



        # Initialize Driver; Launch URL
        # baseURL = "https://svcdemo1.wn.nasinsurance.com/"
        driver = webdriver.Chrome('C:\ChromeDriver\chromedriver.exe')

        # Maximize Window; Launch URL
        driver.maximize_window()
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
        pp.click_NGP_CAMICO()

        # These next (2) lines commented out
        # No prompt for Contract Class

        #pp.click_contract_class_modal()
        #pp.select_contract_class_dropdown()
        #pp.select_contract_class(contract_class_int_value)
        #pp.click_continue_on_contract_class_modal()

        cs = ClientSearch(driver)
        cs.input_bogus_client_data(postal_code)
        cs.manually_input_new_client()
        cs.enter_new_client_name_address(company_name_string, address_value, city, state)
        cc = ClientContact(driver)

        # TODO:
        # Code now parses URL String & retrieves application ID
        #cc.parse_url_get_app_id()

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
        saw_ii = Insured_Information(driver)
        saw_ii.enter_cpa_count(cpa_count)
        saw_ii.enter_annual_revenue(revenue)
        saw_ii.click_next()

        ### Quote Creation Section  ###
        ###                         ###

        saw_PAF = PAF(driver)

        #### If / ELSE to Determine how PAF is completed

        if test_scenario == "1":
            saw_PAF.create_quote_PCI_DSS_No_DQ_50k()
        elif test_scenario == "2":
            saw_PAF.create_quote_PCI_DSS_No_DQ_100k()
        elif test_scenario == "3":
            saw_PAF.create_quote_No_PCI_DSS_No_DQ_50k()
        elif test_scenario == "4":
            saw_PAF.create_quote_No_PCI_DSS_No_DQ_100k()

        # Click Next on PAF Screen
        saw_PAF.click_next()

        ### Coverage Options Section  ###
        ###                           ###

        #### Declare instances of Coverage Options

        saw_CC_PCI_50k = PCI_50k_Coverage_Options(driver)
        saw_CC_PCI_100k = PCI_100k_Coverage_Options(driver)
        saw_CC_No_PCI_50k = No_PCI_50k_Coverage_Options(driver)
        saw_CC_No_PCI_100k = No_PCI_100k_Coverage_Options(driver)

        #### This class is for generic objects that display on the Coverage Options page
        saw_CC = Coverage_Options(driver)

        #### If / ELSE to Determine which Coverage Options are selected based on Test Scenario

        if test_scenario == "1":
            saw_CC_PCI_50k.select_all_deselect_all()
            saw_CC_PCI_50k.select_NetGuard_Plus_PCI_1MM_limit_0_Deductible_50k_embedded()
        elif test_scenario == "2":
            saw_CC_PCI_100k.select_all_deselect_all()
            saw_CC_PCI_100k.select_NetGuard_Plus_PCI_1MM_limit_0_Deductible_100k_embedded()
        elif test_scenario == "3":
            saw_CC_No_PCI_50k.select_all_deselect_all()
            saw_CC_No_PCI_50k.select_NetGuard_Plus_No_PCI_1MM_limit_0_Deductible_50k_embedded()
        elif test_scenario == "4":
            saw_CC_No_PCI_100k.select_all_deselect_all()
            saw_CC_No_PCI_100k.select_NetGuard_Plus_No_PCI_1MM_limit_0_Deductible_100k_embedded()

        # saw_CC.select_all_deselect_all()

        ### Choose PCI / No PCI Options in this block   ###
        ###                                             ###

        ### PCI Options ###
        # select_NetGuard_Plus_1MM_limit_0_Deductible_50k_embedded

        # saw_CC_PCI.select_250K_limit_0_Deductible()
        # saw_CC_PCI.select_500K_limit_0_Deductible()
        # saw_CC_PCI.select_1MM_limit_0_Deductible()

        ### No-PCI Options ###

        # saw_CC_No_PCI.select_250K_limit_0_Deductible()
        # saw_CC_No_PCI.select_500K_limit_0_Deductible()
        # saw_CC_No_PCI.select_1MM_limit_0_Deductible()

        ### Commented out next line; Moved Proceed to Quote button Call into the PCI / Non-PCI Methods
        # saw_CC.proceed_to_quote()

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

        time.sleep(2)

        # This section is necessary ONLY on STAGE
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

cq = CreateQuote()
cq.test_login_search_for_agent_create_quote()