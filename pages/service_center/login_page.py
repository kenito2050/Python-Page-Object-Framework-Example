from selenium.webdriver.common.by import By
from selenium.common.exceptions import NoSuchElementException
from selenium.webdriver.common.action_chains import ActionChains
from selenium.webdriver.common.keys import Keys
import time

class LoginPage():

    def __init__(self, driver):
        self.driver = driver

    def Page_Elements(self):

        # User Name Field
        self.user_field = self.driver.find_element(By.NAME, "user_id")

        # Password Field - Clear
        self.password_clear_field = self.driver.find_element(By.ID, "password-clear")

        # Password Password Field
        self.password_password_field = self.driver.find_element(By.ID, "password-password")

        # Submit Button
        self.submit_button = self.driver.find_element(By.ID, "right")

        return self

    def login(self, username, password):

        LoginPage.Page_Elements(self).user_field.clear()
        LoginPage.Page_Elements(self).user_field.send_keys(username)
        LoginPage.Page_Elements(self).password_clear_field.clear()
        LoginPage.Page_Elements(self).password_password_field.send_keys(password)
        self.driver.implicitly_wait(10)


    def click_login_button(self):
        LoginPage.Page_Elements(self).submit_button.click()

    def test_assert_text_in_url(self):
        # Assert that certain text is in the url
        current_url = self.driver.current_url
        assert "c=home.updates" in current_url

        # Assert Logout is Present
    def assertElementIsPresentByXPath(self, xpath, msg=None):
        try:
            self.driver.find_element_by_xpath(xpath)
            self.driver.assertTrue(True, msg)
        except NoSuchElementException:
            self.driver.assertTrue(False, msg)

    def test_element_exists(self):
        self.assertElementIsPresentByXPath("//h4[contains(text(),'Time Range')][1]")



    def login_new(self, username, password):

        LoginPage.Page_Elements(self).user_field.clear()
        LoginPage.Page_Elements(self).user_field.send_keys(username)
        LoginPage.Page_Elements(self).password_clear_field.clear()
        LoginPage.Page_Elements(self).password_password_field.send_keys(password)

    def click_login_button_new(self):

        LoginPage.Page_Elements(self).submit_button.click()

