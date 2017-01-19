from faker import address
from faker import company
from faker import frandom
from pages.service_center.login_page import LoginPage
from pages.service_center.navigation_bar import NavigationBar
from pages.service_center.agents_page import AgentsPage
from pages.service_center.applications_page import ApplicationsPage
from pages.service_center.subjectivities import Subjectivities
from pages.producer_center.products_programs_page import ProductsAndPrograms
from pages.producer_center.ballpark import BallPark

from pages.producer_center.client_search_page import ClientSearch
from pages.producer_center.client_contact_page import ClientContact
from pages.producer_center.coverage_periods_page import CoveragePeriods
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
from selenium.webdriver.support.wait import WebDriverWait
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
        baseURL = "http://svcdev.wn.nasinsurance.com/"
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
        pp.click_ballpark()

        bp = BallPark(driver)
        bp.switch_windows()
        bp.start_ballpark_enter_faker_company_name_valid_zip(company_name_string, postal_code)

        # Script Works up to this point - Ken


        # Wait
        driver.implicitly_wait(3)

        # Close Browser
        driver.quit()

cq = CreateQuote()
cq.login_search_for_agent_create_quote()