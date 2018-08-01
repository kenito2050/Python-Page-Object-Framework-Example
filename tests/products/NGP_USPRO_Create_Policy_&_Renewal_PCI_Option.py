import unittest
import os
from urllib.parse import urlparse, parse_qs
from xml.etree import ElementTree as ET

from faker import address
from faker import company
from faker import name
from selenium import webdriver
import time

from pages.producer_center.products_programs_page import ProductsAndPrograms
from pages.producer_center.client_search_page import ClientSearch
from pages.producer_center.my_policies.my_policies_screens.active_policies import active_policies
from pages.producer_center.navigation_bar import Navigation_Bar
from pages.producer_center.client_contact_page import ClientContact
from pages.producer_center.saw.coverage_periods_page import CoveragePeriods
from pages.producer_center.saw.products.NGP_USPRO.insured_information.insured_information import Insured_Information
from pages.producer_center.saw.products.NGP_USPRO.PAF.PAF import PAF
from pages.producer_center.saw.products.NGP_USPRO.coverage_options.PCI_coverage_options import PCI_Coverage_Options
from pages.producer_center.saw.products.NGP_USPRO.coverage_options.No_PCI_coverage_options import No_PCI_Coverage_Options
from pages.producer_center.saw.products.NGP_USPRO.coverage_options.coverage_options import Coverage_Options
from pages.producer_center.saw.products.NGP_USPRO.select_option.select_option import Select_Option
from pages.producer_center.saw.quote_review import Quote_Review
from pages.producer_center.saw.invoice import Invoice
from pages.producer_center.saw.confirm_order_details import Confirm_Order_Details
from pages.producer_center.saw.confirm_and_issue import Confirm_and_Issue
from pages.producer_center.saw.thank_you_page import Thank_You_Page
from pages.producer_center.saw.summary import Summary
from pages.service_center.agents_page import AgentsPage
from pages.service_center.applications_page import ApplicationsPage
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
from utilities.zip_codes_state_capitals.zip_codes import ZipCodes


