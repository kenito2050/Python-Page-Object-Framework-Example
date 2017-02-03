from faker import address
from faker import company
from faker import frandom
from pages.service_center.login_page import LoginPage
from pages.service_center.navigation_bar import NavigationBar
from pages.service_center.agents_page import AgentsPage
from pages.service_center.applications_page import ApplicationsPage
from pages.service_center.subjectivities import Subjectivities
from pages.service_center.policies_page import PoliciesPage
from pages.producer_center.products_programs_page import ProductsAndPrograms
from pages.producer_center.client_search_page import ClientSearch
from pages.producer_center.client_contact_page import ClientContact
from pages.producer_center.coverage_periods_page import CoveragePeriods
from pages.producer_center.thank_you_page import Thank_You_Page
from pages.producer_center.saw.products.NGP.insured_information.insured_information import Insured_Information
from pages.producer_center.saw.products.NGP.PAF.PAF import PAF
from pages.producer_center.saw.products.NGP.coverage_options.coverage_options import Coverage_Options
from pages.producer_center.saw.products.NGP.summary.summary import Summary
from pages.producer_center.saw.products.NGP.quote_review.quote_review import Quote_Review
from pages.producer_center.saw.products.NGP.select_option.select_option import Select_Option
from pages.producer_center.saw.products.NGP.confirm_order_details.confirm_order_details import Confirm_Order_Details
from pages.producer_center.saw.products.NGP.confirm_and_issue.confirm_and_issue import Confirm_and_Issue
from pages.producer_center.saw.products.NGP.invoice.invoice import Invoice

from selenium import webdriver
import unittest
from urllib.parse import urlparse, parse_qs
from utilities.contract_classes.contract_classes import ContractClasses
from utilities.create_insured_address.create_insured_address import Create_Insured_Address
from utilities.state_capitals.state_capitals import StateCapitals
from utilities.zip_codes.zip_codes import ZipCodes
from xml.etree import ElementTree as ET

