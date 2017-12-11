import unittest
from selenium import webdriver
from selenium.webdriver.common.proxy import *
from selenium.webdriver.common.desired_capabilities import *
import os
import wd.parallel


class Selenium2OnSauce(unittest.TestCase):

    def setUp(self):
        user = os.getenv('SAUCE_USERNAME', '')
        key = os.getenv('SAUCE_ACCESS_KEY', '')

        caps = [
            {
            'browserName': "firefox",
            'platform': 'Linux',
            'version': '44.0'
            },
            {
            'browserName': "safari",
            'platform': 'OS X 10.11',
            'version': '9.0'
            }
        ]

        print 'starting'

        self.drivers = wd.parallel.Remote(
            command_executor='http://%s:%s@ondemand.saucelabs.com:80/wd/hub' % (user, key),
            desired_capabilities=caps
        )
        #self.driver.implicitly_wait(30)

    @wd.parallel.multiply
    def test_authform(self):
        self.driver.get('http://the-internet.herokuapp.com')
        self.assertTrue(self.driver.title == 'The Internet')
        link = self.driver.find_element_by_link_text('Forgot Password')
        link.click()
        userentry = self.driver.find_element_by_id('email')
        userentry.send_keys('apple@gmail.com')
        self.driver.find_element_by_css_selector('.radius').click()
        print self.driver.find_element_by_id('content').text
        self.assertTrue('Your e-mail\'s been sent!' in self.driver.find_element_by_id('content').text)

    @wd.parallel.multiply
    def tearDown(self):
        print("all done")
        self.driver.quit()

if __name__ == '__main__':
    unittest.main()
