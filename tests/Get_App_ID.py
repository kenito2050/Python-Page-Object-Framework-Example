import unittest
from urllib.parse import urlparse, parse_qs
from xml.etree import ElementTree as ET

from faker import address
from faker import company
from selenium import webdriver

from pages.producer_center.client_contact_page import ClientContact
from pages.producer_center.client_search_page import ClientSearch
from pages.producer_center.products_programs_page import ProductsAndPrograms
from pages.producer_center.saw.coverage_periods_page import CoveragePeriods
from pages.producer_center.saw.products.NGP.PAF.PAF import PAF
from pages.producer_center.saw.products.NGP.insured_information.insured_information import Insured_Information
from pages.service_center.agents_page import AgentsPage
from pages.service_center.login_page import LoginPage
from pages.service_center.navigation_bar import NavigationBar
from utilities.contract_classes.contract_classes import ContractClasses
from utilities.state_capitals.state_capitals import StateCapitals
from utilities.zip_codes.zip_codes import ZipCodes


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

        # Declare Application ID value
        application_id_value = ""

        # Initialize Driver; Launch URL
        baseURL = "http://svcrel.wn.nasinsurance.com/"
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
        # NEED TO RETURN THE application_id STRING
        #cc.parse_url_get_app_id()

        # Get the Application ID from URL
        current_url = driver.current_url
        parts = urlparse(current_url)
        query_dict = parse_qs(parts.query)
        application_id = (query_dict['app_id'][0])

        cc.click_next()

        cp = CoveragePeriods(driver)
        #cp.enter_current_date_as_effective_date()
        cp.click_next()
        saw_ii = Insured_Information(driver)
        saw_ii.enter_annual_revenue()
        saw_ii.click_next()
        saw_PAF = PAF(driver)
        saw_PAF.create_quote_no_DQ()
        saw_PAF.click_next()

        # Wait
        driver.implicitly_wait(3)

        # Close Browser
        driver.quit()

cq = CreateQuote()
cq.login_search_for_agent_create_quote()