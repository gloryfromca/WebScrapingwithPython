import pdb
# pdb.set_trace()
import time
from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from selenium.common.exceptions import StaleElementReferenceException

def webforload(driver):
    count=0
    while True:
        element = driver.find_element_by_tag_name("html")
        count+=1
        if count>100:
            print("Timeout happened after 10 seconds")
            return
        time.sleep(0.5)
        if element != driver.find_element_by_tag_name('html'):
            return


        
driver=webdriver.PhantomJS(executable_path='C:/Users/Administrator/Downloads/phantomjs-2.1.1-windows/bin/phantomjs.exe')
driver.get("http://pythonscraping.com/pages/javascript/redirectDemo1.html")
webforload(driver)
print(driver.page_source)#print web_page from PhantomJS drove by 'driver'