class CreateQuote():

    def test_login_search_for_agent_create_quote(self):

        ## Directory Locations

        tests_directory = os.path.abspath(os.pardir)
        framework_directory = os.path.abspath(os.path.join(tests_directory, os.pardir))
        config_file_directory = os.path.abspath(os.path.join(framework_directory, 'config_files'))
        test_case_directory = os.path.abspath(os.path.join(framework_directory, 'utilities\Excel_Sheets\Products'))
        test_results_directory = os.path.abspath(
            os.path.join(framework_directory, 'utilities\Excel_Sheets\Test_Results'))

        ## Determine Test Environment to run scripts

        ## Read in value from test_environment.xml
        tree = ET.parse(os.path.join(config_file_directory, 'test_environment.xml'))
        test_environment  = tree.getroot()
        environment =(test_environment[0][0].text)

        ## Select Appropriate URL based on the Environment Value from above
        baseURL  = Environments.return_environments(environment)

        # Create "Fake" Variables
        #state = frandom.us_state()
        state = "California"
        #state = Create_Insured_Address.return_alabama(state_value)
        first_name = name.first_name()
        last_name = name.last_name()
        company_name = company.company_name()

        #company_name_string = "QA Test - The Lance Armstrong Live Strong Company"
        #address_value = "7021 Cerritos Ave"
        #city = "Cerritos"
        #postal_code = "90623"

        company_name_string = "QA Test" + " " + "-" + " " + first_name + " " + last_name + " " + "dba" + " " + company_name
        address_value = address.street_address()
        city = StateCapitals.return_state_capital(state)
        postal_code = ZipCodes.return_zip_codes(state)

        revenue = "100000"
        total_num_records = '1 to 100,000'

        # Access XML to retrieve login credentials
        tree = ET.parse(os.path.join(config_file_directory, 'resources.xml'))
        login_credentials = tree.getroot()
        username = (login_credentials[0][0].text)
        password = (login_credentials[1][1].text)

        # Access XML to retrieve the agent to search for
        tree = ET.parse(os.path.join(config_file_directory, 'Agents.xml'))
        agents = tree.getroot()
        agent = (agents[5][0].text)

        # 0,0 = Crump Tester                -- Wholesale Agent - Crump Insurance Services, Boston - Test Account
        # 1,0 = Susan Leeming - TEST        -- Sub Agent of Wholesale Agency
        # 2,0 = Chad Robin                  -- Chad Robin Retail Agent - Robin Insurance
        # 3,0 = Preferred Agent             -- Preferred Agent - Preferred Agency
        # 4,0 = TMLT Test User              -- Account to Test COMM2 Scenarios
        # 5,0 = QA Agent                    -- QA Agent
        # 6,0 = Janice Quinn                -- 2nd Preferred Agent - ABC Insurance

        # TODO: NEED TO FIX SO THAT SCRIPT USES STRING VALUE CONTAINED IN contract_class variable
        # Access XML to retrieve contract_class

        # NOTE: For XML, the array count starts at 0
        # I have inserted a placeholder element at 0 -- Ken
        # Array will be 1 - 74
        # For List of Contract Classes, See Contract_Classes.xml
        tree = ET.parse(os.path.join(config_file_directory, 'Contract_Classes.xml'))
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
        # baseURL = "https://service.wn.nasinsurance.com/"
        driver = webdriver.Chrome(os.path.join(config_file_directory, 'chromedriver.exe'))

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
        pp.click_NGP_USPRO()

        # The following lines added on 5-15-17 work
        pp.click_contract_class_drop_down_select_contract_class(contract_class)
        # pp.select_contract_class_dropdown()

        # pp.select_contract_class(contract_class)  # Script Ends Here
        pp.click_continue_on_contract_class_modal_after_selecting_contract_class()

        ##pp.click_contract_class_modal_NGP_USPRO()
        ##pp.select_contract_class_dropdown()

        # These next (2) lines work
        ##pp.select_contract_class(contract_class_int_value)
        ##pp.click_continue_on_contract_class_modal_NGP_USPRO()


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
        saw_ii = Insured_Information(driver)
        saw_ii.enter_annual_revenue(revenue)
        saw_ii.click_next()
        saw_PAF = PAF(driver)

        ### Quote Creation Section  ###
        ###                         ###

        # Create Quote with PCI Option
        saw_PAF.create_quote_PCI_DSS_No_DQ(total_num_records)

        # Create Quote with NO PCI Option
        # saw_PAF.create_quote_No_PCI_DSS_No_DQ(total_num_records)

        # Create Quote that Triggers DQ


        # Click Next on PAF Screen
        saw_PAF.click_next()

        #### This section determines if PCI / Non-PCI Coverage Options display
        saw_CC_PCI = PCI_Coverage_Options(driver)
        saw_CC_No_PCI = No_PCI_Coverage_Options(driver)

        #### This class is for generic objects that display on the Coverage Options page
        saw_CC = Coverage_Options(driver)

        # saw_CC.select_all_deselect_all()

        ### Choose PCI / No PCI Options in this block   ###
        ###                                             ###

        ### PCI Options ###

        # saw_CC_PCI.select_250K_limit_500_Deductible()
        # saw_CC_PCI.select_250K_limit_1K_Deductible()
        # saw_CC_PCI.select_250K_limit_2pt5K_Deductible()
        # saw_CC_PCI.select_250K_limit_5K_Deductible()
        # saw_CC_PCI.select_250K_limit_10K_Deductible()
        # saw_CC_PCI.select_250K_limit_25K_Deductible()
        # saw_CC_PCI.select_500K_limit_500_Deductible()
        # saw_CC_PCI.select_500K_limit_1K_Deductible()
        # saw_CC_PCI.select_500K_limit_2pt5K_Deductible()
        # saw_CC_PCI.select_500K_limit_5K_Deductible()
        # saw_CC_PCI.select_500K_limit_10K_Deductible()
        saw_CC_PCI.select_500K_limit_25K_Deductible()
        # saw_CC_PCI.select_1MM_limit_500_Deductible()
        # saw_CC_PCI.select_1MM_limit_1K_Deductible()
        # saw_CC_PCI.select_1MM_limit_2pt5K_Deductible()
        # saw_CC_PCI.select_1MM_limit_5K_Deductible()
        # saw_CC_PCI.select_1MM_limit_10K_Deductible()
        # saw_CC_PCI.select_1MM_limit_25K_Deductible()
        # saw_CC_PCI.select_250K_500K_1MM_2MM_limit_500_Deductible()
        # saw_CC_PCI.select_250K_500K_limit_500_Deductible()
        # saw_CC_PCI.select_250K_500K_1MM_2MM_limit_2pt5K_Deductible()

        ### No-PCI Options ###

        # saw_CC_No_PCI.select_250K_limit_500_Deductible()
        # saw_CC_No_PCI.select_250K_limit_1K_Deductible()
        # saw_CC_No_PCI.select_250K_limit_2pt5K_Deductible()
        # saw_CC_No_PCI.select_250K_limit_5K_Deductible()
        # saw_CC_No_PCI.select_250K_limit_10K_Deductible()
        # saw_CC_No_PCI.select_250K_limit_25K_Deductible()
        # saw_CC_No_PCI.select_500K_limit_500_Deductible()
        # saw_CC_No_PCI.select_500K_limit_1K_Deductible()
        # saw_CC_No_PCI.select_500K_limit_2pt5K_Deductible()
        # saw_CC_No_PCI.select_500K_limit_5K_Deductible()
        # saw_CC_No_PCI.select_500K_limit_10K_Deductible()
        # saw_CC_No_PCI.select_500K_limit_25K_Deductible()
        # saw_CC_No_PCI.select_1MM_limit_500_Deductible()
        # saw_CC_No_PCI.select_1MM_limit_1K_Deductible()
        # saw_CC_No_PCI.select_1MM_limit_2pt5K_Deductible()
        # saw_CC_No_PCI.select_1MM_limit_5K_Deductible()
        # saw_CC_No_PCI.select_1MM_limit_10K_Deductible()
        # saw_CC_No_PCI.select_1MM_limit_25K_Deductible()
        # saw_CC_No_PCI.select_250K_500K_1MM_2MM_limit_500_Deductible()
        # saw_CC_No_PCI.select_250K_500K_limit_500_Deductible()
        # saw_CC_No_PCI.select_250K_500K_1MM_2MM_limit_2pt5K_Deductible()

        #saw_CC.select_all_deselect_all()

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

        time.sleep(2)

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