class CreateQuote(unittest.TestCase):

    def login_search_for_agent_create_quote(self):

        # Create "Fake" Variables
        #state = frandom.us_state()
        state = "California"
        #state = Create_Insured_Address.return_alabama(state_value)
        company_name = company.company_name()
        company_name_string = company_name + " " + "-" + " " + state + " " + "Test"
        address_value = address.street_address()
        city = StateCapitals.return_state_capital(state)
        postal_code = ZipCodes.return_zip_codes(state)

        # Access XML to retrieve login credentials
        tree = ET.parse('resources.xml')
        login_credentials = tree.getroot()
        username = (login_credentials[0][0].text)
        password = (login_credentials[0][1].text)

        # Access XML to retrieve the agent to search for
        tree = ET.parse('Agents.xml')
        agents = tree.getroot()
        agent = (agents[0][0].text)

        # TODO: NEED TO FIX SO THAT SCRIPT USES STRING VALUE CONTAINED IN contract_class variable
        # Access XML to retrieve contract_class

        # NOTE: For XML, the array count starts at 0
        # I have inserted a placeholder element at 0 -- Ken
        # Array will be 1 - 74
        # For List of Contract Classes, See Contract_Classes.xml
        tree = ET.parse('Contract_Classes.xml')
        contract_classes_XML = tree.getroot()
        contract_class = (contract_classes_XML[0][7].text)

        # NOTE: For contract_classes.py, the array count starts at 1
        # Array will be 1 - 74
        contract_class_int_value = ContractClasses.return_contract_class_values(contract_class)

        # To Debug, contract_class, uncomment the next line; set value to an integer from the utilities.contract_classes.py class
        #contract_class_value = "74"

        # Initialize Driver; Launch URL
        baseURL = "http://svcdemo9.wn.nasinsurance.com/"
        driver = webdriver.Chrome('C:\ChromeDriver\chromedriver.exe')

        # Maximize Window; Launch URL
        driver.maximize_window()
        driver.get(baseURL)
        driver.implicitly_wait(3)

        # Call Login methods from Pages.home.login_page.py
        lp = LoginPage(driver)
        lp.login(username, password)
        nb = NavigationBar(driver)
        nb.click_agents()
        ap = AgentsPage(driver)
        ap.search_for_agent(agent)

        pp = ProductsAndPrograms(driver)
        pp.click_NGP()
        pp.click_contract_class_modal()
        pp.select_contract_class_dropdown()

        # These next (2) lines work
        pp.select_contract_class(contract_class_int_value)
        pp.click_continue_on_contract_class_modal()

        # These next (2) Lines are NOT working
        #pp.select_contract_class_use_string(contract_class)
        #pp.select_contract_class_use_string()

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
        query_dict_1 = parse_qs(first_url_string.query)
        application_id = (query_dict_1['app_id'][0])

        cc.click_next()

        cp = CoveragePeriods(driver)
        #cp.enter_current_date_as_effective_date()
        cp.click_next()
        saw_ii = Insured_Information(driver)
        saw_ii.enter_annual_revenue()
        saw_ii.click_next()
        saw_PAF = PAF(driver)
        saw_PAF.create_quote_with_PCI_DSS()
        saw_PAF.click_next()
        saw_CC = Coverage_Options(driver)
        saw_CC.select_PCI_DSS_limits_deductibles_on_coverage_options()
        saw_CC.proceed_to_quote()
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
        new_current_url_1 = driver.current_url
        slashparts_1 = new_current_url_1.split('/')
        # Now join back the first three sections 'http:', '' and 'example.com'
        new_base_url_1 = '/'.join(slashparts_1[:3]) + '/'

        # URL strings for Subjectivities
        app_details_string = "?c=app.view&id="
        app_subjectivities_string = "?c=app.track_subjectivities&id="

        application_details_screen = new_base_url_1 + app_details_string + application_id
        application_subjectivites_screen = new_base_url_1 + app_subjectivities_string + application_id

        # Navigate to Application Subjectivities Screen
        driver.get(application_subjectivites_screen)

        # Approve Subjectivities
        sub = Subjectivities(driver)
        sub.change_open_subjectivities_to_received()
        sub.select_yes_to_subjectivities_met()
        sub.click_submit()
        sub.click_agent_link()

        # Return to Producer Center; Issue Policy
        saw_confirm_issue.input_signature()
        saw_confirm_issue.click_accept_terms_issue_policy()

        # Click the Policy Link on Thank You Page -- Need to pass policy number value; Currently not working
        thank_you = Thank_You_Page(driver)

        # Retrieve and Store Policy Number
        policy_number = thank_you.retrieve_store_policy_number()
        ## push it to class
        self.policy_number = policy_number

        # Click on Policy Link
        thank_you.click_policy_link()

        # Get the Policy ID from URL -- This code works
        current_url_policy = driver.current_url
        second_url_string = urlparse(current_url_policy)
        query_dict_2 = parse_qs(second_url_string.query)
        policy_string = (query_dict_2['id'][0])
        policy_id = policy_string[:-4]

        # Return to Admin Interface
        saw_confirm_issue.click_return_to_Admin_Interface()

        # Click Policies
        nb.click_policies()

        # URL Strings for ALL Policies
        new_current_url_2 = driver.current_url
        slashparts_2 = new_current_url_2.split('/')
        # Now join back the first three sections 'http:', '' and 'example.com'
        new_base_url_2 = '/'.join(slashparts_2[:3]) + '/'
        all_policies_string = '?c=policy_list.list&type=all'
        policy_view_string = 'index.php?c=policy.view&id='

        # Problem: In Demo 9, URL String differs
        # Navigate to Policy Details Screen of Policy that was just created
        policies_all_screen = new_base_url_2 + all_policies_string
        policy_details_screen = new_base_url_2 + policy_view_string + policy_id
        driver.get(policy_details_screen)

        policies_page = PoliciesPage(driver)
        # Enter Policy Number and Click Search
        policies_page.enter_policy_name(policy_number)
        policies_page.click_search_button()

        # Wait
        driver.implicitly_wait(3)

        # Close Browser
        driver.quit()

cq = CreateQuote()
cq.login_search_for_agent_create_quote()