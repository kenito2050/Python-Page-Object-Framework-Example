from selenium.webdriver.common.by import By

class ProductsAndPrograms():

    def __init__(self, driver):
        self.driver = driver

    def Page_Elements(self):
        ballpark_link = self.driver.find_element(By.CSS_SELECTOR, "img[alt=\"Get a Ballpark Premium Indication\"]")

        # Products
        EO_MISC_link = self.driver.find_element(By.ID, "Miscellaneous E&O_start")

        NGP_link = self.driver.find_element(By.ID, "Cyber Liability_start")

        NGP_OBLIC_link = self.driver.find_element(By.ID, "OBLIC Cyber Liability_start")

        NGP_USPRO_link = self.driver.find_element(By.ID, "US Pro Cyber Liability_start")

        return self

    # Click Ballpark
    def click_ballpark(self):
        ballpark_link = self.driver.find_element(By.CSS_SELECTOR, "img[alt=\"Get a Ballpark Premium Indication\"]")
        ballpark_link.click()

    # Products

    def click_CYB_CAP(self):

        CYB_CAP_link = self.driver.find_element(By.ID, "CyberRisk™ Liability/Medefense Plus_start")
        CYB_CAP_link.click()

    def click_CYB_PSIC_DDS(self):
        CYB_PSIC_DDS_link = self.driver.find_element(By.ID, "PSIC Regulatory Proceedings and Network Security & Privacy Coverage for Dentists_start")
        CYB_PSIC_DDS_link.click()

    def click_CYB_PSIC_MD(self):
        CYB_PSIC_MD_link = self.driver.find_element(By.ID, "PSIC Regulatory Proceedings and Network Security & Privacy Coverage for Physicians_start")
        CYB_PSIC_MD_link.click()

    def click_CYB_MMIC(self):

        CYB_MMIC_link = self.driver.find_element(By.ID, "MMNC e-MD™ and MEDEFENSE™ Plus_start")
        CYB_MMIC_link.click()

    def click_CYB_MICA(self):

        CYB_MICA_link = self.driver.find_element(By.ID, "MICA e-Med Protection Plus_start")
        CYB_MICA_link.click()

    def click_EO_MISC(self):
        EO_MISC_link = self.driver.find_element(By.ID, "Miscellaneous E&O_start")
        EO_MISC_link.click()

    def click_LTC(self):
        LTC_link = self.driver.find_element(By.ID, "Long Term Care PL/GL_start")
        LTC_link.click()

    def click_NGP(self):

        #ProductsAndPrograms.Page_Elements(self).click_NGP()
        NGP_link = self.driver.find_element(By.ID, "Cyber Liability_start")
        NGP_link.click()

    def click_NGP_OBLIC(self):
        NGP_OBLIC_link = self.driver.find_element(By.ID, "OBLIC Cyber Liability_start")
        NGP_OBLIC_link.click()

    def click_NGP_USPRO(self):
        NGP_USPRO_link = self.driver.find_element(By.ID, "US Pro Cyber Liability_start")
        NGP_USPRO_link.click()

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
        continue_button_contract_class_modal_ = self.driver.find_element(By.XPATH,
                                                                                  "//div[@id='pcs-product-class']/form/div[2]/a/span[2]/span/span")
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

