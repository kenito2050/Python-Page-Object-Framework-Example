from urllib.parse import urlparse, parse_qs
from xml.etree import ElementTree as ET
from selenium import webdriver
import time

from utilities.contract_classes.contract_classes_Medical import ContractClasses_Medical
from utilities.nasonline_test.nasonline_test import NasOnlineTest

from pages.producer_center.products_programs_page import ProductsAndPrograms
from pages.producer_center.client_search_page import ClientSearch
from pages.producer_center.my_policies.my_policies_screens.active_policies import active_policies
from pages.producer_center.navigation_bar import Navigation_Bar
from pages.producer_center.client_contact_page import ClientContact
from pages.producer_center.saw.coverage_periods_page import CoveragePeriods
from pages.producer_center.saw.products.CYB_OMIC.insured_information.insured_information import Insured_Information
from pages.producer_center.saw.products.CYB_OMIC.PAF.PAF import PAF
from pages.producer_center.saw.products.CYB_OMIC.coverage_options.PCI_coverage_options import PCI_Coverage_Options
from pages.producer_center.saw.products.CYB_OMIC.coverage_options.No_PCI_coverage_options import No_PCI_Coverage_Options
from pages.producer_center.saw.products.CYB_OMIC.coverage_options.coverage_options import Coverage_Options
from pages.producer_center.saw.products.CYB_OMIC.select_option.select_option import Select_Option
from pages.producer_center.saw.quote_review import Quote_Review
from pages.producer_center.saw.invoice import Invoice
from pages.producer_center.saw.confirm_order_details import Confirm_Order_Details
from pages.producer_center.saw.confirm_and_issue import Confirm_and_Issue
from pages.producer_center.saw.thank_you_page import Thank_You_Page
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
from utilities.zip_codes_state_capitals.zip_codes import ZipCodes

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
global _OLD_scenario_number


