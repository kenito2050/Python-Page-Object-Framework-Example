import unittest
import os
from xml.etree import ElementTree as ET

from faker import address
from faker import company
from faker import name
from selenium import webdriver
import time

from pages.producer_center.ballpark.ballpark_Indication import BallPark_Indication
from pages.producer_center.ballpark.ballpark_PAF import BallPark_PAF
from pages.producer_center.ballpark.ballpark_download_send import BallPark_Download_Send
from pages.producer_center.products_programs_page import ProductsAndPrograms
from pages.service_center.agents_page import AgentsPage
from pages.service_center.login_page import LoginPage
from pages.service_center.navigation_bar import NavigationBar
from utilities.Environments.Environments import Environments
from utilities.contract_classes.contract_classes_LTC import ContractClasses_LTC
from utilities.state_capitals.state_capitals import StateCapitals
from utilities.zip_codes_state_capitals.zip_codes import ZipCodes


class CreateQuote():

    def test_login_search_for_agent_create_quote(self):

        ## Directory Locations

        tests_directory = os.path.abspath(os.pardir)
        framework_directory = os.path.abspath(os.path.join(tests_directory, os.pardir))
        config_file_directory = os.path.abspath(os.path.join(framework_directory, 'config_files'))
        test_case_directory = os.path.abspath(os.path.join(framework_directory, 'utilities\Excel_Sheets\Products'))
        test_results_directory = os.path.abspath(os.path.join(framework_directory, 'utilities\Excel_Sheets\Test_Results'))

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
        #company_name_string = company_name
        company_name_string = "QA Ballpark Test" + " " + "-" + " " + first_name + " " + last_name + " " + "dba" + " " + company_name
        address_value = address.street_address()
        city = StateCapitals.return_state_capital(state)
        postal_code = ZipCodes.return_zip_codes(state)

        bed_count = "5"
        revenue = "1000000"

        # Access XML to retrieve login credentials
        tree = ET.parse(os.path.join(config_file_directory, 'resources.xml'))
        login_credentials = tree.getroot()
        username = (login_credentials[0][0].text)
        password = (login_credentials[0][1].text)

        # Access XML to retrieve the agent to search for
        tree = ET.parse(os.path.join(config_file_directory, 'Agents.xml'))
        agents = tree.getroot()
        agent = (agents[5][0].text)

        # 0,0 = Crump Tester                -- Wholesale Agent - Crump Insurance Services, Boston - Test Account
        # 1,0 = Susan Leeming - TEST        -- Sub Agent of Wholesale Agency
        # 2,0 = Retail Agent                -- Retail Agent - Boston Retail Insurance
        # 3,0 = Preferred Agent             -- Preferred Agent - Preferred Agency
        # 4,0 = TMLT Test User              -- Account to Test COMM2 Scenarios
        # 5,0 = QA Agent                    -- QA Agent
        # 6,0 = 2nd Preferred Agent         -- 2nd Preferred Agent - ABC Insurance

        # TODO: NEED TO FIX SO THAT SCRIPT USES STRING VALUE CONTAINED IN contract_class variable
        # Access XML to retrieve contract_class

        # NOTE: For XML, the array count starts at 0
        # I have inserted a placeholder element at 0 -- Ken
        # Array will be 1 - 74
        # For List of Contract Classes, See Contract_Classes.xml
        tree = ET.parse(os.path.join(config_file_directory, 'Contract_Classes_LTC.xml'))
        contract_classes_XML = tree.getroot()
        contract_class = (contract_classes_XML[0][1].text)

        # NOTE: For contract_classes.py, the array count starts at 1
        # Array will be 1 - 74
        contract_class_int_value = ContractClasses_LTC.return_contract_class_values(contract_class)

        # To Debug, contract_class, uncomment the next line; set value to an integer from the utilities.contract_classes.py class
        # 'Assisted Living Facilities/RCFEs': '1',

        # Date Variables
        date_today = time.strftime("%m/%d/%Y")
        ad_hoc_effectiveDate = "07/01/2017"

        # Initialize Driver; Launch URL
        # baseURL = "https://svcrel.wn.nasinsurance.com/"
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
        pp.click_ballpark()

        bp_PAF = BallPark_PAF(driver)
        bp_PAF.switch_windows()
        bp_PAF.start_ballpark_enter_faker_company_name_valid_zip(company_name_string, postal_code)
        bp_PAF.select_contract_class(contract_class)
        bp_PAF.click_ballpark_button()

        bp_PAF.select_LTC()
        time.sleep(3)

        # Enter Ad Hoc Effective Date
        # bp_PAF.enter_effective_date(ad_hoc_effectiveDate)

        # Enter Today's Date as Effective Date
        bp_PAF.enter_current_date(date_today)

        time.sleep(3)
        bp_PAF.enter_bed_count(bed_count)
        bp_PAF.click_ballpark_button()

        bp_Indication = BallPark_Indication(driver)
        bp_Indication.click_Download_Send_Indication()

        bp_Download_Send = BallPark_Download_Send(driver)
        bp_Download_Send.input_email()
        bp_Download_Send.click_send_email()

        # Close Ballpark Window
        driver.close()

        # Switch to First Window (Service Center)
        driver.switch_to.window(driver.window_handles[0])

        # Close First Window (Service Center)
        # driver.close()

        # Wait
        driver.implicitly_wait(3)

        # Close Browser
        driver.quit()

cq = CreateQuote()
cq.test_login_search_for_agent_create_quote()