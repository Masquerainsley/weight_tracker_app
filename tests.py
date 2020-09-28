import unittest
from selenium import webdriver

class WeightTrackerTest(unittest.TestCase):
    def test_home(self):
        browser = webdriver.Chrome('/home/ainsley/Desktop/chromedriver_linux64/chromedriver')
        browser.get('http://localhost:5000/')
        self.assertEqual('hello world', browser.find_element_by_tag_name('body').text)