class test_CYB_OMIC (NasOnlineTest):

    def __init__(self):

        product = "CYB_OMIC"
        self.initialSetup()
        self.readTestfile(product)

    def runTests(self):

        # Call Login methods from Pages.home.login_page.py
        lp = LoginPage(self.driver)
        lp.login(self.username, self.password)
        lp.click_login_button()
        nb = NavigationBar(self.driver)
        nb.click_agents()
        ap = AgentsPage(self.driver)
        ap.search_for_agent(agent)
        ap.click_submit_new_application_as_agent()

        pp = ProductsAndPrograms(self.driver)
        pp.click_CYB_OMIC()

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

        cs = ClientSearch(self.driver)
        cs.input_bogus_client_data(self.postal_code)
        cs.manually_input_new_client()
        cs.enter_new_client_name_address(self.company_name_string, self.address_value, self.city, state)
        cc = ClientContact(self.driver)

        # TODO:
        # Code now parses URL String & retrieves application ID
        # cc.parse_url_get_app_id()

        # Get the Application ID from URL -- THIS WORKS
        current_url = self.driver.current_url
        first_url_string = urlparse(current_url)
        query_dict = parse_qs(first_url_string.query)
        application_id = (query_dict['app_id'][0])

        cc.click_next()

        cp = CoveragePeriods(self.driver)

        cp.click_return_to_Admin_Interface()

        # Navigate to Application Details page
        current_url_2 = self.driver.current_url
        slashparts = current_url_2.split('/')
        # Now join back the first three sections 'http:', '' and 'example.com'
        base_url_2 = '/'.join(slashparts[:3]) + '/'

        app_details_string = "?c=app.view&id="
        # app_subjectivities_string = "?c=app.track_subjectivities&id="

        application_details_screen = base_url_2 + app_details_string + application_id

        # Navigate to Application Subjectivities Screen
        self.driver.get(application_details_screen)

        app_details = App_Details(self.driver)

        # Update the Create Date to the Ad Hoc Effective Date Value
        app_details.update_create_date(self.effective_date_formatted)

        # Click Update Button
        app_details.click_update_button()

        # Click on Agent Link to return to Producer Center
        app_details.click_agent_text_link()

        # Return to Coverage Periods screen

        # Enter an Ad Hoc Effective Date
        cp.enter_ad_hoc_effective_date(self.effective_date_formatted)

        # Enter Today's Date as Effective Date
        # cp.enter_current_date_as_effective_date(date_today)

        # Click Next
        cp.click_next()

        # Instantiate Insured Information;
        saw_ii = Insured_Information(self.driver)

        # Enter FTE & NON-FTE Physician Counts
        # Click Next
        saw_ii.enter_fte_physician_count(staff_count)
        saw_ii.enter_non_fte_physician_count(staff_count)
        saw_ii.click_next()

        saw_PAF = PAF(self.driver)

        # Return to Admin Interface / Set Creation Date
        # saw_PAF.click_return_to_Admin_Interface()

        #### If / ELSE Section to Determine how PAF is completed

        # Scenario 1: PCI Options
        # Scenario 2: No PCI Options

        if test_scenario_number == "1":
            saw_PAF.create_quote_PCI_DSS_No_DQ(revenue)
        elif test_scenario_number == "2":
            saw_PAF.create_quote_No_PCI_DSS_No_DQ(revenue)

        # Click Next on PAF Screen
        saw_PAF.click_next()

        ######################################
        ######################################
        ######################################
        ### SCRIPT Will NOT WORK AFTER THIS POINT
        ### RATES NEED TO BE ADDED
        ######################################
        ######################################
        ######################################

        ## Coverage Options Section  ###
        ##                           ###

        #### This class is for generic objects that display on the Coverage Options page
        saw_CC = Coverage_Options(self.driver)

        ### Clear All selections on Coverage Options Screen
        saw_CC.select_all_deselect_all()

        ### Declare instances of Coverage Options

        ## If Test Scenario = 1, Use PCI Options
        ## Else if Test Scenario = 2, Use Non-PCI Options

        if test_scenario_number == "1":
            saw_CC_in_use = PCI_Coverage_Options(self.driver)
            getattr(saw_CC_in_use, _OLD_scenario)()

        elif test_scenario_number == "2":
            saw_CC_in_use = No_PCI_Coverage_Options(self.driver)
            getattr(saw_CC_in_use, _OLD_scenario)()

        ### Commented out next line; Moved Proceed to Quote button Call into the PCI / Non-PCI Methods
        saw_CC.click_proceed_to_quote()

        saw_summary = Summary(self.driver)
        saw_summary.click_generate_quote()
        saw_quote_review = Quote_Review(self.driver)
        saw_quote_review.click_select_option()
        saw_select_option = Select_Option(self.driver)
        saw_select_option.select_premium()
        saw_select_option.click_accept_rate_and_continue()
        saw_confirm_order_details = Confirm_Order_Details(self.driver)
        saw_confirm_order_details.click_next()
        saw_invoice = Invoice(self.driver)
        saw_invoice.click_proceed_to_issuing()

        # Click Return to Admin Interface
        saw_confirm_issue = Confirm_and_Issue(self.driver)

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
        app_page = ApplicationsPage(self.driver)
        app_page.enter_application_id(application_id)
        app_page.click_search_button()

        # Click on application id link
        # THIS IS NOT WORKING
        # app_page.click_application_id_link(application_id)

        # Navigate to Application Details page
        new_current_url = self.driver.current_url
        slashparts = new_current_url.split('/')
        # Now join back the first three sections 'http:', '' and 'example.com'
        new_base_url = '/'.join(slashparts[:3]) + '/'

        app_details_string = "?c=app.view&id="
        app_subjectivities_string = "?c=app.track_subjectivities&id="

        application_details_screen = new_base_url + app_details_string + application_id
        application_subjectivites_screen = new_base_url + app_subjectivities_string + application_id

        # Navigate to Application Subjectivities Screen
        self.driver.get(application_subjectivites_screen)

        # Approve Subjectivities
        sub = Subjectivities(self.driver)
        sub.set_all_subjectivities_to_recieved()
        # sub.change_open_subjectivities_to_received()
        # sub.select_yes_to_subjectivities_met()
        sub.click_submit()
        sub.click_agent_link()

        # Return to Producer Center; Issue Policy
        saw_confirm_issue.input_signature()
        saw_confirm_issue.click_accept_terms_issue_policy()
        # Retrieve Policy Number of Policy that was issued; Policy Number stored in policy_text
        thank_you = Thank_You_Page(self.driver)
        policy_text = thank_you.retrieve_store_policy_number()

        # Return to Admin Interface
        saw_confirm_issue.click_return_to_Admin_Interface()

        # Click on Policies link; Navigate to Policy that was just issued
        nb.click_policies()

        pp = PoliciesPage(self.driver)
        # On Policies Page, Click All link
        pp.click_all_link()

        # Enter Policy Number & Click Search
        pp.enter_policy_name(policy_text)
        pp.click_search_button()

        # Click on the Policy link, Open Policy Details
        pp.click_policy_link(policy_text)

        # Click Effective Periods
        ps = Policy_Screens(self.driver)
        ps.click_Effective_Periods()

        # Change Effective Periods Dates to allow renewals
        ep = Effective_Periods(self.driver)
        ep.change_dates_expire_policy_allow_renewal()
        ep.click_update_dates()

        # Click Details link to display the Policy Details screen
        ps.click_Details()

        # On Details Screen, Click on the Agent that issued the Policy
        details = Details(self.driver)
        details.click_agent_link(agent)

        # Agent Details Screen Displays
        ag = Agent_Details(self.driver)

        # Click "Submit New Application as" link
        ag.click_submit_new_application_as_agent()

        # Click My Policies on Navigation Bar
        pnb = Navigation_Bar(self.driver)
        pnb.click_my_policies()

        # Locate Policy that was issued
        ap = active_policies(self.driver)
        ap.enter_policy_name(policy_text)
        ap.click_search_button()

        # Click Policy
        ap.click_policy_link(policy_text)

        # Code works up to this point

        # Wait
        self.driver.implicitly_wait(3)

        # Close Browser
        self.driver.quit()

cq = test_CYB_OMIC()
cr = NasOnlineTest()
