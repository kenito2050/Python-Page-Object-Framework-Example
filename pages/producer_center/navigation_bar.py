from selenium.webdriver.common.by import By

class Navigation_Bar():

    def __init__(self, driver):
        self.driver = driver

    def Page_Elements(self):

        self.Home_link = self.driver.find_element(By.LINK_TEXT, "Home")
        self.Products_Programs_link = self.driver.find_element(By.LINK_TEXT, "Products & Programs")
        self.My_Submissions_link = self.driver.find_element(By.LINK_TEXT, "My Submissions")
        self.My_Policies_link = self.driver.find_element(By.LINK_TEXT, "My Policies")
        self.My_Clients_link = self.driver.find_element(By.LINK_TEXT, "My Clients")
        self.My_Agents_link = self.driver.find_element(By.LINK_TEXT, "My Agents")
        self.Video_Tutorials_link = self.driver.find_element(By.LINK_TEXT, "Video Tutorials")

        return self

    def click_home(self):
        #applications_link = self.driver.find_element(By.LINK_TEXT, "Home")
        Navigation_Bar.Page_Elements(self).Home_link.click()

    def click_products_programs(self):
        #policies_link = self.driver.find_element(By.LINK_TEXT, "Products Programs")
        Navigation_Bar.Page_Elements(self).Products_Programs_link.click()

    def click_my_submissions(self):
        #clients_link = self.driver.find_element(By.LINK_TEXT, "My Submissions")
        Navigation_Bar.Page_Elements(self).My_Submissions_link.click()

    def click_my_policies(self):
        #agents_link = self.driver.find_element(By.LINK_TEXT, "My Policies")
        Navigation_Bar.Page_Elements(self).My_Policies_link.click()

    def click_my_clients(self):
        #agencies_link = self.driver.find_element(By.LINK_TEXT, "My Clients")
        Navigation_Bar.Page_Elements(self).My_Clients_link.click()

    def click_my_agents(self):
        #products_and_programs_link = self.driver.find_element(By.LINK_TEXT, "My Agents")
        Navigation_Bar.Page_Elements(self).My_Agents_link.click()

    def click_video_tutorials(self):
        #staff_link = self.driver.find_element(By.LINK_TEXT, "Video Tutorials")
        Navigation_Bar.Page_Elements(self).Video_Tutorials_link.click()