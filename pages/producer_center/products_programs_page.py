from selenium.webdriver.common.by import By

class ProductsAndPrograms():

    def __init__(self, driver):
        self.driver = driver

    # Click Ballpark
    def click_ballpark(self):
        ballpark_link = self.driver.find_element(By.CSS_SELECTOR, "img[alt=\"Get a Ballpark Premium Indication\"]")
        ballpark_link.click()

    # Products
    def click_NGP(self):
        NGP_link = self.driver.find_element(By.ID, "Cyber Liability_start")
        NGP_link.click()

    # Declare and Click Contract Class Modal
    def click_contract_class_modal(self):
        contract_class_modal = self.driver.find_element(By.ID, "pcs-product-class")
        contract_class_modal.click()

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

    # Declare and Click Continue button on Contract Class Modal
    def click_continue_on_contract_class_modal(self):
        continue_button_contract_class_modal = self.driver.find_element(By.XPATH, "//div[@id='pcs-product-class']/form/div[3]/a/span[2]/span/span")
        continue_button_contract_class_modal.click()

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

