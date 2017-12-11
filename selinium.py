import unittest
from selenium import webdriver
from selenium.webdriver.common.proxy import *
from selenium.webdriver.common.desired_capabilities import *
import os
from time import sleep

class Selenium2OnSauce(unittest.TestCase):

    def setUp(self):
        user = os.getenv('SAUCE_USERNAME', '')
        key = os.getenv('SAUCE_ACCESS_KEY', '')

        #desired_capabilities = {'browserName': 'firefox'}
        capabilities = DesiredCapabilities.FIREFOX.copy()

        print 'starting'

        self.driver = webdriver.Remote(
            desired_capabilities=capabilities
        )
        self.driver.implicitly_wait(30)

    def test_google(self):
        self.driver.get('https://google.com')
        assert(self.driver.title == 'Google Home Page')
        searchbox = driver.find_element('id', 'searchinput')
        searchbox.sendKeys('kittie pictures')
        assert(searchbox.text = 'kittie pictures')
        searchbutton = driver.find_element('id','submit')
        searchbutton.click()



    def tearDown(self):
        print("all done")
        self.driver.quit()

if __name__ == '__main__':
    unittest.main()
