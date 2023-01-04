from selenium import webdriver
from selenium.webdriver.chrome.service import Service
from selenium.webdriver.common.by import By
import time
from selenium.webdriver.common.keys import Keys
import unittest
from pages.HomePage import homePage
from pages.LoginPage import LoginPage

class LonginTest(unittest.TestCase):
    @classmethod
    def setUpClass(cls):
        cls.s = Service('C:/Users/drzho/PycharmProjects/TestAutomation/chromedriver.exe')
        cls.driver = webdriver.Chrome(service=cls.s)
        cls.driver.implicitly_wait(2)
        cls.driver.maximize_window()

    def test_login_valid(self):
        driver=self.driver
        driver.get("https://opensource-demo.orangehrmlive.com/")

        login=LoginPage(driver)            #initiate object
        login.enter_username('Admin')
        login.enter_password('admin123')
        login.click_login()

        logout=homePage(driver)         #initiate object
        logout.click_menu()
        logout.logout()

        #self.driver.get("https://opensource-demo.orangehrmlive.com/")
        # self.driver.find_element(By.NAME, 'username').send_keys('Admin')
        # self.driver.find_element(By.NAME, 'password').send_keys('admin123')
        # # driver.find_element(By.XPATH,f'//*[@id="app"]/div[1]/div/div[1]/div/div[2]/div[2]/form/div[1]/div/div[2]/input').send_keys('Admin')
        # # driver.find_element(By.XPATH,'//*[@id="app"]/div[1]/div/div[1]/div/div[2]/div[2]/form/div[2]/div/div[2]/input').send_keys('admin123')
        # self.driver.find_element(By.XPATH, '//*[@id="app"]/div[1]/div/div[1]/div/div[2]/div[2]/form/div[3]/button').click()
        # # By.CSS_SELECTOR, #app > div.orangehrm-login-layout > div > div.orangehrm-login-container > div > div.orangehrm-login-slot > div.orangehrm-login-form > form > div.oxd-form-actions.orangehrm-login-action > button
        #
        # # driver.find_element(By.XPATH,'//*[@id="app"]/div[1]/div[1]/header/div[1]/div[2]/ul/li/span/img').click()
        # self.driver.find_element(By.XPATH, '//*[@id="app"]/div[1]/div[1]/header/div[1]/div[2]/ul/li/span/i').click()
        # self.driver.find_element(By.LINK_TEXT, 'Logout').click()

        time.sleep(2)

    @classmethod
    def tearDownClass(cls):

#url='https://www.cctb.ca'

        cls.driver.close()
        cls.driver.quit()

        print('done')

