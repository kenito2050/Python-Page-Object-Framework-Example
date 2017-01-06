from selenium.webdriver.common.by import By

class NavigationBar():

    def __init__(self, driver):
        self.driver = driver

    def click_applications(self):
        applications_link = self.driver.find_element(By.LINK_TEXT, "Applications")
        applications_link.click()

    def click_policies(self):
        policies_link = self.driver.find_element(By.LINK_TEXT, "Policies")
        policies_link.click()

    def click_clients(self):
        clients_link = self.driver.find_element(By.LINK_TEXT, "Clients")
        clients_link.click()

    def click_agents(self):
        agents_link = self.driver.find_element(By.LINK_TEXT, "Agents")
        agents_link.click()

    def click_agencies(self):
        agencies_link = self.driver.find_element(By.LINK_TEXT, "Agencies")
        agencies_link.click()

    def click_products_and_programs(self):
        products_and_programs_link = self.driver.find_element(By.LINK_TEXT, "Products & Programs")
        products_and_programs_link.click()

    def click_staff(self):
        staff_link = self.driver.find_element(By.LINK_TEXT, "Staff")
        staff_link.click()

    def click_admins(self):
        admins_link = self.driver.find_element(By.LINK_TEXT, "Admins")
        admins_link.click()

    def click_products(self):
        products_link = self.driver.find_element(By.LINK_TEXT, "Products")
        products_link.click()