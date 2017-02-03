from selenium.webdriver.common.by import By

class Thank_You_Page():

    def __init__(self, driver):
        self.driver = driver

    def retrieve_store_policy_number(self):
        policy_text = self.driver.find_element(By.PARTIAL_LINK_TEXT, "TEST").text
        return policy_text

    def click_policy_link(self):
        #policy_link = self.driver.find_element_by_css_selector("//a[contains(@href,'/index.php?c=policy.view')]")
        #policy_link = self.driver.find_element(By.XPATH, '//a[@class="db" and @href="/index.php?c=policy.view"]')
        #policy_link = self.driver.find_element(By.XPATH, "//span[starts-with(@href, '/index.php?c=policy.view_')]")
        #policy_link = self.driver.find_element(By.ID, "policy-link")
        policy_link = self.driver.find_element(By.PARTIAL_LINK_TEXT, "TEST")
        policy_number = self.driver.find_element(By.PARTIAL_LINK_TEXT, "TEST").text
        policy_link.click()