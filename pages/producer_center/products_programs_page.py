from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import Select
import time

class ProductsAndPrograms():

    def __init__(self, driver):
        self.driver = driver

    def Page_Elements(self):

        # Ballpark

        self.ballpark_link = self.driver.find_element(By.CSS_SELECTOR, "img[alt=\"Get a Ballpark Premium Indication\"]")

        # Products

        self.ADULTDC_link = self.driver.find_element(By.ID, "Adult Day Care_start")

        self.CAP_CYB_link = self.driver.find_element(By.ID, "CyberRisk™ Liability_start")

        # self.CRYO_link = self.driver.find_element(By.ID, "Cryotherapy PL/GL_start")

        self.CYB_AAO_link = self.driver.find_element(By.ID, "AAO Broad Regulatory Protection Plus and e-MD™_start")

        self.CYB_CAP_link = self.driver.find_element(By.ID, "CyberRisk™ Liability/Medefense Plus_start")

        self.CYB_OMIC_link = self.driver.find_element(By.ID, "OMIC Broad Regulatory Protection Plus and e-MD™_start")

        self.CYB_LAMMICO_link = self.driver.find_element(By.ID, "LAMMICO MEDEFENSE™ Plus and Cyber Liability_start")

        self.CYB_MDA_link = self.driver.find_element(By.ID, "Supreme Advantage PDSI / MPAI_start")

        self.CYB_MMD_link = self.driver.find_element(By.ID, "MedMal Direct MEDEFENSE™ Plus and CyberProtector™_start")

        self.CYB_MMIC_link = self.driver.find_element(By.ID, "MMNC e-MD™ and MEDEFENSE™ Plus_start")

        self.CYB_MICA_link = self.driver.find_element(By.ID, "MICA e-Med Protection Plus_start")

        self.CYB_PAS_link = self.driver.find_element(By.ID, "ProAssurance ProSecure Regulatory Risk Protection and Cyber Liability_start")

        self.CYB_PAS_PICA_link = self.driver.find_element(By.ID, "PICA ProSecure Regulatory Risk Protection and Cyber Liability_start")

        # self.CYB_PIC_link = self.driver.find_element(By.ID, "PIC Cyber Liability / Medefense™ Plus_start")

        # self.CYB_PSIC_DDS_link = self.driver.find_element(By.ID, "PSIC Regulatory Proceedings and Network Security & Privacy Coverage for Dentists_start")
        #
        # self.CYB_PSIC_MD_link = self.driver.find_element(By.ID, "PSIC Regulatory Proceedings and Network Security & Privacy Coverage for Physicians_start")

        self.CYB_LSA_link = self.driver.find_element(By.ID, "LSA Cyber Liability / Medefense™ Plus_start")

        self.CYB_USI_link = self.driver.find_element(By.ID, "PrivaSafe with MEDEFENSE™ Plus_start")

        self.CYB_SVMIC_link = self.driver.find_element(By.ID, "SVMIC MEDEFENSE™ Plus and e-MD™_start")

        self.CYB_TMLT_link = self.driver.find_element(By.ID, "TMLT Cyber Liability / Medefense™ Plus_start")

        self.DAYSPA_link = self.driver.find_element(By.ID, "Day Spa PL/GL_start")

        self.EO_MHC_link = self.driver.find_element(By.ID, "Healthcare Misc. E&O_start")

        self.EO_MISC_link = self.driver.find_element(By.ID, "Miscellaneous E&O_start")

        self.EO_PM_link = self.driver.find_element(By.ID, "Property Manager’s E&O with Cyber Liability and Tenant Discrimination_start")

        self.EPL_link = self.driver.find_element(By.ID, "Employment Practices Liability (Under 50 employees)_start")

        self.GRPHOME_link = self.driver.find_element(By.ID, "Group Home_start")

        self.HHOL_link = self.driver.find_element(By.ID, "Home Health Care_start")

        self.LEXR_TENANT_link = self.driver.find_element(By.ID, "Tenant Discrimination Legal Expense and Loss Reimbursement Insurance_start")

        self.MEDEMD_link = self.driver.find_element(By.ID, "e-MD™ Cyber and MEDEFENSE™ Plus_start")

        self.MED_NCMIC_link = self.driver.find_element(By.ID, "NCMIC MEDEFENSE™ Plus_start")

        self.MMTM_link = self.driver.find_element(By.ID, "Momentum Insurance_start")

        self.NGP_link = self.driver.find_element(By.ID, "Cyber Liability_start")

        self.NGP_CAMICO_link = self.driver.find_element(By.ID, "CAMICO Cyber Liability_start")

        self.NGP_HUB_link = self.driver.find_element(By.ID, "HUB International NetGuard™ Plus_start")

        self.NGP_OBLIC_link = self.driver.find_element(By.ID, "OBLIC Cyber Liability_start")

        self.NGP_RTS_link = self.driver.find_element(By.ID, "R-T Specialty Cyber Liability_start")

        self.NGP_SBDIA_link = self.driver.find_element(By.ID, "Security Broker-Dealers and Investment Advisors Cyber Liability_start")

        self.NGP_USI_link = self.driver.find_element(By.ID, "PrivaSafe Cyber Liability_start")

        self.NGP_USPRO_link = self.driver.find_element(By.ID, "US Pro Cyber Liability_start")

        self.NGP_USPRO_AZIONE_link = self.driver.find_element(By.ID, "AZIONE Cyber Liability_start")

        self.RPM_link = self.driver.find_element(By.ID, "RPM Property Managers and Lessors E&O Program_start")

        self.TLIE_link = self.driver.find_element(By.ID, "Texas Lawyers' Insurance Exchange_start")

        self.Transitional_Living_Facilities_link = self.driver.find_element(By.ID, "Transitional Living Facilities_start")

        return self

    # Click Ballpark
    def click_ballpark(self):
        ballpark_link = self.driver.find_element(By.CSS_SELECTOR, "img[alt=\"Get a Ballpark Premium Indication\"]")
        ballpark_link.click()

    # Products
    def click_Ken_V_Test(self):
        Ken_V_Test_link = self.driver.find_element(By.ID, "Ken Villarruel Agency_start")
        Ken_V_Test_link.click()

    def click_ADULTDC(self):
        ADULTDC_link = self.driver.find_element(By.ID, "Adult Day Care_start")
        ADULTDC_link.click()

    def click_CAP_CYB(self):
        CAP_CYB_link = self.driver.find_element(By.ID, "CyberRisk™ Liability_start")
        CAP_CYB_link.click()

    def click_CRYO(self):
        CRYO_link = self.driver.find_element(By.ID, "Cryotherapy PL/GL_start")
        CRYO_link.click()

    def click_CYB_AAO(self):
        CYB_AAO_link = self.driver.find_element(By.ID, "AAO Broad Regulatory Protection Plus and e-MD™_start")
        CYB_AAO_link.click()

    def click_CYB_CAP(self):
        CYB_CAP_link = self.driver.find_element(By.ID, "CyberRisk™ Liability/Medefense Plus_start")
        CYB_CAP_link.click()

    def click_CYB_OMIC(self):
        CYB_OMIC_link = self.driver.find_element(By.ID, "OMIC Broad Regulatory Protection Plus and e-MD™_start")
        CYB_OMIC_link.click()

    def click_CYB_PIC(self):
        CYB_PIC_link = self.driver.find_element(By.ID, "PIC Cyber Liability / Medefense™ Plus_start")
        CYB_PIC_link.click()

    def click_CYB_LAMMICO(self):
        CYB_LAMMICO_link = self.driver.find_element(By.ID, "LAMMICO MEDEFENSE™ Plus and Cyber Liability_start")
        CYB_LAMMICO_link.click()

    def click_CYB_MDA(self):
        CYB_MDA_link = self.driver.find_element(By.ID, "Supreme Advantage PDSI / MPAI_start")
        CYB_MDA_link.click()

    def click_CYB_MMD(self):
        CYB_MMD_link = self.driver.find_element(By.ID, "MedMal Direct MEDEFENSE™ Plus and CyberProtector™_start")
        CYB_MMD_link.click()

    def click_CYB_MMIC(self):
        CYB_MMIC_link = self.driver.find_element(By.ID, "MMNC e-MD™ and MEDEFENSE™ Plus_start")
        CYB_MMIC_link.click()

    def click_CYB_MICA(self):
        CYB_MICA_link = self.driver.find_element(By.ID, "MICA e-Med Protection Plus_start")
        CYB_MICA_link.click()

    def click_CYB_PAS(self):
        CYB_PAS_link = self.driver.find_element(By.ID, "ProAssurance ProSecure Regulatory Risk Protection and Cyber Liability_start")
        CYB_PAS_link.click()

    def click_CYB_PAS_PICA(self):
        CYB_PAS_PICA_link = self.driver.find_element(By.ID, "PICA ProSecure Regulatory Risk Protection and Cyber Liability_start")
        CYB_PAS_PICA_link.click()

    def click_CYB_PSIC_DDS(self):
        CYB_PSIC_DDS_link = self.driver.find_element(By.ID, "PSIC Regulatory Proceedings and Network Security & Privacy Coverage for Dentists_start")
        CYB_PSIC_DDS_link.click()

    def click_CYB_PSIC_MD(self):
        CYB_PSIC_MD_link = self.driver.find_element(By.ID, "PSIC Regulatory Proceedings and Network Security & Privacy Coverage for Physicians_start")
        CYB_PSIC_MD_link.click()

    def click_CYB_LSA(self):
        CYB_LSA_link = self.driver.find_element(By.ID, "LSA Cyber Liability / Medefense™ Plus_start")
        CYB_LSA_link.click()

    def click_CYB_USI(self):
        CYB_USI_link = self.driver.find_element(By.ID, "PrivaSafe with MEDEFENSE™ Plus_start")
        CYB_USI_link.click()

    def click_CYB_SVMIC(self):
        CYB_SVMIC_link = self.driver.find_element(By.ID, "SVMIC MEDEFENSE™ Plus and e-MD™_start")
        CYB_SVMIC_link.click()

    def click_CYB_TMLT(self):
        CYB_TMLT_link = self.driver.find_element(By.ID, "TMLT Cyber Liability / Medefense™ Plus_start")
        CYB_TMLT_link.click()

    def click_DAYSPA(self):
        DAYSPA_link = self.driver.find_element(By.ID, "Day Spa PL/GL_start")
        DAYSPA_link.click()

    def click_EO_MHC(self):
        EO_MHC_link = self.driver.find_element(By.ID, "Healthcare Misc. E&O_start")
        EO_MHC_link.click()

    def click_EO_MISC(self):
        EO_MISC_link = self.driver.find_element(By.ID, "Miscellaneous E&O_start")
        EO_MISC_link.click()

    def click_EO_PM(self):
        EO_PM_link = self.driver.find_element(By.ID, "Property Manager’s E&O with Cyber Liability and Tenant Discrimination_start")
        EO_PM_link.click()

    def click_EPL(self):
        EPL_link = self.driver.find_element(By.ID, "Employment Practices Liability (Under 50 employees)_start")
        EPL_link.click()

    def click_GRPHOME(self):
        GRPHOME_link = self.driver.find_element(By.ID, "Group Home_start")
        GRPHOME_link.click()

    def click_HHOL(self):
        HHOL_link = self.driver.find_element(By.ID, "Home Health Care_start")
        HHOL_link.click()

    def click_LEXR_TENANT(self):
        LEXR_TENANT_link = self.driver.find_element(By.ID, "Tenant Discrimination Legal Expense and Loss Reimbursement Insurance_start")
        LEXR_TENANT_link.click()

    def click_LTC(self):
        LTC_link = self.driver.find_element(By.ID, "Long Term Care PL/GL_start")
        LTC_link.click()

    def click_MEDEMD(self):
        MEDEMD_link = self.driver.find_element(By.ID, "e-MD™ Cyber and MEDEFENSE™ Plus_start")
        MEDEMD_link.click()

    def click_MED_NCMIC(self):
        MED_NCMIC_link = self.driver.find_element(By.ID, "NCMIC MEDEFENSE™ Plus_start")
        MED_NCMIC_link.click()

    def click_MMTM(self):
        MMTM_link = self.driver.find_element(By.ID, "Momentum Insurance_start")
        MMTM_link.click()

    def click_NGP(self):
        NGP_link = self.driver.find_element(By.ID, "Cyber Liability_start")
        NGP_link.click()

    def click_NGP_CAMICO(self):
        NGP_CAMICO_link = self.driver.find_element(By.ID, "CAMICO Cyber Liability_start")
        NGP_CAMICO_link.click()

    def click_NGP_HUB(self):
        NGP_HUB_link = self.driver.find_element(By.ID, "HUB International NetGuard™ Plus_start")
        NGP_HUB_link.click()

    def click_NGP_OBLIC(self):
        NGP_OBLIC_link = self.driver.find_element(By.ID, "OBLIC Cyber Liability_start")
        NGP_OBLIC_link.click()

    def click_NGP_RTS(self):
        NGP_RTS_link = self.driver.find_element(By.ID, "R-T Specialty Cyber Liability_start")
        NGP_RTS_link.click()

    def click_NGP_SBDIA(self):
        NGP_SBDIA_link = self.driver.find_element(By.ID, "Security Broker-Dealers and Investment Advisors Cyber Liability_start")
        NGP_SBDIA_link.click()

    def click_NGP_USI(self):
        NGP_USI_link = self.driver.find_element(By.ID, "PrivaSafe Cyber Liability_start")
        NGP_USI_link.click()

    def click_NGP_USPRO(self):
        NGP_USPRO_link = self.driver.find_element(By.ID, "US Pro Cyber Liability_start")
        NGP_USPRO_link.click()

    def click_NGP_USPRO_AZIONE(self):
        NGP_USPRO_AZIONE_link = self.driver.find_element(By.ID, "AZIONE Cyber Liability_start")
        NGP_USPRO_AZIONE_link.click()

    def click_RPM(self):
        RPM_link = self.driver.find_element(By.ID, "RPM Property Managers and Lessors E&O Program_start")
        RPM_link.click()

    def click_TLIE(self):
        TLIE_link = self.driver.find_element(By.ID, "Texas Lawyers' Insurance Exchange_start")
        TLIE_link.click()

    def click_Transitional_Living_Facilities(self):
        Transitional_Living_Facilities_link = self.driver.find_element(By.ID, "Transitional Living Facilities_start")
        Transitional_Living_Facilities_link.click()

    # Declare and Click Contract Class Modal
    def click_contract_class_modal(self):
        contract_class_modal = self.driver.find_element(By.ID, "pcs-product-class")
        contract_class_modal.click()

    def click_contract_class_drop_down_select_contract_class(self, contract_class):
        contract_class_drop_down = self.driver.find_element_by_css_selector("select[name=\"contract_class_id\"]")
        contract_class_drop_down.send_keys(contract_class)

    def click_contract_class_modal_NGP_USPRO(self):
        contract_class_modal_NGP_USPRO = self.driver.find_element_by_css_selector("select[name=\"contract_class_id\"]")
        contract_class_modal_NGP_USPRO.click()

    # Declare and Select Contract Class Drop Down
    def select_contract_class_dropdown(self):
        select_contract_class_dropdown = self.driver.find_element(By.XPATH, "//*[@id='class-select-wrap']")
        select_contract_class_dropdown.click()

    def select_contract_class_updated(self, contract_class):
        select_contract_class_dropdown = self.driver.find_element(By.XPATH, "//*[@id='class-select-wrap']")
        select_contract_class_dropdown.click()

        # Code works up to this point -- Ken

        contract_class_drop_down = self.driver.find_element_by_css_selector("select[name=\"contract_class_id\"]")
        contract_class_drop_down.send_keys(contract_class)

    def select_contract_class_updated_rev2(self, contract_class):
        select_contract_class_dropdown = self.driver.find_element(By.XPATH, "//*[@id='class-select-wrap']")
        select_contract_class_dropdown.click()

        contract_class_drop_down = self.driver.find_element_by_css_selector("select[name=\"contract_class_id\"]")
        contract_class_drop_down.send_keys(contract_class)

    # TODO: NEED TO FIX SO THAT SCRIPT USES STRING VALUE CONTAINED IN contract_class variable instead of an integer value
    # 12-23-16
    # Able to select a value from the contract class drop down that is an integer (1,5, 73 etc.)
    # However, I have not found a way to select a text value from the contract class dropdown - Ken

    # Declare and Select a Contract Class value from Drop Down
    def select_contract_class(self, contract_class_int_value):
        select_contract_class = self.driver.find_element(By.XPATH, "//*[@id='class-select-wrap']/select/option[" + contract_class_int_value + "]")
        select_contract_class.click()

    # Declare and Select a Contract Class value from Drop Down
    def select_contract_class_by_visible_text(self, contract_class):
        select_contract_class = self.driver.find_element(By.XPATH, "//*[@id='class-select-wrap']/select/option[" + contract_class + "]")
        select_contract_class.click()

    def select_contract_class_NGP_USPRO(self, contract_class_int_value):
        select_contract_class = self.driver.find_element(By.XPATH, "//*[@id='class-select-wrap']/select/option[" + contract_class_int_value + "]")
        select_contract_class.click()

    # Declare and Click Continue button on Contract Class Modal
    def click_continue_on_contract_class_modal(self):
        continue_button_contract_class_modal = self.driver.find_element(By.XPATH, "//div[@id='pcs-product-class']/form/div[3]/a/span[2]/span/span")
        continue_button_contract_class_modal.click()

    def click_continue_on_contract_class_modal_NGP_USPRO(self):
        continue_button_contract_class_modal_NGP_USPRO = self.driver.find_element(By.XPATH, "//div[@id='pcs-product-class']/form/div[2]/a/span[2]/span/span")
        continue_button_contract_class_modal_NGP_USPRO.click()

    def click_continue_on_contract_class_modal_after_selecting_contract_class(self):
        continue_button_contract_class_modal_ = self.driver.find_element(By.XPATH,"//div[@id='pcs-product-class']/form/div[2]/a/span[2]/span/span")
        continue_button_contract_class_modal_.click()



    # This Method is not yet working -- Ken
    def select_contract_class_use_string(self):

        # Select a contract class from drop down
        select_contract_class = self.driver.find_element(By.XPATH, "//*[@id='class-select-wrap']/select/option[@value='Biotech']")
        select_contract_class.click()

        # get following error
        # selenium.common.exceptions.NoSuchElementException: Message: Message: no such element: Unable to locate element

        #self.driver.find_element_by_css_selector("select[name=\"contract_class_id\"]").select_by_visible_text("Biotech")


        #select = self.driver.find_element(By.XPATH, "//*[@id='class-select-wrap']")

        #self.driver.execute_script("class-select-wrap = function (element) {var event; event = document.createEvent('MouseEvents'); event.initMouseEvent('mousedown', true, true, window); element.dispatchEvent(event); }; showDropdown(arguments[0]);",select)

        # Script Fails at the next Line
        #self.driver.find_element_by_xpath("//select[@id='class-select-wrap']/option[text()='Auto Dealers']").click()

        # Script Fails at the next Line
        #self.driver.execute_script( "var select = arguments[0]; for(var i = 0; i < select.options.length; i++){ if(select.options[i].text == arguments[1]){ select.options[i].selected = true; } }", select, "5")

        #URLS
        # http://stackoverflow.com/questions/38232406/selenium-in-python-selecting-an-option

        ### Return Page Element Text for Use in Test Assertions

    def return_Adult_DayCare_text(self):
        Adult_Daycare_start_button_text = (ProductsAndPrograms.Page_Elements(self).ADULTDC_link.text)
        return Adult_Daycare_start_button_text

    def return_CAP_CYB_text(self):
        CAP_CYB_start_button_text = (ProductsAndPrograms.Page_Elements(self).CAP_CYB_link.text)
        return CAP_CYB_start_button_text

    # def return_CRYO_text(self):
    #     CRYO_start_button_text = (ProductsAndPrograms.Page_Elements(self).CRYO_link.text)
    #     return CRYO_start_button_text

    def return_CYB_AAO_text(self):
        CYB_AAO_start_button_text = (ProductsAndPrograms.Page_Elements(self).CYB_AAO_link.text)
        return CYB_AAO_start_button_text

    def return_CYB_CAP_text(self):
        CYB_CAP_start_button_text = (ProductsAndPrograms.Page_Elements(self).CYB_CAP_link.text)
        return CYB_CAP_start_button_text

    def return_CYB_OMIC_text(self):
        CYB_OMIC_start_button_text = (ProductsAndPrograms.Page_Elements(self).CYB_OMIC_link.text)
        return CYB_OMIC_start_button_text

    def return_CYB_LAMMICO_text(self):
        CYB_LAMMICO_start_button_text = (ProductsAndPrograms.Page_Elements(self).CYB_LAMMICO_link.text)
        return CYB_LAMMICO_start_button_text

    def return_CYB_MDA_text(self):
        CYB_MDA_start_button_text = (ProductsAndPrograms.Page_Elements(self).CYB_MDA_link.text)
        return CYB_MDA_start_button_text

    def return_CYB_MMD_text(self):
        CYB_MMD_start_button_text = (ProductsAndPrograms.Page_Elements(self).CYB_MMD_link.text)
        return CYB_MMD_start_button_text

    def return_CYB_MMIC_text(self):
        CYB_MMIC_start_button_text = (ProductsAndPrograms.Page_Elements(self).CYB_MMIC_link.text)
        return CYB_MMIC_start_button_text

    def return_CYB_MICA_text(self):
        CYB_MICA_start_button_text = (ProductsAndPrograms.Page_Elements(self).CYB_MICA_link.text)
        return CYB_MICA_start_button_text

    def return_CYB_PAS_text(self):
        CYB_PAS_start_button_text = (ProductsAndPrograms.Page_Elements(self).CYB_PAS_link.text)
        return CYB_PAS_start_button_text

    def return_CYB_PAS_PICA_text(self):
        CYB_PAS_PICA_start_button_text = (ProductsAndPrograms.Page_Elements(self).CYB_PAS_PICA_link.text)
        return CYB_PAS_PICA_start_button_text

    def return_CYB_LSA_text(self):
        CYB_LSA_start_button_text = (ProductsAndPrograms.Page_Elements(self).CYB_LSA_link.text)
        return CYB_LSA_start_button_text

    def return_CYB_USI_text(self):
        CYB_USI_start_button_text = (ProductsAndPrograms.Page_Elements(self).CYB_USI_link.text)
        return CYB_USI_start_button_text

    def return_CYB_SVMIC_text(self):
        CYB_SVMIC_start_button_text = (ProductsAndPrograms.Page_Elements(self).CYB_SVMIC_link.text)
        return CYB_SVMIC_start_button_text

    def return_CYB_TMLT_text(self):
        CYB_TMLT_start_button_text = (ProductsAndPrograms.Page_Elements(self).CYB_TMLT_link.text)
        return CYB_TMLT_start_button_text

    def return_DAYSPA_text(self):
        DAYSPA_start_button_text = (ProductsAndPrograms.Page_Elements(self).DAYSPA_link.text)
        return DAYSPA_start_button_text

    def return_EO_MHC_text(self):
        EO_MHC_start_button_text = (ProductsAndPrograms.Page_Elements(self).EO_MHC_link.text)
        return EO_MHC_start_button_text

    def return_EO_MISC_text(self):
        EO_MISC_start_button_text = (ProductsAndPrograms.Page_Elements(self).EO_MISC_link.text)
        return EO_MISC_start_button_text

    def return_EO_PM_text(self):
        EO_PM_start_button_text = (ProductsAndPrograms.Page_Elements(self).EO_PM_link.text)
        return EO_PM_start_button_text

    def return_EPL_text(self):
        EPL_start_button_text = (ProductsAndPrograms.Page_Elements(self).EPL_link.text)
        return EPL_start_button_text

    def return_GRPHOME_text(self):
        GRPHOME_start_button_text = (ProductsAndPrograms.Page_Elements(self).GRPHOME_link.text)
        return GRPHOME_start_button_text

    def return_HHOL_text(self):
        HHOL_start_button_text = (ProductsAndPrograms.Page_Elements(self).HHOL_link.text)
        return HHOL_start_button_text

    def return_LEXR_TENANT_text(self):
        LEXR_TENANT_start_button_text = (ProductsAndPrograms.Page_Elements(self).LEXR_TENANT_link.text)
        return LEXR_TENANT_start_button_text

    def return_MEDEMD_text(self):
        MEDEMD_start_button_text = (ProductsAndPrograms.Page_Elements(self).MEDEMD_link.text)
        return MEDEMD_start_button_text

    def return_MED_NCMIC_text(self):
        MED_NCMIC_start_button_text = (ProductsAndPrograms.Page_Elements(self).MED_NCMIC_link.text)
        return MED_NCMIC_start_button_text

    def return_MMTM_text(self):
        MMTM_start_button_text = (ProductsAndPrograms.Page_Elements(self).MMTM_link.text)
        return MMTM_start_button_text

    def return_NGP_text(self):
        NGP_start_button_text = (ProductsAndPrograms.Page_Elements(self).NGP_link.text)
        return NGP_start_button_text

    def return_NGP_CAMICO_text(self):
        NGP_CAMICO_start_button_text = (ProductsAndPrograms.Page_Elements(self).NGP_CAMICO_link.text)
        return NGP_CAMICO_start_button_text

    def return_NGP_HUB_text(self):
        NGP_HUB_start_button_text = (ProductsAndPrograms.Page_Elements(self).NGP_HUB_link.text)
        return NGP_HUB_start_button_text

    def return_NGP_OBLIC_text(self):
        NGP_OBLIC_start_button_text = (ProductsAndPrograms.Page_Elements(self).NGP_OBLIC_link.text)
        return NGP_OBLIC_start_button_text

    def return_NGP_RTS_text(self):
        NGP_RTS_start_button_text = (ProductsAndPrograms.Page_Elements(self).NGP_RTS_link.text)
        return NGP_RTS_start_button_text

    def return_NGP_SBDIA_text(self):
        NGP_SBDIA_start_button_text = (ProductsAndPrograms.Page_Elements(self).NGP_SBDIA_link.text)
        return NGP_SBDIA_start_button_text

    def return_NGP_USI_text(self):
        NGP_USI_start_button_text = (ProductsAndPrograms.Page_Elements(self).NGP_USI_link.text)
        return NGP_USI_start_button_text

    def return_NGP_USPRO_text(self):
        NGP_USPRO_start_button_text = (ProductsAndPrograms.Page_Elements(self).NGP_USPRO_link.text)
        return NGP_USPRO_start_button_text

    def return_NGP_USPRO_AZIONE_text(self):
        NGP_USPRO_AZIONE_start_button_text = (ProductsAndPrograms.Page_Elements(self).NGP_USPRO_AZIONE_link.text)
        return NGP_USPRO_AZIONE_start_button_text

    def return_RPM_text(self):
        RPM_start_button_text = (ProductsAndPrograms.Page_Elements(self).RPM_link.text)
        return RPM_start_button_text

    def return_TLIE_text(self):
        TLIE_start_button_text = (ProductsAndPrograms.Page_Elements(self).TLIE_link.text)
        return TLIE_start_button_text

    def return_Transitional_Living_Facilities_text(self):
        Transitional_Living_Facilities_start_button_text = (ProductsAndPrograms.Page_Elements(self).Transitional_Living_Facilities_link.text)
        return Transitional_Living_Facilities_start_button_text