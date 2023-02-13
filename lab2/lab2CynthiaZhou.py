from selenium import webdriver
from selenium.webdriver.chrome.service import Service
from selenium.webdriver.common.by import By
import time
from selenium.webdriver.common.keys import Keys
import unittest
from lab2.MainPage import mainPage
from lab2.PythonPage import pythonPage

class SearchTest(unittest.TestCase):
    @classmethod
    def setUpClass(cls):
        cls.s = \
            Service('C:/Users/drzho/PycharmProjects/\
        TestAutomation/chromedriver.exe')
        cls.driver = webdriver.Chrome(service=cls.s)
        cls.driver.implicitly_wait(2)
        cls.driver.maximize_window()

    def test_search_valid(self):
        driver=self.driver
        url= driver.get("https://en.wikipedia.org/")

        search_python = mainPage(driver)

        phrase='Python'
        searched = 'Python (programming language)'
        print(f'Now search something for "{phrase}" related:')

        search_python.enter_search_phrase\
            (phrase,searched)
        time.sleep(1)
      #  search_python.click_search()   # OR by key_enter_search
      #  time.sleep(1)
       # search_python.key_enter_search()
       # time.sleep(1)

        python_page=pythonPage(driver)
        python_page.verify(searched)

        time.sleep(2)

    @classmethod
    def tearDownClass(cls):


        cls.driver.close()
        cls.driver.quit()

        print('done')



