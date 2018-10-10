import unittest
import os
from xml.etree import ElementTree as ET
import xlrd

from faker import address
from faker import company
from faker import name
from selenium import webdriver

from pages.producer_center.ballpark.ballpark_Indication import BallPark_Indication
from pages.producer_center.ballpark.ballpark_PAF import BallPark_PAF
from pages.producer_center.ballpark.ballpark_download_send import BallPark_Download_Send
from pages.producer_center.products_programs_page import ProductsAndPrograms
from pages.service_center.agents_page import AgentsPage
from pages.service_center.login_page import LoginPage
from pages.service_center.navigation_bar import NavigationBar
from utilities.contract_classes.contract_classes_Medical import ContractClasses_Medical
from utilities.Environments.Environments import Environments
from utilities.state_capitals.state_capitals import StateCapitals
from utilities.zip_codes_state_capitals.zip_codes import ZipCodes
import time
from config_globals import *

class TestCreateQuote():

    def test_login_search_for_agent_create_quote(self, browser, env):

        Product = "CYB_MICA_BALLPARK"
        driver = browser

        ## Directory Locations

        tests_directory = ROOT_DIR / 'tests'
        framework_directory = ROOT_DIR
        config_file_directory = CONFIG_PATH
        test_case_directory = framework_directory / 'utilities' / 'Excel_Sheets' / 'Products'
        test_results_directory = framework_directory / 'utilities' / 'Excel_Sheets' / 'Test_Results'

        ## Determine Test Environment to run scripts

        ## Select Appropriate URL based on the Environment Value from above
        baseURL  = Environments.return_environments(env)

        global test_summary
        global effective_date
        global contract_class
        global agent
        global state
        global revenue
        global staff_count

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
                effective_date = sh.cell_value(i, 1)
                contract_class = sh.cell_value(i, 2)
                agent = sh.cell_value(i, 3)
                state = sh.cell_value(i, 4)
                revenue = str(round(sh.cell_value(i, 5)))
                staff_count = int(round(sh.cell_value(i, 6)))

            # Else, the cell is empty
            # End the Loop
            else:
                break

        ## Determine Test Environment to run scripts

        ## Read in value from test_environment.xml
        tree = ET.parse(str(config_file_directory / 'test_environment.xml'))
        test_environment = tree.getroot()
        environment = (test_environment[0][0].text)

        ## Select Appropriate URL based on the Environment Value from above
        baseURL = Environments.return_environments(env)

        first_name = name.first_name()
        last_name = name.last_name()
        company_name = company.company_name()
        # company_name_string = company_name
        company_name_string = "QA Test" + " " + "-" + " " + "Dr." + " " + first_name + " " + last_name + " " + "dba" + " " + company_name
        postal_code = ZipCodes.return_zip_codes(state)

        # Access XML to retrieve login credentials
        tree = ET.parse(str(config_file_directory /  'resources.xml'))
        login_credentials = tree.getroot()
        username = (login_credentials[0][0].text)
        password = (login_credentials[1][1].text)

        date_today = time.strftime("%m/%d/%Y")
        ad_hoc_effectiveDate = "07/01/2017"

        # Maximize Window; Launch URL
        # driver.maximize_window()
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

        bp_PAF.select_CYB_MICA()
        time.sleep(3)

        # Enter Ad Hoc Effective Date
        # bp_PAF.enter_effective_date(ad_hoc_effectiveDate)

        # Enter Today's Date as Effective Date
        bp_PAF.enter_current_date(date_today)

        time.sleep(3)
        bp_PAF.click_doctor_count_field()
        bp_PAF.enter_doctor_count(staff_count)
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
        #driver.close()

        # Wait
        driver.implicitly_wait(3)

        # Close Browser
        driver.quit()