from selenium.webdriver.common.by import By

class NavigationBar():

    def __init__(self, driver):
        self.driver = driver

    def Page_Elements(self):

        self.applications_link = self.driver.find_element(By.LINK_TEXT, "Applications")
        self.policies_link = self.driver.find_element(By.LINK_TEXT, "Policies")
        self.clients_link = self.driver.find_element(By.LINK_TEXT, "Clients")
        self.agents_link = self.driver.find_element(By.LINK_TEXT, "Agents")
        self.agencies_link = self.driver.find_element(By.LINK_TEXT, "Agencies")
        self.products_and_programs_link = self.driver.find_element(By.LINK_TEXT, "Products & Programs")
        self.staff_link = self.driver.find_element(By.LINK_TEXT, "Staff")
        self.admins_link = self.driver.find_element(By.LINK_TEXT, "Admins")
        self.products_link = self.driver.find_element(By.LINK_TEXT, "Products")

        return self

    def click_applications(self):
        #applications_link = self.driver.find_element(By.LINK_TEXT, "Applications")
        NavigationBar.Page_Elements(self).applications_link.click()

    def click_policies(self):
        #policies_link = self.driver.find_element(By.LINK_TEXT, "Policies")
        NavigationBar.Page_Elements(self).policies_link.click()

    def click_clients(self):
        #clients_link = self.driver.find_element(By.LINK_TEXT, "Clients")
        NavigationBar.Page_Elements(self).clients_link.click()

    def click_agents(self):
        #agents_link = self.driver.find_element(By.LINK_TEXT, "Agents")
        NavigationBar.Page_Elements(self).agents_link.click()

    def click_agencies(self):
        #agencies_link = self.driver.find_element(By.LINK_TEXT, "Agencies")
        NavigationBar.Page_Elements(self).agencies_link.click()

    def click_products_and_programs(self):
        #products_and_programs_link = self.driver.find_element(By.LINK_TEXT, "Products & Programs")
        NavigationBar.Page_Elements(self).products_and_programs_link.click()

    def click_staff(self):
        #staff_link = self.driver.find_element(By.LINK_TEXT, "Staff")
        NavigationBar.Page_Elements(self).staff_link.click()

    def click_admins(self):
        #admins_link = self.driver.find_element(By.LINK_TEXT, "Admins")
        NavigationBar.Page_Elements(self).admins_link.click()

    def click_products(self):
        #products_link = self.driver.find_element(By.LINK_TEXT, "Products")
        NavigationBar.Page_Elements(self).products_link.click()