import unittest
from selenium import webdriver
from selenium.webdriver.common.proxy import *
from selenium.webdriver.common.desired_capabilities import *
import os

class Selenium2OnSauce(unittest.TestCase):

    def setUp(self):
        user = os.getenv('SAUCE_USERNAME', '')
        key = os.getenv('SAUCE_ACCESS_KEY', '')

        caps = {'browserName': "chrome"}
        caps['platform'] = "macOS 10.12"
        caps['version'] = "62.0"
        print 'starting'

        self.driver = webdriver.Remote(
            command_executor='http://%s:%s@ondemand.saucelabs.com:80/wd/hub' % (user, key),
            desired_capabilities=caps
        )
        self.driver.implicitly_wait(30)

    def test_authform(self):
        self.driver.get('http://the-internet.herokuapp.com')
        assert(self.driver.title == 'The Internet')
        link = self.driver.find_element_by_link_text('Form Authentication')
        link.click()
        userentry = self.driver.find_element_by_id('username')
        userentry.send_keys('fakeuser')
        passentry = self.driver.find_element_by_id('password')
        passentry.send_keys('badpass')
        self.driver.find_element_by_css_selector('.radius').click()
        assert('Your username is invalid!' in self.driver.find_element_by_id('flash').text)


    def tearDown(self):
        print("all done")
        self.driver.quit()

if __name__ == '__main__':
    unittest.main()
