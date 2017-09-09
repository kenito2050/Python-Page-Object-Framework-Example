from selenium.webdriver.common.by import By
from selenium.webdriver.common.action_chains import ActionChains
from selenium.webdriver.common.keys import Keys

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


    def login_old(self, username, password):

        #self.driver.input("blah")

        # Declare Username field; Input value
        user_field = self.driver.find_element(By.NAME, "user_id")
        user_field.clear()
        user_field.send_keys(username)

        # Declare password fields; Input value
        password_clear_field = self.driver.find_element(By.ID, "password-clear")
        password_password_field = self.driver.find_element(By.ID, "password-password")
        password_clear_field.clear()
        password_password_field.send_keys(password)

        # Wait
        self.driver.implicitly_wait(10)

        #input('please enter something')

        # IF TESTING ON LIVE, Put Breakpoint on Line 32
        # Declare Submit button; click Submit Button
        submit_button = self.driver.find_element(By.ID, "right")
        submit_button.click()

