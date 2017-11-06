from base.selenium_driver import SeleniumDriver
from selenium.webdriver.common.by import By


class LoginPage_New(SeleniumDriver):

    def __init__(self, driver):
        super().__init__(driver)
        self.driver = driver

    # Locators
    _user_name = "user_id"
    _password_clear = "password-clear"
    _password_field = "password-password"
    _submit_button = "right"

    def getUserNameField(self):
        return self.driver.find_element(By.NAME, "user_id")

    def getPasswordClearField(self):
        return self.driver.find_element(By.ID, "password-clear")

    def getPasswordField(self):
        return self.driver.find_element(By.ID, "password-password")

    def getSubmitButton(self):
        return self.driver.find_element(By.ID, "right")

    def selectUserNameField(self):
        self.elementClick(self._user_name, locatorType="name")

    def clearUserNameField(self):
        self.elementClear(self._user_name, locatorType="name")

    def enterUserName(self, username):
        self.sendKeys(username, self._user_name, locatorType="name")

    def clearPasswordField(self):
        self.elementClear(self._password_clear, locatorType="id")

    def enterPassword(self, password):
        self.sendKeys(password, self._password_field)

    def clickSubmitButton(self):
        self.elementClick(self._submit_button, locatorType="id")

    def test_login(self, username, password):
        self.selectUserNameField()
        self.clearUserNameField()
        self.enterUserName(username)
        self.clearPasswordField()
        self.enterPassword(password)

    def test_click_login_button(self):
        self.clickSubmitButton()

    def verifyLoginSuccessful(self):
        result = self.isElementPresent("Clients", locatorType="link")
        return result

    def verifyLoginFailed(self):
        result = self.isElementPresent("login-err", locatorType="id")
        return result