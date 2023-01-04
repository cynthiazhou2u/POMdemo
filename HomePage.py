from selenium.webdriver.common.by import By
class homePage():
    def __init__(self, driver):
        self.driver=driver
        self.drop_down_menu='//*[@id="app"]/div[1]/div[1]/header/div[1]/div[2]/ul/li/span/i'
        self.logout_linkText='Logout'

    def click_menu(self):
        self.driver.find_element(By.XPATH,self.drop_down_menu).click()

    def logout(self):
        self.driver.find_element(By.LINK_TEXT,self.logout_linkText).click()
