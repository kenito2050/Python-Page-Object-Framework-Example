from selenium.webdriver.common.by import By

class LoginPage():

    def __init__(self, driver):
        self.driver = driver

    def login(self, username, password):

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

        # Declare Submit button; click Submit Button
        submit_button = self.driver.find_element(By.ID, "right")
        submit_button.click()