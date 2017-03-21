from selenium import webdriver
from selenium.webdriver import ActionChains
import unittest


class Test_assert_and_selenium (unittest.TestCase):
    driver=None
    def setUp(self):
        global driver
        driver = webdriver.PhantomJS('C:/Users/Administrator/Downloads/phantomjs-2.1.1-windows/bin/phantomjs.exe')
        driver.get('http://pythonscraping.com/pages/javascript/draggableDemo.html')
    def tearDown(self):
        print("tearDown the test!")
    def test_drag(self):
        element = driver.find_element_by_id("draggable")
        target = driver.find_element_by_id("div2")
        actions = ActionChains(driver)
        actions.drag_and_drop(element, target).perform()
        self.assertEqual("You are definitelynot a bot!", driver.find_element_by_id("message").text)

if __name__ == '__main__':
    unittest.main()