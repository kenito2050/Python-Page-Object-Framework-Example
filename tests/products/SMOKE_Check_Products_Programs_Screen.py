from xml.etree import ElementTree as ET
import xlrd
from pages.producer_center.products_programs_page import ProductsAndPrograms
from pages.service_center.agents_page import AgentsPage
from pages.service_center.login_page import LoginPage
from pages.service_center.navigation_bar import NavigationBar
from utilities.Environments.Environments import Environments
from config_globals import *

class TestCreateQuote:

    def test_login_verify_products_programs(self, browser, env):

        Product = "Regression_Suite"
        driver = browser

        ## Directory Locations

        tests_directory = ROOT_DIR / 'tests'
        framework_directory = ROOT_DIR
        config_file_directory = CONFIG_PATH
        test_case_directory = framework_directory / 'utilities' / 'Excel_Sheets' / 'Products'
        test_results_directory = framework_directory / 'utilities' / 'Excel_Sheets' / 'Test_Results'

        global test_summary
        global agent

        # Open Test Scenario Workbook; Instantiate worksheet object
        # 0 - First Worksheet
        # 1 - Second Worksheet...etc

        wb = xlrd.open_workbook(str(test_case_directory / Product) + '.xlsx')
        sh = wb.sheet_by_name("Verify_Products_Programs")

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
                agent = sh.cell_value(i, 1)

            # Else, the cell is empty
            # End the Loop
            else:
                break

        ## Select URL to run test given the "env" variable
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

        # Verify that Products & Programs Screen is populated
        # Code checks to verify that start button elements are present

        # Assert that Program Page Elements display on page

        _Adult_Daycare_text = pp.return_Adult_DayCare_text()
        assert _Adult_Daycare_text == "Start"

        _CAP_CYB_text = pp.return_CAP_CYB_text()
        assert _CAP_CYB_text == "Start"

        _CYB_AAO_text = pp.return_CYB_AAO_text()
        assert _CYB_AAO_text == "Start"

        _CYB_CAP_text = pp.return_CYB_CAP_text()
        assert _CYB_CAP_text == "Start"

        _CYB_OMIC_text = pp.return_CYB_OMIC_text()
        assert _CYB_OMIC_text == "Start"

        _CYB_LAMMICO_text = pp.return_CYB_LAMMICO_text()
        assert _CYB_LAMMICO_text == "Start"

        _CYB_MDA_text = pp.return_CYB_MDA_text()
        assert _CYB_MDA_text == "Start"

        _CYB_MMD_text = pp.return_CYB_MMD_text()
        assert _CYB_MMD_text == "Start"

        _CYB_MMIC_text = pp.return_CYB_MMIC_text()
        assert _CYB_MMIC_text == "Start"

        _CYB_MICA_text = pp.return_CYB_MICA_text()
        assert _CYB_MICA_text == "Start"

        _CYB_PAS_text = pp.return_CYB_PAS_text()
        assert _CYB_PAS_text == "Start"

        _CYB_PAS_PICA_text = pp.return_CYB_PAS_PICA_text()
        assert _CYB_PAS_PICA_text == "Start"

        _CYB_LSA_text = pp.return_CYB_LSA_text()
        assert _CYB_LSA_text == "Start"

        _CYB_USI_text = pp.return_CYB_USI_text()
        assert _CYB_USI_text == "Start"

        _CYB_SVMIC_text = pp.return_CYB_SVMIC_text()
        assert _CYB_SVMIC_text == "Start"

        _CYB_TMLT_text = pp.return_CYB_TMLT_text()
        assert _CYB_TMLT_text == "Start"

        _DAYSPA_text = pp.return_DAYSPA_text()
        assert _DAYSPA_text == "Start"

        _EO_MHC_text = pp.return_EO_MHC_text()
        assert _EO_MHC_text == "Start"

        _EO_MISC_text = pp.return_EO_MISC_text()
        assert _EO_MISC_text == "Start"

        _EO_PM_text = pp.return_EO_PM_text()
        assert _EO_PM_text == "Start"

        _EPL_text = pp.return_EPL_text()
        assert _EPL_text == "Start"

        _GRPHOME_text = pp.return_GRPHOME_text()
        assert _GRPHOME_text == "Start"

        _HHOL_text = pp.return_HHOL_text()
        assert _HHOL_text == "Start"

        _LEXR_TENANT_text = pp.return_LEXR_TENANT_text()
        assert _LEXR_TENANT_text == "Start"

        _MEDEMD_text = pp.return_MEDEMD_text()
        assert _MEDEMD_text == "Start"

        _MED_NCMIC_text = pp.return_MED_NCMIC_text()
        assert _MED_NCMIC_text == "Start"

        _MMTM_text = pp.return_MMTM_text()
        assert _MMTM_text == "Start"

        _NGP_text = pp.return_NGP_text()
        assert _NGP_text == "Start"

        _NGP_CAMICO_text = pp.return_NGP_CAMICO_text()
        assert _NGP_CAMICO_text == "Start"

        _NGP_HUB_text = pp.return_NGP_HUB_text()
        assert _NGP_HUB_text == "Start"

        _NGP_OBLIC_text = pp.return_NGP_OBLIC_text()
        assert _NGP_OBLIC_text == "Start"

        _NGP_RTS_text = pp.return_NGP_RTS_text()
        assert _NGP_RTS_text == "Start"

        _NGP_SBDIA_text = pp.return_NGP_SBDIA_text()
        assert _NGP_SBDIA_text == "Start"

        _NGP_USI_text = pp.return_NGP_USI_text()
        assert _NGP_USI_text == "Start"

        _NGP_USPRO_text = pp.return_NGP_USPRO_text()
        assert _NGP_USPRO_text == "Start"

        _NGP_USPRO_AZIONE_text = pp.return_NGP_USPRO_AZIONE_text()
        assert _NGP_USPRO_AZIONE_text == "Start"

        _RPM_text = pp.return_RPM_text()
        assert _RPM_text == "Start"

        _TLIE_text = pp.return_TLIE_text()
        assert _TLIE_text == "Start"

        _Transitional_Living_Facilities_text = pp.return_Transitional_Living_Facilities_text()
        assert _Transitional_Living_Facilities_text == "Start"

        # Wait
        driver.implicitly_wait(3)
