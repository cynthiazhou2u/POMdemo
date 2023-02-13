from selenium.webdriver.common.by import By
from selenium.webdriver.common.keys import Keys
class mainPage():

    def __init__(self,driver):
        self.driver=driver
        self.search_textbox="search"
        self.search_id='searchButton'
        title = 'Wikipedia, the free encyclopedia'
        if driver.current_url == 'https://en.wikipedia.org/wiki/Main_Page' \
                and driver.title==title:
            print('Hello, Wikepedia!')

    def enter_search_phrase(self,search_phrase,searched):

        self.driver.find_element(By.NAME,self.search_textbox).clear()
        self.driver.find_element(By.NAME,self.search_textbox).send_keys(search_phrase)
        self.driver.find_element(By.LINK_TEXT,searched).click()


    def click_search(self):
        self.driver.find_element(By.ID,self.search_id).click()

    def key_enter_search(self):
        self.driver.find_element(By.NAME, self.search_textbox).send_keys(Keys.ENTER)
