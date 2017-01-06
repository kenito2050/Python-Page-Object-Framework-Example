class LandingPage():

    def __init__(self, driver):
        self.driver = driver

    def click_agent_page(self):

        # Declare Page Elements on Login Page
        user_field = self.driver.find_element_by_name("user_id")
        password_clear_field = self.driver.find_element_by_id("password-clear")
        password_password_field = self.driver.find_element_by_id("password-password")
        submit_button = self.driver.find_element_by_id("right")