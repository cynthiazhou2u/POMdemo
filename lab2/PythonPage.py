from selenium.webdriver.common.by import By
class pythonPage():
    def __init__(self, driver):
        self.driver=driver
    #    self.python_header='//*[@id="firstHeading"]/span'
        self.url="https://en.wikipedia.org/wiki/Python_(programming_language)"
        self.title='Python (programming language) - Wikipedia'

    def verify(self,phrase):
    #    found=self.driver.find_element(By.XPATH, self.python_header)
     #   if found==phrase:
        if self.driver.current_url == self.url and \
                self.driver.title==self.title:
            print(f'OK, found the page for {phrase} ...')
